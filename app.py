import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# --CONFIGURATION-- #

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# --ALL RECIPES -- #


@app.route("/")
@app.route("/get_recipes")
def get_recipes():

    limit = 20
    recipe_name = lambda recipes: recipes[1]

    recipes = list(
        mongo.db.recipes.find().sort("recipe_name", -1).limit(limit))
    return render_template("index.html", recipes=recipes)

# -- CATEGORIES -- #


@app.route("/filter_recipes/<category_name>")
def filter_recipes(category_name):
    if category_name == "cooking":
        recipes = list(mongo.db.recipes.find({"category_name": "cooking"}))
    elif category_name == "baking":
        recipes = list(mongo.db.recipes.find({"category_name": "baking"}))
    elif category_name == "snacks":
        recipes = list(mongo.db.recipes.find({"category_name": "snacks"}))
    return render_template(
        "index.html", recipes=recipes, page_title=category_name)

# -- PROFILE -- #


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        recipes = mongo.db.recipes.find({"created_by": session["user"]})
        return render_template("profile.html", username=username, recipes=recipes)

    return redirect(url_for("login"))

# -- INDIVIDUAL RECIPES -- #


@app.route("/single_recipe/<recipe_id>")
def single_recipe(recipe_id):
    recipes = list(mongo.db.recipes.find())

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "single_recipe.html", recipe=recipe)

# -- SEARCH -- #


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("index.html", recipes=recipes)

# -- REGISTRATION -- #


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

        # put new user into 'session' cookie
        session['user'] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")

# -- LOGIN -- #


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")



# -- LOGOUT -- #


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

# -- ADD RECIPE -- #


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe_is_vegetarian = "on" if request.form.get(
            "recipe_is_vegetarian") else "off"
        recipe_is_vegan = "on" if request.form.get(
            "recipe_is_vegan") else "off"
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_cals": request.form.get("recipe_cals"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_is_vegan": recipe_is_vegan,
            "recipe_is_vegetarian": recipe_is_vegetarian,
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)

# -- EDIT RECIPE -- #


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        recipe_is_vegetarian = "on" if request.form.get(
            "recipe_is_vegetarian") else "off"
        recipe_is_vegan = "on" if request.form.get(
            "recipe_is_vegan") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_cals": request.form.get("recipe_cals"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_is_vegan": recipe_is_vegan,
            "recipe_is_vegetarian": recipe_is_vegetarian,
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return render_template("single_recipe.html", recipe=recipe)

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)

# -- DELETE RECIPE -- #


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
