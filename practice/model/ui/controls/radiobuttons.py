from selene import have, command, Collection


class RadioButton:
    def __init__(self, all: Collection):
        self.all = all

    def enable_gender_radio(self, gender):
        self.all.element_by(have.value(gender)).perform(command.js.click)

# def enable_gender_radio(selector: Collection, gender='Male'):
#     selector.element_by(have.value(gender)).perform(command.js.click)
