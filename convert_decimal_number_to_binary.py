# TODO way-1
""""""

decimal_number = 42
binary_number = bin(decimal_number)

print(binary_number)

# TODO way-2
"""In this example, we use the same code as before,
but we slice the resulting string from index 2 to the end to remove the 0b prefix."""

decimal_number = 42
binary_number = bin(decimal_number)[2:]

print(binary_number)
