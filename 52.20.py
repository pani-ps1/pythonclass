class a:
    def __init__(self,name):
        self.name = name

class b(a):
    def __init__(self, name):
        super().__init__(name)

class c(b):
    def __init__(self, name):
        super().__init__(name)


giah = c("chaman")
giah = b("gol")

print(giah.name)
