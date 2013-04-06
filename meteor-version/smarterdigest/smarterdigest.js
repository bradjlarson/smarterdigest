
if (Meteor.isServer) {
	Feeds = new Meteor.Collection("Feeds");

	Articles = new Meteor.Collection("Articles");
		
	Meteor.publish('Feeds', function () {
	  return Feeds.find();
	});
	
	Meteor.publish('Articles', function () {
	  return Articles.find();
	});
	
}

if (Meteor.isClient) {
	Session.setDefault("current-feed", "Hacker News");
	Session.set("current-feed", "Hacker News");
	
	Feeds = new Meteor.Collection("Feeds");
	
	Articles = new Meteor.Collection("Articles");
	
	Template.sidebar.feed = function() {
		return Feeds.find({}, {sort: {feed_name: 1}});
	};
	
	Template.feed.current_feed = function() {
		console.log(Session.get("current-feed"));
		return Session.get("current-feed");
	};
	
	Template.feed.feed_articles = function() {
		return Articles.find({}, {sort: {article_id: -1}});
	};
	

	
	/*
  Template.hello.events({
    'click input' : function () {
      // template data, if any, is available in 'this'
      if (typeof console !== 'undefined')
        console.log("You pressed the button");
    }
  });
	*/
}
