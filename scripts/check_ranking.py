from utils import *

def get_language_ranking(keyword, langCode):
	url = "https://itunes.apple.com/search?term=%s&country=%s&entity=software&limit=200" % (keyword, langCode)
	json_response = get_jsonparsed_data(url)

	counter = 1
	visited = False
	for app_item in json_response["results"]:
	  # print "#%d %s" %(counter, app_item["trackName"])
	  if "SmartStory" in app_item["trackName"]:
			# print "SMART STORY, ranking: %d, lang: %s" % (counter, langCode)
			return counter
	  counter=counter+1
	
	if not visited:
		return 201
		

languages = ["us", "fr", "de", "jp", "kr",  "cn", "es", "mx", "ca"]
keywords = ["slideshow", "slide+show", "create+video", "slideshow+maker", "slideshow+with+music", "video+maker"]



for langCode in languages:
	for keyword in keywords:
		print "Checking app store for %s in %s: %d" % (keyword, langCode, get_language_ranking(keyword, langCode)) 
		


