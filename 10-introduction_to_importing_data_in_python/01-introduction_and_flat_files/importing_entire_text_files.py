# Open a file: file
file = open('moby_dick.txt', mode='r')

# Print it
print(file.read())

# Check whether file is closed
print(file.close())

# Close file
print(file.closed)

# Check whether file is closed
with open('moby_dick.txt', 'r') as file:
    print(file.closed)
