from selene import have
from selene.support.shared import browser
from practice.model.ui.controls.text_fields import TextField
from practice.model.ui.controls.buttons import Button



class Textboxes:

    def open(self):
        browser.open('/text-box')

    def set_full_name(selfm, name):
        TextField(browser.element('#userName')).type_name(name)

    def set_email(self, email):
        TextField(browser.element('#userEmail')).type_email(email)

    def set_current_address(self,address):
        TextField(browser.element('#currentAddress')).type_address(address)

    def set_permanent_address(self, permanent_address):
        TextField(browser.element('#permanentAddress')).type_address(permanent_address)

    def submit(self):
        Button(browser.element('#submit')).submit_form()

class Output:
    def __init__(self):
        self.name = browser.element('#name')
        self.email = browser.element('#email')

    def should_have_exact_name(self, name):
        self.name.should(have.exact_text(name))

    def should_have_exact_email(self, email):
        self.email.should(have.exact_text(email))


