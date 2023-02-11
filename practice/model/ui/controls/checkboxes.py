from selene import have, Collection


def enable_hobby_check(selector: Collection, *hobbies):

    for hobby in hobbies:
        selector.element_by(have.text(hobby)).click()
