import datetime

from demoqa_tests.model.data import user
from demoqa_tests.model.pages import practice_page


def test_submit_filled_form():
    practice_page.open()

    practice_page.fill_name('Lev', 'Zavodskov')
    practice_page.fill_email('lev@zavodskov.xyz')
    practice_page.fill_gender(user.Gender.Male)
    practice_page.fill_phone('7000000000')
    practice_page.fill_birthday(datetime.date(1997, 7, 29))
    '''
    # not needed in this test, but just for example
    practice_page.assert_filled_birthday(datetime.date(1997, 7, 29))
    '''
    practice_page.fill_subjects('Maths', 'English', 'Computer Science')
    practice_page.fill_hobbies(user.Hobby.Music, user.Hobby.Reading)
    practice_page.select_picture('../resources/picture.png')
    practice_page.fill_address('Country/State/City/Street/ Street num')
    practice_page.select_state('NCR')
    practice_page.select_city('Gurgaon')
    practice_page.submit_form()

    practice_page.assert_form_sent(
        ('Student Name', 'Lev Zavodskov'),
        ('Student Email', 'lev@zavodskov.xyz'),
        ('Gender', user.Gender.Male.name),
        ('Mobile', '7000000000'),
        ('Date of Birth', datetime.date(1997, 7, 29)),
        ('Subjects', 'Maths, English, Computer Science'),
        ('Hobbies', f'{user.Hobby.Music.value}, {user.Hobby.Reading.value}'),
        ('Picture', 'picture.png'),
        ('Address', 'Country/State/City/Street/ Street num'),
        ('State and City', 'NCR Gurgaon'),
    )
