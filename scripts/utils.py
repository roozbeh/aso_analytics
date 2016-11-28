from urllib import urlopen
import json

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def fetch_competitor_apps():
    keyword = "slide+show"
    langCode = 'us'

    url = "https://itunes.apple.com/search?term=%s&country=%s&entity=software&limit=200" % (keyword, langCode)
    return get_jsonparsed_data(url)


def parse_keywords(cursor, db_app_id, instring, type):
	keywords = re.split(';|,|\*|\n| |-|&|:|\+|\(|\)|\'|\"|\.', instring)
	save_keywords(cursor, db_app_id, keywords, type)

