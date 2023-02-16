credit_card_number = "1234 5678 9012 3456"

# Hide all but the last 4 digits
hidden_number = "*" * 12 + credit_card_number[-4:]

print(hidden_number)


"""
In this example, we first define a credit card number ("1234 5678 9012 3456"). We then create a new string called hidden_number.

To hide all but the last 4 digits of the credit card number, we create a string of 12 asterisks ("*" * 12) and concatenate it with the last 4 digits of the credit card number (credit_card_number[-4:]). The [-4:] slice means "take the last 4 characters of the string".

Finally, we print the hidden_number string, which shows only the last 4 digits of the credit card number and hides the rest with asterisks.
"""