![Welcome](https://raw.githubusercontent.com/nikl881/california-roadtrip/master/assets/css/images/img_readme.jpg)

## Italian CookBook project


This is the readme file for the online CookBook milestone project. 
The main purpose of this is a website is to provide a recipes database from the Italian kitchen, displayed in a custom UI.  
In addition, the user of the website can also add, update, edit and remove recipes in accordance with the CRUD principles.
The user also can filter recipes based on the following criterea: Dish type, Author, Cuisine Region, Likes, Allergens, Difficulty and Cooking time. 
The website is fitted for mobile, tablet and desktop (fully responsive). 


Niels de Klerk (March, 2019)


## UX perspective 


This project had a preparation phase. Various topics were dealt with in this phase. 
The documents are included in a project location, which can be found at in the link below. 
This includes wireframes and mockups and basic images for the branddesign. 

Link to the external project documentation: https://drive.google.com/open?id=1-JhsaICva--uwgd_QD44ifeaJxX9_GPm


## Features

Existing Features (week 7 - 2019) 

* Landing page with a list of recently added recipes (clickable overview)
* About page with background information about the function of the website and a image
* Recipes page with some information about the recipes, a filter function, a 'add your own recipe' function, a help function, and a overview of all recipes with image. 
* Detailpage of a recipe, including: Dynamicaly generated recipe name, description, cuisine region, allergens information, author, likes, ingredients, image and cooking instruction. And modify options: edit and delete recipe. 
* Edit page with the possibility to edit all functions mentioned in the previous feature description.
* Contact page with the possibily to write and send a text message. 

Features Left to Implement (in a random order listed below)

* Create a simple user login and move the 'edit / update' and 'delete' functions so that they are only available for a logged in user. ; 


## Technologies Used

In this section all of the languages, frameworks, libraries, and other tools that have been used are mentioned. 

*	HTML 5: 
    *The website uses HTML5 as a fundamental basis for building the website.

*	CSS3: 
    *The website uses CSS3 with regard to the styling of all elements within the website. For this a separate layout has been created within the page structure. 
    *CSS is used for all content, including: images, layout of color and background, etc.

*	Bootstrap 3.7.6.: 
    * The open-source Bootstrap framework has been used to implement some basic templates for forms, buttons and navigation. 
    *   Bootstrap has also been used to stand with a responsive design of the web page.

*	Cloud9:
    *AWS (Amazon) Cloud9, a cloud-based integrated development environment (IDE) that has been used to write, run, and debug the code used for the website. 

*	GitHub: 
    *GitHub has been used for version control of the code by using Git. 
    *During the realization of the project, Git was daily used.

*	Core JavaScript: 
    *Core Javascript has been used to use the event handling functionality's on specific buttons. 

*	Jquery libraries: 
    *Jquery has been used for most interactive parts of the SPI. JQuery has been used to render the maps with specific routes and selections on specific buttons. 

*	Fontawesome: 
    *Fontawesome as a toolkit has been used to the UX/UI so the SPI has is own brand identity. 

*   Heroku:
*   *In this project data is actually transported between frontend and backend, GitHub pages are no longer sufficient as a project deploy location on its own. 
    That is why Heroku has been used to facilitate this functions of the application.
    *During the realization of the project, Git deployment was daily used.

*   Python / Flask:
    An important aspect of this project is the dynamic generation, modification and adaptation of data. 
    This is made possible by different routes between pages and data. The chosen framework to implement this is Flask.

*   MongoDB
    MongoDB is used to store the user input in a (non-relational) database. 
    In addition, the site is already filled with stored data that is retrieved from the mongoDB database.



## Testing

Various methods have been used to test the code of the website. During development, there has been continuously tested on the quality of the code. 
This has been done by checking the correct functionality of the code on different screensizes, different resolutions,
different devices (mobile, tablet, desktop). This approach is used from the start to the end of the realization of the project.


The SPI has been tested on the following devices and is fitted for purpose on a laptop, desktop or large desktop: 

    * Macbook 13" 
    * Windows 10 desktop 27" 
    * Windows 10 laptop 17" 
    * Iphone 10
    * Huawei mate 20
    * Huawei P30 pro
    
Site viewed and tested in the following browsers:

    * Firefox
    * Chrome
    * Internet Explorer    
    
Mockups and sketches were also used to continuously build and deliver in accordance to the initial plan and design of the website.
In the final phase of the project, the opinion of a number of people was asked. We used professinoals and non professionals to see iff the site functions properly from a certain perspective. 
In order to be able to check whether the code functions as it was conceived during the design phase, we tested the functions on a basis of different scenarios.
Below the main features described that are basic functions as currently available on the site.

* Main navigation and information - 
    * Open recipes in the 'recently added' list. 
    * Navigate back to index.html using the main navigation function (menu).
    * Try to navigate on different devices with different screenresolutions within the main navigation. 
    * Use specific navigation buttons, i.e. 'recipes' or 'quickview'. 
  
* Use of the recipes page - 
    * Select a recipe based on filter criterea (i.e. region, author, allergens). 
    * Open recipe to navigate to detailpage of a specific recipe.
    * Use the add recipe button. 
 
* Use of the detailpage - 
    * Give a like/upvote to the recipe.
    * Edit recipe, i.e. ingredients, author, allergens, cooking instruction. 
    * Delete the recipe and return to recipe page. 

* Use of the contactpage - 
    * Send (feedback) message using the form. 


## Autmated unit testing using Jasmine

In order to guarantee the proper functioning of the software, automatic testing has been been added into this project. 
This paragraph contains a short explanation of the test setup, test code and explain the idea behind the testing of this code.

The following test setup has been used
The 'Test Runner' will execute the tetst in order to summarize the results. 
The 'Assertion Libary' is used to define testing logic and conditions and to verify the quality of the testscript.
 
The Jasmine testpage, with automatic unit testresults, are available at: https://nikl881.github.io/california-roadtrip/test.html 


## Issuelist 

| Issue number    | Description     | Implemented Solution  |
| ------------- |:-------------:| -----:|
| 1	| Detailpage shows all recipes and not ID of one recipe | Changed app.py route based on proper ID fields "({'_id': ObjectId(recipe_id)})" 
    return render_template("detailpage.html", recipe=recipe)    |
| 2	|  Descriptio 2 |  Solution 2 |
| 3	| Favicon won't load      | Added correct references to the link  |
| 4 | W3C error about deprecated form styling   | Debugging form styling  |


## Work method 

During the development of this project Trello (Trello.com) is used as a simple project management tool to develop in a controlled project environment. I have used the 'trello-board' for all the 
actions within the project; initializing the project until the completion. The trello-board has been used for: preperation actions, building functionalities, testwork and debugging. 


## Deployment

The website is made in the AWS Cloud9 environment. To give a good idea of the development progress, short deliveries are always placed at the workspace on Heroku and GitHub. 
During the development period a upload was made to GitHub after every 3 to 4 hours of development work.

It has happened a few times that i faced some debugging actions that also changed good working code. Thanks to a restoration via GitHub, i was able to continue working on improving the project quickly. 
The way the Git process is used is as follows:

1. Builded the site on a local environment.
2. Staged the files in the stage area.
3. Perform push to Github to renew the working environment. (Git directory / repository).

*   The website is available at the following link: https://nikl881.github.io/california-roadtrip/
*   After implementing the remaining features listed above the site will be live at: www.nortstack.com/portfolio/california_roadtrip/index.html. 


## Credits

This README file is based on the Code Institute template.

## Media

*  All media files, used for the design of the project are selfmade. 
*  The used demo photo's are downloaded from the Shutterstock database (https://www.shutterstock.com) 

## Acknowledgements


