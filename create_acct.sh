#!/bin/ksh
username="brad3"
password=""

mkdir /Dropbox/Coding/smarterdigest/users/$username
cp /Dropbox/Coding/smarterdigest/default/index.php /Dropbox/Coding/smarterdigest/users/$username/index_1.php
cp /Dropbox/Coding/smarterdigest/default/stars_test.php /Dropbox/Coding/smarterdigest/users/$username/stars_test_1.php
cp /Dropbox/Coding/smarterdigest/default/top_bar.php /Dropbox/Coding/smarterdigest/users/$username/top_bar_1.php
cp /Dropbox/Coding/smarterdigest/default/votes_test.php /Dropbox/Coding/smarterdigest/users/$username/votes_test_1.php
cp /Dropbox/Coding/smarterdigest/default/share_test.php /Dropbox/Coding/smarterdigest/users/$username/share_test_1.php
cp /Dropbox/Coding/smarterdigest/default/submit_suggestion.php /Dropbox/Coding/smarterdigest/users/$username/submit_suggestion_1.php
cp /Dropbox/Coding/smarterdigest/default/acct_mgmt.php /Dropbox/Coding/smarterdigest/users/$username/acct_mgmt_1.php
cp /Dropbox/Coding/smarterdigest/default/last_thirty.php /Dropbox/Coding/smarterdigest/users/$username/last_thirty_1.php
cp /Dropbox/Coding/smarterdigest/default/logout.php /Dropbox/Coding/smarterdigest/users/$username/logout_1.php
cp /Dropbox/Coding/smarterdigest/default/queue.php /Dropbox/Coding/smarterdigest/users/$username/queue_1.php
cp /Dropbox/Coding/smarterdigest/default/show_starred.php /Dropbox/Coding/smarterdigest/users/$username/show_starred_1.php
cp /Dropbox/Coding/smarterdigest/default/top_bar_thirty.php /Dropbox/Coding/smarterdigest/users/$username/top_bar_thirty_1.php
cp /Dropbox/Coding/smarterdigest/default/get_predictions.php /Dropbox/Coding/smarterdigest/users/$username/brad3_predictions_1.php
cd /Dropbox/Coding/smarterdigest/users/$username
cp index_1.php index_2.php

sed -e 's/$username/brad3/g' index_2.php > index_1.php
sed -e 's/$password//g' index_1.php > index.php
sed -e 's/$username/brad3/g' stars_test_1.php > stars_test.php
sed -e 's/$username/brad3/g' top_bar_1.php > top_bar.php
sed -e 's/$username/brad3/g' votes_test_1.php > votes_test.php
sed -e 's/$username/brad3/g' share_test_1.php > share_test.php
sed -e 's/$username/brad3/g' submit_suggestion_1.php > submit_suggestion.php
sed -e 's/$username/brad3/g' acct_mgmt_1.php > acct_mgmt.php
sed -e 's/$username/brad3/g' last_thirty_1.php > last_thirty.php
sed -e 's/$username/brad3/g' logout_1.php > logout.php
sed -e 's/$username/brad3/g' queue_1.php > queue.php
sed -e 's/$username/brad3/g' show_starred_1.php > show_starred.php
sed -e 's/$username/brad3/g' top_bar_thirty_1.php > top_bar_thirty.php
sed -e 's/$username/brad3/g' brad3_predictions_1.php > brad3_predictions.php

mv brad3_predictions.php /Dropbox/Coding/smarterdigest/engine/users/

rm *_1.php
rm *_2.php
chmod a+rwx -R /Dropbox/Coding/smarterdigest/users/$username/.
