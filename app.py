from flask import Flask
app = Flask(__name__)

# Different URLs can be redirected to the same page.
@app.route("/")
@app.route("/home/")
def home():
	return "Home"

# This URL will return a 404 error if you try to access it with a trailing slash ("/about/").
@app.route("/about") # Always add a trailing slash at the end to avoid this error.
def about():
	return "About"

# URLs can accept inputs through its variable parts.
@app.route("/about/<location>/")
def about_location(location):
	return "I am from %s." % location

@app.route("/skills/")
def skills():
	return "Skills"

# It can also accept inputs with specified data types.
@app.route("/skills/<int:toeic_score>/")
def skills_toeic(toeic_score):
	return "My TOEIC score is %d / 90." % toeic_score

@app.route("/projects/")
def projects():
	return "Projects"

@app.route("/contact/")
def contact():
	return "Contact"

if __name__ == "__main__":
	app.run()