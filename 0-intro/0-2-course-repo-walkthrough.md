# Course Repository Walkthrough

Now that you've opened the course repository in VS Code (either in a dev container on your computer or in a Codespace), let's take it for a spin. This walkthrough will demonstrate how to:

- [Get to know the VS Code window](#-getting-to-know-vs-code)
- [Run code in a Python file](#-run-code-in-a-python-file)
- [Run code in a notebook](#-run-code-in-a-notebook)
- [Debug code in a Python file (breakpoints)](#-debug-code-in-a-python-file)
- [Debug code in a notebook](#-debug-code-in-a-notebook)
- [Run a Streamlit app](#-run-a-streamlit-app)
- [Preview a Markdown file](#-preview-a-markdown-file)
- [Run pytest tests](#-run-pytest-tests)
- [Create your own code files](#-create-your-own-code-files)
- [Take notes](#-take-notes)
- [Save your work to GitHub](#-save-your-work-to-github)

> 💡 **New to VS Code?** Don't rush. Do each section in order with the file open in front of you. The goal isn't to memorize — it's to know that these features *exist* and roughly where to find them.

---

## 🧭 Getting to know VS Code

When VS Code opens, you'll see a few main areas. Get familiar with them before you start clicking around.

- **Activity Bar** (far left, vertical strip of icons) — this switches what the side panel shows. The ones you'll use most:
  - 📄 **Explorer** — the file/folder tree of the course repository.
  - 🔍 **Search** — find text across every file.
  - 🔀 **Source Control** — git: save and back up your work (covered below).
  - ▶️ **Run and Debug** — run and debug programs.
  - 🧪 **Testing** — run the pytest tests (the beaker/flask icon).
  - 🧩 **Extensions** — add-ons like Python and Jupyter (already installed for you in the dev container).
- **Editor** (center) — where your files open. You can have several open as tabs.
- **Terminal** (bottom) — a command line *inside* VS Code. Open it with the menu **Terminal → New Terminal**. This is where you type commands and where program output/prompts appear.
- **Command Palette** — press **`F1`** (or `Ctrl+Shift+P` / `Cmd+Shift+P` on Mac) to search every command VS Code can do by typing its name. When these instructions say "open the Command Palette," this is it.

Click the **Explorer** 📄 icon now. You'll see the course folders: `0-intro`, `1-python`, `2-ui`, and so on. Expand `0-intro` — that's where the files for this walkthrough live.

---

## ▶️ Run code in a Python file

Let's run a plain Python program.

1. In the **Explorer**, open `0-intro/hello.py`. It's two lines: it asks for your name and greets you.
2. This program uses `input()`, so it needs the **terminal** to type into. In the top-right corner of the editor, click the **▶ Run** button's dropdown arrow and choose **Run Python File** (or use the menu **Run → Run Without Debugging**).
3. Look at the **terminal** at the bottom. You'll see `Enter your name:`. Click in the terminal, type your name, and press **ENTER**.
4. You should see `Hello, <your name>!` printed, followed by a fresh prompt.

🎉 That's a Python file running. Output and input both happen in the terminal.

---

## 📓 Run code in a notebook

A **Jupyter notebook** (`.ipynb`) mixes formatted text with runnable code, broken into **cells**. This is the primary teaching format in this course.

1. In the **Explorer**, open `0-intro/hello.ipynb`.
2. You'll see two kinds of cells:
   - A **Markdown cell** with the title text (formatted notes).
   - A **Code cell** with the same two lines of Python as before.
3. Click on the **code cell**, then press **`SHIFT+ENTER`** to run it (or click the little **▶** button on the left edge of the cell).
4. **First time only:** VS Code asks you to pick a **kernel** (the Python that runs your code). Choose the recommended **Python** interpreter — in the dev container it's already set up for you.
5. An input box appears **at the top of the window**, not in the terminal — this is a notebook quirk. Type your name there and press **ENTER**. The greeting prints just below the cell.

> 🔑 **Key difference:** In a `.py` file, `input()` uses the terminal. In a notebook, it pops up an input box at the top of the VS Code window. Watch for it there.

---

## 🐞 Debug code in a Python file

**Debugging** lets you pause your program mid-run and look at what's happening — invaluable when code misbehaves.

1. Open `0-intro/hello.py` again.
2. Set a **breakpoint**: hover just to the **left of the line number** for line 2 (`print(...)`) and click. A **red dot** appears. The program will pause *before* running that line.
3. Start debugging: open the **Run and Debug** ▶️ panel, and at the top choose **Python Debugger: Current File**, then click the green ▶ (or just press **`F5`**).
4. Type your name in the terminal and press ENTER. The program runs, then **pauses** at your red dot.
5. While paused, notice:
   - The **variables** panel (left) shows `name` holds what you typed.
   - A **debug toolbar** appears at the top with controls: **Continue** (▶), **Step Over** (⤵), **Step Into**, and **Stop** (⏹).
6. Click **Continue** (▶) to let it finish, or **Stop** (⏹) to end early.

Remove a breakpoint by clicking the red dot again.

---

## 🐞 Debug code in a notebook

Notebooks can be debugged too, one cell at a time.

1. Open `0-intro/hello.ipynb`.
2. Click a red-dot **breakpoint** to the left of a line inside the code cell.
3. Click the **dropdown arrow next to the cell's ▶ Run button** and choose **Debug Cell**.
4. It pauses at your breakpoint, and the same variables/step controls appear. Step through and inspect variables just like in a `.py` file.

---

## 🎈 Run a Streamlit app

Later in the course you'll build interactive web apps with **Streamlit**. These don't run like a normal Python file — they launch a little web server. We've set up a one-click way to do it.

1. In the **Explorer**, open `2-ui/2-hello.py` (a simple Streamlit demo).
2. Open the **Run and Debug** ▶️ panel. At the top, click the configuration dropdown and choose **Streamlit Run: Current File**.
3. Click the green ▶ (or press **`F5`**). Streamlit starts in the terminal.
4. The app opens in a browser tab (locally) or, in a Codespace/dev container, VS Code shows a **"Open in Browser"** popup for the forwarded **Streamlit** port — click it.
5. Interact with the app in the browser. Back in VS Code, **stop** it with the ⏹ button in the debug toolbar (or press `Ctrl+C` in the terminal).

> 💡 The **Streamlit Run: Current File** option always runs *whatever file is currently open*, so use it for any `streamlit` demo in the course.

---

## 👀 Preview a Markdown file

A lot of the course reading — including this very file — is written in **Markdown** (`.md`). You can read the nicely formatted version right inside VS Code instead of looking at the raw text and symbols.

1. In the **Explorer**, open a Markdown file, e.g. `0-intro/0-0-setup.md` (or this walkthrough, `0-2-course-repo-walkthrough.md`).
2. At the **top-right of the editor**, click the **Open Preview to the Side** icon (a magnifying glass over a page). Or open the Command Palette (`F1`) and type **Markdown: Open Preview**.
3. A formatted, easy-to-read version appears. Headings, links, bullet lists, and code blocks all render the way they're meant to be read.

> 💡 Preview-to-the-side is handy for reading instructions on one half of the screen while you work in a file on the other half.

---

## 🧪 Run pytest tests

Testing is a topic in this course, so tests live *inside* the code files. Here's how to run them.

1. Open the **Testing** 🧪 panel (the beaker/flask icon in the Activity Bar).
2. You'll see the tests VS Code has discovered — this repo is set up to find the tests in `1-python/solutions/dateutils.py`.
3. Click the **▶ Run** (play) icon at the top to run all of them, or hover a single test and run just that one.
4. Passing tests get a green ✓; failures get a red ✗ that you can click to see what went wrong.

You can also run a file's tests from the terminal:

```bash
pytest 1-python/solutions/dateutils.py
```

---

## 📝 Create your own code files

Remember, you're working in **your own fork** — your personal copy of the repository. That means you can add files and edit freely, then commit and push your work to *your* GitHub (see [Save your work to GitHub](#-save-your-work-to-github)). It's yours.

To keep your own work tidy and out of the way of course updates (see the ⚠️ note below), make yourself a personal folder for it.

1. In the **Explorer**, hover over the top-level area and click the **New Folder** icon. Name it something like `my-work`.
2. With `my-work` selected, click the **New File** icon. Name it `practice.py` (for a Python file) or `notes.ipynb` (for a notebook — the `.ipynb` extension makes it a notebook).
3. Type some code and run it using the steps above.

> ⚠️ **Tip — keep your own work in its own folder:** Throughout the semester the professor adds and updates files in the upstream repository, and you'll pull those in by **syncing your fork** (the **Sync Fork** button on GitHub, then updating your local copy). If you've edited the *professor's* files, syncing can cause **merge conflicts** you'd have to untangle. You'll avoid that headache entirely by keeping your own code and notes in your own folder (like `my-work/`) instead of editing the course files directly.

---

## 🗒️ Take notes

The nicest way to take notes in this course is a **notebook**, because you can mix written notes with code you can actually run.

1. In your `my-work` folder, create a notebook, e.g. `class-notes.ipynb`. Keeping your notes here (rather than typing into the lecture slide notebooks) means they won't collide with course updates when you sync your fork.
2. Add a **Markdown cell** for written notes: with a cell selected, switch its type to **Markdown** (there's an **M↓ / Markdown** toggle on the cell, or press `M` when the cell is selected but not being edited). Type notes using Markdown — `# Heading`, `- bullet`, `**bold**` — then press `SHIFT+ENTER` to render it.
3. Add a **Code cell** below it to try out the idea you just wrote about, and run it.

This way your notes and your working examples live side by side — and because it's your fork, you can commit and push them to GitHub so they're backed up and follow you to any computer.

---

## 💾 Save your work to GitHub

Saving to GitHub means your work is **backed up in the cloud** on *your* fork — safe even if your computer dies or a Codespace is deleted. This uses **git**, and VS Code makes it point-and-click.

> You can only push to **your fork** (`https://github.com/YOURGITHUB/ist356`) — you set that up in the [Setup guide](0-0-setup.md). You cannot push to the professor's copy, and that's expected.

1. Open the **Source Control** 🔀 panel. It lists every file you've **changed** or **created**.
2. **Stage** your changes: hover a file and click the **+** (or click **+** next to "Changes" to stage everything). Staging marks what you want to save.
3. Type a short **commit message** in the box at the top describing what you did — e.g. *"my week 1 practice and notes"*.
4. Click the **✓ Commit** button. This saves a snapshot **locally**.
5. Click **Sync Changes** (or the **↑ Push**) to upload the commit to your fork on GitHub.
6. Verify: visit `https://github.com/YOURGITHUB/ist356` in a browser — your files are there. ✅

> 🔁 **Do this often** — after each class or work session. Committing and pushing regularly is both good backup habit and good professional practice. It also means your notes are safely on GitHub *before* you pull the professor's updates.

---

## 🎉 You're ready!

You now know how to run and debug code, launch a Streamlit app, preview Markdown, run tests, create your own files, take notes, and back everything up to GitHub. That's the full daily workflow for this course — welcome to IST356!
