from selene.support.shared import browser
from practice.utils import utils
from practice.model import app
from practice.model import controls


def test_register_a_student(browser_management):

    app.form.open()

    utils.delete_interrupt_elements()

    (
        controls
        .TextField(browser.element('#firstName'))
        .type_name('Aleksei')
    )

    (
        controls
        .TextField(browser.element('#lastName'))
        .type_lastname('Torsukov')
    )

    (
        controls
        .TextField(browser.element('#userEmail'))
        .type_email('torsukov@gmail.com')
    )

    (
        controls
        .RadioButton(browser.all('[name=gender]'))
        .enable_gender_radio('Male')
    )

    (
        controls
        .TextField(browser.element('#userNumber'))
        .type_phone('8999123123')
    )

    (
        controls
        .DatePicker(browser.element('#dateOfBirthInput'))
        .select_year_by_click('2000')
    )

    (
        controls
        .DatePicker(browser.element('#dateOfBirthInput'))
        .select_month_by_click('3')
    )

    (
        controls
        .DatePicker(browser.element('#dateOfBirthInput'))
        .select_day_by_click('12')
    )

    (
        controls
        .TagsInput(browser.element('#subjectsInput'))
        .type_tags('Math', 'Computer Science')
    )

    (
        controls
        .Checkbox(browser.all('[for^=hobbies-checkbox]'))
        .enable_hobby_check('Sports', 'Music')
    )

    (
        controls
        .Avatar(browser.element('#uploadPicture'))
        .upload_avatar('cat.jpeg')
    )

    (
        controls
        .TextField(browser.element('#currentAddress'))
        .type_address('My address')
    )

    (
        controls
        .Dropdown(browser.element('#state'))
        .select_state_by_click('Uttar Pradesh')
    )

    (
        controls
        .Dropdown(browser.element('#city'))
        .select_city_by_click('Lucknow')
    )

    (
        controls
        .Button(browser.element('#submit'))
        .submit_registration_form()
    )

    (
        controls
        .Table(browser.element('.modal-content')
        .all('tr'))
        .table_should_have_values(

                    'Label Values',
            'Student Name Aleksei Torsukov',
            'Student Email torsukov@gmail.com',
            'Gender Male',
            'Mobile 8999123123',
            'Date of Birth 12 March,2000',
            'Subjects Maths, Computer Science',
            'Hobbies Sports, Music',
            'Picture cat.jpeg',
            'Address My address',
            'State and City Uttar Pradesh Lucknow'

        )
    )