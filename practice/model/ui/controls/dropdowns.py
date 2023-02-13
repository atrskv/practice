from selene.support.shared import browser
from selene import have, Element


class Dropdown:

    def __init__(self, element: Element):
        self.element = element


    def select_state_by_click(self, state):
        self.element.click()
        browser.all('[id*=react-select-3-option]').element_by(have.text(state)).click()


    def select_city_by_click(self, city):
        self.element.click()
        browser.all('[id*=react-select-4-option]').element_by(have.text(city)).click()



