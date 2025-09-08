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
if(step == ""):
    step = 1
else:
    # Ensures step is positive
    # May add feature to allow counting backwards
    while (isInteger(step) == False or step < 1):
        step = input("Input is not an integer. Please try again: ")

# Prints values

# Ensures values are printed from smallest to largest
start = input1
end = input2

if(input1 > input2):
    start = input2
    end = input1

print("Values:")
for i in range(int(start), int(end) + 1, int(step)):
    print(i)

