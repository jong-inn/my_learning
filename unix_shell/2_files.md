
#### Sources : https://swcarpentry.github.io/shell-novice/
<br>

---
## __Working with Files and Directories__
<br>
<br>

### __1) Create a directory: mkdir__
<br>

&ensp;Input
```bash
$ mkdir unix_shell
```
<br>

&ensp;Input
```bash
# -p option allows to create a nested directory.
$ mkdir -p ./test/type1 ./test/type2
```
<br>
<br>

### __2) Create a simple text file: nano__
<br>

&ensp;Input
```bash
$ nano draft.txt
```
<br>

&ensp;Input
```bash
# Create a 0 size file.
$ touch draft.txt
```
<br>
<br>

### __3) Move files or directories: mv__
<br>

&ensp;Input
```bash
$ mv draft.txt ./test/
```
<br>

&ensp;Input
```bash
# Rename the file or directory name.
$ mv ./draft.txt ./quotes.txt
```
<br>
<br>

### __4) Copy files or directories: cp__
<br>

&ensp;Input
```bash
$ cp draft.txt ./test/
```
<br>

&ensp;Input
```bash
# Use recursive option to backup the folder
$ cp -r thesis thesis_backup
```
<br>
<br>

### __5) Remove files or directories: rm__
<br>

&ensp;Input
```bash
$ rm quotes.txt
```
<br>

&ensp;Input
```bash
# Remove directories by using recursive option.
$ rm -r thesis
```
<br>

&ensp;Input
```bash
# Using an interactive option to protect against making a mistake.
$ rm -i thesis
```
<br>

---