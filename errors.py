# -*- coding: utf-8 -*-

class Error(Exception):
    pass


class TooManyMorphsError(Error):
    '''raised when there are more divisions on the parsing line
       than on the glossing line'''

    def __init__(self, lineNumber, morphs, glosses):
        super().__init__()
        self.lineNumber = lineNumber
        self.morphs = morphs
        self.glosses = glosses


class TooManyGlossesError(Error):
    '''raised when there are more divisions on the glossing line
       than on the parsing line'''

    def __init__(self, lineNumber, morphs, glosses):
        super().__init__()
        self.lineNumber = lineNumber
        self.morphs = morphs
        self.glosses = glosses


class EmptyTiersError(Error):
    '''raised when there are fewer than two filled tiers'''

    def __init__(self, lineNumber):
        super().__init__()
        self.lineNumber = lineNumber


class MissingSpeechTiersError(Error):
    '''raised when there is nothing on the speech tier'''

    def __init__(self, lineNumber):
        super().__init__()
        self.lineNumber = lineNumber
