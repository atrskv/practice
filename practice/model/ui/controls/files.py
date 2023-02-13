from practice.utils import utils
from selene import Element

class Avatar:

    def __init__(self, element: Element):
        self.element = element

    def upload_avatar(self, jpeg_name):
        self.element.send_keys(utils.resource(jpeg_name))






