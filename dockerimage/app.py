from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Configure db
app.config['MYSQL_HOST'] = os.environ['DB_HOST']
app.config['MYSQL_USER'] = os.environ['DB_USER']
app.config['MYSQL_PASSWORD'] = os.environ['DB_PASSWORD']
app.config['MYSQL_DB'] = os.environ['DB_DATABASE']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)
# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(host="0.0.0.0", port=8000, debug=True)