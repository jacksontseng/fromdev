

favorite = raw_input("what's your favorite:")
least = raw_input("what's your least favorite food:")
def speak(favorite,times):

    favorite= favorite.upper()
    vowels = 'AEIOU'

    for c in favorite:
        if c in vowels:
            favorite = favorite.replace(c, (c * times))
    favorite += (times*'!')
    print favorite

speak(favorite,10)
speak(least,5)

"""
empty_list = []
dessert = ['ice cream']
groceries = ['eggs', 'milk', 'butter', dessert]

print groceries

print groceries[1:3] # range from index 2 to 4
"""
