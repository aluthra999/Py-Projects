from barcode import EAN13
from barcode.writer import ImageWriter
number = input("Number: ")
my_code = EAN13(number, writer=ImageWriter())
my_code.save("new_code 1")

# Provided Barcodes
# EAN-8
# EAN-13
# EAN-14
# UPC-A
# JAN
# ISBN-10
# ISBN-13
# ISSN
# Code 39
# Code 128
# PZN
