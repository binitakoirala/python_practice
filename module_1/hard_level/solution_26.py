#
# Write a program that asks the user to enter a word and then prints the word in reverse.
# word = input("Enter a word to reverse: ")
# reverse = word[::-1]
# print(reverse)


word = input("Enter a word to reverse: ")

reverse = " "

for i in range(len(word) -1, -1, -1):
    reverse += word[i]
print(reverse)
