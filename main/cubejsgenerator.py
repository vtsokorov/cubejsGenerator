# -*- coding: utf-8 -*-
import sys
import os
import re
import fnmatch
import inspect

from jinja2 import Template

'''
todo:
1. account_id = GeneralAccounts.account_id
2. Удалить measure из таблиц измерений ***
3. Скрывать некоторые поля (shown:)
Вопросы:
*Изменил имена модулей
'''


def getModuleNameList(modelspath):
    listOfFiles = list(map(os.path.abspath, os.listdir(modelspath)))
    modulelist = list()
    for file in listOfFiles:
        if fnmatch.fnmatch(file, "*.py"):
            modulelist.append(inspect.getmodulename(file))
    return modulelist


def findModelsByTable(modulelist, tablename, package='models'):
    models = __import__(package, globals(), locals(), modulelist, 0)
    for module in modulelist:
        for name, classname in inspect.getmembers(eval(package+'.'+module), inspect.isclass):
            if classname.__tablename__ == tablename:
                return classname
    return None


def factsModels(modulelist, package='models'):
    models = __import__(package, globals(), locals(), modulelist, 0)
    for module in modulelist:
        for name, classname in inspect.getmembers(eval(package+'.'+module), inspect.isclass):
            if re.match(r".*_facts$", classname.__tablename__):
                yield classname
    return None


def addQuotes(line):
    return '`' + line + '`'


def addBrackets(line):
    return '[' + line + ']'


def cubejsGenerator(model, modules, cubejspath, measuretypes = dict()):

    if not hasattr(model, '__name__') or os.path.exists(cubejspath+'/'+model.__name__+'.js'):
        return

    table = model.metadata.tables[model.__tablename__]
    params = dict()
    params['CUBENAME'] = model.__name__
    params['TABLENAME'] = table.name
    params['COLUMNS'] = table.columns.keys()

    if hasattr(model, '__humanname__'):
        params['TITLE'] = model.__humanname__

    mapTypes = {'Integer': 'number', 'String': 'string', 'Unicode': 'string', 'Numeric': 'number', 'DateTime': 'time', 'Date': 'time', 'Boolean': 'string'}

    dimensionlist = list()
    joinsList = list()
    measureslist = list()
    for column in table.columns:
        dimensionMap = dict()
        measuresMap = dict()

        if bool(column.foreign_keys):
            fk = next(iter(column.foreign_keys))
            mainTable, pkIndex = fk._get_colspec().rsplit('.', 2)
            dinamycModel = findModelsByTable(modules, mainTable)
            cubejsGenerator(dinamycModel, modules, cubejspath)
            if mainTable in model.__mapper__.relationships.keys():
                join = addQuotes('${'+model.__name__+'}.'+column.name+' = ${'+dinamycModel.__name__+'}.'+pkIndex)
                joinsList.append({dinamycModel.__name__: {'relationship': addQuotes('belongsTo'), 'sql': join}})
        else:
            if column.primary_key:
                dimensionMap.update({column.name: {'sql': addQuotes(column.name), 'type': addQuotes(mapTypes[column.type.__class__.__name__]), 'primaryKey': 'true'}})
                dimensionlist.append(dimensionMap)

            '''Добовляем меры только в таблицы фактов'''
            if column.primary_key and re.match(r".*_facts$", model.__tablename__):
                measuresMap.update({'count': {'drillMembers': addBrackets(column.name), 'type': addQuotes('count')}})
                if 'verbose_name' in column.info:
                    measuresMap['count'].update({'title': addQuotes(column.info['verbose_name'])})
                measureslist.append(measuresMap)

            '''Добовляем меры только в таблицы фактов'''
            if not column.primary_key and re.match(r".*_facts$", model.__tablename__) and mapTypes[column.type.__class__.__name__] == 'number': 
                type = measuretypes[column.name] if bool(measuretypes) else 'sum'
                measuresMap.update({column.name: {'sql': addQuotes(column.name), 'type': addQuotes(type)}})
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
    with open(cubejspath+'/'+model.__name__+'.js', 'w', encoding="utf-8") as f:
        f.write(cube)
    return cube


def convertModeltoCubejs(modelspath, cubepath):
    modules = getModuleNameList(modelspath)
    for fact in factsModels(modules):
        cubejsGenerator(fact, modules, cubepath)
        print(fact)

