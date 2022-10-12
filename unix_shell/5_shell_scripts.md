
#### Sources : https://swcarpentry.github.io/shell-novice/
<br>

---
## __Shell Scripts__
<br>
<br>

### __1) Command-line arguements__
<br>

&ensp;Input
```bash
$ cat sample.txt
```

&ensp;Output
```bash
2013-11-05,deer,5
2013-11-05,rabbit,22
2013-11-05,raccoon,7
2013-11-06,rabbit,19
2013-11-06,deer,2
2013-11-06,fox,1
2013-11-07,rabbit,18
2013-11-07,bear,1
```
<br>

&ensp;Input
```bash
$ nano middle.sh

# There are three arguments.
# i.e., $1 is the first argument.
head -n "$2" "$1" | tail -n "$3"
```
<br>

&ensp;Input
```bash
$ bash middle.sh sample.txt 5 3
```

&ensp;Output
```bash
2013-11-05,raccoon,7
2013-11-06,rabbit,19
2013-11-06,deer,2
```
<br>

### __2) Command-line multiple arguements__
<br>

&ensp;Input
```bash
$ nano sorted.sh

# Sort files by their length.
wc -l "$@" | sort -n
```
<br>

&ensp;Input
```bash
$ bash sorted.sh ./*.md ./*.txt
```

&ensp;Output
```bash
      8 ./sample.txt
     62 ./5_shell_scripts.md
    100 ./2_files.md
    117 ./3_pipes_filters.md
    117 ./4_loops.md
    194 ./1_basics.md
    598 total
```
<br>

### __3) Example: List unique species__
<br>

&ensp;Input
```bash
$ nano species.sh

# Script to find unique species in csv files where species is the second data field
# Make a loop
for file in $@
do
    echo "Unique species in $file:"
    # Extract species name
    cut -d , -f 2 $file | sort | uniq
done
```

&ensp;Input
```bash
$ bash species.sh ./sample.test
```

&ensp;Output
```
Unique sepcies in ./sample.txt:
bear
deer
fox
rabbit
raccoon
```
<br>

### __4) Practice: Make a folder structure in README.md file using tree__
<br>

&ensp;Input
```bash
$ nano species.sh

# Make a folder structure in README.md file using tree whenever directories are updated.
# Usage: bash readme_directory.sh

# check whether README.md exists
if test -f './README.md'
then
    # create new README.md
    rm README.md
    touch README.md
    # header
    echo '# Welcome to my learning materials

### __Directories__' >> README.md
else
    # create new README.md if it doesn't exist
    touch README.md
    # header
    echo '# Welcome to my learning materials

### __Directories__' >> README.md
fi

# add structure of directories using tree
tree ./ >> README.md
# delete summary sentence
sed -i '' '$d
' README.md # sed in mac os.

# add ``` to make tree as a code block
sed -i '' '4i\
\```
' README.md # sed in mac os. \ is used in this block to keep the block in the markdown file.

echo '```' >> README.mde
```
<br>

&ensp;Input
```bash
$ bash readme_directory.sh
```

&ensp;Output

# Welcome to my learning materials

### __Directories__
```
./
├── README.md
├── readme_directory.sh
└── unix_shell
    ├── 1_basics.md
    ├── 2_files.md
    ├── 3_pipes_filters.md
    ├── 4_loops.md
    ├── 5_shell_scripts.md
    ├── middle.sh
    ├── sample.txt
    ├── sorted.sh
    └── species.sh

```
<br>

---