from flask import *
from replit import db
import random
import init_jokes
init_jokes.initdb()
app = Flask('app')
def log(text, file="event_logs.log"):
	with open(file,'a' ) as f: 
		f.write(text)
		f.write('\n')

t=4
@app.route('/joke')
def serve_route1():
  ldb = [i for i in db]
  log("user visited /joke")
  return render_template('yomomma.html', joke=db[random.choice(ldb)])
	
@app.route('/')
def serve_main_route():
	log("user visited /")
	return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def serve_add_route():
	global t;
	if (request.args.get('joke')) == None: return 'invalad joke'
	with open("pending.txt","a") as file:
		file.write( request.args.get('joke'))
		file.write("\n")
	t+=1
	log(f"user visited /add, joke={request.args.get('joke')}")
	return "joke pending approval<br><a href='/'>home</a>"

@app.route("/all")
def serve_route_all():
	res = ''
	for k in db.keys():
		res += f'{db[k]} <br>'
	log("user visited /all")
	lenjoke = len(db)
	print(lenjoke)
	return render_template("all.html", cont=res)

	
@app.route("/addjoke")
def serve_route_add():
	log("user visited /addjoke")

	return render_template("add.html")
	



app.run(host='0.0.0.0', port=8080)
