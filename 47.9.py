start = 0

while start <= 100:
    print(start)
    command =input("bazam boro bala:\n")
    if command == "bala":
        start += 1
    if command == "payin":
        start -= 1
    elif command == "hichkodam":
        break

print("khodahafez")
