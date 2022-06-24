from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def given_opened_text_box():
    browser.open('/text-box')
    (
        ss('[id^=google_ads][id$=container__]').with_(timeout=10)
        .should(have.size_greater_than_or_equal(2))
        .perform(command.js.remove)
    )


def test_submit_form():
    given_opened_text_box()

    s('#userName').type('yasha')
    s('#userEmail').type('yashaka@gmail.com')
    s('#currentAddress').type('Earth')
    s('#permanentAddress').type('Universe & abroad')
    s('#submit').click()

    ss('#output p').should(have.texts(
        'yasha',
        'yashaka@gmail.com',
        'Earth',
        'Universe & abroad',
    ))

