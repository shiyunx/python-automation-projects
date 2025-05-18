## Automate Rename Files
This script automates rename files in desktop.

<code>import os</code>
- Interact with operating system

<code>os.chdir</code>
- Change current working directory

<code>os.listdir()</code>
- Extract list of all files and directories

<code>os.path.splitext(file)</code>
- Splits a pathname into its name (root) and extension (ext)

### How does it work?
- Example scenario: files in docs

      docs_1.pdf
      docs_2.pdf
      docs_3.pdf

- Run python file
- Output: renamed files

      1_docs.pdf
      2_docs.pdf
      3_docs.pdf
