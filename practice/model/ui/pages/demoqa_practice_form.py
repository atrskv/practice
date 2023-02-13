from selene.support.shared import browser
from practice.model.ui.controls import (
    buttons,
    checkboxes,
    datepickers,
    dropdowns,
    radiobuttons,
    tables,
    tags_inputs,
    text_fields,
    files
    # ...
)


class StudentRegistrationForm:

    def open(self):
        browser.open('/automation-practice-form')





        return self

# def open():
#     browser.open('/automation-practice-form')
#
#
# def set_name(name):
#     (
#         text_fields
#         .type_name(
#             browser.element('#firstName'), name)
#     )
#
# def set_lastname(lastname):
#     (
#         text_fields.type_lastname(
#         browser.element('#lastName'), lastname)
#     )
#
# def set_email(email):
#     (
#         text_fields.type_email(
#         browser.element('#userEmail'), email)
#     )
#
# def set_phone(phone):
#     (
#         text_fields.type_phone(
#         browser.element('#userNumber'), phone)
#     )
#
#
# def set_address(address):
#     (
#         text_fields.type_address(
#         browser.element('#currentAddress'), address)
#     )
#
#
# def set_gender(gender):
#     (
#         radiobuttons.enable_gender_radio(
#         browser.all('[name=gender]'), gender)
#     )
#
#
# def set_bdate(day: str, month_index: str, year: str):
#     (
#         datepickers.select_year_by_click(
#         browser.element('#dateOfBirthInput'), year)
#     )
#
#     (
#         datepickers.select_month_by_click(
#         browser.element('#dateOfBirthInput'), month_index)
#     )
#
#     (
#         datepickers.select_day_by_click(
#         browser.element('#dateOfBirthInput'), day)
#     )
#
# def set_subjects(*tags):
#     (
#         tags_inputs.type_tags(
#         browser.element('#subjectsInput'), *tags)
#     )
#
# def set_hobbies(*hobbies):
#     (
#         checkboxes.enable_hobby_check(
#         browser.all('[for^=hobbies-checkbox]'), *hobbies)  # *hobbies
#     )
#
# def set_avatar(png_name):
#     (
#         upload_a_pictures.upload_avatar(
#         browser.element('#uploadPicture'), png_name)
#     )
#
# def set_birthplace(state, city):
#     (
#         dropdowns.select_state_by_click(
#         browser.element('#state'), state)
#     )
#
#     (
#         dropdowns.select_city_by_click(
#         browser.element('#city'), city)
#     )
#
# def submit():
#     (
#         buttons.submit(
#         browser.element('#submit'))
#     )


def should_be_filled(*texts):
    (
        tables.modal_content_should_have_values(
            browser.element('.modal-content').all('tr'),

            *texts

        )
    )

