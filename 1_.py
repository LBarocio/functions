# funtions are ways to wrap your code into reusable units
# place () after the function name to invoke it 
#  ex min, max, square root 

# # define a function 
# def happy_birthday():
#     print("Happy birthday to you!")
#     print("You are old!")
#     print()

# # call a function 
# happy_birthday()
# happy_birthday()
# happy_birthday()


# # next
# #use a perameter
# # perameter is a placeholder while you call the function 
# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print()

# # argument is what is displayed 
# # ex bro is the argument 
# happy_birthday("bro", 20)
# happy_birthday("Manny", 18)
# happy_birthday("Lilly", 52)

# # If you want another argument you have to add another perameter 

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")


# display_invoice("MannySal", 42.40, "01/01")

# # Returning!
# # return = statement used to end a function and send a result back to the caller

# def add(x, y):
#     z = x + y 
#     return z

# def subtract(x, y):
#     z = x - y 
#     return z

# def multiply(x, y):
#     z = x * y 
#     return z

# def divide(x, y):
#     z = x / y 
#     return z

# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))

# function to create full name 

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("manny", "salgado")
print(full_name)