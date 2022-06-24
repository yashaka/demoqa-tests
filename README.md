# QA.GURU Python Course. Group 01. Lesson 05 «Selene 50»

## Running tests from terminal with custom options

From unix terminal (under Windows you can use git bash at least):
```bash
env -S "selene.browser_name=firefox selene.hold_browser_open=True" pytest tests
```

The list of «customizable through command line options» can be found at `tests/conftest.py` ;)
