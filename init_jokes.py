# init db to contain jokes
from replit import db
def load_joke_file(file="jokes.txt"):
	with open(file, 'r') as f:
		global r
		r = f.readlines()
		
load_joke_file()
def initdb():
	global r
	c = 0
	for n in r:
		db[str(c)] = n
		c+=1
	print(db.keys())

