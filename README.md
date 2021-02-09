# McTastic Recipes

### [Live Site](https://mctastic-recipes.herokuapp.com/)

### [GitHub](https://github.com/Sean-Mc-Mahon/McTasticRecipes)

![Various Devices](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/resposiveness.JPG)

McTastic Recipes is a Milestone 3 project, it is part of the Fullstack Software Development Course of [Code Institute](https://codeinstitute.net/).

# Table of Contents

**<details><summary>Project overview</summary>**
* [**_Project overview_**](#project-overview)
* [**_User Stories_**](#user-stories)
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

**<details><summary>Testing</summary>**
* [**_Problems and Solutions_**](#problems-and-solutions)
* [**_Validators_**](#validators)
* [**_Manual Testing_**](#manual-testing)
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
- User Story B: As a registered user I would like to add, edit, update or delete my own recipes.
- User Story C: As a registered user I would like to be able to edit my recipes.
- User Story D: As a registered user I would like to view what recipes other users have created.
- User Story E: I would like to be able to view the recipes clearly regardless of the type of device I use.
- User Story F: I would like confirmation of what I'm doing, such as when I've registered, logged in, added, edited or deleted a recipe.
- User Story G: I would to be able to convert units from metric to imperial and vice versa.

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


### Structure/Skeleton Planes

- The site uses a consistent structure, a navbar is at the top of the page which allow a user to navigate the site and login if needed. A burger menu is used for small devices.
- The index page has a search bar, filter and sort feature. If a user performs a search they will be able to sort the search results. 
- The content is consistant with text kept to a minimum. Majority of imagery and text is determined by users.
- A footer at the bottom provides copyright information and links to social media pages and a key guide of icon meanings to aid users on mobile devices who do not have the benefit of tooltips. 
- The number of clicks needed to reach any page is kept to a minimum. Sections such as user profiles will not be visible to users who are not logged in.
- Buttons/modals/links are consistant in design.

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

#### Wireframes

I used Balsamiq and figma to create the wireframes. The layout has altered since I created the wireframes as I decided to replace the contact page with a newsletter sign up in the footer. The parallax felt too distracting and so that has been omitted. Originally there were to be seperate pages for Cooking/Baking/snacks but instead I implemented a feature to filter recipes by category.
I used affinity designer to design the logo, I went through many iterations of the design until I was happy with two final logos, one for the navigation bar on the site and the other for the browser tab icon.

- [Balsamiq Wireframe](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/mctastic-wire.pdf)

- [Affinity Designer Logo Process](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/logo-design.jpg)

##### back to [top](#table-of-contents)

---

# Features

## Existing Features

### Elements on every page
- **Navbar**
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

- **Footer**

    The footer features:
        - Newsletter signup: Users may submit an email to request a newsletter.
        - Key Information
        - Copyright Information
        - Links to social media platforms.

### Individual Pages

- **Home**

    The index page has a search bar, filter and sort feature. The search feature searches for keywords in recipe titles and ingredients. If a user performs a search they will be able to sort the search results. <br>
    The sort feature allows users to sort the results by A-Z, Z-A, latest created and oldest created. <br>
    The filter allows users to display recipes under the categories of cooking, baking, snacks or all. <br>
    The main section of the home page displays cards for each recipe. On small devices the cards may be expnded to reveal more information (one card per row on small devices, two cards per row on medium devices). <br>
    On large devices users can hover over cards to reveal more information (3 cards per row). <br>
    Pagination links allow users to navigate to the next page of results (6 per page).

- **Single Recipes**
    A search function is available below the navigation. The sort and filter functions not available as there is only one recipe. <br>
    The recipe image and information rows are revealed using animations upon loading. The recipe title is displayed on top with a link to the creator profile below. <br>
    On larger devices the content is displayed in two columns, on the left an image which may be clicked to enlarge if a valid image is provided, if not a blank image with the recipe title is displayed. <br>
    Under the image are icons to summarize key information about the recipe, tooltips give further context on large devices. Alternatively a key guide to the icons is provided in the footer.<br>
    On the right are the ingredients and instructions which may be toggled. Checkboxes allow the user to mark off ingredients and steps as they progress. <br>
    If viewed by the creater a recipe may be edited or deleted. If viewed by the admin a recipe may be deleted.

- **Login**

    This section contains a form where users may login and be redirected to their profile. Below the form is a link to register.

- **Register**

    This section contains a form where users may register and be redirected to their profile.

- **Profile** 

    This section contains a form where users may update their information and view their recipes.

- **Add Recipes**

    This section contains a form where users may provide details for their recipes. Asterixes are used where a field is required. Dropdowns are used for multiple choice fields and switches are used for binary choices. When the user inputs a valid image url a preview image will take the place of a placeholder image. <br>
    A list of ingredients is displayed under the form for users to reference for calory informtion as they add ingredients to their recipes.

- **Profile**

    This section displays the user name and number of recipes in a card at the top as well as a welcome message if they are after logging in. <br>
    Below this card the recipes created by the user are displayed and if the user has contributed more than 6 recipes then pagination links are displayed below the recipes.


# Features Left to Implement

- **Image Hosting** <br>
    Currently, images are stored by pointing to an external url and pulling the image from there. I plan to eventually add the option to allow the user to upload an image to the server instead as this will make it easier for the user.

-   **Deleted Recipes**
    When a recipe/user is deleted it is/they are gone forever. Instead, I'd like to have them stored in a deleted items list for review by an admin.

##### back to [top](#table-of-contents)

# Technologies Used

1. **HTML (Hyper Text Markup Language):** Used throughout the site;  
   https://developer.mozilla.org/en-US/docs/Web/HTML
2. **CSS (Cascading Style Sheets):** Used throughout the site;
   https://www.w3.org/Style/CSS/Overview.en.html
3. **Bootstrap:** Used to aid responsive design and for componants such as carousels and buttons https://getbootstrap.com/
4. **Gitpod:** Code Editor used to create the site.
   https://code.visualstudio.com/
5. **GitHub:** Used to host repos for the site https://https://github.com/Sean-Mc-Mahon/ms2-seanmcmahon-digital-design
6. **Chrome/Firefox/Bing DevTools:** Regularly used to test the site https://developers.google.com/web/tools/chrome-devtools
7. **W3C Markup Validation Service** Used to test code for errors; https://validator.w3.org/https://jigsaw.w3.org/css-validator/validator
8. **Affinity Designer** Illustration software used to create ...; https://affinity.serif.com/en-gb/
9. **Figma** Collaborative interface design tool used for creating wireframes as well logos and SVGs; https://figma.com
10. **Balsamiq** Used to create wireframes; https://balsamiq.com/?gclid=EAIaIQobChMIuoqlhfWi6wIV6YBQBh2f9w7DEAAYASAAEgLUTfD_BwE
11. **Tinypng** Used to compress images; https://tinypng.com/
12. **Croppola** Used to crop images; https://croppola.com/
13. **Randomkeygen/** Used to generate random keys; https://randomkeygen.com/
14. **Kaffeine** Used to keep Heroku app from falling asleep; https://kaffeine.herokuapp.com/
15. **Uptime Robot** Used to keep Heroku app from falling asleep; https://uptimerobot.com/

### Libraries

- [Bootstrap 4](https://getbootstrap.com/) - is a framework for building responsive, mobile-first websites. I primarily used bootstrap to format layouts and for certain components such as image carousels and buttons.

- [JQuery](https://jquery.com/) - is a Javascirpt library. I primarily used JQuery to add and remove classes on hover states.

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - is a lightweight WSGI web application framework. I primarily used it to construct and render pages.

- [Jinja](https://flask.palletsprojects.com/en/1.1.x/) - is a templating language for Python. I primarily used it to display data from the backend in HTML.

- [PyMongo](https://flask.palletsprojects.com/en/1.1.x/) - is the recommended way to work with MongoDB from Python, used to make communication between Python and MongoDB.

- [dnspython](https://pypi.org/project/dnspython/) - is a DNS toolkit for Python.

### Version Control

- [Git](https://git-scm.com/) - used for version control

- Branches were used to ...

# Testing

### User Stories

_- User Story A: ._   
Joe can ...

_- User Story B: Liz would also like to..._  
Liz can...

_- User Story C: Harry is interested in..._  
Harry can ...

_- User Story D: Hazel would like to..._
Hazel can ...

### Problems and Solutions

- 

- 

- 

### Validators

1. **HTML:** [W3C HTML Validator](https://validator.w3.org/) Used to identify HTML errors.

2. **CSS:** [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) Used to identify CSS errors.

3. **Javascript:** [JSHint](https://jshint.com/) Used to identify Javascript errors.

### Manual Testing

1. **Developer Tools:** Chrome, Firefox and Microsoft Edge web dev tools using iPhone 5 and Ipad as toggle devices to test responsiveness.

2. **Lighthouse:** A number of issues were resolved using lighthouse.

3. **Mobile Devices:** I used my Google Pixel 3a phone and Amazon Fire tablet to test the site.

4. **amiresponsive:** [Am I Responsive](http://ami.responsivedesign.is/) Used to test responsiveness across a range of devices.

5. **Friends and family:** I asked for feedback from friends and family in order to get a users perspective.

6. **Contact Form:** On the contact page the form may not be submitted without using correct syntax for the e-mail input or if either input is blank. Once inputs are filled properly and submit is clicked the form will clear without the page being refreshed and an alert will inform user that the message has been sent.

9. **Navigation:** Clicked through all links to ensure they all go to the correct location.

# Deployment

CHANGE DEBUG=TRUE TO FALSE IN APP.PY PRIOR TO DEPLOYMENT

1. I Created a Github account at https://github.com
   My account url; https://github.com/Sean-Mc-Mahon

2. I installed Git and set up a username and password.

3. I created a repository on Github (https://github.com/Sean-Mc-Mahon/cat-rescue)

4. On VS Code I opened the command pallette and selected Git Clone, I pasted in the URL for the repo on GitHub and selected a folder on my computer to sync to.

5. I uploaded all files to my Github repository.

6. To publish the project to see it on the web, I then went into the Settings on my respository, scrolled down to the heading, GitHub Pages. Under the Source setting, I used the drop-down menu to select master branch as a publishing source and saved it. Refreshed the github page, and you are then given a url where your page is published;
   Your site is published at https://github.com/Sean-Mc-Mahon/

7. To run this code on a local machine, you would go to my respository at
   https://github.com/Sean-Mc-Mahon/cat-rescue and on the home page on the right hand side just above all the files, you will see a green button that says,
   "Clone or download", this button will give you options to clone with HTTPS, open in desktop or download as a zip file.
   To continue with cloning, you would;

- Open Git Bash
- Change the current working directory to the location where you want the cloned directory to be made.
- Type git clone, and then paste this URL; https://github.com/Sean-Mc-Mahon/ Press Enter. Your local clone will be created.

For more information about the above process; https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

---

# Credits

### Content

1.  Google Fonts for font styles; https://fonts.google.com/

2.  Youtube; Various resources for Materialize taken from [The Net Ninja](https://www.youtube.com/playlist?list=PL4cUxeGkcC9gGrbtvASEZSlFEYBnPkmff)

3.  Stack Overfow; Code to implement ... taken from answer by ... [Stack Overflow](https://stackoverflow.com/)

7.  Slack; ... inspired by tutorial via ....

8.  Youtube; Bootstrap Carousel inspired by youtube tutorial by [Clever Techie](https://youtu.be/AvMl3StAju4)

9.  Format of README modified from Mr-Smyth: https://github.com/Mr-Smyth/circles/blob/master/README.md

### Acknowledgements

1.  My mentor Adegbenga Adeye for his support and input.

2.  My peers on slack for their generosity in sharing their knowledge and experience.

##### back to [top](#table-of-contents)