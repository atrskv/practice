from selene import have, Collection


def modal_content_should_have_values(selector: Collection, *texts_in_rows):
    selector.should(have.texts(texts_in_rows))
