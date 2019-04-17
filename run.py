"""import tools and packages"""
import os
import json
import pymongo
from flask import Flask
from flask import render_template, request, flash
from flask import redirect, request, url_for, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pprint import pprint

"""connections to db"""

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

app.config["MONGO_DBNAME"] = 'recipe_book'
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "monogodb://localhost")
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
mongo = PyMongo(app)


"""routing the index page"""


@app.route('/')
def index():
    return render_template("index.html", page_title="Home",
                           recipes=mongo.db.recipes.find().sort('_id'))

"""routing the about page"""


@app.route('/about')
def about():
    data = [1]
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)

"""show recipe on detailpage (single recipe page)"""


@app.route('/detailpage')
@app.route('/detailpage/<recipe_id>')
def detailpage(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template("detailpage.html", recipe=recipe)


@app.route('/')
@app.route('/get_recipes/<recipe_id>')
def get_recipes():
        return render_template("detailpage.html", page_title="detailpage",
                               recipes=mongo.db.recipes.find())

"""upvotes/likes"""


@app.route('/upvote/<recipe_id>')
def upvotes(recipe_id):
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'upvotes': 1}}
    )
    return redirect(url_for('detailpage', recipe_id=recipe_id))


"""show recipes and filter categories on recipes.html page"""


@app.route('/')
@app.route('/recipes')
def recipes():
    valid_args = [
        'dish_type',
        'author_name',
        'upvotes',
        'cuisine_region',
        'allergens',
        'difficulty',
        'cooking_time',
    ]

    filter = {}

    for arg in valid_args:
        filter[arg] = request.args.get(arg)

    print(filter)

    recipes = mongo.db.recipes.find(filter)

    return render_template("recipes.html", page_title="Recipes",
                           recipes=recipes)

"""Follow page (show all recipes)"""


@app.route('/recipesfollow')
def recipesfollow():

        return render_template("recipesfollow.html",
                               page_title="Second recipe page")

"""add a new recipe on addrecipes.html"""


@app.route('/addrecipes')
def addrecipes():
        return render_template("addrecipes.html", page_title="Add recipes")


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipes
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('recipes'))

"""edit recipe"""


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_recipes = mongo.db.recipes.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           recipes=all_recipes)

"""update recipe"""


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
                   {
        'recipe_name': request.form.get('recipe_name'),
        'description': request.form.get('description'),
        'author_name': request.form.get('author_name'),
        'cuisine_region': request.form.get('cuisine_region'),
        'difficulty': request.form.get('difficulty'),
        'allergens': request.form.get('allergens'),
        'ingredients': request.form.get('ingredients'),
        'cooking_time': request.form.get('cooking_time'),
        'dish_type': request.form.get('dish_type'),
        'recipe_image': request.form.get('recipe_image'),
        'cooking_instruction': request.form.get('cooking_instruction'),
        'upvotes': request.form.get('upvotes'),
        'views': request.form.get('views'),
    })
    return redirect(url_for('get_recipes'))

"""delete a recipe"""


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


"""routing for the contact page"""


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks, {}, I have recieved your message!"
              .format(request.form["name"]))
    return render_template("contact.html", page_title="Contact")

"""run location"""


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', "0.0.0.0."),
            port=int(os.environ.get("PORT", "5000")),
            debug=True)
