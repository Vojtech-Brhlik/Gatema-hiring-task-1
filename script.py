################################################
##                                            ##
##          Gatema hiring task                ##
##                                            ##
##  author: Vojtech Brhlik                    ##
##  vojta.brhlik@gmail.com                    ##
##                                            ##
##  Brno, 27. 2. 2023                         ##
##                                            ##
################################################

import re                   # all of the regex tools
import sys                  # working with arguments
import os.path              # os.path.exists

# Function used for the group sorting
def sort_fn(group):
    split = re.split(r"T", group[0])
    return split[1]

# Function returns X and Y values
def get_nums(string):
    nums = re.split(r"[XYT]", string)
    return(nums[1:3])

# Function checks if instruction format is correct
def valid_check(line):
    if re.search(LINE, line) is None:
            
        # End of instructions 
        if line == "":
            return 1
        # Throw error for invalid instruction
        else:
            print("ERROR(3): Invalid instruction format:", line)
            exit(3)
    return 0

# Function for the "-funkce1" argument
def F1(lines):
    
    # Temporary lists for splitting string into groups
    group =  []
    groups = []

    """ Go through each line of instruction.
        If X value > 50, increment Y value by 10.
        Also split lines into groups by drill."""
    for line in lines:
        
        # Check for correct format of inscturtions
        if valid_check(line) == 1:
            groups.append(group)
            break
        
        # Check for the XY condition
        nums = get_nums(line)
        if float(nums[0]) > 50:
            nums[1] = float(nums[1]) + 10
            line = re.sub(r"Y\d+.\d+", f"Y{nums[1]:.3f}", line)
        
        # Look for lines with T0? to split lines into groups
        if re.search(r"T0\d+?", line):
            
            """ Append the previous group to groups (but only if 
                it's not empty).
                Create new group to start putting lines into.
                """
            if group:
                groups.append(group)
            group = []
        
        group.append(line)
        
    # Sort groups based by the drill number
    groups.sort(key=sort_fn)

    # Put each group back together into one string
    temp = ["\n".join(group) for group in groups]

    # Now just create one giant string, add the cropped parts at the start
    out = "Zacatek bloku vrtani)\n\n" + "\n".join(temp) + "\n\n$\n\n(M47, Konec bloku vrtani"

    # Now we replace the former data with our new string
    cnc = re.sub(KWD, out, input)

    # Create the file, write the output
    f = open("cnc.txt", "w")
    f.write(cnc)
    f.close()
    return

# Function for the "-funkce2" argument
def F2(lines):
    
    # INIT
    X_min = None
    X_max = None
    Y_min = None
    Y_max = None
    
    """ Go through each line and find the highest and lowest coordinates.
        ...
        I am not very happy with this solution, but it works and it does not require other imports. 
        I considered putting all of the values into a list and then running min() and max() functions, 
        but this solution is more memory friendly."""
    for line in lines:
       
        # Check for correct format of inscturtions
        if valid_check(line) == 1:
            break
            
        nums = get_nums(line)
        
        # Variables for cleaner code
        X = float(nums[0])
        Y = float(nums[1])

        # Fill the variables with actual values for the first line
        if (X_min is None or X_max is None or
            Y_min is None or Y_max is None):
                X_max = X
                X_min = X
                Y_max = Y
                Y_min = Y
            
        # Now just check if X is smaller or bigger than current min/max
        if X > X_max:
            X_max = X
        if X < X_min:
            X_min = X
            
        # Do the same for Y
        if Y > Y_max:
            Y_max = Y
        if Y < Y_min:
            Y_min = Y
    
    # Print the answers in format matching to input (3 decimals)
    print(f"Min_X = {(X_min):.3f}")
    print(f"Max_X = {(X_max):.3f}")
    print(f"Min_Y = {(Y_min):.3f}")
    print(f"Max_Y = {(Y_max):.3f}")
    
""" Key regex to fish out the only part that we'll be working with. 
    We intentionally leave out one '\n' character at the end of the string, 
    so we can use it in the 'for' loop where we split lines into groups.
    LINE defines regex for checking the instruction format.
    Also define the filename, so the script is easier to use for multiple files."""
KWD = r"(?s)Zacatek bloku vrtani\)\n\n(.+?)\n\$\n\n\(M47, Konec bloku vrtani"
LINE = r"X(-)?\d+(.)\d+Y\d+(.)\d+T?\d+"
FILENAME = "D327971_fc1.i"

# Check if file exists
if os.path.exists(FILENAME) == True:
    input = open(FILENAME).read()
# If file does not exist, exit the script with code 1
else:
    print("ERROR(1): Could not locate the", FILENAME, "file.")
    exit(1)

# Take out the relevant part of the file
data = re.findall(KWD, input)[0]
lines = re.split("\n", data)

# Check for correct argument count
if len(sys.argv) != 2:
    print("ERROR(21): Incorrect arguments.")
    exit(21)

# Check arguments
if sys.argv[1] == "-funkce1":
    F1(lines)
elif sys.argv[1] == "-funkce2":
    F2(lines)

# For other arguments, exit with code 22
else:
    print("ERROR(22): Incorrect arguments.")
    exit(22)