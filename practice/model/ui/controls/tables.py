from selene import have, Collection


class Table:
    def __init__(self, all: Collection):
        self.rows = all

    def table_should_have_values(self, *texts_in_rows):
        self.rows.should(have.texts(texts_in_rows))
