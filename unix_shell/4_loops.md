
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
$ for num in $(seq 1 3)
> do
>     touch "test${num}.txt"
>     for iter in $(seq 1 3)
>     do
>         printf -v myString "%${iter}s"
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

---