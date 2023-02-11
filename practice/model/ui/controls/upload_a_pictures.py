from practice.utils import utils
from selene import Element


def upload_avatar(selector: Element, png_name: str):
    selector.send_keys(utils.resource(png_name))
