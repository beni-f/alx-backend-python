from instascrape import *

wsj = Profile('https://www.instagram.com/wsj/')
wsj_hashtag = Hashtag('https://www.instagram.com/explore/tags/wsj')

wsj.scrape()
wsj_hashtag.scrape()