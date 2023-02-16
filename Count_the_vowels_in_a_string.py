string = "Hello, World!"
vowels = "aeiouAEIOU"

# Initialize the count to 0
count = 0

# Iterate over each character in the string
for char in string:
    # Check if the character is a vowel
    if char in vowels:
        # If it's a vowel, increment the count
        count += 1

print("Number of vowels:", count)
