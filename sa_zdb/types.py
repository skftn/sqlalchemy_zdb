from sqlalchemy.types import UserDefinedType


class _ZdbDomain(UserDefinedType):
    """
    phrases/fulltext/fulltext_with_shingles are postgres DOMAIN's
    that sits on top of the standard text datatype. As far as
    Postgres is concerned, it is functionally no different than
    the text datatype, however they have special meaning to
    ZomboDB when indexing and searching. In brief, they indicate
    that such fields should be analyzed.
    """
    def __init__(self, *args):
        self._args = args

    def convert_bind_param(self, value, engine):
        return value

    def convert_result_value(self, value, engine):
        return value

    @property
    def python_type(self):
        return str


class Phrase(_ZdbDomain):
    def __init__(self, *args):
        super(Phrase, self).__init__(*args)

    def get_col_spec(self):
        return "phrase"

    def is_mutable(self):
        return True


class Fulltext(_ZdbDomain):
    def __init__(self, *args):
        super(Fulltext, self).__init__(*args)

    def get_col_spec(self):
        return "fulltext"

    def is_mutable(self):
        return True


class FulltextWithShingles(_ZdbDomain):
    def __init__(self, *args):
        super(FulltextWithShingles, self).__init__(*args)

    def get_col_spec(self):
        return "fulltext_with_shingles"

    def is_mutable(self):
        return True
