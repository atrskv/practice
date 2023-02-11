from selene import Element
from selene.support.shared import browser


def select_day_by_click(selector: Element, day='11'):
    selector.click()
    browser.element(f'.react-datepicker__day--0{day}').click()


def select_month_by_click(selector: Element, month_index='3'):
    selector.click()
    browser.element('.react-datepicker__month-select').element(f'[value="{month_index}"]').click()


def select_year_by_click(selector: Element, year='2000'):
    selector.click()
    browser.element('.react-datepicker__year-select').element(f'[value="{year}"]').click()
