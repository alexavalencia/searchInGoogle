import pytest
from pages.search import SearchPage
from pages.result import  ResultPage
from validations.resultvalidation import validationResult

@pytest.mark.parametrize('phrase',['LendingFront','ラララ - ヤングガンガ fgfdsgfdg','panda'])
def test_basic_google_search(browser,phrase):
    search_page=SearchPage(browser)
    result_page=ResultPage(browser)
    search_page.load()
    search_page.search(phrase)
    titles=result_page.result_link_title()
    validationResult.linksContainsWord(titles,phrase)
 