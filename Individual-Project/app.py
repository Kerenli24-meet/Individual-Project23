from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


firebaseConfig = {
"apiKey": "AIzaSyAZ3hlM0hPda7DvQ8BZF7yz-QOOfe2GVD4",
"authDomain": "style-44578.firebaseapp.com",
"projectId": "style-44578",
"storageBucket": "style-44578.appspot.com",
"messagingSenderId": "754926842813",
"appId": "1:754926842813:web:8b09d4279a92f1eb02d8d4",
"measurementId": "G-DXEM697MTL",
"databaseURL": "https://style-44578-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()



app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        fullname = request.form['fullname']
        username = request.form['username']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user={'user':username, "fullname":fullname, "password":password, "email":email}
            UID=login_session['user']['localId']
            db.child('Users').child(UID).set(user)
            return redirect(url_for('signin'))
        except:
            error = "Authentication failed"
    return render_template("signup.html")


@app.route('/', methods=['GET', 'POST'])
def signin():
   error = ""
   if request.method == 'POST':
       # fname = request.form['fname']
       # lname = request.form['lname']
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
       except:
           error = "Authentication failed"
   return render_template("signin.html")


@app.route('/removeC')
def remove():
    try:
        UID = login_session['user']['localId']
        print((UID))
        db.child("Users").child(UID).remove()
        return redirect(url_for('signin'))
    except Exception as e:
        error = "Couldn’t remove object"
        print (error)
        return render_template("home.html")
    return render_template("signin.html")

@app.route("/display_user")
def display_user():
    # Gets the current user’s information from the database
    UID = login_session['user']['localId']
    user = db.child("users").child(UID).get().val()
    return render_template("home.html", fullname=user["fullname"])




@app.route('/home', methods=['GET', 'POST'])
def home():
   return render_template("home.html")

# @app.route("/display_user")
# def display_user():
#     # Gets the current user’s information from the database
#     UID = login_session['user']['localId']
#     user = db.child("Users").child(UID).get().val()
#     return render_template("home.html",  fullname=user["fullname"])


@app.route('/women')
def women():
    return render_template("women.html")

@app.route('/men')
def men():
    return render_template("men.html")





@app.route('/cart')
def Cart():
    return render_template("cart.html")



# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#    error = ""
#    if request.method == 'POST':
#        email = request.form['email']
#        password = request.form['password']
#        fullN = request.form['fullname']
#        UserN = request.form['username']
#        Bio= request.form['bio']
#        try:
#             login_session['user'] = auth.create_user_with_email_and_password(email, password)
#             return redirect(url_for("home.html"))

#        user={
#        "email": email,
#        "password": password,
#        "fullname":fullN,
#        "username":UserN,
#        "bio":Bio,
#        }
#        db.child("Users").get().val()
#        except:
#            error = "Authentication failed"
#     return render_template("signup.html")
# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)


from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below












    


    




@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)