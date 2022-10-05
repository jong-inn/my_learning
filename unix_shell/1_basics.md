

#### Sources : https://swcarpentry.github.io/shell-novice/
<br>

---
## __The Shell__

&ensp;&ensp;The shell is a program where users can type commands. With the shell, it’s possible to invoke complicated programs like climate modeling software or simple commands that create an empty directory with only one line of code. The most popular Unix shell is Bash.

---
<br>
<br>

---
## __Basic Commands__
<br>
<br>

### __1) List the contents of directory: ls__
<br>

&ensp;Input
```bash
$ ls
```

&ensp;Output
```bash
Applications    Library         Public
Desktop         Movies          opt
Documents       Music
Downloads       Pictures
```
<br>

&ensp;Input
```bash
# Make output more comprehensible.
## / - directory
## @ - link
## * - executable
$ ls -F
```

&ensp;Output
```bash
Applications/   Library/        Public/
Desktop/        Movies/         opt/
Documents/      Music/
Downloads/      Pictures/
```
<br>

&ensp;Input
```bash
# Take a look at other directory.
$ ls -F Desktop/my_learning
```

&ensp;Output
```bash
README.md       unix_shell
```
<br>

&ensp;Input
```bash
# Get the size of files.
$ ls -s Desktop/my_learning
```

&ensp;Output
```bash
total 8
8 README.md     0 unix_shell
```
<br>
<br>

### __2) Show the current working directory: pwd__
<br>

&ensp;Input
```bash
$ pwd
```

&ensp;Output
```bash
/Users/your_folder
```
<br>
<br>

### __3) Get help: _command_ --help or man _command___
<br>

&ensp;Input
```bash
$ ls --help
```
<br>

```bash
$ man ls
```
<br>
<br>

### __4) Change directory: cd _path___
<br>

&ensp;Input
```bash
$ cd Desktop/my_learning
```
<br>

&ensp;Input
```bash
# Move up one directory level.
$ cd ..
```
<br>

&ensp;Input
```bash
# Move to current user's home directory.
$ cd ~
```
<br>

&ensp;Input
```bash
# Move to previous directory I was in.
$ cd -
```
<br>

&ensp;Input
```bash
# Move to the root directory.
$ cd /
```
<br>

### __5) Concatenate and print words: cat__
<br>

&ensp;Input
```bash
$ cat test.txt
```

&ensp;Output
```bash
test1
test2
```
<br>

---