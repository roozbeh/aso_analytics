from utils import *
from db import *
import string
import re



def fetch_competitor_apps():
	keyword = "slide+show"
	langCode = 'us'

	url = "https://itunes.apple.com/search?term=%s&country=%s&entity=software&limit=200" % (keyword, langCode)
	return get_jsonparsed_data(url)
	
def parse_keywords(cursor, db_app_id, instring, type):
	keywords = re.split(';|,|\*|\n| |-|&|:|\+|\(|\)|\'|\"|\.', instring)
	save_keywords(cursor, db_app_id, keywords, type)
	
cursor = connect_db()


json_response = fetch_competitor_apps()

counter = 1
for app_item in json_response["results"]:
	name = app_item["trackName"]
	app_url = app_item["trackViewUrl"]
	app_id = app_item["trackId"]
	desc = app_item["description"]

	print("# %d %s" % (counter, name))
	
	db_app_id = lookup_app(cursor, app_id, name, app_url)
	if "SmartStory - " in name:
		print "SMART STORY, ranking: %d, lang: %s" % (counter, langCode)
	else:
		parse_keywords(cursor, db_app_id, name, 'name')
		parse_keywords(cursor, db_app_id, desc, 'description')
	  	
	counter=counter+1


close_db(cursor)

# select keyword, count(keyword) from keyword where source = 'name' AND keyword != ' ' and keyword != '&' group by keyword order by count(keyword);
# select keyword, count(keyword) from keyword where source = 'description' AND keyword != ' ' and keyword != '&' group by keyword order by count(keyword);


