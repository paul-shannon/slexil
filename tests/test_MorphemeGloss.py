import sys
sys.path.append("..")
from morphemeGloss import *
#------------------------------------------------------------------------------------------------------------------------
sampleLines = ["HAB=3A=MOUTH•cry",
               "1S=walk–INC",
               "HAB=3A=work=IAM",
               "PROG=1A=know–INTR",
               "more",
               "1PRO",
               ]


#----------------------------------------------------------------------------------------------------
grammaticalTermsFiles = ["../testData/monkeyAndThunder/grammaticalTerms.txt",
                         "../testData/inferno-threeLines/grammaticalTerms.txt"]
grammaticalTerms = []
for file in grammaticalTermsFiles:
   newTerms = open(file).read().split("\n")
   grammaticalTerms += newTerms[:-1]


#----------------------------------------------------------------------------------------------------
def runTests():

    test_constructor()
    test_parse()
    test_inferno()
    test_toHTML_sampleLine_0()
    test_toHTML_sampleLine_1()
    test_toHTML_sampleLine_2()
    test_toHTML_sampleLine_3()
    test_toHTML_sampleLine_4()
    test_toHTML_sampleLine_5()


def test_constructor():

    #grammaticalTerms = open(grammaticalTermsFile).read().split("\n")
    mg = MorphemeGloss(sampleLines[0], grammaticalTerms)

def test_parse():

    #grammaticalTerms = open(grammaticalTermsFile).read().split("\n")
    mg = MorphemeGloss(sampleLines[0], grammaticalTerms)
    mg.parse()
    assert(mg.getParts() == ['HAB', '=', '3', 'A', '=', 'MOUTH', '•', 'cry'])

def test_toHTML_sampleLine_0(displayPage=False):
    """
      create an empty htmlDoc, then render the MorhphemeGloss into it
    """
    print("--- test_toHTML_sampleLine_0")

    #grammaticalTerms = open(grammaticalTermsFile).read().split("\n")
    mg = MorphemeGloss(sampleLines[0], grammaticalTerms)
    mg.parse()
    assert(mg.getParts() == ['HAB', '=', '3', 'A', '=', 'MOUTH', '•', 'cry'])

    htmlDoc = Doc()

    htmlDoc.asis('<!DOCTYPE html>')
    with htmlDoc.tag('html', lang="en"):
        with htmlDoc.tag('head'):
            htmlDoc.asis('<link rel="stylesheet" href="ijal.css">')
            with htmlDoc.tag('body'):
                mg.toHTML(htmlDoc)

    htmlText = htmlDoc.getvalue()
    assert(htmlText.count('<span class="grammatical-term">') == 3)  # HAB, A, MOUTH

    if(displayPage):
        f = open("morphemeGloss.html", "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % "morphemeGloss.html")

def test_toHTML_sampleLine_1(displayPage=False):
    """
      create an empty htmlDoc, then render the MorhphemeGloss into it
    """
    print("--- test_toHTML_sampleLine_1")

    #grammaticalTerms = open(grammaticalTermsFile).read().split("\n")
    mg = MorphemeGloss(sampleLines[1], grammaticalTerms)
    mg.parse()
    assert(mg.getParts() == ['1', 'S', '=', 'walk', '–', 'INC'])

    htmlDoc = Doc()

    htmlDoc.asis('<!DOCTYPE html>')
    with htmlDoc.tag('html', lang="en"):
        with htmlDoc.tag('head'):
            htmlDoc.asis('<link rel="stylesheet" href="ijal.css">')
            with htmlDoc.tag('body'):
                mg.toHTML(htmlDoc)

    htmlText = htmlDoc.getvalue()
    assert(htmlText.count('<span class="grammatical-term">') == 2)  # S  INC

    if(displayPage):
        f = open("morphemeGloss.html", "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % "morphemeGloss.html")

def test_toHTML_sampleLine_2(displayPage=False):
    """
      create an empty htmlDoc, then render the MorhphemeGloss into it
    """
    print("--- test_toHTML_sampleLine_2")

    #grammaticalTerms = open(grammaticalTermsFile).read().split("\n")
    mg = MorphemeGloss(sampleLines[2], grammaticalTerms)
    mg.parse()
    mg.getParts()
    assert(mg.getParts() == ['HAB', '=', '3', 'A', '=', 'work', '=', 'IAM'])

    htmlDoc = Doc()

    htmlDoc.asis('<!DOCTYPE html>')
    with htmlDoc.tag('html', lang="en"):
        with htmlDoc.tag('head'):
            htmlDoc.asis('<link rel="stylesheet" href="ijal.css">')
            with htmlDoc.tag('body'):
                mg.toHTML(htmlDoc)

    htmlText = htmlDoc.getvalue()
    assert(htmlText.count('<span class="grammatical-term">') == 3)  # HAB A IAM

    if(displayPage):
        f = open("morphemeGloss.html", "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % "morphemeGloss.html")

def test_toHTML_sampleLine_3(displayPage=False):
    """
      create an empty htmlDoc, then render the MorhphemeGloss into it
    """
    print("--- test_toHTML_sampleLine_3")

    #grammaticalTerms = open(grammaticalTermsFile).read().split("\n")
    mg = MorphemeGloss(sampleLines[3], grammaticalTerms)
    mg.parse()
    mg.getParts()
    assert(mg.getParts() == ['PROG', '=', '1', 'A', '=', 'know', '–', 'INTR'])

    htmlDoc = Doc()

    htmlDoc.asis('<!DOCTYPE html>')
    with htmlDoc.tag('html', lang="en"):
        with htmlDoc.tag('head'):
            htmlDoc.asis('<link rel="stylesheet" href="ijal.css">')
            with htmlDoc.tag('body'):
                mg.toHTML(htmlDoc)

    htmlText = htmlDoc.getvalue()
    assert(htmlText.count('<span class="grammatical-term">') == 3)  # PROG A INTR

    if(displayPage):
        f = open("morphemeGloss.html", "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % "morphemeGloss.html")

def test_toHTML_sampleLine_4(displayPage=False):
    """
      create an empty htmlDoc, then render the MorhphemeGloss into it
    """
    print("--- test_toHTML_sampleLine_4")

    #grammaticalTerms = open(grammaticalTermsFile).read().split("\n")
    mg = MorphemeGloss(sampleLines[4], grammaticalTerms)
    mg.parse()
    mg.getParts()
    assert(mg.getParts() == ['more'])

    htmlDoc = Doc()

    htmlDoc.asis('<!DOCTYPE html>')
    with htmlDoc.tag('html', lang="en"):
        with htmlDoc.tag('head'):
            htmlDoc.asis('<link rel="stylesheet" href="ijal.css">')
            with htmlDoc.tag('body'):
                mg.toHTML(htmlDoc)

    htmlText = htmlDoc.getvalue()
    assert(htmlText.count('<span class="grammatical-term">') == 0)  # none in this gloss

    if(displayPage):
        f = open("morphemeGloss.html", "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % "morphemeGloss.html")


def test_toHTML_sampleLine_5(displayPage=False):
    """
      create an empty htmlDoc, then render the MorhphemeGloss into it
    """
    print("--- test_toHTML_sampleLine_5")

    #grammaticalTerms = open(grammaticalTermsFile).read().split("\n")
    mg = MorphemeGloss(sampleLines[5], grammaticalTerms)
    mg.parse()
    mg.getParts()
    assert(mg.getParts() == ['1', 'PRO'])

    htmlDoc = Doc()

    htmlDoc.asis('<!DOCTYPE html>')
    with htmlDoc.tag('html', lang="en"):
        with htmlDoc.tag('head'):
            htmlDoc.asis('<link rel="stylesheet" href="ijal.css">')
            with htmlDoc.tag('body'):
                mg.toHTML(htmlDoc)

    htmlText = htmlDoc.getvalue()
    assert(htmlText.count('<span class="grammatical-term">') == 1)  # PRO

    if(displayPage):
        f = open("morphemeGloss.html", "w")
        f.write(indent(htmlText))
        f.close()
        os.system("open %s" % "morphemeGloss.html")


def test_inferno(displayPage=False):
    """
      a bunch of new terms came with this text.  test them all out here
    """
    print("--- test_inferno")

    mg = MorphemeGloss("in=DEF-MASC-SG", grammaticalTerms)
    mg.parse()
    assert(mg.getParts() == ['in', '=', 'DEF', '-', 'MASC', '-', 'SG'])

    mg = MorphemeGloss("middle-MASC", grammaticalTerms); mg.parse()
    assert(mg.getParts() == ['middle', '-', 'MASC'])

    mg = MorphemeGloss("of=DEF-MASC-SG", grammaticalTerms); mg.parse();
    assert(mg.getParts() == ['of', '=', 'DEF', '-', 'MASC', '-', 'SG'])

    mg = MorphemeGloss("journey-MASC", grammaticalTerms); mg.parse();
    assert(mg.getParts() == ['journey', '-', 'MASC'])

    mg = MorphemeGloss("our-FEM-SG", grammaticalTerms); mg.parse();
    assert(mg.getParts() == ['our', '-', 'FEM', '-', 'SG'])

    mg = MorphemeGloss("life-FEM", grammaticalTerms); mg.parse();
    assert(mg.getParts() == ['life', '-', 'FEM'])

    mg = MorphemeGloss("be-3SG-IMPF", grammaticalTerms); mg.parse();
    assert(mg.getParts() == ['be', '-', '3', 'SG', '-', 'IMPF'])

    mg = MorphemeGloss("found–1SG-INDEF-REM-PAST", grammaticalTerms); mg.parse();
    assert(mg.getParts() ==  ['found', '–', '1', 'SG', '-', 'INDEF', '-', 'REM', '-', 'PAST'])



if __name__ == '__main__':
    runTests()

