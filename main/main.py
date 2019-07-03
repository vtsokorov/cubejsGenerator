# -*- coding: utf-8 -*-
import sys
import os
import fnmatch
import inspect

from jinja2 import Template

from app import *
from models.googlemodels import *
from models.generalmodel import *


def findModelsByTable(modelspath, tablename):
    listOfFiles = os.listdir(modelspath)
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, "*.py"):
            modulename = entry.rsplit('.', 2)[0]
            for name, classname in inspect.getmembers(sys.modules['models.'+modulename], inspect.isclass):
                if classname.__tablename__ == tablename:
                    return classname
    return None


def removeCharacter(string):
    s = list(string)
    for index, char in enumerate(s):
        if char == '_':
            del s[index]
            s[index] = s[index].title()
    return "".join(s)


def addQuotes(line):
    return '`' + line + '`'


def addBrackets(line):
    return '[' + line + ']'


def cubejsGenerator(model):
    table = model.metadata.tables[model.__tablename__]
    params = dict()
    params['CUBENAME'] = model.__name__
    params['TABLENAME'] = table.name
    params['COLUMNS'] = table.columns.keys()

    if hasattr(model, '__humanname__'):
        params['TITLE'] = model.__humanname__

    mapTypes = {'Integer': 'number', 'String': 'string', 'Unicode': 'string', 'Numeric': 'number', 'DateTime': 'datatime', 'Date': 'date'}

    dimensionlist = list()
    joinsList = list()
    measureslist = list()
    for column in table.columns:
        dimensionMap = dict()
        measuresMap = dict()

        if len(column.foreign_keys) != 0:
            fk = next(iter(column.foreign_keys))
            mainTable, pkIndex = fk._get_colspec().rsplit('.', 2)
            modelspath = os.path.dirname(os.path.abspath(__file__))+'/models'
            dinamycModel = findModelsByTable(modelspath, mainTable)
            cubejsGenerator(dinamycModel)
            if mainTable in model.__mapper__.relationships.keys():
                join = addQuotes('${'+model.__name__+'}.'+column.name+' = ${'+dinamycModel.__name__+'}.'+pkIndex)
                joinsList.append({dinamycModel.__name__: {'relationship': addQuotes('belongsTo'), 'sql': join}})
        else:
            if column.primary_key:
                dimensionMap.update({column.name: {'sql': addQuotes(column.name), 'type': addQuotes(mapTypes[column.type.__class__.__name__]), 'primaryKey': 'true'}})
                dimensionlist.append(dimensionMap)

                measuresMap.update({'count': {'drillMembers': addBrackets(column.name), 'type': addQuotes('count')}})
                measureslist.append(measuresMap)

            if not column.primary_key and mapTypes[column.type.__class__.__name__] == 'number': 
                measuresMap.update({column.name: {'sql': addQuotes(column.name), 'type': addQuotes('sum')}})
                if 'verbose_name' in column.info:
                    measuresMap[column.name].update({'title': addQuotes(column.info['verbose_name'])})
                measureslist.append(measuresMap)

            if not column.primary_key and mapTypes[column.type.__class__.__name__] == 'string':
                dimensionMap.update({column.name: {'sql': addQuotes(column.name), 'type': addQuotes(mapTypes[column.type.__class__.__name__])}})
                if 'verbose_name' in column.info:
                    dimensionMap[column.name].update({'title': addQuotes(column.info['verbose_name'])})
                dimensionlist.append(dimensionMap)
    params['CUBECONTENT'] = [{'joins': joinsList}, {'measures': measureslist}, {'dimensions': dimensionlist}]
    
    template = Template(open('cubejs.template').read())
    cube = template.render(params=params)
    with open('cubejs/'+model.__name__+'.js', 'w') as f:
        f.write(cube)
    return cube


def main():

    db.create_all()
    cube = cubejsGenerator(AnalyticsSessionFact)

if __name__ == '__main__':
    main()
