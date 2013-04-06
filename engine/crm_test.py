#!/usr/bin/python
from crm import Classifier
from urllib import unquote_plus
import MySQLdb as mdb
import sys

c = Classifier("/Dropbox/Coding/smarterdigest/engine/data", ["like", "dislike"])

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
			c.learn("like", t)
		else:
			c.learn("dislike", t)
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
				(prediction, probability) = c.classify(t)
				print "Pred: %s, Prob: %.4f" % (prediction, probability)
				print "Prediction for: %d is %s, naive predicted %s and I chose %s. CRM probability was %.4f" % (row["article_id"], prediction, row["prediction"], row["like_flag"], probability)
				query = """INSERT into test_predictions (article_id, user_name, like_flag, naive_bayes, crm, crm_prob) VALUES (%s, '%s', %s, '%s', '%s', %s)""" % (row["article_id"], "brad", row["like_flag"], row["prediction"], prediction, probability)
				print query
				cur.execute(query)
		
		
		
		
		
		
		
		
		
			