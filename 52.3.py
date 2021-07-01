class Cat:
    name = ""
    age = 0

    def hello(self):
        print("meow!!")


kitty = Cat()
kitty.name = "kitty"
kitty.age = 2
kitty.color = "brown"
kitty.gender = "male"

pishi = Cat()
pishi.name = "pishi"
pishi.age = 3
pishi.color = "black"
pishi.gender = "female"

print(pishi.name)
print(kitty.color)
print(kitty.age)

pishi.hello()
