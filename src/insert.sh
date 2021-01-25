#!/bin/zsh

echo "Enter temperature (celsius):"
read temp
sqlite3 ../db/temperature.sqlite "insert into temperature (celsius) values (\"$temp\");"

sqlite3 ../db/temperature.sqlite "select * from temperature;"
