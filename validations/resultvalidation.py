import pytest

class validationResult:


    def linksContainsWord(links,phrase):
        if(bool(links)):
            matcher= [t for t in links if phrase.lower() in t.lower()]
            size=len(matcher)
        else:
            size=0

        assert size >0, phrase+' not found'
        