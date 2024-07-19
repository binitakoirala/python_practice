#
# Write a function that takes a list of names and returns a list with each name capitalized.
#First Solution
names = ["binita" , "koirala"]
def capitalize_name(names):
    capitalized_name = []
    for name in names:
        capitalized_name.append(name.title())
    return capitalized_name
capitalized_name = capitalize_name(names)
print(capitalized_name)


#Second Solution using List Comprehension
names = ["binita" , "koirala"]
capitalized_name = [name.title() for name in names]
# print(capitalized_name)
