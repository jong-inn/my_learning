
#### Sources : https://swcarpentry.github.io/shell-novice/
<br>

---
## __Loops__
<br>
<br>

### __1) Basic syntax__
<br>

&ensp;Input
```bash
$ for thing in list_of_things
> do
>     command $thing
> done
```
<br>

&ensp;Input
```bash
$ for filename in *.txt
> do
>     echo $filename
> done
```

&ensp;Output
```bash
test1.txt
test2.txt
test3.txt
```
<br>
<br>

### __2) Examples 1: Save it to file__
<br>

&ensp;Input
```bash
# Make a for-loop by the sequence from 1 to 3.
$ for num in $(seq 1 3)
> do
>     # Make a 0 byte text file.
>     touch "test${num}.txt"
>     # Make another for-loop to write sentences in the file.
>     for iter in $(seq 1 3)
>     do
>         # Allocate white spaces string to myString
>         printf -v myString "%${iter}s"
>         # Replace white spaces with the number and write into the text file
>         echo "test${myString// /${num}}" >> "test${num}.txt"
>     done
> done
```
<br>

&ensp;Input
```bash
$ ls
```

&ensp;Output
```bash
test1.txt
test2.txt
test3.txt
```
<br>

&ensp;Input
```bash
$ for filename in *.txt
> do
>     cat $filename
> done
```

&ensp;Output
```bash
test1
test11
test111
test2
test22
test222
test3
test33
test333
```
<br>
<br>

### __3) Examples 2: Link with pipes__
<br>

&ensp;Input
```bash
$ for filename in *.txt
> do
>     # Allocate the second sentence to string
>     string=$(head -n 2 $filename | tail -n 1)
>     echo ${string/test/}
> done
```

&ensp;Output
```bash
11
22
33
```
<br>

---