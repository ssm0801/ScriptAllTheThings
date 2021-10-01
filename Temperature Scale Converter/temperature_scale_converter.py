"""
Name : Temperature Scale Converter
Aim : Inputs the value from the user and converts it to Fahrenheit,Kelvin & Celsius
Author : (Niyoj Oli)[https://github.com/niyoj]
Update: Added Kelvin scale
        Converted the data type to float, so that temperature in decimals can be considered
        Added comments to make it user-friendly
        By (Mayank Goyal) [https://github.com/mayankgoyal-13]
Date : 01/10/21
"""

temp = input("Input the  temperature you would like to convert? (e.g., 45F, 102C, 373K ) : ")
degree = float(temp[:-1])   # the first value of the input is taken as the degree
i_convention = temp[-1]     # second value becomes the unit

if i_convention.upper() == "C":
    result_1 = float((degree*1.8)+32)
    o_convention_1 = "Fahrenheit"
    result_2 = float(degree+273.15)
    o_convention_2 = "Kelvin"

elif i_convention.upper() == "F":
    result_1 = float((degree-32)/1.8)
    o_convention_1 = "Celsius"
    result_2 = float(result_1+273.15)
    o_convention_2 = "Kelvin"

elif i_convention.upper() == "K":
    result_1 = float((degree-273.15)*1.8+32)
    o_convention_1 = "Fahrenheit"
    result_2 = float(degree-273.15)
    o_convention_2 = "Celsius"

else:
    print("Input proper convention.")
    quit()           # stops the program and code after this will not be executed

print("The temperature in", o_convention_1, "is", result_1, "degrees. \nThe temperature in", o_convention_2, "is",
      result_2, "degrees.")      # \n represents new line
