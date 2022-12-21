from demoqa_tests import app


def test_register_admin():
    app.main.given_opened()
    app.given_opened()

    app.pages.main.open_registration_form()

    app.wait_for_loading()
