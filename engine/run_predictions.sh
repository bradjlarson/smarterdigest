#!/bin/ksh
cd /Dropbox/Coding/smarterdigest/engine/users/
list=`ls *.php`
for script in $list
do
php $script &
done
exit
