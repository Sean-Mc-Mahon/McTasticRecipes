import os
import math
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo, pymongo
from flask_paginate import get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# CONFIGURATION

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# GLOBAL
recipes_coll = mongo.db.recipes
users_coll = mongo.db.users


# ALL RECIPES
@app.route("/")
@app.route("/recipes")
def recipes():
    """
    READ
    Displays all recipes in the order they were
    created with the latest being shown first
    pagination limits the number of recipes displayed.
    """
    # code for pagination modified from irinatu17:
    # https://github.com/irinatu17/MyCookBook
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))
    # total of recipes in database
    number_of_all_rec = recipes_coll.count()
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)
    # recipes to display in order of latest created
    recipes = recipes_coll.find().sort('_id', pymongo.DESCENDING).skip(
        (current_page - 1)*limit_per_page).limit(limit_per_page)

    return render_template(
        "index.html",
        recipes=recipes,
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec)


# SORT
@app.route("/sort", methods=['GET', 'POST'])
def sort():
    """
    READ
    Displays all recipes in the order of the
    users preference.
    """
    # code for pagination modified from JDBennison:
    # https://github.com/JDBennison/playparkpubs/blob/master/app.py
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))
    # total of recipes in database
    number_of_all_rec = recipes_coll.count()
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)
    # recipes to display in order of latest created
    recipes = recipes_coll.find().skip(
        (current_page - 1)*limit_per_page).limit(limit_per_page)
    # sort recipes
    sort_by = request.form.get('sort_by')
    if sort_by == 'az':
        recipes = recipes_coll.find().sort('recipe_name', 1).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)
    elif sort_by == 'za':
        recipes = recipes_coll.find().sort('recipe_name', -1).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)
    elif sort_by == 'newest':
        recipes = recipes_coll.find().sort('_id', pymongo.DESCENDING).skip(
        (current_page - 1)*limit_per_page).limit(limit_per_page)
    else:
        recipes = recipes_coll.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*limit_per_page).limit(limit_per_page)

    return render_template(
        "index.html",
        recipes=recipes,
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec)


# ALL USERS
@app.route("/")
@app.route("/users")
def users():
    """
    READ
    Displays all users. This feature
    is only available to the admin.
    """
    # set active page to apply active-link to nav link
    active_page = 'users'
    # code for pagination modified from irinatu17:
    # https://github.com/irinatu17/MyCookBook
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))
    # total of users in database
    number_of_all_users = users_coll.count()
    pages = range(1, int(math.ceil(number_of_all_users / limit_per_page)) + 1)
    users = users_coll.find().sort('_id', pymongo.DESCENDING).skip(
        (current_page - 1)*limit_per_page).limit(limit_per_page)

    return render_template(
        "users.html",
        active_page=active_page,
        users=users,
        current_page=current_page,
        pages=pages,
        number_of_all_users=number_of_all_users)


# SEARCH
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    READ
    Searches recipes using the
    title and ingredients.
    """
    # code for pagination modified from irinatu17:
    # https://github.com/irinatu17/MyCookBook
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))

    query = request.args.get('query')

    #  Search results
    query = request.form.get("query")
    recipes = recipes_coll.find(
        {"$text": {"$search": query}}).sort('_id', pymongo.ASCENDING).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)
    number_of_all_rec = recipes.count()
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)

    return render_template(
        "search.html",
        recipes=recipes,
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec,
        query=query)


# COOKING
@app.route("/cooking")
def cooking():
    """
    READ
    Searches recipes with a category
    of cooking.
    """
    # set active page to apply active-link to nav link
    active_page = 'cooking'
    # code for pagination modified from irinatu17:
    # https://github.com/irinatu17/MyCookBook
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))
    # recipes to display in order of latest created
    recipes = recipes_coll.find(
            {"category_name": "cooking"}).sort('_id', pymongo.DESCENDING).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)
    # total of recipes in database
    number_of_all_rec = recipes.count()
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) +1)

    return render_template(
        "cooking.html",
        active_page=active_page,
        recipes=recipes,
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec)


# BAKING
@app.route("/baking")
def baking():
    """
    READ
    Searches recipes with a category
    of baking.
    """
    # set active page to apply active-link to nav link
    active_page = 'baking'
    # code for pagination modified from irinatu17:
    # https://github.com/irinatu17/MyCookBook
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))
    # recipes to display in order of latest created
    recipes = recipes_coll.find(
            {"category_name": "baking"}).sort('_id', pymongo.DESCENDING).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)
    # total of recipes in database
    number_of_all_rec = recipes.count()
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)

    return render_template(
        "baking.html",
        active_page=active_page,
        recipes=recipes,
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec)


# SNACKS
@app.route("/snacks")
def snacks():
    """
    READ
    Searches recipes with a category
    of snacks.
    """
    # set active page to apply active-link to nav link
    active_page = 'snacks'
    # code for pagination modified from irinatu17:
    # https://github.com/irinatu17/MyCookBook
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))
    # recipes to display in order of latest created
    recipes = recipes_coll.find(
            {"category_name": "snacks"}).sort('_id', pymongo.DESCENDING).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)
    # total of recipes in database
    number_of_all_rec = recipes.count()
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)

    return render_template(
        "snacks.html",
        active_page=active_page,
        recipes=recipes,
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec)


# PROFILE
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    READ
    Displays the username and recipes
    of the session user.
    """
    # set active page to apply active-link to nav link
    active_page = 'profile'
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        user_recipes = recipes_coll.find({"created_by": session["user"]})
        number_of_user_rec = user_recipes.count()
        limit_per_page = 6
        current_page = int(request.args.get('current_page', 1))
        pages = range(
            1, int(math.ceil(number_of_user_rec / limit_per_page)) + 1)
        recipes = user_recipes.sort('_id', pymongo.DESCENDING).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)

        return render_template(
            "profile.html",
            active_page=active_page,
            username=username,
            recipes=recipes,
            user_recipes=user_recipes,
            current_page=current_page,
            pages=pages)

    return redirect(url_for("login"))


# ADMIN VIEW PROFILE
@app.route("/admin_profile/<username_view>", methods=["GET", "POST"])
def admin_profile(username_view):
    """
    READ
    Displays the username and recipes
    of the user selected by the admin.
    """
    # set active page to apply active-link to nav link
    active_page = 'users'
    # grab the session user's username from db
    user = users_coll.find_one(
        {"username": username_view})
    username = users_coll.find_one(
        {"username": username_view})["username"]
    user_recipes = recipes_coll.find({"created_by": username_view})
    number_of_user_rec = user_recipes.count()
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))
    pages = range(1, int(math.ceil(number_of_user_rec / limit_per_page)) + 1)
    # recipes to display in order of latest created
    recipes = user_recipes.sort('_id', pymongo.DESCENDING).skip(
            (current_page - 1) * limit_per_page).limit(limit_per_page)
    return render_template(
        "admin_profile.html",
        active_page=active_page,
        user=user,
        recipes=recipes,
        username=username,
        number_of_user_rec=number_of_user_rec,
        user_recipes=user_recipes,
        current_page=current_page,
        pages=pages)


# INDIVIDUAL RECIPES
@app.route("/single_recipe/<recipe_id>")
def single_recipe(recipe_id):
    """
    READ
    Displays a single recipe.
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "single_recipe.html", recipe=recipe)


# REGISTRATION
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    READ
    Registers a user providing there
    is not already an existing user
    using the name provided. If successful
    the user is logged in and is directed
    to their page, if not they are prompted
    to try again.
    """
    # set active page to apply active-link to nav link
    active_page = 'register'
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
    return render_template(
        "register.html",
        active_page=active_page)


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    READ
    Logs in user provided they provide
    correct username and password, if not
    they are prompted to try again. If
    successful the user is directed to
    their profile.
    """
    # set active page to apply active-link to nav link
    active_page = 'login'
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

    return render_template(
        "login.html",
        active_page=active_page)


# LOGOUT
@app.route("/logout")
def logout():
    """
    READ
    Logs out user and redirects them
    to the login page.
    """
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# ADD RECIPE
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    READ
    Inserts new recipe to the database
    and redirects user to homepage with
    a message to say recipe has been added.
    """
    # set active page to apply active-link to nav link
    active_page = 'add'
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
        return redirect(url_for("recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "add_recipe.html",
        categories=categories,
        active_page=active_page)


# EDIT RECIPE
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    READ
    Edits a recipe and redirects user to
    the recipe with a message to say edit
    has been successful.
    """
    # set active page to apply active-link to nav link
    active_page = 'edit'
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
        "edit_recipe.html",
        recipe=recipe,
        categories=categories,
        active_page=active_page)


# DELETE RECIPE
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    READ
    Deletes a recipe and redirects user to
    the homepage with a message to say recipe
    has been deleted.
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("recipes"))


# DELETE USER
@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    """
    READ
    Deletes a user and redirects user to
    the users page with a message to say
    user has been deleted. Only available
    to admin.
    """
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("User Successfully Deleted")
    return redirect(url_for("users"))


# UNITS
@app.route("/units")
def units():
    """
    READ
    Allows users to convert units
    """
    # set active page to apply active-link to nav link
    active_page = 'units'
    return render_template(
        "units.html",
        active_page=active_page)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
