from . import controls
from .pages import (personal_info_form, practice_form, main)

def given_opened():
    pages.main.given_opened()

def wait_for_loading():
    controls.progress_bar.wait_for_loading()
