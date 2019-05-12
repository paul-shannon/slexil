# -*- coding: utf-8 -*-

class Error(Exception):
    pass

class TooManyMorphsError(Error):
    '''raised when there are more divisions on the parsing line
       than on the glossing line'''
    def __init__(self,lineNumber):
        super().__init__()
        self.lineNumber = lineNumber

class TooManyGlossesError(Error):
    '''raised when there are more divisions on the glossing line
       than on the parsing line'''
    def __init__(self,lineNumber):
        self.lineNumber = lineNumber
