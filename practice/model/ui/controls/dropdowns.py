from selene.support.shared import browser
from selene import have, Element


def select_state_by_click(selector: Element, state='Uttar Pradesh'):
    selector.click()
    browser.all('[id*=react-select-3-option]').element_by(have.text(state)).click()


def select_city_by_click(selector, city='Lucknow'):
    selector.click()
    browser.all('[id*=react-select-4-option]').element_by(have.text(city)).click()
