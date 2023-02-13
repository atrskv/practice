from selene import command, Element


class TagsInput:
    def __init__(self, element: Element):
        self.element = element

    def type_tags(self, *tags):
        self.element.perform(command.js.scroll_into_view)
        self.element.perform(command.js.click)

        for tag in tags:
            self.element.type(tag).press_tab()




# (
    #     controls.tags_inputs.type_tags(
    #     browser.element('#subjectsInput'), 'Math', 'Computer Science')  # *tags
    # )
    #