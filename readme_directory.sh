
if test -f './README.md'
then
    rm README.md
    touch README.md
    echo '# Welcome to my learning materials

### __Directories__' >> README.md
else
    touch README.md
    echo '# Welcome to my learning materials

### __Directories__' >> README.md
fi

tree ./ >> README.md
sed -i '' '$d
' README.md

sed -i '' '4i\
```
' README.md

echo '```' >> README.md