from flaskext.mysql import MySQL
from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)
mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = ''
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
@app.route("/")
def index():
	return render_template("index1.html", title="SignUP")
@app.route("/signUp",methods=["POST"])
def signUp():
	username = str(request.form["user"])
	password = str(request.form["password"])
	email = str(request.form["email"])
	
	cursor = conn.cursor()
	
	cursor.execute("INSERT INTO mydatabase (UserName,Password,EmailId)VALUES(%s,%s,%s)",(username,password,email))
	conn.commit()
	return redirect(url_for("login"))
	

@app.route("/login")
def login():
	return render_template("login.html",title="data")

@app.route("/checkUser",methods=["POST"])
def check():
	username = str(request.form["user"])
	password = str(request.form["password"])
	cursor = conn.cursor()
	cursor.execute("SELECT name FROM mydatabase WHERE name ='"+username+"'")
	user = cursor.fetchone()
	
	if len(user) is 1:
		return redirect(url_for("home"))
	else:
		return "failed"
@app.route("/home")
def home():
	return render_template("home.html")
if __name__ == "__main__":
    app.run(debug=True)
