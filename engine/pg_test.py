#!/usr/bin/python

import bayes
from urllib import unquote_plus
import MySQLdb as mdb
import sys

storage = bayes.Storage("pg_test.dat", 10)
try:
    storage.load()
except IOError:
    pass  # don't fail if bayes.dat doesn't exist, it will be created

bayes = bayes.Bayes(storage)

con = None
	
con = mdb.connect('localhost', 'root', 'Shop!1856', 'jobs');
	
with con: 
		
	cur = con.cursor(mdb.cursors.DictCursor)
	cur.execute("SELECT a.article_id, like_flag, article_text \
	from test_user_activity a, test_article b \
	where a.article_id = b.article_id \
	and a.like_flag is not null \
	order by a.article_id")
	
	rows = cur.fetchall()
	
	total = 0
	for row in rows:
		
		t = row["article_text"]
		t = unquote_plus(t)
		if row["like_flag"] == 1:
			bayes.train(t, False)
		else:
			bayes.train(t, True)
		total = total + 1
		print total
		if (total % 100) == 0:
			query = "SELECT a.article_id, a.prediction, a.like_flag, b.article_text from test_user_activity a, \
			test_article b where a.article_id = b.article_id and a.article_id between %s and %s and user_name ='brad'" % (row["article_id"] + 1, (row["article_id"] + 101))
			print query
			cur.execute(query) 
			rows = cur.fetchall()
	
			for row in rows:
				t = row["article_text"]
				t = unquote_plus(t)
				prediction = bayes.classify(t)
				rating = bayes.article_rating(t)
				print "Pred: %s, Prob: %.4f" % (prediction, rating)
				print "Prediction for: %d is %s, naive predicted %s and I chose %s. CRM probability was %.4f" % (row["article_id"], prediction, row["prediction"], row["like_flag"], rating)
				#query = """INSERT into test_predictions (article_id, user_name, like_flag, naive_bayes, crm, crm_prob) VALUES (%s, '%s', %s, '%s', '%s', %s)""" % (row["article_id"], "brad", row["like_flag"], row["prediction"], prediction, probability)
				query = """UPDATE test_predictions set pg_bayes = '%s', pg_dislike_score = %.4f where user_name = 'brad' and article_id = '%s'""" % (prediction, rating, row["article_id"])
				print query
				cur.execute(query)

#spam_message = "Viagra, cialis for $2.59!!! Call 555-54-53"
#bayes.train(spam_message, True)
#
#ham_message = "Paul Graham doesn't need Viagra. He is NP-hard."
#bayes.train(ham_message, False)
#
#m1 = "Cheap viagra for 2.59"
#print bayes.classify(m1)       # => True
#print bayes.article_rating(m1)   # => 0.97
#
#m2 = "I don't use viagra (yet)"
#print bayes.classify(m2)       # => False
#print bayes.article_rating(m2)   # => 0.16



storage.finish()