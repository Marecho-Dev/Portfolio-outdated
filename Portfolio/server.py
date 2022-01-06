#flask implements http.server. It's a framework built off of that module. Flask/Django -> flask is a micro framework
#within your web server folder do the command -m venv venv and then .\.\scripts\activate.bat to begin running virtual environment
#now you can begin updating your server with whatever information you need to
#pip3 install flask
#set FLASK_APP=servername.py
#flask run
#debug mode FLASK_ENV=development
from flask import Flask, render_template, url_for, request, redirect #render template allows us to process html file
import csv
app = Flask(__name__)
print(__name__)

# @app.route('/<username>/<int:post_id>') #decorator -> gives us extra tools to build a server ->anytime we hit '/'
# #<username> is something we can pass on <> 
# #look at converter types to see what you can pass
# def hello_world(username=None, post_id=None):#setting default variables
# 	return render_template('index.html',name=username,post_id=post_id) #template in flask defaults to looking in current dir for a templates folder
#MIME stands for multipurpose internet mail extensions
@app.route('/<string:page_name>') #do this so the route is passed as a string variable creating our render_template variable
#this makes it so we don't have to copy and paste this for every single html file that exists
def my_home(page_name):
	return render_template(page_name)

# @app.route('/favicon.ico')
#  def favicon():
# 	return "test"
#Flask Templates
#route route,
def write_to_file(data):
	with open('database.txt',mode='a') as my_db:
		my_db.write(f"\n{data['email']},{data['subject']},{data['message']}")
def write_to_csv(data):
	with open('database.csv',newline = '',mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',',quotechar  ='"',quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])#get sends information, post saves information
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_file(data)
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'did not save to database'	
	else:
		return 'something went wrong'
    	
