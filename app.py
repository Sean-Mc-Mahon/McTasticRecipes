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
prep_coll = mongo.db.prep
ingredients_coll = mongo.db.ingredients


# ALL RECIPES
@app.route("/")
@app.route("/recipes")
def recipes():
    """
    READ
    Displays all recipes in the order they were
    created with the latest being shown first.
    Pagination limits the number of recipes displayed.
    """
    # set title to display in browser tab
    title = 'Recipes'
    # code for pagination modified from irinatu17:
    # https://github.com/irinatu17/MyCookBook
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))
    # sort recipes by newest first
    recipes = recipes_coll.find().sort('_id', pymongo.DESCENDING).skip(
        (current_page - 1)*limit_per_page).limit(limit_per_page)
    # total of recipes in database
    number_of_all_rec = recipes.count()
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)

    return render_template(
        "index.html",
        title=title,
        recipes=recipes,
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec)


# SEARCH
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    READ
    Searches recipes using the
    title and ingredients.
    """
    # set title to display in browser tab
    title = 'Search'
    # code for pagination modified from irinatu17:
    # https://github.com/irinatu17/MyCookBook
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))

    if request.method == "POST":
        # used when a search is made
        query = request.form.get('query')
    else:
        # used when a pagination link is clicked following a search
        query = request.args.get('query')

    sort_by = "Sort By"
    #  Search results
    recipes = recipes_coll.find(
        {"$text": {"$search": str(
            query)}}).sort('_id', pymongo.DESCENDING).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)

    #  Number of Search results
    number_of_all_rec = recipes.count()
    print(number_of_all_rec)

    #  Number of Pages
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)

    return render_template(
        "index.html",
        title=title,
        recipes=recipes,
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec,
        query=query,
        sort_by=sort_by)


# SORT
@app.route("/sort", methods=["GET", "POST"])
def sort():
    """
    READ
    Sorts recipes by user preference
    """
    # set title to display in browser tab
    title = 'Recipes Sort'

    # pagination
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))

    if request.method == "POST":
        # used when a sort parameter is selected
        query = request.args.get('query')
        sort_by = request.form.get('sort_by')
    else:
        # used when a pagination link is clicked following a sort
        query = request.args.get('query')
        sort_by = request.args.get('sort_by')

    # sort recipes by user preference
    # selected preference is displayed in the sort label
    if sort_by == 'A-Z':
        recipes = mongo.db.recipes.find().sort('recipe_name', 1).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)
    elif sort_by == 'Z-A':
        recipes = mongo.db.recipes.find().sort('recipe_name', -1).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)
    elif sort_by == 'Oldest':
        recipes = mongo.db.recipes.find().sort('_id', pymongo.ASCENDING).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)
    else:
        recipes = mongo.db.recipes.find().sort('_id', pymongo.DESCENDING).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)

    # total of recipes
    number_of_all_rec = recipes.count()

    # number of pages
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)

    return render_template(
        "index.html",
        title=title,
        recipes=recipes,
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec,
        query=query,
        sort_by=sort_by)


# SORT QUERY
@app.route("/sort_query", methods=["GET", "POST"])
def sort_query():
    """
    READ
    Sorts ingredients by user preference.
    Used following a search
    """
    # set title to display in browser tab
    title = 'Recipes Search Sort'

    # pagination
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))

    if request.method == "POST":
        # used when a sort parameter is selected following a search
        query = request.args.get('query')
        sort_by = request.form.get('sort_by')
    else:
        # used when a pagination link is clicked
        query = request.args.get('query')
        sort_by = request.args.get('sort_by')

    # sort recipes by user preference
    if sort_by == 'A-Z':
        recipes = recipes_coll.find(
            {"$text": {"$search": str(
                query)}}).sort('recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
    elif sort_by == 'Z-A':
        recipes = recipes_coll.find(
            {"$text": {"$search": str(
                query)}}).sort('recipe_name', -1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
    elif sort_by == 'Oldest':
        recipes = recipes_coll.find(
            {"$text": {"$search": str(
                query)}}).sort('_id', pymongo.ASCENDING).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
    else:
        recipes = recipes_coll.find(
            {"$text": {"$search": str(
                query)}}).sort('_id', pymongo.DESCENDING).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)

    # total of recipes
    number_of_all_rec = recipes.count()
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)

    return render_template(
        "index.html",
        title=title,
        recipes=recipes,
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec,
        query=query,
        sort_by=sort_by)


# SORT FILTER
@app.route("/sort_filter", methods=["GET", "POST"])
def sort_filter():
    """
    READ
    Sorts filter by user preference.
    Used following a filter
    """
    # set title to display in browser tab
    title = 'Recipes Sort Filter'

    # pagination
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))

    if request.method == "POST":
        # used when a sort parameter is selected following a search
        sort_by = request.form.get('sort_by')
        filter_by = request.args.get('filter_by')
    else:
        # used when a pagination link is clicked
        sort_by = request.args.get('sort_by')
        filter_by = request.args.get('filter_by')

    # sort recipes by user preference and chosen filter
    if sort_by == 'A-Z':
        if filter_by == "Cooking":
            recipes = recipes_coll.find(
                {"category_name": "cooking"}).sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Baking":
            recipes = recipes_coll.find(
                {"category_name": "baking"}).sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Snacks":
            recipes = recipes_coll.find(
                {"category_name": "snacks"}).sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        else:
            recipes = recipes_coll.find().sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
    elif sort_by == 'Z-A':
        if filter_by == "Cooking":
            recipes = recipes_coll.find(
                {"category_name": "cooking"}).sort(
                    'recipe_name', -1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Baking":
            recipes = recipes_coll.find(
                {"category_name": "baking"}).sort(
                    'recipe_name', -1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Snacks":
            recipes = recipes_coll.find(
                {"category_name": "snacks"}).sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        else:
            recipes = recipes_coll.find().sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
    elif sort_by == 'Oldest':
        if filter_by == "Cooking":
            recipes = recipes_coll.find(
                {"category_name": "cooking"}).sort(
                    '_id', pymongo.ASCENDING).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Baking":
            recipes = recipes_coll.find(
                {"category_name": "baking"}).sort(
                    '_id', pymongo.ASCENDING).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Snacks":
            recipes = recipes_coll.find(
                {"category_name": "snacks"}).sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        else:
            recipes = recipes_coll.find().sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
    else:
        if filter_by == "Cooking":
            recipes = recipes_coll.find(
                {"category_name": "cooking"}).sort(
                    '_id', pymongo.DESCENDING).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Baking":
            recipes = recipes_coll.find(
                {"category_name": "baking"}).sort(
                    '_id', pymongo.DESCENDING).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Snacks":
            recipes = recipes_coll.find(
                {"category_name": "snacks"}).sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        else:
            recipes = recipes_coll.find().sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)

    # total of recipes
    number_of_all_rec = recipes.count()
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)

    return render_template(
        "index.html",
        title=title,
        recipes=recipes,
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec,
        sort_by=sort_by,
        filter_by=filter_by)


# FILTER
@app.route("/filter", methods=["GET", "POST"])
def filter():
    """
    READ
    filter recipes by user preference
    """
    # set title to display in browser tab
    title = 'Recipes Filter'

    # pagination
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))

    if request.method == "POST":
        # used when a filter parameter is selected
        query = request.args.get('query')
        filter_by = request.form.get('filter_by')
    else:
        # used when a pagination link is clicked
        query = request.args.get('query')
        filter_by = request.args.get('filter_by')

    # filter recipes by user preference
    # selected preference is displayed in the sort label
    if filter_by == 'Baking':
        recipes = recipes_coll.find(
            {"category_name": "baking"}).sort('_id', pymongo.DESCENDING).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)
    elif filter_by == 'Snacks':
        recipes = recipes_coll.find(
            {"category_name": "snacks"}).sort('_id', pymongo.DESCENDING).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)
    elif filter_by == 'Cooking':
        recipes = recipes_coll.find(
            {"category_name": "cooking"}).sort('_id', pymongo.DESCENDING).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)
    else:
        recipes = recipes_coll.find().sort('_id', pymongo.DESCENDING).skip(
            (current_page - 1)*limit_per_page).limit(limit_per_page)

    # total of recipes
    number_of_all_rec = recipes.count()

    # number of pages
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)

    return render_template(
        "index.html",
        title=title,
        recipes=recipes,
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec,
        query=query,
        filter_by=filter_by)


# FILTER SORT
@app.route("/filter_sort", methods=["GET", "POST"])
def filter_sort():
    """
    READ
    Filters ingredients by user preference.
    Used following a sort
    """
    # set title to display in browser tab
    title = 'Recipes Filter Sort'

    # pagination
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))

    if request.method == "POST":
        # used when a sort parameter is selected following a search
        sort_by = request.args.get('sort_by')
        filter_by = request.form.get('filter_by')
    else:
        # used when a pagination link is clicked
        sort_by = request.args.get('sort_by')
        filter_by = request.args.get('filter_by')

    # sort recipes by user preference
    if sort_by == 'A-Z':
        if filter_by == "Cooking":
            recipes = recipes_coll.find(
                {"category_name": "cooking"}).sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Baking":
            recipes = recipes_coll.find(
                {"category_name": "baking"}).sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Snacks":
            recipes = recipes_coll.find(
                {"category_name": "snacks"}).sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        else:
            recipes = recipes_coll.find().sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
    elif sort_by == 'Z-A':
        if filter_by == "Cooking":
            recipes = recipes_coll.find(
                {"category_name": "cooking"}).sort(
                    'recipe_name', -1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Baking":
            recipes = recipes_coll.find(
                {"category_name": "baking"}).sort(
                    'recipe_name', -1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Snacks":
            recipes = recipes_coll.find(
                {"category_name": "snacks"}).sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        else:
            recipes = recipes_coll.find().sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
    elif sort_by == 'Oldest':
        if filter_by == "Cooking":
            recipes = recipes_coll.find(
                {"category_name": "cooking"}).sort(
                    '_id', pymongo.ASCENDING).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Baking":
            recipes = recipes_coll.find(
                {"category_name": "baking"}).sort(
                    '_id', pymongo.ASCENDING).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Snacks":
            recipes = recipes_coll.find(
                {"category_name": "snacks"}).sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        else:
            recipes = recipes_coll.find().sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
    else:
        if filter_by == "Cooking":
            recipes = recipes_coll.find(
                {"category_name": "cooking"}).sort(
                    '_id', pymongo.DESCENDING).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Baking":
            recipes = recipes_coll.find(
                {"category_name": "baking"}).sort(
                    '_id', pymongo.DESCENDING).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        elif filter_by == "Snacks":
            recipes = recipes_coll.find(
                {"category_name": "snacks"}).sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)
        else:
            recipes = recipes_coll.find().sort(
                    'recipe_name', 1).skip(
                (current_page - 1)*limit_per_page).limit(limit_per_page)

    # total of recipes
    number_of_all_rec = recipes.count()
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)

    return render_template(
        "index.html",
        title=title,
        recipes=recipes,
        current_page=current_page,
        pages=pages,
        number_of_all_rec=number_of_all_rec,
        filter_by=filter_by,
        sort_by=sort_by)


# ALL USERS
@app.route("/")
@app.route("/users")
def users():
    """
    READ
    Displays all users. This feature
    is only available to the admin.
    Pagination limits the number of recipes displayed.
    """
    # set title to display in browser tab
    # and apply active-link to nav link
    title = 'Users'

    # pagination
    limit_per_page = 6
    current_page = int(request.args.get('current_page', 1))
    # total of users in database
    number_of_all_users = users_coll.count()
    #  Number of Pages
    pages = range(1, int(math.ceil(number_of_all_users / limit_per_page)) + 1)
    # sort users by alphabetical order
    users = users_coll.find().sort('username', 1).skip(
        (current_page - 1)*limit_per_page).limit(limit_per_page)

    return render_template(
        "users.html",
        title=title,
        users=users,
        current_page=current_page,
        pages=pages,
        number_of_all_users=number_of_all_users)


# VIEW PROFILE
@app.route("/view_profile/<username_view>", methods=["GET", "POST"])
def view_profile(username_view):
    """
    READ
    Allows users to view other users profiles
    """
    if request.method == "POST":
        ingredient_name = request.args.get('ingredient_name')
        mongo.db.ingredients.remove({"ingredient_name": ingredient_name})
        flash("Ingredient Successfully Deleted")
        print(ingredient_name)

    # grab the user's username from db
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
    ingredients = mongo.db.ingredients.find(
        {"created_by": username_view}).sort("ingredient_name", 1)
    num_ingredients = ingredients.count()

    # Foodgroups and units to edit ingredients
    food_groups = mongo.db.food_groups.find().sort("group_name", 1)
    units = mongo.db.units.find().sort("unit_name", 1)

    # set title to display in browser tab
    # and apply active-link to nav link if profile belongs to session user
    title = username_view.capitalize()

    return render_template(
        "view_profile.html",
        title=title,
        user=user,
        recipes=recipes,
        ingredients=ingredients,
        num_ingredients=num_ingredients,
        food_groups=food_groups,
        units=units,
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
    # set title to display in browser tab
    title = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})['recipe_name']

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    username = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})['created_by']
    return render_template(
        "single_recipe.html",
        title=title,
        username=username,
        recipe=recipe)


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
    # set title to display in browser tab
    # and apply active-link to nav link
    title = 'Registration'
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
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("view_profile", username_view=session["user"]))
    return render_template(
        "register.html",
        title=title,)


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
    # set title to display in browser tab
    # and apply active-link to nav link
    title = 'Login'
    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(
                    url_for("view_profile", username_view=session["user"]))
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
        title=title,)


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
    return redirect(url_for(
        "login"))


# INSERT RECIPE
@app.route("/insert_recipe", methods=["GET", "POST"])
def insert_recipe():
    """
    READ
    Inserts new recipe to the database
    and redirects user to homepage with
    a message to say recipe has been added.
    """
    # set title to display in browser tab
    # and apply active-link to nav link
    title = 'Add Recipe'
    if request.method == "POST":
        recipe_is_vegetarian = "on" if request.form.get(
            "recipe_is_vegetarian") else "off"
        recipe_is_vegan = "on" if request.form.get(
            "recipe_is_vegan") else "off"

        # url validation code modified from paulloy:
        # https://github.com/paulloy/whiskey_herald_msp3/blob/master/app.py
        # image addresses must end with one of these extensions
        allow_exten = ["jpg", "jpeg", "png"]
        form_url = str(request.form.get("recipe_image"))
        # split the inputted url and check the extension
        x = form_url.split(".")
        y = x[-1].lower()

        #  url submitted if it ends with an acceptable suffix
        if y == allow_exten[0] or y == allow_exten[1] or y == allow_exten[2]:
            recipe_image = request.form.get("recipe_image")
        # if not a blank string is submitted
        else:
            recipe_image = ""

        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "recipe_image": recipe_image,
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

        return redirect(url_for(
            "recipes",
            title=title,))

    categories = mongo.db.categories.find().sort("category_name", 1)
    ingredients = mongo.db.ingredients.find(
        {"created_by": session["user"]}).sort("ingredient_name", 1)
    num_ingredients = ingredients.count()
    prep = mongo.db.prep.find().sort("prep", 1)
    return render_template(
        "insert_recipe.html",
        categories=categories,
        ingredients=ingredients,
        num_ingredients=num_ingredients,
        title=title,
        prep=prep)


# INSERT INGREDIENT
@app.route("/insert_ingredient", methods=["GET", "POST"])
def insert_ingredient():
    """
    READ
    Inserts new ingredient to the database.
    """
    # set title to display in browser tab
    # and set active page to apply active-link to nav link
    title = 'Units'
    if request.method == "POST":
        food_groups = mongo.db.food_groups.find().sort("group_name", 1)
        units = mongo.db.units.find().sort("unit_name", 1)
        # check if ingredient already exists in db
        existing_ingredient = mongo.db.ingredients.find_one(
            {"ingredient_name": request.form.get("ingredient_name")})
        # If ingredient already exists then only Creator may edit it
        if existing_ingredient:
            if existing_ingredient["created_by"] == session['user']:
                mongo.db.ingredients.remove(existing_ingredient)
            else:
                flash("Ingredient already exists")
                return redirect(url_for("units"))

        ingredient = {
            "ingredient_name": request.form.get("ingredient_name"),
            "ingredient_cal": request.form.get("ingredient_cal"),
            "group_name": request.form.get("group_name"),
            "unit_name": request.form.get("unit_name"),
            "created_by": session["user"]
        }

        mongo.db.ingredients.insert_one(ingredient)
        flash("Ingredient Successfully Added")

        username = session['user']

        return redirect(url_for(
            "view_profile",
            username_view=username,
            title=title))


# EDIT RECIPE
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    READ
    Edits a recipe and redirects user to
    the recipe with a message to say edit
    has been successful.
    """
    # set title to display in browser tab
    title = 'Edit Recipe'

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
        username = session['user']
        return redirect(url_for("view_profile", username_view=username))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    user_image = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})["recipe_image"]
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html",
        title=title,
        recipe=recipe,
        user_image=user_image,
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

    username = session['user']
    if username == 'admin':
        return redirect(url_for("recipes"))
    return redirect(url_for(
        "view_profile",
        username_view=username))


# DELETE INGREDIENT
@app.route("/delete_ingredient/<ingredient_id>")
def delete_ingredient(ingredient_id):
    """
    READ
    Deletes an ingredient and redirects user to
    the units page with a message to say recipe
    has been deleted. Only for admin use.
    """
    mongo.db.ingredients.remove({"_id": ObjectId(ingredient_id)})
    flash("Ingredient Successfully Deleted")

    username = session['user']
    if username == 'admin':
        return redirect(url_for("recipes"))
    return redirect(url_for(
        "view_profile",
        username_view=username))


# DELETE USER
@app.route("/delete_user/<username>")
def delete_user(username):
    """
    READ
    Deletes a user and redirects user to
    the users page with a message to say
    user has been deleted. Only available
    to admin.
    """
    mongo.db.users.remove({"username": username})
    mongo.db.recipes.remove({"created_by": username})
    mongo.db.ingredients.remove({"created_by": username})
    flash("Profile Successfully Deleted")
    if session["user"] == 'admin':
        return redirect(url_for("users"))
    else:
        session.pop("user")
        return redirect(url_for("recipes"))


# UNITS
@app.route("/units")
def units():
    """
    READ
    Allows users to convert units
    """
    # set title to display in browser tab
    # and apply active-link to nav link
    title = 'Units'
    dairy_ingredients = ingredients_coll.find(
        {"group_name": "Dairy"}).sort("ingredient_name", 1)
    fruit_ingredients = mongo.db.ingredients.find(
        {"group_name": "Fruit"}).sort("ingredient_name", 1)
    grain_ingredients = mongo.db.ingredients.find(
        {"group_name": "Grains"}).sort("ingredient_name", 1)
    protein_ingredients = mongo.db.ingredients.find(
        {"group_name": "Protein"}).sort("ingredient_name", 1)
    spice_ingredients = mongo.db.ingredients.find(
        {"group_name": "Oils & Spices"}).sort("ingredient_name", 1)
    sweet_ingredients = mongo.db.ingredients.find(
        {"group_name": "Sweet"}).sort("ingredient_name", 1)
    veg_ingredients = mongo.db.ingredients.find(
        {"group_name": "Veg"}).sort("ingredient_name", 1)
    food_groups = mongo.db.food_groups.find().sort("group_name", 1)
    units = mongo.db.units.find().sort("unit_name", 1)
    return render_template(
        "units.html",
        title=title,
        food_groups=food_groups,
        units=units,
        dairy_ingredients=dairy_ingredients,
        fruit_ingredients=fruit_ingredients,
        grain_ingredients=grain_ingredients,
        spice_ingredients=spice_ingredients,
        sweet_ingredients=sweet_ingredients,
        veg_ingredients=veg_ingredients,
        protein_ingredients=protein_ingredients)


# 404 ERROR
@app.errorhandler(404)
def error_404(error):
    '''
    READ
    Handles 404 error (page not found)
    '''
    return render_template('error/404.html', error=True,
                           title="Page not found"), 404


# 500 ERROR
@app.errorhandler(500)
def error_500(error):
    '''
    READ
    Handles 500 error (internal server error)
    '''
    return render_template('error/500.html', error=True,
                           title="Internal Server Error"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
