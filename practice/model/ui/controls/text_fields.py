from selene import Element


def type_name(selector: Element, name='Alex'):
    selector.type(name)


def type_lastname(selector: Element, lastname='Torrie'):
    selector.type(lastname)


def type_email(selector: Element, email='trrskv@aol.com'):
    selector.type(email)


def type_phone(selector: Element, phone: str):
    selector.type(phone)


def type_address(selector: Element, address: str):
    selector.type(address)
