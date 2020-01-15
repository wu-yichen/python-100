class custom_exception(Exception):
    def __init__(self, string):
        self.string = string


raise custom_exception("this is my custom exception")
