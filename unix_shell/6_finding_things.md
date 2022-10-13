
#### Sources : https://swcarpentry.github.io/shell-novice/
<br>

---
## __Finding Things__
<br>
<br>

### __1) Select lines from text files: grep__
<br>

&ensp;Input
```bash
$ cat haiku.txt
```

&ensp;Output
```
The Tao that is seen
Is not the true Tao, until
You bring fresh toner.

With searching comes loss
and the presence of absence:
"My Thesis" not found.

Yesterday it worked
Today it is not working
Software is like that.
```
<br>

&ensp;Input
```bash
$ grep not haiku.txt
```

&ensp;Output
```
Is not the true Tao, until
"My Thesis" not found.
Today it is not working
```
<br>

&ensp;Input
```bash
# -w option for a word and " for a phrase.
$ grep -w "is not" haiku.txt
```

&ensp;Output
```bash
Today it is not working
```
<br>

&ensp;Input
```bash
# -n option for line number and -i for case-insenstivie.
$ grep -n -w -i "the" haiku.txt
```

&ensp;Output
```
1:The Tao that is seen
2:Is not the true Tao, until
6:and the presence of absence:
```
<br>

&ensp;Input
```bash
# -v option for inverting.
$ grep -n -w -i -v "the" haiku.txt
```

&ensp;Output
```
3:You bring fresh toner.
4:
5:With searching comes loss
7:"My Thesis" not found.
8:
9:Yesterday it worked
10:Today it is not working
11:Software is like that.
```
<br>

&ensp;Input
```bash
# -r option for searching recursively.
$ grep -r -w Sources ./unix_shell
```

&ensp;Output
```
./unix_shell/2_files.md:#### Sources : https://swcarpentry.github.io/shell-novice/
./unix_shell/1_basics.md:#### Sources : https://swcarpentry.github.io/shell-novice/
./unix_shell/3_pipes_filters.md:#### Sources : https://swcarpentry.github.io/shell-novice/
./unix_shell/5_shell_scripts.md:#### Sources : https://swcarpentry.github.io/shell-novice/
./unix_shell/6_finding_things.md:#### Sources : https://swcarpentry.github.io/shell-novice/
./unix_shell/4_loops.md:#### Sources : https://swcarpentry.github.io/shell-novice/
```
<br>

&ensp;Input
```bash
# -E option for regular expressions.
# Find lines that have an "o" in the second position.
$ grep -E "^.o" haiku.text
```

&ensp;Output
```
You bring fresh toner.
Today it is not working
Software is like that.
```
<br>

### __2) Find files and directory: find__
<br>

&ensp;Input
```bash
# Find directories in current directory.
$ find . -type d
```

&ensp;Output
```
.
./proteins
./animal-counts
./creatures
./writing
```
<br>

&ensp;Input
```bash
# Find files in current directory.
$ find . -type f
```

&ensp;Output
```
./numbers.txt
./proteins/propane.pdb
./proteins/octane.pdb
./proteins/cubane.pdb
./proteins/ethane.pdb
./proteins/pentane.pdb
./proteins/methane.pdb
./animal-counts/animals.csv
./creatures/minotaur.dat
./creatures/unicorn.dat
./creatures/basilisk.dat
./writing/LittleWomen.txt
./writing/haiku.txt
```
<br>

&ensp;Input
```bash
# Find exact files using -name option.
$ find . -name haiku.txt
```

&ensp;Output
```
./writing/haiku.txt
```
<br>

&ensp;Input
```bash
# Find exact files with pattern
# Without double quotes, it gets * as a wildcard.
$ find . -name "*.txt"
```

&ensp;Output
```
./numbers.txt
./writing/LittleWomen.txt
./writing/haiku.txt
```
<br>

&ensp;Input
```bash
# Count words of files in the list.
$ wc -l $(find . -name "*.txt")
```

&ensp;Output
```
     5 ./numbers.txt
    14 ./writing/LittleWomen.txt
     7 ./writing/haiku.txt
    26 total
```
<br>

&ensp;Input
```bash
# Find .txt files that contain the word "searching"
$ grep "searching" $(find . -name "*.txt")
```

&ensp;Output
```
./writing/LittleWomen.txt:searching for her book, but was
./writing/haiku.txt:With searching comes loss
```
<br>

---