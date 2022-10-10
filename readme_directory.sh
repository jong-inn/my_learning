

rm test.md
touch test.md

tree ./ >> test.md

string=$(<test.md)
printf "$string" | tr '\n' '\n <br>' > test.md
