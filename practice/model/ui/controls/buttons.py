from selene import command, Element


def submit(selector: Element):
    selector.perform(command.js.click)
