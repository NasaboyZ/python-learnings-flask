# name = input("Enter your name: ")

# print(name)

size_input = input("how big is your house (in square feets): ")
square_feet = int(size_input)
squer_meter = square_feet  / 10.822
print(f"{square_feet} square feet is {squer_meter:,.2f} square meter")