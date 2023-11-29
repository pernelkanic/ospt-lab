def case_conversion(string, case):
if case == "upper":
return string.upper()
elif case == "lower":
return string.lower()
else:
raise ValueError("Invalid case: {}".format(case))
string = input("Enter a string: ")
print("Uppercase string:”, case_conversion(string, "upper"))
print("Lowercase string:", case_conversion(string, "lower"))
print("String length:", len(string))