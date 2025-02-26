# Instagram-Following
Simple Python Script to output non-mutual following. This script is for those who want a dead simple script without installing a random appliaction or extension onto their computer.
This will require some knowledge on how to install and run python on your machine. There are great tutorials on youtube, Python is a very beginner friendly programming language. 
This includes detailed instructions on how to run so those with more technical knowledge can tell their peeps to read this instruction list.

**REQUIRED:**
1. Python installed on your machine
2. Understanding of how to execute a python file via a terminal or IDE
3. Understanding of how to update a python string variable
4. Have the JSON library installed to your python environment via PIP
5. Downloaded files from Meta https://accountscenter.instagram.com/info_and_permissions/

**HOW TO RUN SCRIPT:**

**1. First request a file download of your followers and following from Meta via the above link, if you don't link clicking random links on the internet, follow these steps:**
- Go to your instagram account (via a computer, cannot be performed on mobile)
- Click the hamburger menu labeled 'More' in the bottom left and select 'Settings'
- Go to Meta's 'Accounts Center' by clicking 'See more in Accounts Center'
- Click 'Your information and permissions'
- Click 'Download your information'
- Click 'Download or transfer information'
- Select your account
- Select 'Some of your information'
- Select 'Followers and following'
- Select 'Download to Device'
- Select Date range as you see fit, most people will want to select 'All Time'
- Select e-mail you would like the files to be sent to
- Change the format from HTML to JSON ... media quality is irrelevant 
- Click 'Create files'

**2. You've now requested your files, wait for an email from Meta/Instagram**
- Download the files from the provided link from Meta, this will download a zip file to your computer 
- Extract the two files 'followers_1.json' and 'following.json', this means just drag them out of the zipped folder to anywhere you like, I typically choose my desktop.

**3. Now you must alter the python script for this to work, you're basically telling the script where your files are located on your machine.**
- Find the path for the files 'followers_1.json' and 'following.json' remember those two files you dragged out of the zipped folder? Save the path on your clipboard.
- Your file path should look something like this (assuming windows machine) -> C:\Users\CHANGE_ME\Desktop\followers_1.json
- Open the python file (the one from this git repo) and change the file path for both python variables on lines 8 and 9:
  - followers_path = r'C:\Users\CHANGE_ME\Desktop\followers_1.json'
  - following_path = r'C:\Users\CHANGE_ME\Desktop\following.json'

**4. Now that the file paths are updated run the script in the terminal or your prefered IDE**
-  python .\instagram_following.py

**5. That's it you'll see a printed out list of all the people who are not mutual followers, all without downloading random appliactions or suspicious extensions.**
