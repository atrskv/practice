# from selene.support.shared import browser
from practice.utils import utils
from practice.model import app

# from practice.model import controls


def test_register_a_student(browser_management):

    (
        app
        .form
        .open()
    )

    utils.delete_interrupt_elements()

    (
        app
        .form
        .set_name('Aleksei', 'Torsukov')
    )

    (
        app
        .form
        .set_email('torsukov@gmail.com')
    )

    (
        app
        .form
        .set_gender('Male')
    )

    (
        app
        .form
        .set_phone('8999123123')
    )

    (
        app
        .form
        .set_bdate('12', '3', '2000')
    )

    (
        app
        .form
        .set_subjects('Math', 'Computer Science')
    )

    (
        app
        .form
        .set_hobbies('Sports', 'Music')
    )

    (
        app
        .form
        .set_avatar('cat.jpeg')
    )

    (
        app
        .form
        .set_address('My address')
    )

    (
        app
        .form
        .set_birthplace('Uttar Pradesh', 'Lucknow')
    )

    (
        app
        .form
        .submit()
    )

    (
        app
        .modal_dialog
        .modal_content_should_have_values(

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

def test_fill_the_textboxes(browser_management):

    (
        app
        .textboxes
        .open()
    )

    (
        app
        .textboxes
        .set_full_name('Aleksei Torsukov')
    )

    (
        app
        .textboxes
        .set_email('torsukov@gmail.com')
    )

    (
        app
        .textboxes
        .set_current_address('My address')
    )

    (
        app
        .textboxes
        .set_permanent_address('My permanent_address')
    )

    (
        app
        .textboxes
        .submit()
    )

    # THEN:
    (
        app
        .output
        .should_have_exact_name('Name:Aleksei Torsukov')
    )

    (
        app
        .output
        .should_have_exact_email('Email:torsukov@gmail.com')
    )

    # ...