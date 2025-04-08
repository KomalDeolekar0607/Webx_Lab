from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET'])

def home():
    # name = request.form.get('name', 'Guest')  # Get name from form input
    name = request.args.get('name', 'Guest')  # Get name from form input

    return f'''
        <html>
        <head>
            <title>Flask App</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin: 50px;
                    background-color: #f4f4f4;
                }}
                h1 {{
                    color: #333;
                }}
                form {{
                    margin-top: 20px;
                }}
                input, button {{
                    padding: 10px;
                    font-size: 16px;
                    margin: 5px;
                }}
                button {{
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    cursor: pointer;
                }}
                button:hover {{
                    background-color: #0056b3;
                }}
            </style>
        </head>
        <body>
            <h1>Welcome, {name}!</h1>
            <form method="get">
                <input type="text" name="name" placeholder="Enter your name" required>
                <button type="submit">Submit</button>
            </form>
            <p><a href="/contact">Go to Contact Form</a></p>
        </body>
        </html>
    '''

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        return f"""
<html>
            <head>
                <title>Thank You</title>
                <style>
                    body {{ font-family: Arial, sans-serif; text-align: center; margin: 50px; }}
                    h1 {{ color: #28a745; }}
                    a {{ text-decoration: none; color: #007BFF; }}
                    a:hover {{ color: #0056b3; }}
                </style>
            </head>
            <body>
                <h1>Thank You, {name}!</h1>
                <p>Your email: {email}</p>
                <a href="/">Back to Home</a>
            </body>
        </html>
"""

    return """
        <html>
        <head>
            <title>Contact Us</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin: 50px; background-color: #f4f4f4; }
                form { margin-top: 20px; }
                input, button { padding: 10px; font-size: 16px; margin: 5px; }
                button { background-color: #28a745; color: white; border: none; cursor: pointer; }
                button:hover { background-color: #218838; }
            </style>
        </head>
        <body>
            <h1>Contact Us</h1>
            <form method="post">
                <input type="text" name="name" placeholder="Your Name" required><br>
                <input type="email" name="email" placeholder="Your Email" required><br>
                <button type="submit">Submit</button>
            </form>
            <p><a href="/">Back to Home</a></p>
        </body>
        </html>
    """

# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         # Use request.form instead of request.args
#         name = request.form.get('name')  
#         email = request.form.get('email')

#         return f"""
#         <html>
#             <head>
#                 <title>Thank You</title>
#                 <style>
#                     body {{ font-family: Arial, sans-serif; text-align: center; margin: 50px; }}
#                     h1 {{ color: #28a745; }}
#                     a {{ text-decoration: none; color: #007BFF; }}
#                     a:hover {{ color: #0056b3; }}
#                 </style>
#             </head>
#             <body>
#                 <h1>Thank You, {name}!</h1>
#                 <p>Your email: {email}</p>
#                 <a href="/">Back to Home</a>
#             </body>
#         </html>
#         """
    
#     return """
#         <html>
#         <head>
#             <title>Contact Us</title>
#             <style>
#                 body { font-family: Arial, sans-serif; text-align: center; margin: 50px; background-color: #f4f4f4; }
#                 form { margin-top: 20px; }
#                 input, button { padding: 10px; font-size: 16px; margin: 5px; }
#                 button { background-color: #28a745; color: white; border: none; cursor: pointer; }
#                 button:hover { background-color: #218838; }
#             </style>
#         </head>
#         <body>
#             <h1>Contact Us</h1>
#             <form method="post">
#                 <input type="text" name="name" placeholder="Your Name" required><br>
#                 <input type="email" name="email" placeholder="Your Email" required><br>
#                 <button type="submit">Submit</button>
#             </form>
#             <p><a href="/">Back to Home</a></p>
#         </body>
#         </html>
#     """


if __name__ == '__main__':
    app.run(debug=True)
