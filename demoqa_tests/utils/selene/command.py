from selene import command
from selene.core.wait import Command


class js(command.js):
    scroll_one_page = Command(
        'scroll one page',
        lambda browser: browser.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)'
        ),
    )
