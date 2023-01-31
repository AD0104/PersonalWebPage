from flask import Flask, render_template,request, make_response, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder="./static/", template_folder="./templates/")
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'programmer'
app.config['MYSQL_DB'] = 'comments_submissions'
 
mysql = MySQL(app)

def make_custom_response(status: str, message: str):
    return make_response(
            jsonify(
                {
                    "message": message,
                    "status": status
                }
            )
        )

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')
@app.route("/testimonials")
def testimonials():
    return render_template('testimonials.html')
@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/contact/submit", methods=["POST"])
def contact_form_submit():
    form_name = request.form.get("form-name-input")
    form_email = request.form.get("form-email-input")
    form_message = request.form.get("form-message-textarea")
    if(form_name == "" or form_email == "" or form_message == ""):
        return make_custom_response("400", "There're some empty fields!")
    cursor = mysql.connection.cursor()
    try:
        query_result = cursor.execute(f"""INSERT INTO submissions (submission_user_name,submission_user_email,submission_user_msg)
                       VALUES ('{form_name}','{form_email}','{form_message}')""")
        if(query_result == 0):
            return make_custom_response("500", "Error when submiting your message, please try again later!")
    except Exception as e:
        print("\n[Exception commiting to MySQL]")
        print(e)
        return make_custom_response("500", "Error when submiting your message, please try again later!")
    mysql.connection.commit()
    cursor.close()
    return make_custom_response("200","Ok") 

