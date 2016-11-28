from utils import *
from db import *
import string
import re
import datetime
import time
import statsmodels.formula.api as sm

def calc_features_for_app(app_data):
    name = app_data["trackName"]
    isUniversal = 1 if app_data["features"] == [u'iosUniversal'] else 0
    meanAge = int(app_data["contentAdvisoryRating"].split('+')[0])
    rateCountCurrVersion = app_data["userRatingCountForCurrentVersion"] if "userRatingCountForCurrentVersion" in app_data else 0
    releaseDate = int(time.mktime(time.strptime(app_data["releaseDate"], '%Y-%m-%dT%H:%M:%SZ')))
    size = int(app_data["fileSizeBytes"])
    numLangs = len(app_data["languageCodesISO2A"])
    
    currVerReleaseDate = int(time.mktime(time.strptime(app_data["currentVersionReleaseDate"], '%Y-%m-%dT%H:%M:%SZ')))
    rateCount = app_data["userRatingCount"] if "userRatingCount" in app_data else 0
    avgRatingCurr = app_data["averageUserRatingForCurrentVersion"] if "averageUserRatingForCurrentVersion" in app_data else 0
    avgRating = app_data["averageUserRating"] if "averageUserRating" in app_data else 0
    minVersion = float(app_data["minimumOsVersion"].split('.')[0])
    # TODO: add genres
    #       1            2         3                      4           5      6         7                  8
    # return [isUniversal, meanAge, rateCountCurrVersion, releaseDate, size, numLangs, currVerReleaseDate, rateCount, avgRatingCurr, avgRating, minVersion]
    return [currVerReleaseDate, rateCount, avgRatingCurr, minVersion]


json_response = fetch_competitor_apps()
features = [calc_features_for_app(x) for x in json_response["results"]]
y = range(0, 200)
result = sm.OLS( y, features ).fit()
result.summary()

    