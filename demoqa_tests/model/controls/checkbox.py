from selene import have


def check_options(elements, *options: str):
    for option in options:
        elements.by(have.exact_text(option)).first.element('..').click()
