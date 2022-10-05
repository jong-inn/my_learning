
#### Sources : https://swcarpentry.github.io/shell-novice/
<br>

---
## __Pipes and Filters__
<br>
<br>

### __1) Capture an output: >__
<br>

&ensp;Input
```bash
$ wc -l unix_shell/*.md > lengths.txt
```
<br>

&ensp;Input
```bash
$ cat lengths.txt
```

&ensp;Output
```bash
    162 unix_shell/1_basics.md
    100 unix_shell/2_files.md
     24 unix_shell/3_pipes_filters.md
    286 total
```
<br>

&ensp;Input
```bash
# >> operator appends the string to the file
$ echo hello >> lengths.txt
```
<br>

&ensp;Input
```bash
$ cat lengths.txt
```

&ensp;Output
```bash
    162 unix_shell/1_basics.md
    100 unix_shell/2_files.md
     24 unix_shell/3_pipes_filters.md
    286 total
hello
```
<br>
<br>

### __2) Sort the contents: sort__
<br>

&ensp;Input
```bash
# -n option allows to sort numerically
$ sort -n lengths.txt
```

&ensp;Output
```bash
     24 unix_shell/3_pipes_filters.md
    100 unix_shell/2_files.md
    162 unix_shell/1_basics.md
    286 total
```
<br>
<br>

### __3) Combining multiple commands: |__
<br>

&ensp;Input
```bash
$ wc -l unix_shell/*.md | sort -n | head -n 1
```

&ensp;Output
```bash
    52 unix_shell/3_pipes_filters.md
```
<br>

&ensp;Input
```bash
$ cat animals.csv
```

&ensp;Output
```bash
2022,deer,3
2021,rabbit,10
2022,bird,5
2021,deer,50
2022,deer,6
2021,bird,7
```
<br>

&ensp;Input
```bash
$ cut -d , -f 2 animals.csv | sort | uniq -c
```

&ensp;Output
```bash
   2 bird
   3 deer
   1 rabbit
```
<br>

---