import os, shutil
from datetime import datetime

# Get the current date
now = datetime.now()

# Set the path to the directory you want to clean up
path = ''

# Get the list of files in the directory
files = os.listdir(path)

# Set the path and name of the new folder
new_folder = ''
os.mkdir(new_folder)

# Loop through the list of files
for file in files:

    # Get the date the file was created
    created_date = datetime.fromtimestamp(os.path.getctime(path + file))

    # Calculate the difference between the created date and the current date
    diff = now - created_date

    # If the difference is more than 30 days, move the file to the new folder
    if diff.days > 30:
        shutil.move(path + file, ''+ file)