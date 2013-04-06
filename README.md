smarterdigest
=============

Predictive RSS

This project uses bayesian classification to predict which articles I'll like based on the articles I've read and tagged in the past. 

I use the open source text extraction tool Goose (https://github.com/jiminoc/goose) to get the article text for my classification engine. 

I use the open source RSS library Simplepie (http://simplepie.org/) to process the RSS feed. 

The primary classification engine is a modified version of (https://github.com/dhotson/classifier-php), which I modified to allow the classifications to persist between sessions. 
I've added a second classification engine that is a modified version of (https://github.com/dchest/pybayesantispam) to connect to my database and save the predictions. 
Finally, I've added a third classification engine, a python interface to CRM114 (http://crm114.sourceforge.net/ and http://www.elegantchaos.com/node/129).

I used project for over a month, classifying over 1000 articles and capturing the predictions for each. The engine worked pretty well for articles it thought I would dislike, with the primary classification being 85% accurate. The likes were less accurate - around 60%.

However, when I used all three methods, I was able to get the accuracy up to ~93% for the dislikes and ~73% for the likes. 

Right now I'm working on converting the frontend to Meteor.js for more rapid development, and then I'd like to add some sort of latent semantic indexing/analysis to try and improve the predictions even further. I'm also looking to add the ability to have multiple RSS feeds. 
