![Welcome](https://raw.githubusercontent.com/nikl881/portfolio/master/static/img/readme.jpg)

## Italian CookBook project


This is the readme file for the online CookBook milestone project of Code Institute.<br/>
The main purpose of this website is to show recipes in a so-called 'online cookbook'.<br/> 
The chosen design and (layout)style is a blog-like cookbook of specific dishes from the Italian kitchen.<br/>
This data-driven website is dynamic in nature, this means that the user of the website can add, update, edit and remove recipes in accordance with the CRUD principles.<br/>
The user also can filter recipes based on the following criterea: Dish type, Author, Cuisine Region, Likes, Allergens, Difficulty and Cooking time. 
The website is fitted for mobile, tablet and desktop (fully responsive). 


Niels de Klerk (April, 2019)


## UX perspective 


The documents of the preparation phase are included in a project location, which can be found at in the link below. 
This includes wireframes and mockups and basic images for the branddesign. 

Link to the external project documentation: https://drive.google.com/open?id=1-JhsaICva--uwgd_QD44ifeaJxX9_GPm



## Features

Existing Features (week 12 - 2019) 

* Landing page with a list of recently added recipes (clickable overview)
* About page with background information about the function of the website and a image
* Recipes page with information about the recipes, a filter function, a 'add your own recipe' function, a help function, and a overview of all recipes with image. 
* Detailpage of a recipe, including: Dynamicaly generated recipe name, description, cuisine region, allergens information, author, likes, ingredients, image and cooking instruction. And modify options: edit and delete recipe. 
* Edit page with the possibility to edit all functions mentioned in the previous feature description, including recipe image source. 
* Contact page with the possibily to write and send a text message. 

Features Left to Implement (in a random order listed below)

* Create a simple user login and move the 'edit / update' and 'delete' functions so that they are only available for a logged in user. (optional project requirement)

## Database schema and initial design

In order to make a good and deliberate start with this project, careful consideration was given first to the exact data flows that will become part of the (dynamic) content of the website.
I have decided to use a non-relational data structure (No SQL). 
This because it is quite straightforward to link recipes (as a main part / general data) to different subcategories (authors, geographic data, difference in dishes, etc.)
Based on the studied theory, I came to the conclusion that the combination of Flask, MongoDB and Heroku will work well.

Drafts and the defensive version of the database schema can be found in the following folder:
https://drive.google.com/open?id=1-JhsaICva--uwgd_QD44ifeaJxX9_GPm


## Technologies Used

In this section all of the languages, frameworks, libraries, and other tools that have been used are mentioned. 

*	HTML 5 <br/>
    The website uses HTML5 as a fundamental basis for building the website.

*	CSS3 <br/>
    The website uses CSS3 with regard to the styling of all elements within the website. For this a separate layout has been created within the page structure. 
    CSS is used for all content, including: images, layout of color and background, etc.

*	Bootstrap 3.7.6. <br/>
    The open-source Bootstrap framework has been used to implement some basic templates for forms, buttons and navigation. 
    Bootstrap has also been used to stand with a responsive design of the web page.

*	Cloud9 <br/>
    AWS (Amazon) Cloud9, a cloud-based integrated development environment (IDE) that has been used to write, run, and debug the code used for the website. 
 
*	GitHub <br/>
    GitHub has been used for version control of the code by using Git. 
    During the realization of the project, Git was daily used.

*	Core JavaScript<br/>
    Core Javascript has been used to use the event handling functionality's on specific buttons. 

*	Jquery libraries<br/>
    Jquery has been used for most interactive parts. 

*	Fontawesome<br/>
    Fontawesome as a toolkit has been used to the UX/UI, especialy for icon styling. 

*   Heroku <br/>
    In this project data is actually transported between frontend and backend, GitHub pages are no longer sufficient as a project deploy location on its own. 
    That is why Heroku has been used to facilitate this functions of the application.
    During the realization of the project, Git deployment was daily used.

*   Python / Flask <br/> 
    An important aspect of this project is the dynamic generation, modification and adaptation of data. 
    This is made possible by different routes between pages and data. The chosen framework to implement this is Flask.

*   MongoDB <br/>
    MongoDB is used to store the user input in a (non-relational) database. 
    In addition, the site is already filled with stored data that is retrieved from the mongoDB database.



## Testing

Various methods have been used to test the code of the website. During development, there has been continuously tested on the quality of the code. 
This has been done by checking the correct functionality of the code on different screensizes, different resolutions,
different devices (mobile, tablet, desktop). This approach is used from the start to the end of the realization of the project.


The code has been tested on the following devices and is fitted for purpose on a laptop, desktop or large desktop: 

    * Macbook 13" 
    * Windows 10 desktop 27" 
    * Windows 10 laptop 17" 
    * Iphone 10
    * Huawei mate 20 lite
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
    * Change recipe image with new URL.
    * Delete the recipe and return to recipe page. 

* Use of the contactpage - 
    * Send (feedback) message using the form. 


## Issuelist 

| Issue number    | Description     | Implemented Solution  |
| ------------- |:-------------:| -----:|
| 1	| Detailpage shows all recipes and not ID of one recipe | Changed app.py route based on proper ID fields return render_template("detailpage.html", recipe=recipe)    |
| 2	|  Menu items in main navigation are outside navbar |  Replaced the custom header into Bootstrap header and rebuild into desired style|
| 3	|   Width of page not neat on all views during testphase  | Created a container class with a max width of 700px on all elements |
| 4 | Recipe images did not load via Flask/Python   | Added url based datbasefields to routing paths  |
| 5 | New recipes only loaded on /recipes page not in overview on /index  | Added additional Flask routing with specific fields on needed places  |
| 6 | Database data is not shown on front-end   | Changed the @app.route with the correct paths. Issue was that the data was searched in the wrong db collection  |
| 7 | Option field in form gave duplicate data when refreshing page  | Changed Flask routing paths to single injection instead of multiinjection in option form fields  |
| 8 | Heroku could not load app from heroku page (git staging had no issues) | Changed Procfile to similair procfile on Heroku dashboard  |
| 9 | Filter route wont show result of selected filter options | Still an open issue (4-4-19)  |
| 10 | Security variable / PORT settings | Still an open issue (4-4-19)  |

## Work method 

During the development of this project Trello (Trello.com) is used as a simple project management tool to develop in a controlled project environment. I have used the 'trello-board' for all the 
actions within the project; initializing the project until the completion. The trello-board has been used for: preperation actions, building functionalities, testwork and debugging. 


## Deployment

The website is made in the AWS Cloud9 environment. To give a good idea of the development progress, short deliveries are always placed at the workspace on Heroku and GitHub. 
During the development period a upload was made to GitHub after every 3 to 4 hours of development work or after a relative bigger change to the code. The way the Git process is used is as follows:

1. Builded the site on a local environment.
2. Staged the files in the stage area.
3. Perform push to Heroku (workspace / remote app)
4. Perform push to Github (Git directory / repository).

*   The website is available at the following link: https://personal-blog-2019.herokuapp.com/

## Credits

This README file is based on the Code Institute template.

## Media

*  All media files, used for the design of the project are selfmade. 
*  The used recipe images/photo's are downloaded from the Shutterstock database (https://www.shutterstock.com), from Istockphoto (https://www.istockphoto.com/nl), and from Adobe Images (used Adobe Pro)

