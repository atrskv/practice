from selene import Element

class TextField:

    def __init__(self, element: Element):
        self.element = element

    def type_name(self, name):
        self.element.type(name)
        return self

    def type_lastname(self, lastname):
        self.element.type(lastname)
        return self

    def type_email(self, email):
        self.element.type(email)
        return self

    def type_phone(self, phone):
        self.element.type(phone)
        return self

    def type_address(self, address):
        self.element.type(address)







#
# def type_name(selector: Element, name='Alex'):
#     selector.type(name)
#
#
# def type_lastname(selector: Element, lastname='Torrie'):
#     selector.type(lastname)
#
#
# def type_email(selector: Element, email='trrskv@aol.com'):
#     selector.type(email)
#
#
# def type_phone(selector: Element, phone: str):
#     selector.type(phone)


def type_address(selector: Element, address: str):
    selector.type(address)
