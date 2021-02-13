# McTastic Recipes

### [Live Site](https://mctastic-recipes.herokuapp.com/)

### [GitHub](https://github.com/Sean-Mc-Mahon/McTasticRecipes)

![Various Devices](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/resposiveness.JPG)

McTastic Recipes is a Milestone 3 project, it is part of the Fullstack Software Development Course of [Code Institute](https://codeinstitute.net/).

# Table of Contents

**<details><summary>Project overview</summary>**
* [**_Project overview_**](#project-overview)
* [**_User Stories_**](#user-stories)
* [**_Admin Stories_**](#admin-stories)
</details>

**<details><summary>UX</summary>**
* [**_Strategy Plane_**](#strategy-plane)
* [**_Scope Plane_**](#scope-plane)
* [**_Structure Plane_**](#structure-plane)
* [**_Skeleton Plane_**](#skeleton-plane)
* [**_Surface Plane_**](#surface-plane)
    * [_Color Scheme_](#color-scheme)
    * [_Typography_](#typography)
    * [_Media_](#Media)
    * [_Wireframes_](#wireframes)
</details>

**<details><summary>Features</summary>**
* [**_Existing Features_**](#existing-features)
* [**_Features Left to Implement_**](#features-left-to-implement)
</details>

**<details><summary>Technologies Used</summary>**
* [**_Libraries_**](#libraries)
* [**_Version Control_**](#version-control)
</details>

**<details><summary>Accessibility</summary>**
* [**_Semantics_**](#semantics)
</details>

**<details><summary>Testing</summary>**
* [**_Testing_**](#testing)
</details>

**<details><summary>Deployment</summary>**
* [**Deployment**](#deployment)
</details>

**<details><summary>Credits</summary>**
* [**_Content_**](#content)
* [**_Acknowledgements_**](#acknowledgements)
</details>

---

# Project Overview

McTastic Recipes is a recipe website. It is designed to be useful for people with different levels of abilities in the kitchen, from complete novice to experienced cook. <br> 
It is also designed to be easy to navigate for users of all ages. Users may add not just recipes but also ingredients so that when they add recipes in the future the may easily view the calory values of their favourite recipes.

---

### User Stories

- User Story A: As a casual user I would to easily browse recipes.
- User Story B: As a user I would like to create a profile and delete it if I no longer want it.
- User Story C: As a registered user I would like to add, edit, update or delete my own recipes.
- User Story D: As a registered user I would like to view what recipes other users have created.
- User Story E: I would like to be able to view the recipes clearly regardless of the type of device I use.
- User Story F: I would like to be able to easily share recipes.
- User Story G: I would to be able to convert units from metric to imperial and vice versa.
- User Story H: As a registered user I would like to add, edit, update or delete my own ingredients.

### Admin Stories

- Admin Story A: As the admin I would like to be able to delete any user along with all recipes created by that user.

---

## Opportunities arising from user stories

<div align="center">
 
|Opportunities | Importance | Viability / Feasibility
|-----|:------:|:-----:|
|**Simple Clean UI** | 5 | 5 |
|**Clearly indicate purpose** | 5 | 5 |
|**Clear Simple Instructions** | 5 | 5 |
|**Simple creation of recipes/ingredients** | 5 | 5 |
|**Simple edit of recipes/ingredients** | 5 | 5 |
|**Search/filter/sort Feature** | 5 | 5 |
|**Share Feature** | 3 | 5 |
|**Unit Conversion** | 3 | 5 |

</div>

---

## UX Planes

### Strategy Plane

- Business Goals: The purpose of McTastic Recipes is to provide a platform for users to be able to casually view recipes or register to add and edit their own recipes. Users may store their own recipes so that they essentially have their own online personal cookbook while also being able to view other peoples recipes. 


- Audience: The audience of the site is broad and it cannot be assumed that even the registered users of the site will be technically savvy, it is therefore necessary to make the site easily navigable not just for casual users but also the registered users.

- Content: The content is determined by the users and presented in a uniform and clear manner.

#### Personal Goals

- To learn and practice frontend and backend programming together for the first time. To combine the use of HTML, CSS, Materialize and JavaScript with Python, MongoDB, Flask and Jinja.

### Scope Plane

- What is needed is a site which integrates input from users in a way which is clean, simple and easily navigable. Users must be able to upload photographs as well as provide information such as ingredients, instructions prep time etc...

- The data on each recipe must be presented in a visually compelling way to encourage interaction with the site with the ultimate goal of casual users deciding to register and add their own recipes.

- Recipes may be filtered into categories of cooking baking and snacks, as well as being sorted by alphabetical order or order of creation.

- User profiles allow users to store their recipes and ingredients in a convenient location.

- In the future a blog or video instructions for recipes may be integrated.


### Structure Plane

- The site uses a consistent structure, a navbar is at the top of the page which allow a user to navigate the site and login if needed. A burger menu is used for small devices.
- The index page has a search bar, filter and sort feature. If a user performs a search they will be able to sort the search results. 
- The content is consistant with text kept to a minimum. Majority of imagery and text is determined by users.
- A footer at the bottom provides copyright information and links to social media pages and a key guide of icon meanings to aid users on mobile devices who do not have the benefit of tooltips. 
- The number of clicks needed to reach any page is kept to a minimum. Sections such as user profiles will not be visible to users who are not logged in.
- Buttons/modals/links are consistant in design.

### Skeleton Plane
#### Wireframes

I used Balsamiq and figma to create the wireframes. The layout has altered since I created the wireframes as I decided to replace the contact page with a newsletter sign up in the footer. The parallax felt too distracting and so that has been omitted. Originally there were to be seperate pages for Cooking/Baking/snacks but instead I implemented a feature to filter recipes by category.
I used affinity designer to design the logo, I went through many iterations of the design until I was happy with two final logos, one for the navigation bar on the site and the other for the browser tab icon.

### Surface Plane

- The number is fonts is kept at a minimum as well as using a limited and consistant color scheme.

#### Design

A standard layout is fully responsive on mobile devices and larger screens.

#### Color Scheme

Colors are kept to a minimum in order to keep focus on the imagery of the recipes, chosen colousr are various shades of grey. Color scheme can be found on my Coolors profile: [Coolors](https://coolors.co/u/sean_mcmahon)

![Color Palette](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/mctastic-colors.JPG)

#### Typography

2 [Google Fonts](https://fonts.google.com/) were used across the site:

- [Pattaya](https://fonts.google.com/specimen/Pattaya?query=patt) : Logo & Headings, used for it's flowing relaxed style.
- [Montserrat](https://fonts.google.com/specimen/Montserrat?query=montse) : Body, used for it's excellent readability.

#### Media

All images, and recipes are the authors own unless provided by other users. Logos are also produced by the author using Affinity Design.

- [Balsamiq Wireframe](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/mctastic-wire.pdf)

- [Affinity Designer Logo Process](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/logo-design.jpg)

##### back to [top](#table-of-contents)

---

# Features

## Existing Features

### Elements on every page
#### Navbar
- The navigation bar features a logo and name in the top left corner, both are links to the home page. Navigation links are in the top right. An animation slides the logo, name and navigation links into view on loading but only on the home page in order that it not be too distracting while navigationg the site.

- For visitors to the site who are not logged in, list items links are available for them to use.
    1. Login
    2. Register
    3. Units

- For users who are logged in, the list items are as follows: 
    1. Logout
    2. Add Recipes
    3. Profile
    4. Users
    5. Units

- Python determines if the user is logged in or not by checking `if 'user' in session` and passes this data to Jinja to display the correct navbar for the user.

- On the smaller resolutions (tablet, mobile) the navbar is collapsed into a burger icon. A slide out menu opens when the burger icon is clicked.

#### Footer

The footer features:
    - Newsletter signup: Users may submit an email to request a newsletter.
    - Key Information
    - Copyright Information
    - Links to social media platforms.

#### Share

The share button is displayed on the bottom right corner at all times on all pages that do not require a user to be logged in.

### Elements on Multiple Pages

#### Search Sort Filter 
(index, search, single_recipe)

- The index page has a search bar, filter and sort feature. The search feature searches for keywords in recipe titles and ingredients. If a user performs a search they will be able to sort the search results.
- The sort feature allows users to sort the results by A-Z, Z-A, latest created and oldest created.
- The filter allows users to display recipes under the categories of cooking, baking, snacks or all.

#### Recipe Cards 
(index, view_profile)

- Cards are displayed for each recipe. On small devices the cards may be expnded to reveal more information (one card per row on small devices, two cards per row on medium devices). <br>
- On large devices users can hover over cards to reveal more information (3 cards per row). <br>

#### Ingredient Cards 
(units, add_recipe)

- Cards are displayed for each ingredient. On small devices the cards may be expnded to reveal more information (one card per row on small devices, two cards per row on large devices). If logged in a user may add ingredients, if ingredient name does not already exist it will be entered. If a user created the ingredient they may edit or delete it. Admin user may see the creator of any ingredient and may delete any ingredient. 

#### Pagination 
(index, view_profile, users)

- Where there are more than six results navigation links to pages are displayed below the number of results (6 results per page). 

### Individual Pages

### Home
- [Search/Sort/Filter](#search-sort-filter)
- [Recipe Cards](#recipe-cards)
- [Pagination](#pagination)
- [Share](#share)

### Single Recipes
- [Search/Sort/Filter](#search-sort-filter) (The sort and filter functions not available as there is only one recipe)
- [Share](#share)
- The recipe image and information rows are revealed using animations upon loading. The recipe title is displayed on top with a link to the creator profile below.
- On larger devices the content is displayed in two columns, on the left an image which may be clicked to enlarge if a valid image is provided, if not a blank image with the recipe title is displayed.
- Under the image are icons to summarize key information about the recipe, tooltips give further context on large devices. Alternatively a key guide to the icons is provided in the footer.
- On the right are the ingredients and instructions which may be toggled. Checkboxes allow the user to mark off ingredients and steps as they progress. <br>
- If viewed by the creater a recipe may be edited or deleted. If viewed by the admin a recipe may be deleted.

### Login

- This section contains a form where users may login and be redirected to their profile. Below the form is a link to register.

### Logout

- Clicking 'Logout' ends a user session and redirects them to the 'Login' page.

### Register

- This section contains a form where users may register and be redirected to their profile. Below the form is a link to login.

### 404 and 500 error pages

- Customized 404 and 500 pages contain short information about the error and a button "Back Home" placed below a custom logo. As well as that, they display the navbar which allows users to go back easily to any page if they got lost.

### Profile
- [Recipe Cards](#recipe-cards)
- [Pagination](#pagination)
- [Share](#share)
- Below the header is a card displaying the username and number of recipes. Any user can navigate to any other user's profile by clicking the corresponding 'view' button on the 'Users' page.
- If a logged in user wants to quickly navigate to their own page they can click the 'Profile' link in the navigation menu or side nav on smaller devices.
- A logged in user may delete their own profile along with all associated recipes by clicking the 'delete' button in their profile. 'Admin' user may delete any user.

### Add Recipes

- [Ingredient Cards](#ingredient-cards)
- This section contains a form where users may provide details for their recipes. Asterisks are used where a field is required. Dropdowns are used for multiple choice fields and switches are used for binary choices. When the user inputs a valid image url a preview image will take the place of a placeholder image.

### Edit Recipes

- [Ingredient Cards](#ingredient-cards)
- This section contains a form where users may edit details for their recipes. Asterixes are used where a field is required. Dropdowns are used for multiple choice fields and switches are used for binary choices. When the user inputs a valid image url a preview image will take the place of a placeholder image.

### Users

- [Pagination](#pagination)
- [Share](#share)
- Cards display Usernames with a link to their profile.

### Units

- [Ingredient Cards](#ingredient-cards)
- [Share](#share)
- Users can convert units from imperial to metric and vice-versa.

# Features Left to Implement

- **Image Hosting** <br>
    Currently, images are stored by pointing to an external url and pulling the image from there. I plan to eventually add the option to allow the user to upload an image to the server instead as this will make it easier for the user.

-   **Deleted Recipes**
    When a recipe/user is deleted it is/they are gone forever. Instead, I'd like to have them stored in a deleted items list for review by an admin.

-   **Favourites**

    I'd like to implement a feature to give users an opportunity to "like" other recipes, saving them a "Favourites" collection, which would be displayed on a their own profile. Each recipe card will include a small "heart" icon, clicking which will enable user to add the selected recipe to "my favourits".

##### back to [top](#table-of-contents)

# Technologies Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - Used throughout the site
- [CSS (Cascading Style Sheets)](https://www.w3.org/Style/CSS/Overview.en.html) - Used throughout the site 
- [JavaScript](https://www.javascript.com/) - Used for animtions and functions such as unit conversion. 
- [Materialize](https://materializecss.com/) - Used to aid responsive design and for componants such as modals and functions such as mediabox
- [Gitpod](https://code.visualstudio.com/) - Code Editor used to create the site.
- [GitHub](https://github.com/) - Used to host repos for the site.
- [Imgur](https://imgur.com/) - Used to host images for the site.
- [Screen Recorder](https://chrome.google.com/webstore/detail/screen-recorder/hniebljpgcogalllopnjokppmgbhaden?hl=en) - Used to make GIFs for README.
- [Chrome/Firefox/Bing DevTools](https://developers.google.com/web/tools/chrome-devtools) - Regularly used to test the site (Primarily Chrome).
- [W3C Markup Validation Service](https://validator.w3.org/https://jigsaw.w3.org/) - Used to test code for errors.
- [Affinity Designer](https://affinity.serif.com/en-gb/) - Illustration software used to create logos and icons.
- [Figma](https://figma.com) - Collaborative interface design tool used for creating wireframes as well logos and SVGs.
- [Balsamiq](https://balsamiq.com/?) - Used to create wireframes.
- [Tinypng](https://tinypng.com/) - Used to compress images.
- [Croppola](https://croppola.com/) - Used to crop images.
- [Randomkeygen](https://randomkeygen.com/) - Used to generate random keys.
- [Kaffeine](https://kaffeine.herokuapp.com/) - Used to keep Heroku app from falling asleep.
- [Uptime Robot](https://uptimerobot.com/) - Used to keep Heroku app from falling.

### Libraries

- [Materialize](https://materializecss.com/) - is a framework for building responsive, mobile-first websites. I used materialize to create grid layouts, navbar, cards, forms, buttons and modals as well as features such as collapsibles, materialbox, tooltips and tabs.

- [JQuery](https://jquery.com/) - is a Javascirpt library. I primarily used JQuery to add and remove classes on hover states as well as run various Materialize functions.

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - is a lightweight WSGI web application framework. I primarily used it to construct and render pages.

- [Jinja](https://flask.palletsprojects.com/en/1.1.x/) - is a templating language for Python. I primarily used it to display data from the backend in HTML.

- [PyMongo](https://flask.palletsprojects.com/en/1.1.x/) - is the recommended way to work with MongoDB from Python, used to make communication between Python and MongoDB.

- [dnspython](https://pypi.org/project/dnspython/) - is a DNS toolkit for Python.

### Version Control

- [Git](https://git-scm.com/) - used for version control

- Branches were used to experimaent with pagination.

---

# Accessibility

### Semantics

- HTML5 Semantics used throughout (header, nav, main etc...)
- Titles used throughout (McTastic Recipes, McTastic Profiles etc...)
- Language is set to english (`<html lang="en">`)

---

- Aria labels used throughout eg `<button id="submit" aria-label="submit" type="submit">`
- Alt Text: Alt text dynamically applied to images eg `alt="{{recipe.recipe_name}} image"`

# Testing
All testing and validation is contained within a separate .md file. <br> [View TESTING.md](TESTING.md)

# Deployment

1. This repository may be cloned directly into an editor by pasting the following command into the terminal:   
`git clone https://github.com/Sean-Mc-Mahon/McTasticRecipes`    
Alternatively, you can save a copy of this repository by clicking the green button "Clone or download" , then "Download Zip" button, and after extract the Zip file to your folder.
2. In the terminal window change directory (CD) to the correct file location (directory that you have just created).
3. Set up environment variables:
    - Create **.env** file in the root directory.
    - On the top of the file add `import os` to set the environment variables in the operating system.
    - Set the connection to your MongoDB database(MONGO_URI) and a SECRET_KEY with the following syntax:
    `os.environ["SECRET_KEY"] = "YourSecretKey"`   
    `os.environ["MONGO_URI"] = "YourMongoURI"`  
    .
4. Install all requirements from the **requirements.txt** file putting this command into your terminal:   
`pip3 install -r requirements.txt`  
*Note: GitPod does not require `sudo`, so if you use another IDE, you will need to include `sudo` in the beginning of the command: `sudo pip3 install -r requirements.txt`.*
5. Create a new Database called "recipe_manager" in [MongoDB Atlas](https://www.mongodb.com/).   
*You can sign up for free account, if you do not have one.*
6. In "recipe_manager" database create eight following collections:
###### categories
```
_id: <ObjectId>
category_name: <String>
```
###### food Groups
```
_id: <ObjectId>
group_name: <String>
```
###### ingredients
```
_id: <ObjectId>
ingredient_name: <String>
ingredient_cal: <String>
group_name: <String>
unit_name: <String>
created_by: <String>
```
###### prep
```
_id: <ObjectId>
prep: <String>
```
###### Recipes
```
_id: <ObjectId>
category_name: <String>
recipe_name: <String>
recipe_ingredients: <String>
recipe_instructions: <String>
recipe_image: <String>
recipe_serves: <String>
recipe_time: <String>
recipe_cals: <String>
recipe_description: <Array>
recipe_is_vegan: <Array>
recipe_is_vegetarian: <ObjectId>
created_by: <String>
```
###### sort_parameters
```
_id: <ObjectId>
parameter_name: <String>
```
###### units
```
_id: <ObjectId>
unit_name: <String>
```
###### users
```
_id: <ObjectId>
username: <String>
password: <String>
```
7. You will now be able to run the application using the following command `python3 run.py`. 

### Heroku Deployment
To deploy the project to [Heroku](https://heroku.com/) the following steps need to be completed:
1. Create a **requirement.txt** file, which contains a list of the dependencies, using the following command in the terminal:  
`pip3 freeze > requirements.txt`
2. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:   
`echo web: python run.py > Procfile`
3. `git add`, `git commit` and `git push` these files to GitHub repository
4. Create a **new app** in Heroku, assigning a name (must be unique) and set a region (for my project I set Europe)
5. From the Heroku dashboard link the new Heroku app to your GitHub repository:    
    - "Deploy" -> "Deployment method" -> "GitHub"
    - then "Enable automatic deployment"
6. To start the web process, put the following command into the terminal: `heroku ps:scale web=1` to scale dynos
7. In the **Settings** tab of the new Heroku app, click on "Reveal Config Vars" and set the following config vars:
    - **IP** : 0.0.0.0
    - **PORT** : 8080
    - **MONGO_URI** : `<link to your MongoDB database>`
    - **SECRET_KEY** : `<your secret key>`
    - **DEBUG**: **FALSE**  
*Note: your MONGO_URI and SECRET_KEY must match the ones you entered in .env.py file*

8. The app will be deployed and ready to run. Click "Open App" to view the app.   

**Note**: if you have not linked GitHub and Heroku following step **5**, alternatively as the last step of deployment, you can put the following command into your terminal:   
 `heroku login`, after a successful log in `git push heroku master` - to push the app to Heroku, and finally click "Open App" in Heroku dashboard to view the app.

---

# Credits

### Content

1.  Google Fonts for font styles; https://fonts.google.com/

2.  Youtube; Various resources for Materialize taken from [The Net Ninja](https://www.youtube.com/playlist?list=PL4cUxeGkcC9gGrbtvASEZSlFEYBnPkmff)

3.  Youtube; Code for temperature conversion modified from [Whatsdev](https://youtu.be/EHclqGV_KME)

4.  Youtube; Code for temperature conversion modified from [Whatsdev](https://youtu.be/EHclqGV_KME)

5.  Github; Code for pagination modified from [irinatu17](https://github.com/irinatu17/MyCookBook)

6.  Github; Code for url validation and placehoder image modified from [Paulloy](https://github.com/paulloy/whiskey_herald_msp3/blob/master/app.py)

7.  Github; Format of README modified from [Mr-Smyth](https://github.com/Mr-Smyth/circles/blob/master/README.md) and [irinatu17](https://github.com/irinatu17/MyCookBook/blob/master/README.md)

7.  Icons sourced from [Iconmonstr](https://iconmonstr.com/)

8.  Button icons sourced from [Fontawesome](https://fontawesome.com/)

 

### Acknowledgements

1.  My mentor Adegbenga Adeye for his support and input.

2.  My peers on slack for their generosity in sharing their knowledge and experience.

---

This project is for educational use only

##### back to [top](#table-of-contents)