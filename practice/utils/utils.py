from selene.support.shared import browser

from faker import Faker
from faker.providers.phone_number import Provider

def delete_interrupt_adds():

    '''
    For delete google adds
    '''

    browser.driver.execute_script('document.querySelector(".Advertisement-Section").remove')


def resource(path):
    import practice
    from pathlib import Path
    return str(
        Path(practice.__file__)
        .parent
        .parent
        .joinpath(f'practice/resources/{path}')
    )



from faker import Faker


from faker.providers.phone_number import Provider

class RussiaPhoneNumberProvider(Provider):

    def russia_phone_number(self):
        return f'8{self.msisdn()[4:]}'



