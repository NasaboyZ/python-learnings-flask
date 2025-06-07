# # friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]

# # print("Jen" in friends)



# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter something you've watched recently: ")
# print(user_movie in movies_watched)



# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter something you've watched recently: ")

# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too!")
# else:
#     print("I haven't watched that yet.")


# magic number act
number = 3
user_input = input("enter 'y' if you would like to play: ")

if user_input in ["y", "Y"]:
    user_number = int(input("guess our number: "))
    if user_number == number:
        print("you guessed correctly!")
    elif abs(user_number - number) == 1:  #abs ist die absolute wert von der differenz zwischen user_number und number
        print("you were off by one")
    else:
        print("sorry, it's wrong!")
    print("thanks for playing!")
else:
    print("okay, bye!")