# # magic number act
# number = 3

# while True:
#     user_input = input("Möchten Sie spielen? (y/n): ")
#     if user_input == 'n':
#         print("Auf Wiedersehen!")
#         break
    
#     user_number = int(input("Rate unsere Zahl: "))
#     if user_number == number:
#         print("Sie haben richtig geraten!")
#     elif abs(user_number - number) == 1:  #abs ist die absolute wert von der differenz zwischen user_number und number
#         print("Sie lagen nur um 1 daneben!")
#     else:
#         print("Leider falsch!")
#     print("Danke fürs Spielen!")


# friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]

# for friend in friends:
#     print(f"you have {friend} is my friend")

grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

print(total / amount)
