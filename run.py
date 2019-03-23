import os
import json
from flask import Flask, render_template, request, flash, redirect, request, url_for, jsonify, json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask (__name__)
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

app.config["MONGO_DBNAME"] = 'myCookBook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
mongo = PyMongo(app)



### routing index page ###

@app.route('/') 
def index():
    return render_template("index.html", page_title="Home" )  

    
### routing for the about page ###    
    
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

### routing for the contact page ###         
        
    
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks, {}, I have recieved your message!".format(request.form["name"]))
    return render_template("contact.html", page_title="Contact")
    
    
### show recipe on detail page ###     
        
@app.route('/')
@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    return render_template("detailpage.html", recipe=mongo.db.myMDB.find())

@app.route('/detailpage')
def detailpage(recipe_id):
    
    recipe = mongo.db.myMDB.find()
    
    return render_template("detailpage.html", page_title="Detailpage", recipe=recipe)       
    
@app.route('/recepten/<recipe_id>')
def recepten(recipe_id):
    a_recipe =  mongo.db.MyMDB.find_one({"_id": ObjectId(recipe_id)})
    print(a_recipe)
    return render_template('detailpage.html', recipe=a_recipe)    
    
## show all recipes and filter categories ###    

@app.route('/recipes')
def recipes():
    
              return render_template("recipes.html", page_title="Recipes") 
              
@app.route('/recipesfollow')
def recipesfollow():
        return render_template("recipesfollow.html", page_title="Second recipe page")               
              
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.myMDB
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipe'))    
    
## add a new recipe ###

@app.route('/addrecipes')
def addrecipes():
        return render_template("addrecipes.html", page_title="Add recipes")
        
## run location ## 
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
    

    

