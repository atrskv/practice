from selene.support.shared import browser

from practice.model.ui.controls.text_fields import TextField
from practice.model.ui.controls.radiobuttons import RadioButton
from practice.model.ui.controls.datepickers import DatePicker
from practice.model.ui.controls.tags_inputs import TagsInput
from practice.model.ui.controls.checkboxes import Checkbox
from practice.model.ui.controls.files import Avatar
from practice.model.ui.controls.dropdowns import Dropdown
from practice.model.ui.controls.buttons import Button
from practice.model.ui.controls.tables import Table


class StudentRegistrationForm:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def set_name(self, firstname, lastname):
        TextField(browser.element('#firstName')).type_name(firstname)
        TextField(browser.element('#lastName')).type_lastname(lastname)
        return self

    def set_email(self, email):
        TextField(browser.element('#userEmail')).type_email(email)
        return self

    def set_gender(self, gender):
        RadioButton(browser.all('[name=gender]')).enable_gender_radio(gender)
        return self

    def set_phone(self, phone):
        TextField(browser.element('#userNumber')).type_phone(phone)
        return self

    def set_bdate(self, bdate: list):
        DatePicker(browser.element('#dateOfBirthInput')).select_year_by_click(bdate[2])
        DatePicker(browser.element('#dateOfBirthInput')).select_month_by_click(bdate[1])
        DatePicker(browser.element('#dateOfBirthInput')).select_day_by_click(bdate[0])
        return self

    def set_subjects(self, tags: list):
        TagsInput(browser.element('#subjectsInput')).type_tags(tags)
        return self

    def set_hobbies(self, hobbies: list):
        Checkbox(browser.all('[for^=hobbies-checkbox]')).enable_hobby_check(hobbies)
        return self


    def set_avatar(self, jpeg_name):
        Avatar(browser.element('#uploadPicture')).upload_avatar(jpeg_name)
        return self


    def set_address(self, address):
        TextField(browser.element('#currentAddress')).type_address(address)
        return self

    def set_birthplace(self, state, city):
        Dropdown(browser.element('#state')).select_state_by_click(state)
        Dropdown(browser.element('#city')).select_city_by_click(city)
        return self


    def submit(self):
        Button(browser.element('#submit')).submit_form()
        return self

class ModalDialog:
        def __init__(self):
            self.element = browser.element('.modal-content')
            self.table = Table(browser.element('.modal-content').all('tr'))

        def modal_content_should_have_values(self, *values):
            self.table.table_should_have_values(*values)
            return self


