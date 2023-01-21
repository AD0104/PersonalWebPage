from flask import Flask, render_template,request, make_response, jsonify

app = Flask(__name__, static_folder="./static/", template_folder="./templates/")

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
    return make_custom_response("200","Ok") 

