from selene import have, command,Collection


def enable_gender_radio(selector: Collection, gender='Male'):
    selector.element_by(have.value(gender)).perform(command.js.click)
