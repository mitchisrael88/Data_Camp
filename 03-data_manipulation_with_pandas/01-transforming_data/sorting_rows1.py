Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Sort homelessness by individual
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> # Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)

# Print the top few rows
print(homelessness_fam.head())
SyntaxError: multiple statements found while compiling a single statement
>>> 
=============================== RESTART: Shell ===============================
>>> # Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)

# Print the top few rows
print(homelessness_fam.head())
SyntaxError: multiple statements found while compiling a single statement
>>> 
=============================== RESTART: Shell ===============================
>>> # Sort homelessness by individual
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())
