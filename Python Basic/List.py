# Creating a FruitsList with
# the use of multiple values
FruitsList = ["mango", "banana", "cherry", "Papaya", "Grapes",
              "Pomegranate", "Lychee", "Watermelon", "Strawberry", "Plum","Kiwi","Lime","Lemon"]
# print("\nList containing Fruits name: ")
# print(FruitsList)

# # accessing a element from the FruitsList using index number
# print("Accessing element from the FruitsList")
# print("The First Fruit of the List is:",FruitsList[0])
# print("The 2nd Fruit of the List is:",FruitsList[2])


# print("Accessing element using negative indexing")
# # print the last element of FruitsList
# print("The Last Fruit of the List is:",FruitsList[-1])

# # print the third last element of FruitsList
# print("The 3rd Last Fruit of the List is:",FruitsList[-3])

find_Fruits=input("Enter the fruit name which you want to buy :")

if find_Fruits in FruitsList:(
        print("Hey ! Congo We have your item :",find_Fruits)
)
else:
    print("Sorry we don't have ",find_Fruits)