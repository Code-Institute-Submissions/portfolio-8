import pymongo

import os, requests
from pprint import pprint
import json
import bson

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "recipe_book"
COLLECTION_NAME = "recipes"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def get_record():
    print("")
    recipe_name = input("Enter recipe name > ")
    description = input("Enter recipe description > ")

    try:
        doc = coll.find_one({'recipe_name': recipe_name.lower(), 'description': description.lower()})
    except:
        print("Error accessing the database")
    
    if not doc:
        print("")
        print("Error! No results found.")
    
    return doc


def show_menu():    
    print("")
    print("1. Add a recipe")
    print("2. Find a recipe by name")
    print("3. Edit a recipe")
    print("4. Delete a recipe")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def add_record():
    print("")
    recipe_name = input("Enter recipe name > ")
    description = input("Enter recipe description > ")
    dish_type = input("Enter dish type > ")
    author_name = input("Enter author name > ")
    cuisine_region = input("cuisine region > ")
    difficulty = input("Enter difficulty > ")
    allergens = input("Enter allergens > ")

    new_doc = {'recipe_name': recipe_name.lower(), 'description': description.lower(), 'dish_type': dish_type,
               'author_name': author_name, 'cuisine_region': cuisine_region, 'difficulty':
               difficulty, 'allergens': allergens}
    
    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")

def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v
        
        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")


def delete_record():

    doc = get_record()

    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
        
        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")
        print("")

        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("Document deleted!")
            except:
                print("Document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")



 
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()

