from flask import Flask, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return f'''
    <html lang="en">
    <head>
        <title>Flask App</title>
        <link rel="stylesheet" href="{url_for('static', filename='styles.css')}">
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the App!!!</h1>
            <p><a href="{url_for('profile', name='Komal')}">Go to Profile Page</a></p>
            <p><a href="{url_for('submit')}">Go to Submit Page</a></p>
        </div>
    </body>
    </html>
    '''

@app.route('/profile/<name>')
def profile(name):
    return f'''
    <html lang="en">
    <head>
        <title>Profile</title>
        <link rel="stylesheet" href="{url_for('static', filename='styles.css')}">
    </head>
    <body>
        <div class="container">
            <h1>Welcome, {name}!</h1>
            <a href="{url_for('home')}">Back to Home</a>
        </div>
    </body>
    </html>
    '''

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        return f'''
        <html lang="en">
        <head>
            <title>Submission Successful</title>
            <link rel="stylesheet" href="{url_for('static', filename='styles.css')}">
        </head>
        <body>
            <div class="container">
                <h1>Thank You, {name}!</h1>
                <p>Your age ({age}) has been submitted successfully.</p>
                <a href="{url_for('home')}">Back to Home</a>
            </div>
        </body>
        </html>
        '''
    return f'''
    <html lang="en">
    <head>
        <title>Submit Form</title>
        <link rel="stylesheet" href="{url_for('static', filename='styles.css')}">
    </head>
    <body>
        <div class="container">
            <h1>Submit Your Details</h1>
            <form method="post">
                <input type="text" name="name" placeholder="Enter your name" required>
                <input type="number" name="age" placeholder="Enter your age" required>
                <button type="submit">Submit</button>
            </form>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, request , url_for

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return f'''
#     <html>
#         <head>
#             <title>Flask App</title>
#             <style>
#                 body {{
#                     font-family: Arial, sans-serif;
#                     text-align: center;
#                     margin: 50px;
#                     background-color: #f4f4f4;
#                 }}
#                 h1 {{
#                     color: #333;
#                 }}
#                 form {{
#                     margin-top: 20px;
#                 }}
#                 input, button {{
#                     padding: 10px;
#                     font-size: 16px;
#                     margin: 5px;
#                 }}
#                 button {{
#                     background-color: #007BFF;
#                     color: white;
#                     border: none;
#                     cursor: pointer;
#                 }}
#                 button:hover {{
#                     background-color: #0056b3;
#                 }}
#             </style>
#         </head>
#         <body>
#             <h1>Welcome ti the App!!!</h1>
#             <p><a href="{url_for('profile',name="Komal")}">Go to Profile Page</a></p>
#             <p><a href="{url_for('submit')}">Go to Submit Page</a></p>

#         </body>
#         </html>
#     '''

# @app.route('/profile/<name>')
# def profile(name):
#     return f'''
#     <html lang="en">
# <head>
#     <title>Profile</title>
#     <link rel="stylesheet" href="{ url_for('static', filename='styles.css') }">
# </head>
# <body>
#     <div class="container">
#         <h1>Welcome, { name }!</h1>
#         <a href="{ url_for('home') }">Back to Home</a>
#     </div>
# </body>
# </html>
# '''

# @app.route('/submit',methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         age = request.form.get('age')
#         return f"<h1>Thank you, {name}! Your age ({age}) has been submitted successfully.</h1> <a href='/'>Back to Home</a>"
#     return f"""
#     <html lang="en">
# <head>
#     <title>Submit Form</title>
#     <link rel="stylesheet" href="{url_for('static', filename='styles.css') }">
# </head>
# <body>
#     <div class="container">
#         <h1>Submit Your Details</h1>
#             <form method="post">
#                 <input type="text" name="name" placeholder="Enter your name" required>
#                 <input type="number" name="age" placeholder="Enter your age" required>
#                 <button type="submit">Submit</button>
#             </form>
#     </div>
# </body>
# </html>
    
# """

# if __name__ == '__main__':
#     app.run(debug=True)