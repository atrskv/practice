from selene import command
from selene.support.shared import browser
from utils.utils import delete_interrupt_elements, resource
from selene import have


def test_register_a_student(browser_management):

    # GIVEN:
    browser.open('/automation-practice-form')

    delete_interrupt_elements()

    # WHEN:
    browser.element('#firstName').type('Aleksei')

    browser.element('#lastName').type('Torsukov')

    browser.element('#userEmail').type('torsukov@gmail.com')

    male = browser.element('label[for="gender-radio-2"]')
    male.click()

    browser.all('[name=gender]').element_by(have.value('Male')).perform(command.js.click)

    phone = browser.element('#userNumber')
    phone.type('89996666666')

    calendar = browser.element('#dateOfBirthInput')
    calendar.click()

    browser.element('.react-datepicker__month-select').element('[value="0"]').click()
    browser.element('.react-datepicker__year-select').element('[value="2000"]').click()
    browser.element('.react-datepicker__day--019').click()

    subjects = browser.element('#subjectsInput')
    subjects.type('Maths').press_tab()

    sport_hobbie = browser.element('[for="hobbies-checkbox-1"]')
    sport_hobbie.click()

    avatar = browser.element('#uploadPicture')
    avatar.send_keys(resource('cat.jpeg'))

    browser.element('#currentAddress').type('My address')

    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()

    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()

    browser.element('#submit').click()

    # THEN:
    table_rows = browser.element('.modal-content').all('tr')
    result = table_rows.should(have.texts(
        'Label Values',
        'Student Name Aleksei Torsukov',
        'Student Email torsukov@gmail.com',
        'Gender Male',
        'Mobile 8999666666',
        'Date of Birth 19 January,2000',
        'Subjects Maths',
        'Hobbies Sports',
        'Picture cat.jpeg',
        'Address My address',
        'State and City Uttar Pradesh Lucknow'))
