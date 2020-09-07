#!/bin/bash

password24="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
for pin in {0000..9999}
do
    echo "$password24 $pin"
done | nc localhost 30002 > output.txt

cat output.txt | grep -v "Wrong"