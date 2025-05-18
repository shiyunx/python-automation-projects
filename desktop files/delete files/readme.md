## Automate Delete Files
This script automates delete files from non empty directory.

<code>import os</code>
- Interact with operating system

<code>os.chdir</code>
- Change current working directory

<code>shutil.rmtree(</code>
- Delete an entire directory tree

### How does it work?
- Example scenario: files in docs > copied_docs

      docs_1.pdf
      docs_2.pdf
      docs_3.pdf

- Run python file
- Output: Copied_docs of docs_1 to docs_3 will be deleted
