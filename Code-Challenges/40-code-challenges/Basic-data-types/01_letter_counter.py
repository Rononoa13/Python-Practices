name = input("What is your name: ")

print(f"Hello {name.capitalize()}!")
print(f"I will count the number of times that a specific letter occurs in a message.")

msg = input("Please enter a message: ")
letter_count = input("Which letter would you like to count the occurance of: ")

#converts user message into lower case.
lower_letters = msg.lower()
# Counts the occurance of a letter from `letter_count`
total_letter_count = lower_letters.count(letter_count)

print(f"{name}, your message has {total_letter_count} {letter_count}'s in it")
