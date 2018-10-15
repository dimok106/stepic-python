class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def append(self, val):
        if val > 0:
            super().append( val)
        if val <= 0:
            raise NonPositiveError
