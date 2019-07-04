# -*- coding: utf-8 -*-
from app import *
from cubejsgenerator import cubejsGenerator, getFactsModels

from models.googlemodels import *
from models.generalmodel import *
from models.comagic import *

def main():

    db.create_all()

    modelspath = './main/models'
    for fact in getFactsModels(modelspath):
        cube = cubejsGenerator(fact, modelspath, './cubejs')
        print(fact)

if __name__ == '__main__':
    main()
