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
' README.md

# add ``` to make tree as a code block
sed -i '' '4i\
```
' README.md

echo '```' >> README.md