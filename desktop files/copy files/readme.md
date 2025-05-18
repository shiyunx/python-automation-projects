## Automate Copy Files
This script automates copy files from old to new folder.

<code>import os</code>
- Interact with operating system

<code>os.chdir</code>
- Change current working directory

<code>os.listdir()</code>
- Extract list of all files and directories

<code>shutil.copy</code>
- Copy a file or directory from source to destination

<code>os.path.exists(path)</code>
- Check whether directory already exists

### How does it work?
- Example scenario: files in docs

      docs_1.pdf
      docs_2.pdf
      docs_3.pdf

- Run python file
- Output: docs_1 to docs_3 will be copied from old docs to new copied_docs folder

