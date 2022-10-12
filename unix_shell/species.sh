# Script to find unique species in csv files where species is the second data field
# Make a loop
for file in $@
do
    echo "Unique sepcies in $file:"
    #Extract species name
    cut -d , -f 2 $file | sort | uniq
done