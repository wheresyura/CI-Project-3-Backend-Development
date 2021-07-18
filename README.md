<img src="assets/images/readme_1.png" style="margin: 0;">
 
# CI: Project-3 Backend Development - Recipe website
 
[View the live project here.](https://ci-project-3.herokuapp.com/)
 
I have chosen to build a recipe website for students that allows users to register, login and create their own recipes on this website. There are a few main functionalities that follow the CRED requirements set out by the code institute guidelines. 
 
The goal with this website is threefold; 
1. I want to learn how to connect to an external database using python to be able to collect and display the data that was created by other users. For each user to have their own ability to add their own recipes as well as edit and delete them.
2. I wanted to learn from tutorials provided by the code institute and also improve on the code to create my own milestone project which can satisfy all of the requirements and be fun to use.
3. The website was built to learn all about python and put the previous lessons into practice. As well as fulfilling the main requirements for this Milestone Project - CRED and exception handling. 
 
 
## 1.UX
 
### Project Goals
 
The primary goal is for ‘students’ the users of this website to create, edit and delete the recipes they wish to make. This website is meant to be a fun place where users can create and share their recipes for all other students to see. However editing and deleting the recipes can only be done by the users who created the recipe in the first place. The site is meant to serve as an inspiration board for all students in a university to share their favourite meals and for others to try them.
 
The secondary goal is to learn how to use python a bit more and put what we have learned so far into practice. I mainly focused on the backend of the website although the frontend also got attention too.
 
### User Goals (Students)
- A website that will serve as a database for all sorts of inspiring recipes for all other users to gain inspiration from.
- A website where the user can add their own recipes, including preparation time, and the ingredients and also add their own image to the database.
- Have an ability to edit these recipes if they were the ones who created the recipes.
- Easy to navigate and understand what the website is used for, navigation bar changes depending if you are logged in or not.
- Have useful messages appear when an action has been successfully completed.
- Graceful error handling by using the try and except handlers, redirecting to our page in the case of an error.
- Have the ability to register and login to this site.
 
 
### Developer Goals
 
- Learn how to use python to connect with a database like MongoDB and also learn how to use external libraries to get additional functionality quicker and easier. 
- Make the data displayed clear, easy to understand as well as intuitive to the end user, and also very actionable. For example a user has a good user experience and to be able to select the actions they want easily.
- Really looking forward to learning how to use Python and work with a database.
 
 
### User Stories 
 
This project is aimed at students and ‘foodies’ who want to share their recipes with their friends and classmates:
 
1. Have clear navbar that will change depending on what user is using it. It will change depending if the user is logged in or still needs to register.
2. The end user will use this mainly on their desktop so it will be mostly optimised for this, however it will still be compatible with tablets and phones.
3. The user can easily create, edit and delete the recipes on the website, it is very intuitive and as they navigate the site and submit they get a pleasant message describing their progress. 
4. The form is made so that the end user can easily edit what they have selected before.
5. The edited recipes will be displayed in the recipes home page where all other users can see all of the recipes of other users.
6. Have minimal design and simple white colours on the website.
7. Have very few icons and only once that make logical sense in accurate locations, like the add recipe button.
8. To have login and register functionality that works accurately.
 
 
### Design Choices
 
The website was designed so that a user can scroll from the top to the bottom and could easily navigate and intuitively select all of the options for successfully adding their delicious recipe to the website.
 
#### Fonts
The website does not use any custom fonts as I used custom once in other projects in the past and wanted to stick to the default once.
 
#### Icons
The website uses minimal iconography as I did not want to clutter my website, or compromise the user experience. I made this decision after watching the videos on the design principles, I decided to keep this minimal. I use it only when it makes logical sense and improves the user experience so in this case I used it when explaining how to use the website.
 
#### Colours
The website uses all of the basic colours that bootstrap offers, I experimented with different colour pallets from bootstrap but decided on using the simple and most basic once, as colours are not the main focus of the project. I wanted to keep the website clear and found that the normal white background that comes with bootstrap did this best.
 
#### Styling
Most of my styling and responsiveness was done using bootstrap built in functionality offered by bootstrap. With the bootstrap classes I tried to use the most basic options they had available as I wanted my site to look minimal and simple. I used CSS in only a few instances.
 
#### Backgrounds
The single time I used a background image as the hero cover I took it from Google images.
 
### Wireframes
The wireframes were created using pen and paper during the scoping part of the project, when I planned the design of this website for the desktop and be responsive version on mobile and tablet.
- [Schema](static/images/mockups/wire_schema.jpg)
- [Mobile Version](static/images/mockups/wire_phone.jpg)
- [Tablet Version](static/images/mockups/wire_tablet.jpg)
- [Web Version](static/images/mockups/wire_desktop.jpg)
 
 
## 2.Features
 
The website has 5 main features:
 
### Existing Features
- Feature 1 - Register, that allows you to create a new user and password.
- Feature 2 - Login/logout, allows you to log into the user you previously created, or logout of the user previously created. 
- Feature 3 - A form that allows logged in users to add new recipes, as well as ingredients, preparation time, select the category and finally add an image. 
- Feature 4 - An extension to the previous feature, this allows you to edit the fields above, once you are the once who created this recipe.
- Feature 5 - This is the final feature and it allows you to delete the recipes you have created if you are the person who made the recipes in the first place.
 
 
 
 
 
### Features Left to Implement
- Future Feature 1 - To have the ability to search for all of the recipes with a search field.
- Future Feature 2 - A feature that allows you to categorise visually all of the different recipes that were included in the site.
- Future Feature 3 - A contact form, that allows users to get in touch with you easily.
- Future Feature 4 - a dark mode button, that would change the whole look and feel of the website from white to dark, and dark to white when clicked back.
- Future Feature 5 - To have some recipes suggested to you based on what you have selected you will make in the past.
- Future Feature 6 - To have a profile page that you can customize and change your private details about yourself.
- Future Feature 7 - To be able to see a different view as an admin, this currently does not work properly, you should be able to change categories as an admin, didn't have time to finish this.
 
 
 
 
 
## 3.Technologies Used
 
### Languages Used
 
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
 
 
### Frameworks, Libraries & Programs Used
 
1. [Bootstrap](https://getbootstrap.com/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
3. [jQuery](https://jquery.com/)
    - jQuery came with Bootstrap and with DataTables to create some of the functionality for the filtering in the table.
4. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
5. [GitHub](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
6. [Flask](https://flask.palletsprojects.com/en/2.0.x/)
-   Used to reuse code across HTML pages.
7. [MongoDB](https://www.mongodb.com/)
-   Used as a database to store data created by users.
8. [Heroku](https://www.heroku.com)
- Where the project is hosted.
 
## 4.Testing
- registering new user - worked as expected.
- login as an existing user - worked as expected.
- logging out - worked as expected.
- Adding and submitting a new recipe - worked as expected.
- Editing a new recipe (if you are a user that created it) - worked as expected, but one small part you can not edit the ingredients.
- Deleting a recipe (if you are the user that created it) - worked as expected.
 
 
1. When the user clicks register on the navbar, he is asked to choose a name and password with at least 5 characters.
- On both mobile and desktop the register button worked as expected, providing a field to fill out.
- The filter worked only allowing you to continue if you selected 5 characters worked successfully.
- The registered user shows the users profile once logged in and shows you a new navbar.
2. The login feature was tested in a similar manner, on both desktop and mobile and functioned as intended with no errors.
- Data was imputed in the field for passwords and name, if the data matched then successful login occured.
- If data was not correct an error message would gracefully be presented.
3. The next main part of the website is the adding of recipes; this also was tested on desktop and mobile.
- Navigating on each field, like the recipe name, preparation time, ingredients, method and image would all be done and if all the fields were filled out then the recipe would update successfully. This was seen on the website’s recipe page and also in the database at MongoDB.
- Filling out each field correctly making sure that all the requirements are met, all works.
- Pressing the add recipe button and seeing the message that your recipe was successfully added, also can now view it in the home page with the rest of the recipes.
- Doing parts of the process wrong and seeing them handled gracefully, when filled out wrong, like for example I tested not attaching an image or leaving out a part the form would not submit.
4. Deleting the recipe, this page also worked as intended for both mobile and desktop, however some of the fields were not customizable in particular the ingredients, I knew this was happening but did not have the time to fix.
- When you are logged in to the user the delete button shows up in the main part of the website where you can see all of the recipes, this only shows up if you are the user who created the recipe, and therefore working as intended. 
- If you are not the user who made the recipe you can not delete or edit the recipe - working as intended..
 
The website is mobile responsive and works on all devices and fills the page as needed, optimising the content for that device.
 
#### Using Code Validators & Lighthouse
 
- I used the [W3C](https://validator.w3.org/) and was able to solve all problems associated with my code, and pass all of the tests except the once not on my url link, from other resources I used. 
- I used the [Html validator](https://validator.w3.org/) and was able to solve all problems and had no issues with my html, I did get a score of four warnings but they were not errors.
- I used the 	[Jshint](https://jshint.com/) and was able to not get any errors but I did get 51 warnings, most of which seemed like they were just browser dependent.
- I used [Lighthouse click here for the report](https://developers.google.com/web/tools/lighthouse) in the developers tools and was able to get a good score under those parameters.
 
 
 
#### Discovered & Solved Bugs
 
1. The first problem I encountered was when I used the tutorial video and then changed the names of all of the different files to match my database requirements, I went from ‘task’ like in tutorial to ‘recipe’ like in my current database, this was a tedious process and changing the names everywhere was wasting time, I would not do it this way in the future but was able to overcome this problem.
 
2. Another problem solved after consulting with my dad, was how to add multiple ingredients to my page and display this visually. The form itself was not difficult to do but getting the ingredients to display needed to use a hidden field where this would appear.
```python
 
function add_ingridient(){
  
   let hidden_ingredients = $('#ingredients');
   let ingredients = [];
 
   let ingr_name = $('#ingredient_name').val();
   let ingr_amount = $('#ingredient_amount').val();
   let ingr_measure = $('#ingredient_measure').val();
 
   let ingr = { name: ingr_name, amount: ingr_amount, measure: ingr_measure };
 
   if (hidden_ingredients.val() !== "") {
       ingredients = JSON.parse(hidden_ingredients.val());
   }
 
   ingredients.push(ingr);
 
   display_ingridients(ingredients);
}
 
 
```
 
3. Another bug that I solved after speaking with my mentor was around exception handling, I initially tried using unique exceptions within the python code for each of the functions I made. My mentor told me this was not the best practice and a better approach was to use general one that captures all exceptions. 
 
```python
@app.errorhandler(Exception)
def handle_generic_error(e):
   traceback.print_exc()
   if isinstance(e, KeyError):
       flash("Seems like you're not logged in yet!")
   return (render_template('error.html',
           error_message="We couldn't handle your request",
           error_code=500), 500)
 
 
```
#### Known Bugs
1. On some mobile devices the recipe page is not filled as expected and the text is compromised (you can not see it all). I know how to fix it but just did not get the time to do it. 
2. You can not edit the ingredients this was as they used a different logic and were saved as objects, I was unable to resolve this issue but if I had time, I might of been able to do it.
 
 
 
 
 
## 5.Deployment
 
 
### GitHub Pages
 
The project was deployed to GitHub Pages using the following steps...
 
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Create heroku application.
7. Add the heroku remote with repository by typing in terminal: heroku git: remote -a CI-Project-3-Backend-Development
 
7. In main Repository folder create env. py file.
Add below configuration variables to the env. py file:
os.environ["MONGO_URI"]= "place here your Mongo DB URI" - needed for manipulating database
os.environ['SECRET_KEY']= "place here your SECRET KEY" - needed for forms in webpage
os.environ['MONGO_DBNAME
']='your email username' 
 
8. Add and push created files to repository by commands: 'git add', 'git commit', 'git push' for github and 'git push heroku master' for heroku.
 
 
9. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.
 
 
### Forking the GitHub Repository
 
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...
 
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.
 
### Making a Local Clone
 
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.
 
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
 
 
7. Press Enter. Your local clone will be created.
 
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
 
Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.
 
 
## 6.Credits
 
### Code
 
- Template code for the navbar, form and heroimage was taken from [GetBoostrap](https://getbootstrap.com/docs/5.0/components/navbar/) and heavily modified to suit the site's needs.
- When I was stuck on a problem for a long period of time I would go to my dad, who is a software developer and he would help me find a solution, as well as explain or point me in the direction of where to look for the relevant information online. 
- Also used the tutorial video from Code Institute to get everything connected and working before changing and adding to it. 
 
### Content
- The content are recipes I discovered on the internet, a fun fact all the once I uploaded, I have made myself before.
 
### Media
- All of the photos in this site were obtained from Google Images.
 
### Acknowledgements
 
- My Dad who has helped me with any technical questions that I had throughout this project. Explaining anything I did not in ways that was easy to understand.
- Thank you to my project mentor [Reuben Ferrante](https://uk.linkedin.com/in/reuben-ferrante) for his continued guidance and support during this project. 
- The lesson videos from Code Institute.
 
 
 
 
 





