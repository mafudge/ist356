# IST356 : Programming Techniques for Data Analytics

Course Content Git Repository

- Michael Fudge 

## Contents:

- Syllabus: `syllabus.md` 
- Course Setup Information: `0-intro` folder
- Course topics in each numbered folder: `1-python, 2-ui, 3-data` etc...

## Using the repository

### Student Information

- As a public repository, you have permissions to pull code and get updates
- You **do not** have permissions to update this code on Github. 

### Getting Updates

If your prof updated the code, here's how you get it in VS Code:

1. Open your Terminal in VS Code: menu => Terminal => New Terminal
2. In the terminal, enter the command: `git fetch --all` to download the latest updates.
3. Next in the terminal, enter the command: `git reset --hard origin/main` to merge the changes into your local repository and force your working directory to match the update.
4. Download the pip dependencies: `pip3 install -r requirements.txt`

### Requirements

The packages necessary to run the code here are found in `requirements.txt` install using `pip` as follows:

1. From VS Code, open a terminal: menu => Terminal => New Terminal
2. In the terminal, enter `pip3 install -r requirements.txt`
