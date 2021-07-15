import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
import json, sys
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'static/images/recipes'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mongo = PyMongo(app)


"""
Example:
https://github.com/richardhenyash/freefrom
https://github.com/dejvoss/cs_cdins-msp3-recipe-book
https://github.com/elisamunoz/docu-llamas

Frontend

1. CRUD
    
    - Make sure that add/edit/delete can only be done by the person who created the recipe --> Required
    - Exception Handling --> Required
        https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling
        https://docs.python.org/3/tutorial/errors.html
    - Use of Forms --> Optional

    HTML:
        POST --> Saving to the db without validation

    Form:
        POST --> forms.validate_on_submit() (basically passes the data in the request through the Form validations for each field) --> Save the form data not the request data

    https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
    https://hackersandslackers.com/flask-wtforms-forms/

    - Using different apps for Profiles and Recipes (blueprint as a library) --> Optional
    - Upload and save a file --> Needed
    - Add email --> Adding some JS (recommended)

2. Experiment with the schema:

users collection
{
    username
    password
}

recipes collection
{
    name: str
    description: str
    cooking_time: str
    photo: str --> file location where the photo is saved <img src="{{ recipe.photo }}">
        https://stackoverflow.com/questions/44926465/upload-image-in-flask
    ingredients: List[dict] = [
        {
            _id: ObjectId(...)
            amount: int
            measure: str
        },
        ...
        {

        }        
    ]
}

ingredients collection
{
    name
    description
    additives
    photo
}

"""


def is_logged_in():
    """
    return: None or the username
    """
    return session.get("user")


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    try:
        if request.method == "POST":
            # # check if the post request has the file part
            # if 'file' not in request.files:
            #     flash('No file part')
            #     return redirect(request.url)

            file = request.files['file']

            # # if user does not select file, browser also
            # # submit an empty part without filename
            # if file.filename == '':
            #     flash('No selected file')
            #     return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                recipe = {
                    "category_name": request.form.get("category_name"),
                    "recipe_name": request.form.get("recipe_name"),
                    "recipe_description": request.form.get("recipe_description"),
                    "preparation_time": request.form.get("preparation_time"),
                    "created_by": session["user"],
                    "ingredients": json.loads(request.form.get("ingredients")),
                    "photo": os.path.join(app.config['UPLOAD_FOLDER'], filename)
                }
                file = request.files['file']
                mongo.db.recipes.insert_one(recipe)
                flash("recipe Successfully Added")
                return redirect(url_for("get_recipes"))
            else:
                flash ("Unexpected error: Please attach the image")
                raise Exception("Please attach the image")

        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("add_recipe.html", categories=categories)

    except:
        return redirect(url_for("get_recipes"))



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "preparation_time": request.form.get("preparation_time"),
            "created_by": session["user"],
            "ingredients": json.loads(request.form.get("ingredients"))
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, recipe)
        flash("Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)

    # return recipe.ingredients

    return render_template("edit_recipe.html", recipe=recipe, categories=categories)

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))

@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")

"""
@app.errorhandler(404)
def handle_keyerror(e):
    return render_template("/error.html", {...}), 404

@app.errorhandler(KeyError)
def handle_keyerror(e):
    return render_template("/error.html", {...}), 500

@app.errorhandler(Exception)
def handle_bad_request(e):
    if isinstance(e, bson.errors.InvalidId):
        flash("An error with the database occurred, couldn't find recipe", e)
        return render_template("/error.html", {"message": "..."})

    if isinstance(e, pymongo.errors.CursorNotFound):
        flash("An error with the database occurred, couldn't find recipe", e)
    print(type(e))
    return render_template("/error.html", {...}), 500
"""

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)