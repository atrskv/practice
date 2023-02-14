# from practice.model import controls
from practice.utils import utils
from practice.model.app import Application
from data.users import Student


def test_register_a_student(browser_management):

    # GIVEN:
    (
        Application
        .form
        .open()
    )

    utils.delete_interrupt_adds()

    # WHEN:
    (
        Application
        .form
        .set_name(Student.firstname, Student.lastname)
        .set_email(Student.email)
        .set_gender(Student.gender)
        .set_phone(Student.phone)
        .set_bdate(Student.bdate)
        .set_subjects(Student.subjects)
        .set_hobbies(Student.hobbies)
        .set_avatar(Student.avatar)
        .set_address(Student.address)
        .set_birthplace(Student.state, Student.city)
        .submit()
    )

    # THEN:
    (
        Application
        .modal_dialog
        .modal_content_should_have_values(
                    'Label Values',
                    f'Student Name {Student.firstname} {Student.lastname}',
                    f'Student Email {Student.email}',
                    f'Gender {Student.gender}',
                    f'Mobile {Student.phone}',
                    f'Date of Birth {Student.bdate[0]} March,{Student.bdate[2]}',  # BUG? The type of writing of the month may not be correct
                    f'Subjects {Student.subjects[0]}, {Student.subjects[1]}',
                    f'Hobbies {Student.hobbies[0]}, {Student.hobbies[1]}',
                    f'Picture {Student.avatar}',
                    f'Address {Student.address}',
                    f'State and City {Student.state} {Student.city}'
        )
    )

# def test_fill_the_textboxes(browser_management):
#
#     (
#         Application
#         .textboxes
#         .open()
#     )
#
#     (
#         Application
#         .textboxes
#         .set_full_name('Aleksei Torsukov')
#     )
#
#     (
#         Application
#         .textboxes
#         .set_email('torsukov@gmail.com')
#     )
#
#     (
#         Application
#         .textboxes
#         .set_current_address('My address')
#     )
#
#     (
#         Application
#         .textboxes
#         .set_permanent_address('My permanent_address')
#     )
#
#     (
#         Application
#         .textboxes
#         .submit()
#     )
#
#     # THEN:
#     (
#         Application
#         .output
#         .should_have_exact_name('Name:Aleksei Torsukov')
#     )
#
#     (
#         Application
#         .output
#         .should_have_exact_email('Email:torsukov@gmail.com')
#     )
#
#     # ...