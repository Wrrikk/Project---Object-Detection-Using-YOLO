"""
Creating Custom Dataset in YOLO format
File: creating-files-data-and-name.py
"""


# Creating files custom_data.data and classes.names
# for training in Darknet framework
#
# Algorithm:
# Setting up full paths --> Reading file classes.txt -->
# --> Creating file classes.names -->
# --> Creating file custom_data.data
#
# Result:
# Files classes.names and custom_data.data needed to train
# in Darknet framework


"""
Start of:
Setting up full path to directory with downloaded images
"""

# Full or absolute path to the folder with images
# Find it with Py file getting-full-path.py
full_path_to_images = \
    'C:/Users/royri/OIDv4_ToolKit/OID/Dataset/train/Car_Bicycle_wheel_Bus'

"""
End of:
Setting up full path to directory with downloaded images
"""


"""
Start of:
Creating file classes.names
"""

# Defining counter for classes
c = 0

# Creating file classes.names from existing one classes.txt
with open(full_path_to_images + '/' + 'classes.names', 'w') as names, \
     open(full_path_to_images + '/' + 'classes.txt', 'r') as txt:

    # Going through all lines in txt file and writing them into names file
    for line in txt:
        names.write(line)  # Copying all info from file txt to names

        # Increasing counter
        c += 1

"""
End of:
Creating file classes.names
"""


"""
Start of:
Creating file custom_data.data
"""

# Creating file custom_data.data
with open(full_path_to_images + '/' + 'custom_data.data', 'w') as data:
    # Writing needed 5 lines
    # Number of classes
    # By using '\n' we move to the next line
    data.write('classes = ' + str(c) + '\n')

    # Location of the train.txt file
    data.write('train = ' + full_path_to_images + '/' + 'train.txt' + '\n')

    # Location of the test.txt file
    data.write('valid = ' + full_path_to_images + '/' + 'test.txt' + '\n')

    # Location of the classes.names file
    data.write('names = ' + full_path_to_images + '/' + 'classes.names' + '\n')

    # Location where to save weights
    data.write('backup = backup')

"""
End of:
Creating file custom_data.data
"""
