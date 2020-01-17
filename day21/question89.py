class Person:
    pass


class Male(Person):
    def getGender(self):
        print("Male")


class Female(Person):
    def getGender(self):
        print("Female")


Male().getGender()
Female().getGender()
