class Cat:
    def __init__(self, name, age, color, gender):
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender

kitty = Cat("kitty", 7, "brown", "male")
pishi = Cat("pishi", 2, "black", "female")

print(pishi.name)
print(kitty.color)
