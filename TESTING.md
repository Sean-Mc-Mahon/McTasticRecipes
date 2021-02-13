# Testing

[return to README.md](https://github.com/Sean-Mc-Mahon/McTasticRecipes)


**<details><summary>Testing</summary>**
* [**_User Testing_**](#user-testing)
* [**_Problems and Solutions_**](#problems-and-solutions)
* [**_Validators_**](#validators)
* [**_Manual Testing_**](#manual-testing)
</details>

---

# User Testing

### User Story Testing

_- User Story A:_ As a casual user I would to easily browse recipes.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-a.gif)

User can search by ingredient, sort results, hover over an image to preview information with the help of tooltips, navigate to the recipe, enlarge the image and check off ingredients and steps as they make the recipe.

_- User Story B:_ As a user I would like to create a profile and delete it if I no longer want it.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-b.gif)

User can navigate to registration, enter a username and password and if they are valid and the username is not taken she can create a profile and be redirected to their new profile with a flash message to wwelcome them. They can later delete the profile after clicking past a warning from a modal and will be notified by a flash message that the profile has been deleted.

_- User Story C:_ As a registered user I would like to add, edit, update or delete my own recipes.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-c.gif)

User can input information, choose categories and preview image prior to adding recipe. User may then edit the recipe or delete it.

_- User Story D:_ As a registered user I would like to view what recipes other users have created.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-d.gif)

User can navigate to users page and view any user to browse their reciepes, they may also click the 'Created By' link on any recipe to view the corresponding profile.

_- User Story E:_ I would like to be able to view the recipes clearly regardless of the type of device I use.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-e.gif)

The app is fully resonsive and a user can use the app comfortably on any device size.

_- User Story F:_ I would like to be able to easily share recipes.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-f.gif)

User can hover or click on the share icon on the bottom right of the screen and choose what platform thay would like to use to share the page.

_- User Story G:_ I would to be able to convert units from metric to imperial and vice versa.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-g.gif)

User can click on any field of a card on the conversions section and any figures they input will be converted to all other units on that card.

_- User Story H:_ As a registered user I would like to add, edit, update or delete my own ingredients.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-g.gif)

User can click add button on units page to add ingredient using a modal, if fields are filled and ingredient name is not in use the ingredient will be added and the user may edit or delete the ingredient as long as they are logged in.

### Admin Story Testing

_- Admin Story A:_ As the admin I would like to be able to delete any user along with all recipes created by that user.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/admin-story-a.gif)

Admin may access any profile by the 'Created By' link in a single_recipe page or by the corresponding 'view' button on the users page and after confirming the intention to delete in a modal the user will be deleted along with any recipe they created.

---

# Manual Testing

1. **Developer Tools:** Chrome, Firefox and Microsoft Edge web dev tools using iPhone 5 and Ipad as toggle devices to test responsiveness.

2. **Lighthouse:** A number of issues were resolved using lighthouse.
**Accessability**
- Contrast: Alpha level on .blank-image was set to 0.6 which did not offer sufficient contrast with white text. Alpah level rasied to 0.8.
- Aria labels: Aria labels added to buttons such as #search-button and #submit
- Alt Text: Alt text dynamically applied to images eg `alt="{{recipe.recipe_name}} image"`
- Lists: <h5> moved from inside pagination <ul> to above the list.

3. **Mobile Devices:** I used my Google Pixel 3a phone and Amazon Fire tablet to test the site.

4. **amiresponsive:** [Am I Responsive](http://ami.responsivedesign.is/) Used to test responsiveness across a range of devices.

5. **Friends and family:** I asked for feedback from friends and family in order to get a users perspective.

## Functionality

### Header and Footer
#### base.html

action taken | expected result | pass/fail
------------ | --------------- | ---------    
**Logo** |
Clicked Logo | display index.html, browser tab displays 'McTastic Recipes' | pass
**Topnav** |
When not logged in with on displays > 900px topnav | Home/Log in/ Register/Users/Units links should display | pass
Clicked Log In within topnav | Display login.html | pass
Clicked Log In within topnav | Display login.html, browser tab displays 'McTastic Login' | pass
Clicked Register within topnav | Display register.html, browser tab displays 'McTastic Registration' | pass
Clicked Users within topnav | Display users.html, browser tab displays 'McTastic Users' | pass
Clicked Users within topnav | Display users.html, browser tab displays 'McTastic Users' | pass
Clicked Units within topnav | Display units.html, browser tab displays 'McTastic Units' | pass
When logged in with a large screen, display topnav | Home/ Log Out/ Add Recipe/ / Profile/ Users/ Units links should display | pass
Clicked Add Recipe within topnav | Display insert_recipe.html, browser tab displays 'McTastic Add Recipe' | pass
Clicked Logout within topnav | Display login.html and a flashed message, browser tab displays 'McTastic Login' | pass
**sidenav** |
Clicked burger icon multiple times | Sidenav is toggled between being displayed and hidden. | pass
When not logged in with a medium or small screen, display sidenav | Home/ Log in/ Register/ Users/ Units links should display | pass
Clicked Home within sidenav | Display index.html, browser tab displays 'McTastic Recipes' | pass
Clicked Log In within sidenav | Display login.html, browser tab displays 'McTastic Login' | pass
Clicked Register within sidenav | Display register.html, browser tab displays 'McTastic Registration' | pass
Clicked Users within sidenav | Display users.html, browser tab displays 'McTastic Users' | pass
Clicked Users within sidenav | Display users.html, browser tab displays 'McTastic Users' | pass
Clicked Units within sidenav | Display units.html, browser tab displays 'McTastic Units' | pass
When logged in  on displays <= 900px display sidenav | Home/ Log Out/ Add Recipe/ / Profile/ Users/ Units links should display | pass
Clicked Add Recipe within sidenav | Display insert_recipe.html, browser tab displays 'McTastic Add Recipe' | pass
Clicked Logout within sidenav | Display login.html and a flashed message, browser tab displays 'McTastic Login' | pass
**Footer** |
Enter valid email adress and submit #form-contact | Alert displayed thanking user for signing up. Email sent. | pass
Enter email adress without an '@' and submit #form-contact | Alert is displayed informing user that a '@' is required | pass
Enter incomplete email adress and submit #form-contact | Alert is displayed informing user that adress is incomplete | pass
Clicked 'All Done' on modal following newsletter signup | Modal is closed | pass
Clicked LinkedIn icon | LinkedIn profile opened in new tab | pass
Clicked Github icon | Github profile opened in new tab | pass

### Search/Filter/Sort
#### index.html & single_recipe.html
action taken | expected result | pass/fail
------------ | --------------- | --------- 
**Search, Sort By and Filter**|
On displays =< 600px |Search coccupies 12 columns, sort by and filter occupy 6 columns|pass
On displays > 600px  |Search coccupies 6 columns, sort by and filter occupy 3 columns|pass
On displays > 1200px  |Search, sort by and filter all occupy 4 columns|pass
**Search**|
Entered a value into #search form and submitted it. | index.html loads with query results, browser tab displays 'McTastic Search', number of results are displayed as well as the searched term, pagination links function correctly, recipe filter no longer present | pass 
Entered a value with no expected results into #search form and submitted it. | index.html loads with query results, browser tab displays 'McTastic Search', flashed message displayed stating no results found for <query>, recipe filter no longer present | pass 
**Sort By**|
'Sort By' option chosen. | index.html loads with all recipes sorted in accordance with chosen parameter. Browser tab displays 'McTastic Recipes Sort'. | pass
Search & Sort By|
'Sort By' option chosen for search query. | index.html loads with query results sorted in accordance with chosen parameter. Browser tab displays 'McTastic Recipes Search Sort'. | pass 
**Sort By & Filter**|
'Sort By' option chosen after 'Filter' option chosen. | index.html loads with all recipes filtered in accordance with chosen parameter and sorted by order chosen. Number of results and chosen filter displayed above recipe cards. Chosen filter parameter displayed in filter input and chosen filter displayed in sort by input. Browser tab displays 'McTastic Recipes Sort Filter'| pass
**Filter**|
'Filter' option chosen. | index.html loads with all recipes filtered in accordance with chosen parameter. number of results and chosen filter displayed above recipe cards. Chosen filter parameter displayed in filter input. Browser tab displays 'McTastic Recipes Filter'| pass
**Filter & Sort By**|
'Filter' option chosen after 'Sort By' option chosen. | index.html loads with all recipes filtered in accordance with chosen parameter and sorted by order chosen. Number of results and chosen filter displayed above recipe cards. Chosen filter parameter displayed in filter input and chosen filter displayed in sort by input. Browser tab displays 'McTastic Recipes Filter Sort'| pass
On single_recipe: | Search field occupies 12 columns, sort_by and filter options not present| pass

### Recipe Cards
#### index.html & view_profile.html
action taken | expected result | pass/fail
------------ | --------------- | --------- 
**On displays =< 600px**|recipe_cards displayed occupying 12 columns, card displays square image above title/anchor and card reveal icon|pass
**On displays > 600px**|recipe_cards displayed occupying 6 columns, card displays square image above title/anchor and card reveal icon|pass
**recipe_cards**|
Clicked #recipe-link |single_recipe.html loads displaying corresponding recipe|pass
Clicked .activator |.card-reveal revealed. Recipe name, prep time, Servings, Description, creator and link to recipe shown|pass
Clicked 'View Recipe' anchor |single_recipe.html loads displaying corresponding recipe|pass
Clicked close icon |.card-reveal collapse|pass
**On displays > 1200px**|recipe_cards_lg displayed occupying 4 columns, card displays square image|pass
Hovered over .overlay |.gallery item revealed displaying recipe name, creator, prep time, servings, calories(if present), vegan(if vegan) and vegetarian (if vegetarian) but NOT description|pass
Hovered over .icon |Tooltip displays|pass
Clicked on .overlay |single_recipe.html loads displaying corresponding recipe|pass
**On displays => 1500px**|recipe_cards_lg displayed occupying 4 columns, card displays square image|pass
Hovered over .overlay |.gallery item revealed displaying recipe name, description, creator, prep time, servings, calories(if present), vegan(if vegan) and vegetarian (if vegetarian)|pass

### Single Recipes
#### single_recipe.html
action taken | expected result | pass/fail
------------ | --------------- | --------- 
single_recipe.html loaded|correct recipe loaded, reveal animations triggered, Browser tab displays 'McTastic + Recipe Name'|pass
On displays =< 992px:|image section and text section each occupy 12 columns|pass
On displays > 992px|image section and text section each occupy 6 columns|pass
On displays =< 992px:|image section and text section each occupy 12 columns|pass
Clicked on image|materialbox activated|pass
Hovered over icons|tooltips activated|pass
Clicked inactive tab|tabs toggled|pass
Clicked checkbox|checkbox is toggled|pass
Clicked 'Edit' button|edit_recipe.html loaded|pass
Clicked 'Delete' button|Delete recipe modal activated|pass
Clicked 'CANCEL' button in 'Delete Modal'|Modal closedd|pass
Clicked 'DELETE' button in 'Delete Modal'|Recipe is deleted, index.html loaded, message flashed|pass

### Registration
#### registration.html
action taken | expected result | pass/fail
------------ | --------------- | --------- 
registration.html loaded|Browser tab displays 'McTastic Registration' and #register nav link is active|pass
Submit registration without password or username |User prompted to fill required fields|pass
Submit registration with too few characters for password or username |User prompted to fill required fields|pass
Submit registration with username that has been taken |register.html loaded and message flashed|pass
Submit registration valid username and password |view_profile.html loaded and message flashed|pass
Clicked 'Log In' link |login.html loaded|fail

Failed tests remedied following testing.

### Login
#### login.html
action taken | expected result | pass/fail
------------ | --------------- | --------- 
login.html loaded|Browser tab displays 'McTastic Login' and #login nav link is active|pass
Submit login without password or username |User prompted to fill required fields|pass
Submit login with incorrect username or password |login.html loaded and message flashed|pass
Submit login with valid username and password |view_profile.html loaded and message flashed|pass
Clicked 'Register' link |register.html loaded|pass

### Logout
action taken | expected result | pass/fail
------------ | --------------- | --------- 
Clicked 'Logout' link in topnav |login.html loaded and user session ends, message flashed|pass
Clicked 'Logout' link in sidenav |login.html loaded and user session ends, message flashed|pass

### 404 error
#### 404.html
action taken | expected result | pass/fail
------------ | --------------- | --------- 
invalid characters added to url in browser and submitted |404.html loaded|pass
Clicked 'HOME' button |index.html loaded|pass

### Profile
#### view_profile.html
action taken | expected result | pass/fail
------------ | --------------- | --------- 
 Pagination:|Pagination links displayed if user has created more than 7 recipes|pass
 Pagination links clicked|next/previous recipes loaded|pass
 **If session user does not match profile username**|
 view_profile.html loaded|Browser tab displays 'McTastic Profile'|pass
 **If session user matches profile username**|
 view_profile.html loaded|Browser tab displays 'McTastic + Username' and #profile nav link is active|pass
 Clicked Delete|modal displayed asking user for confirmation|pass
 Clicked 'Cancel' button in Delete Profile modal|modal closes|pass
 Clicked 'Delete' button in Delete Profile modal|Profile and associated recipes deleted, index.html loaded, message flashed|pass
 **If session user is 'admin'**|
 Clicked Delete|modal displayed asking user for confirmation|pass
 Clicked 'Cancel' button in Delete Profile modal|modal closes|pass
 Clicked 'Delete' button in Delete Profile modal|Profile and associated recipes deleted, users.html loaded, message flashed|pass

### Add Recipe
#### insert_recipe.html
action taken | expected result | pass/fail
------------ | --------------- | --------- 
 insert_recipe.html loaded|Browser tab displays 'McTastic Add Recipe' and #add-recipe nav link is active|pass
 'Add Recipe' submitted without all required fields|User prompted to fill all fields|pass
 'Add Recipe' submitted with all required fields but no image url or else url not ending in .png/.jpg/.jpeg|Recipe added and 'blank' image with Recipe Name takes place of recipe image|pass
 Valid url ending with .png/.jpg/.jpeg entered prior to submission|Placeholder image replaced with a preview image|pass
 'Add Recipe' submitted with all required fields and valid image url|Recipe added and recipe image is displayed in square aspect regardless of image aspect|pass

### Edit Recipe
#### edit_recipe.html
action taken | expected result | pass/fail
------------ | --------------- | --------- 
 edit_recipe.html loaded|Browser tab displays 'McTastic Edit Recipe'|pass
 View edit_recipe.html|Fields are filled with corresponding values from MongoDB|pass
 Clicked 'Submit' without all required fields filled|User prompted to fill required fields|pass
 Clicked 'Submit' with all required fields filled|Recipe is updated, view_profile.html loaded, message flashed|pass

### Users
#### users.html
action taken | expected result | pass/fail
------------ | --------------- | --------- 
 users.html loaded|Browser tab displays 'McTastic Users' and #users nav link is active|pass
 Clicked 'View' button|view_profile.html loaded displaying information for correct user|pass
 Clicked pagination links|users.html loaded with next/previous user cards displayed|pass

### Units
#### units.html
action taken | expected result | pass/fail
------------ | --------------- | --------- 
units.html loaded|Browser tab displays 'McTastic Units' and #units nav link is active|pass
**Conversions**|
**On displays =< 600px**|
 For .card-content:|Input occupies 12 columns|pass
**On displays > 600px**|
 For each .card-content:|Input occupies 6 columns for all except 'Cups' card where each input occupies 12 columns|pass
**On displays > 992px**|
 For each .card-content:|Input occupies 3 columnsn for 'Weight' card, 6 for Cups, 4 for Volume and Temperature|pass
**for each input**|
 Value entered|all associated inputs are updated|pass

### Add Ingredients
action taken | expected result | pass/fail
------------ | --------------- | --------- 
**If not logged in**|
view units.html |links present to login or register in order to add ingredients|pass
Clicked 'Log In' link |login.html loaded|pass
Clicked 'Register' link |register.html loaded|pass
**If logged in**|
view units.html |Button to add ingredients displayed|pass
Clicked 'Add' button |Modal to add ingredient displayed|pass
Clicked 'Add' button |Modal to add ingredient displayed|pass
Clicked 'Add' button |Modal to add ingredient displayed|pass
Submit ingredient without all required fileds |User prompted to fill required fields|pass
Submit ingredient with all required fileds |units.html loaded, ingredient added, message flashed|pass

### Ingredient Cards
#### units.html & insert_recipe.html
action taken | expected result | pass/fail
------------ | --------------- | --------- 
For each .users-cards:|ingredients are displayed in alphabetical order filtered by category|pass
**On displays =< 992px**|
view units.html or insert_recipe.html |ingredient_cards displayed occupying 12 columns, card displays ingredient name along with calory information and creator name if user is admin. Options available to edit or delete if user is the creator, option to delete if user is admin|pass
**On displays > 992px**|
view units.html or insert_recipe.html |ingredient_cards displayed occupying 6 columns, same info as displays =< 992px|pass
view units.html or insert_recipe.html |ingredient_cards displayed occupying 6 columns, same info as displays =< 992px|pass
**If user is creator**|
Clicked edit|modal to add ingredient displayed|pass
Clicked delete|Ingredient deleted|pass

---

# Problems and Solutions

#### Edit Recipe Changing the Creator: 

- Problem: If the admin were to edit a recipe then the created by value would become 'admin'

- Solution: I felt that while there are valid reasons for the admin to have the ability to delete a recipe it was not appropriate for them to be able to edit a recipe, for this reason only the recipe creator may now edit a recipe.

#### Deleting User Error

- Problem: If a user deletes their profile they may cause an error if they click the 'Profile' link.

- Solution: If the Admin user deletes a profile they are redirected back to the users page. If any other user deletes their own profile they are redirected to the home page and removed from their session.

    `if session["user"] == 'admin':` <br>
    &nbsp;&nbsp;&nbsp;&nbsp;`return redirect(url_for("users"))` <br>
    `else:` <br>
    &nbsp;&nbsp;&nbsp;&nbsp;`session.pop("user")` <br>
    &nbsp;&nbsp;&nbsp;&nbsp;`return redirect(url_for("recipes"))`

#### GSAP Warnings

- Problem: Warning of `gsap.min.js:10 GSAP target [object NodeList] not found. ` shown on pages using GSAP animations.

- Solution: `nullTargetWarn` set to `false` in GSAP's configuration using `gsap.config()`


#### Recipe Cards not displaying at 1200px
- Problem: For displays with width of exactly 1200px neither the recipe-cards nor the recipe_cards_lg were displayed.

- Soution: xl media query rule adjusted from `min-width: 1200px` to `min-width: 1201px`

### Currently Unsolved Problems
#### Back button prompts request to confirm resubmission
- If a user were to sort the recipes on the home page and them filter them and finally press the back button they would be asked to confirm resubmission. Currently I do not have a solution to this problem.

#### 'addthis' causing console errors
- If an adblocker is present a console error will occur (moatframe.js:1 Failed to load resource: net::ERR_BLOCKED_BY_CLIENT) on pages where the 'addthis' script is running. I only run this script on pages where I require that the user be able to share the page via email, social media etc...

---

# Validators

1. **HTML:** [W3C HTML Validator](https://validator.w3.org/) Used to identify HTML errors, as it does not recognize Jinja2 templating language, it showed a number of errors. Apart from that, no other errors were found across the html pages.

2. **CSS:** [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) Used to identify CSS errors, no errors found.

3. **Javascript:** [JSHint](https://jshint.com/) Used to identify Javascript errors.

4. **Python:** [Pep8](http://pep8online.com/) Used to check that python files are PEP8 compliant, no errors found.

---

##### back to [top](#testing)