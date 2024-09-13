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

1. Switch to source code control: menu => View => Source Control
2. Click more actions (the three dots) `...` to the right of SOURCE CONTROL
3. Select **pull** from the menu.

If the pull does not work, you'll need to use the "rebase" strategy. This strategy pulls contents, then places the current state of your working folder on top of it.

1. From VS Code, open a terminal: meun => Terminal => New Terminal
2. In the terminal, enter `git pull --rebase`

### Requirements

The packages necessary to run the code here are found in `requirements.txt` install using `pip` as follows:

1. From VS Code, open a terminal: meun => Terminal => New Terminal
2. In the terminal, enter `pip install -r requirements.txt`
