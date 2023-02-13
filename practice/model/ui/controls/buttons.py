from selene import command, Element


class Button:
    def __init__(self, element: Element):
        self.element = element

    def submit_form(self):
        self.element.perform(command.js.click)
