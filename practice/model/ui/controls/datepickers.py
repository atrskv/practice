from selene import Element
from selene.support.shared import browser


class DatePicker:

    def __init__(self, element: Element):
        self.element = element


    def select_year_by_click(self, year):
        self.element.click()
        browser.element('.react-datepicker__year-select').element(f'[value="{year}"]').click()
        return self

    def select_month_by_click(self, month: str):
        month_index = int(month) - 1
        browser.element('.react-datepicker__month-select').element(f'[value="{str(month_index)}"]').click()
        return self

    def select_day_by_click(self, day):
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self
#
# (
#     controls.datepickers.select_month_by_click(
#     browser.element('#dateOfBirthInput'), month_index='5')
# )
#
# (
#     controls.datepickers.select_day_by_click(
#     browser.element('#dateOfBirthInput'), day='13')
# )
#
#
# def select_day_by_click(selector: Element, day='11'):
#     selector.click()
#     browser.element(f'.react-datepicker__day--0{day}').click()
#
#
# def select_month_by_click(selector: Element, month_index='3'):
#     selector.click()
#     browser.element('.react-datepicker__month-select').element(f'[value="{month_index}"]').click()
#
#
# def select_year_by_click(selector: Element, year='2000'):
#     selector.click()
#     browser.element('.react-datepicker__year-select').element(f'[value="{year}"]').click()
