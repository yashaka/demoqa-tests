
from selene.support.shared import browser
import selene


def rows(*, inside: selene.Browser | selene.Element = browser):
    return inside.all('tbody tr')
'''
# OR for python < 3.10
from typing import Union
def rows(*, inside: Union[selene.Browser, selene.Element] = browser):
    return inside.all('tbody tr')
'''
