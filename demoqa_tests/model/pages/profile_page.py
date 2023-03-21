from selene import have

from demoqa_tests.data.users import User


class ProfilePage:
    ...

    def should_have_data(self, user: User):
        self.full_name.should(have.text(user.full_name))
