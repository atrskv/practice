from practice.utils import utils
from practice.model import app

# from practice.model import controls


def test_register_a_student(browser_management):

    (
        app.
        registration_form
        .open()
    )


    utils.delete_interrupt_elements()


    (
        app.
        registration_form
        .set_name('Aleksei')
    )

    (
        app.registration_form
        .set_lastname('Torsukov')
    )

    (
        app
        .registration_form
        .set_email('torsukov@gmail.com')
    )

    (
        app
        .registration_form
        .set_gender('Male')
    )

    (
        app
        .registration_form
        .set_phone('8999123123')
    )

    (
        app
        .registration_form
        .set_bdate('13', '5', '2000')
    )

    (
        app
        .registration_form
        .set_subjects('Math', 'Computer Science')
    )

    (
        app
        .registration_form
        .set_hobbies('Sports', 'Music')
    )

    (
        app
        .registration_form
        .set_avatar('cat.jpeg')
    )

    (
        app
        .registration_form
        .set_address('My address')
    )

    (
        app
        .registration_form
        .set_birthplace('Uttar Pradesh', 'Lucknow')
    )

    (
        app
        .registration_form
        .submit()
    )

    (
        app
        .registration_form
        .should_be_filled(

                    'Label Values',
            'Student Name Aleksei Torsukov',
            'Student Email torsukov@gmail.com',
            'Gender Male',
            'Mobile 8999123123',
            'Date of Birth 13 June,2000',
            'Subjects Maths, Computer Science',
            'Hobbies Sports, Music',
            'Picture cat.jpeg',
            'Address My address',
            'State and City Uttar Pradesh Lucknow'
            )
        )

# OR:
# def test_register_a_student(browser_management):

    # app.registration_form.open()
    #
    # utils.delete_interrupt_elements()
    #
    # (
    #     controls.text_fields
    #     .type_name(
    #     browser.element('#firstName'), name='Aleksei')
    # )
    #
    # (
    #     controls.text_fields.type_lastname(
    #     browser.element('#lastName'), lastname='Torsukov')
    # )
    #
    # (
    #     controls.text_fields.type_email(
    #     browser.element('#userEmail'), email='torsukov@gmail.com')
    # )
    #
    # (
    #     controls.radiobuttons.enable_gender_radio(
    #     browser.all('[name=gender]'), gender='Male')
    # )
    #
    # (
    #     controls.text_fields.type_phone(
    #     browser.element('#userNumber'), phone='8999123123')
    # )
    #
    # (
    #     controls.datepickers.select_year_by_click(
    #     browser.element('#dateOfBirthInput'), year='2000')
    # )
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
    # (
    #     controls.tags_inputs.type_tags(
    #     browser.element('#subjectsInput'), 'Math', 'Computer Science')  # *tags
    # )
    #
    # (
    #     controls.checkboxes.enable_hobby_check(
    #     browser.all('[for^=hobbies-checkbox]'), 'Sports', 'Music')  # *hobbies
    # )
    #
    # (
    #     controls.upload_a_pictures.upload_avatar(
    #     browser.element('#uploadPicture'), png_name='cat.jpeg')
    # )
    #
    # (
    #     controls.text_fields.type_address(
    #     browser.element('#currentAddress'), address='My address')
    # )
    #
    # (
    #     controls.dropdowns.select_state_by_click(
    #     browser.element('#state'), state='Uttar Pradesh')
    # )
    #
    # (
    #     controls.dropdowns.select_city_by_click(
    #     browser.element('#city'), city='Lucknow')
    # )
    #
    # (
    #     controls.buttons.submit(
    #     browser.element('#submit'))
    # )
    #
    # (
    #     controls.tables.modal_content_should_have_values(
    #     browser.element('.modal-content').all('tr'),
    #
    #         'Label Values',
    #         'Student Name Aleksei Torsukov',
    #         'Student Email torsukov@gmail.com',
    #         'Gender Male',
    #         'Mobile 8999123123',
    #         'Date of Birth 13 June,2000',
    #         'Subjects Maths, Computer Science',
    #         'Hobbies Sports, Music',
    #         'Picture cat.jpeg',
    #         'Address My address',
    #         'State and City Uttar Pradesh Lucknow'
    #     )
    # )
