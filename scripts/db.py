import pymysql.cursors
connection = 0

def connect_db():
	global connection
	connection = pymysql.connect(host='localhost',
	                         user='root',
	                         password='',
	                         charset='utf8mb4',
	                         cursorclass=pymysql.cursors.DictCursor)
	cursor = connection.cursor()
	connection.select_db("keywords")
		
	return cursor

def close_db(cursor):
	global connection

	connection.commit()
	cursor.close()
	
def lookup_app(cur, app_id, name, app_url):
	# find or create
	cur.execute("SELECT id FROM app WHERE app_id='%s'" % app_id)
	
	first = cur.fetchone()
	if first:
	    return first['id']

	cur.execute("INSERT INTO app (name, url, type, app_id, created) VALUES ('%s', '%s', 'ios', '%s', NOW())" % (name, app_url, app_id))
	
	return cur.lastrowid
	
def save_keywords(cur, db_app_id, keywords, type):
  # find or create
	cur.execute("DELETE FROM keyword WHERE (app_id='%s' AND source = '%s')" % (db_app_id, type))
	
	for keyword in keywords:
		if keyword in [' ', '-', '&', '']:
			continue
			
		sql = "INSERT INTO keyword (keyword, app_id, source, created) VALUES ('%s', '%s', '%s', NOW())" % (keyword.lower(), db_app_id, type)
		try:
			cur.execute(sql)
		except:
			print "Exception in saving keyword: ", keyword
	
	return 0


def test_db():
	cursor = connect_db()
	test_app_id = 123
	cursor.execute("DELETE FROM keyword WHERE app_id= (select id from app where app_id = '%s')" % test_app_id)
	cursor.execute("DELETE FROM app WHERE app_id='%s'" % test_app_id)
	
	for i in range(0,2):
		db_app_id = lookup_app(cursor, 123, '123', '123')
		print "db_app_id (%d) : %d" % (i, db_app_id)
		
	save_keywords(cursor, db_app_id, ['1', '2', '3'], 'name')
	save_keywords(cursor, db_app_id, ['11', '22', '33'], 'description')
	
	close_db(cursor)
	
	
