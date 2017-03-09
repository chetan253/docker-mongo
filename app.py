import pymongo
import bottle

@bottle.route('/')
def start_page():
	return bottle.template('main',"")
	
	
@bottle.post('/')
def process_add():
	firstname = bottle.request.forms.get('firstname')
	lastname = bottle.request.forms.get('lastname')
	age = bottle.request.forms.get('age')
	try:
		collection.insert({'firstname':firstname, 'lastname':lastname,'age':age})
		return("detail inserted")
	except pymongo.errors.OperationFailure:
            	print("oops, mongo error")
            	
connection = pymongo.MongoClient("mongodb://datastore:27017/dockermongo")
database = connection.people
collection = database.details

bottle.debug(True)
bottle.run(host = '0.0.0.0')
