from flask import Flask, render_template , url_for,redirect,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/user/<username>')
def user(username):
    return render_template("user.html", username=username)

# @app.route('/user_redirect')
# def user_redirect():    
#     username = request.args.get('name' , 'Guest')
#     return redirect(url_for('user', username = username))

@app.route('/user_redirect', methods=['GET', 'POST'])
def user_redirect():    
    if request.method == 'POST':
        username = request.form.get('name', 'Guest')  # Use request.form for POST
    else:
        username = request.args.get('name', 'Guest')  # Use request.args for GET

    return redirect(url_for('user', username=("Guest" if username=="" else username[0].upper()+username[1:])))


if __name__ == '__main__' :
    app.run(debug=True)