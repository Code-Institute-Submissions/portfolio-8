import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myCookBook"
COLLECTION_NAME = "myMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def get_record():
    print("")
    first = input("Enter recipe name > ")
    last = input("Enter recipe description > ")

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
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
    name = input("Enter recipe name > ")
    desc = input("Enter recipe description > ")
    dtype = input("Enter dish type > ")
    author = input("Enter author name > ")
    region = input("cuisine region > ")
    difficulty = input("Enter difficulty > ")
    allergens = input("Enter allergens > ")

    new_doc = {'first': name.lower(), 'last': desc.lower(), 'dob': dtype,
               'gender': author, 'hair_colour': region, 'occupation':
               difficulty, 'nationality': allergens}
    
    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()

