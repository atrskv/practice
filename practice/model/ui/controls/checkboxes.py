from selene import have, Collection


class Checkbox:

    def __init__(self, all: Collection):
        self.all = all

    def enable_hobby_check(self, hobbies: list):

        for hobby in hobbies:
            self.all.element_by(have.text(hobby)).click()
