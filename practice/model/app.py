'''
one entry point for pages
'''

from practice.model.ui.pages.demoqa_practice_form import StudentRegistrationForm, ModalDialog
from practice.model.ui.pages.demoqa_textbox import Textboxes, Output


class Application:
    form = StudentRegistrationForm()
    modal_dialog = ModalDialog()
    textboxes = Textboxes()
    output = Output()

