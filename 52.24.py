class gentelman:
    def __init__(self, value):
        self.__value = value
    def show_value(self):
        return self.__value

    def update_value(self, new_value):
        if new_value != 7000000:
            self.__value = new_value
        else:
            self.__value = 6000000

daramad = gentelman(7000000)

print(daramad.show_value())
