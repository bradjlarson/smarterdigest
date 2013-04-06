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
	order by a.article_id \
	limit 100")
	
	rows = cur.fetchall()
	
	for row in rows:
		t = row["article_text"]
		t = unquote_plus(t)
		if row["like_flag"] == 1:
			c.learn("like", t)
		else:
			c.learn("dislike", t)
	
	cur.execute("SELECT a.article_id, a.prediction, a.like_flag, b.article_text from test_user_activity a, \
	test_article b where a.article_id = b.article_id and a.article_id between 1334 and 1434 and user_name ='brad'")
	
	rows = cur.fetchall()
	
	like_like = 0
	like_dislike = 0
	dislike_like = 0
	dislike_dislike = 0
	nblike_like = 0
	nblike_dislike = 0
	nbdislike_like = 0
	nbdislike_dislike = 0
	total = 0
	
	for row in rows:
		t = row["article_text"]
		t = unquote_plus(t)
		(prediction, probability) = c.classify(t)
		print "Pred: %s, Prob: %.4f" % (prediction, probability)
		print "Prediction for: %s is %s, naive predicted %s and I chose %s. CRM probability was %.4f" % (row["article_id"], prediction, row["prediction"], row["like_flag"], probability)
		if prediction == "like" and row["like_flag"] == 1:
			like_like = like_like + 1
		elif prediction == "like" and row["like_flag"] == 0:
			like_dislike = like_dislike + 1 
		elif prediction == "dislike" and row["like_flag"] == 1:
			dislike_like = dislike_like + 1
		else:
			dislike_dislike = dislike_dislike + 1
			
		if row["prediction"] == "like" and row["like_flag"] == 1:
			nblike_like = nblike_like + 1
		elif row["prediction"] == "like" and row["like_flag"] == 0:
			nblike_dislike = nblike_dislike + 1 
		elif row["prediction"] == "dislike" and row["like_flag"] == 1:
			nbdislike_like = nbdislike_like + 1
		else:
			nbdislike_dislike = nbdislike_dislike + 1	
		
		total = total + 1
	
	crm_total = ((like_like + dislike_dislike) / total)
	crm_like = (like_like / (like_like + like_dislike))
	crm_dislike = (dislike_dislike / (dislike_like + dislike_dislike))
	nb_total = ((nblike_like + nbdislike_dislike) / total)
	nb_like = (nblike_like / (nblike_like + nblike_dislike))
	nb_dislike = (nbdislike_dislike / (nbdislike_like + nbdislike_dislike))
	
	print "CRM Accuracy was: %.4f" % crm_total
	print "CRM Like Accuracy was: %.4f" % crm_like
	print "CRM Dislike Accuracy was: %.4f" % crm_dislike	
	print "NB Accuracy was: %.4f" % nb_total
	print "NB Like Accuracy was: %.4f" % nb_like
	print "NB Dislike Accuracy was: %.4f" % nb_dislike	
			