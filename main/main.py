# -*- coding: utf-8 -*-
from cubejsgenerator import convertModeltoCubejs

#???
from models.googlemodels import *
from models.generalmodel import *
from models.comagic import *


def main():

    convertModeltoCubejs('./main/models', './cubejs')

if __name__ == '__main__':
    main()
