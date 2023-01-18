from flask import Flask, render_template

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
