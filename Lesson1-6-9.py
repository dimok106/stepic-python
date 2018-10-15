class LoggableList(list, Loggable):
    def append(self, object):
        super().log(object)
        super().append(object)
