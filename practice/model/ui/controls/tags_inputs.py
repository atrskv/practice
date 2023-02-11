from selene import command


def type_tags(selector, *tags):
    selector.perform(command.js.scroll_into_view)
    selector.perform(command.js.click)

    for tag in tags:
        selector.type(tag).press_tab()



