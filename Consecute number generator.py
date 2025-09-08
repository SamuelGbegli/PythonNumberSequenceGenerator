# Generates a list of consecutive numbers from user input inclusive

# Checks if input is integer
def isInteger(value):
    try:
        number = int(value)
        return True
    except ValueError:
        return False

# Sets starting number
input1 = input("Please enter starting integer: ")
while (isInteger(input1) == False):
    input1 = input("Input is not an integer. Please try again: ")

# Sets end number
input2 = input("Please enter end integer: ")
while (isInteger(input2) == False):
    input2 = input("Input is not an integer. Please try again: ")

# Sets steps number
step = input("Please enter step integer (leave blank for 1): ")
# Ensures step is positive
# May add feature to allow counting backwards
while (isInteger(step) == False or (int(step) < 1)):
    if(step == ""):
        step = 1
        break
    step = input("Input is invalid. Please try again: ")

# Prints values

# Converts string input to integers
start = int(input1)
end = int(input2)

# Swaps values if start is larger than end
if(start > end):
    start = int(input2)
    end = int(input1)

print("Values:")
for i in range(start, end + 1, int(step)):
    print(i)

input("Complete. Press enter to exit")