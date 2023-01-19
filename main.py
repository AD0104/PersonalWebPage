from flask import Flask, render_template,request

app = Flask(__name__, static_folder="./static/", template_folder="./templates/")

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
    form_name = request.form.get("form-name")
    form_email = request.form.get("form-email")
    form_message = request.form.get("form-message")
    print("\n[MENSAJES POST]")
    print(f"[form_name]: [{form_name}]")
    print(f"[form_email]: [{form_email}]")
    print(f"[form_message]: [{form_message}]")
    return 200

