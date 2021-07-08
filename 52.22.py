class number:
    def __init__(self, value):
        self.value = value + 0.5

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        return self.value+ other.value

n1 = number(2)
n2 = number(2)

print(n1 + n2)
