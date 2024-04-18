# BookWish
[View website here]()

![Website on different views]()

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
3. [Design Choices](#design-choices)
    1. [Colour](#colours)
    2. [Images](#images)
    3. [Structure](#structure)
    4. [Wireframes](#wireframes)
    5. [Database schema & User Journey](#database-schema--user-journey)
4. [Features](#features)
5. [User Authentication](#user-authentication)
6. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks--tools)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Credits](#credits) 
    1. [Media](#media)
    2. [Code](#code)

# Project Goals 
The concept for the BookWish website stemmed from observing the needs of my book-loving family and friends. As avid readers, they constantly seek out new books, discovering titles they're drawn to but often face challenges in obtaining or reading them. Additionally, they struggle to keep track of their growing list of desired reads. I've witnessed friends excitedly stumble upon a book they fancy, only to forget about it later due to lack of a tracking system. Recognizing this common dilemma among readers, I envisioned BookWish as a solution, empowering users to effortlessly compile and manage their book wishlist in one convenient platform.

## User Goals 
* Seamlessly create and manage a personalized wishlist of books they want to read or buy.

## Site Owner Goals 
* Provide an intuitive and enjoyable platform for users to curate their book wishlist.
* Ensure the website is interactive, responsive, and accessible across various devices.

# User Experience 
## Target Audience 
BookWish caters to avid readers and book enthusiasts who seek a centralized platform to organize their reading preferences and track desired books.

## User Requirements and Expectations 
* A simple, intuitive navigation system.
* Smooth functionality of links and buttons.
* Accessibility 

## User Stories 
1.  **Understanding the Site:** As a user, I want to understand the purpose of the site and navigate it easily.
2.  **Registration:** As a user, I want to register for an account.
3.  **Login:** As a user, I want to log into my account.
4.  **Adding Books:** As a user, I want to easily add books to my wishlist.
5.  **Editing Books:** As a user, I want to be able to edit the details of books I have added to my wishlist.
6.  **Deleting Books:** As a user, I want to have the option to remove books from my wishlist.

# Design Choices 

## Colour 
The color scheme for this project was carefully chosen to harmonize with the background imagery of books, creating a visually cohesive and engaging user experience.
#### Color Choices
- **Orange Accent-3**: The vibrant "orange accent-3" from the Materialize color palette was selected to infuse energy and warmth into the design. This bold color choice evokes feelings of enthusiasm and creativity, adding dynamism to key elements of the interface.
  
- **Blue-Grey Lighten-1**: Complementing the vibrant orange accent, the "blue-grey lighten-1" color offers a balanced and calming backdrop. This neutral hue provides visual harmony while ensuring readability and professionalism.
  
- **White Text**: To ensure optimal readability and clarity, white text was chosen against the colored backgrounds. This choice creates a high contrast, enhancing legibility and accessibility for users. Additionally, white text conveys a sense of cleanliness and modernity, aligning with contemporary design principles.

- **Harmonious Palette**: By integrating the orange accent, blue-grey background, and white text, a harmonious color palette was achieved. This cohesive combination reflects the ambiance and theme of the project, enhancing overall visual appeal and coherence.

- **Brand Identity**: Consistent use of colors throughout the project establishes a recognizable brand identity. The cohesive color scheme fosters brand association and strengthens user engagement, contributing to a memorable user experience.

- **User Experience**: The vibrant orange accent guides users' attention to important elements, while the calming blue-grey background promotes a relaxed browsing experience. These color choices enhance user engagement and facilitate intuitive navigation.

## Images 
The background imagery of books was carefully selected to resonate with the website's purpose and theme. Books symbolize knowledge, exploration, and personal growth, aligning perfectly with the concept of a book wishlist platform. The use of imagery not only enhances visual appeal but also reinforces the website's identity and mission. The image used is credited in the credits section at the bottom of this file.
## Structure 
The website is structured in a user-friendly accessible way. The webiste consists of 4 pages:
1. Homepage:
- The user is greeted straight away with a welcome message and the purpose of the website is explained and a link to register for an account or sign in if you already have an account. 
2. Register page:
- The user is shown a form that will need to be completed if they want an account. 
- Once they have registered, they will be redirected to the sign in page. 
3. Sign in page:
- Again a form is displayed where users can enter their account details to sign in.
- Once they have signed in they have access to their own book wishlist.
4. Wishlist page:
- This is the main page of the webiste where users can add, edit and delete books to their wishlist. Only users logged in can access this if not theyre redirected to the log in page with a message saying you need to be logged in to view the wishlist.

## Wireframes 
* [Home page](documentation/wireframes/welcomepage.png)
* [Sign Up page](documentation/wireframes/signuppage.png)
* [Sign In page](documentation/wireframes/signin.png)
* [Wishlist page](documentation/wireframes/wishlistpage.png)

## Database Schema & User journey 

#### User Journey 
<details>
<summary>Screenshot</summary>
<br>
<img src="documentation/userjourney.png">
</details>

#### Database Schema
<details>
<summary>Screenshot</summary>
<br>
<img src="documentation/databaseschema.png">
</details>

# Features 
This website consists of 6 pages which are extended from a base template.
- Welcome page 
- Sign Up page 
- Login Page
- Wishlist Page
- Add Book page 
- Edit Book page 

### Home page
- Welcomes the user and explains the purpose of the site and has links to sign up or log in. 
<details>
<summary>Screenshots</summary>
<br>
<img src="documentation/features/welcomepage.png">
</details>

### Sign Up Form
- Users can register for an account their information will be stored and will be redirected to the sign in page. A message will appear if the username already exists. 
<details>
<summary>Screenshots</summary>
<br>
<img src="documentation/features/usernamealrexist">
<img src="documentation/features/signupredirect.png">
</details>

### Log In Form
- The details users input will be checked against the database and if the details are correct users are signd into their account where they have access to their personal book wishlist. Once signed in too the navbar has another link where a user can log out of their account.
<details>
<summary>Screenshots</summary>
<br>
<img src="documentation/features/invalidlogin.png">
<img src="documentation/features/loginsuccess.png">
</details>

### Wishlist 
- If a user presses the wishlist in the navbar without signing in they are redirected to the log in page and shown a message saying you need to log into your account to see your wishlist. Once a user is signed in, they can add books to their wishlist, as well as edit and delete them. The wishlist items are personalized to each user, ensuring that only they can see and modify their own wishlist.
<details>
<summary>Screenshots</summary>
<br>
<img src="documentation/features/loginsuccess.png">
</details>

### Add Book 
- Users can add a book to their wishlist by clicking on the "Add Book" button, which redirects them to the add book page. Here, they fill out a form with details such as book title, author, etc. Once submitted, the book is added to their wishlist.
<details>
<summary>Screenshots</summary>
<br>
<img src="documentation/features/addbook.png">
</details>

### Edit Book
- If a user needs to make changes to a book's details, they can click on the "Edit" button. This action redirects them to the edit book page, where they can modify any section of the book's information and save the updated version.
<details>
<summary>Screenshots</summary>
<br>
<img src="documentation/features/editbook.png">
</details>

### Delete Book
- To remove a book from their wishlist, users can click on the "Delete" button. This action triggers a modal confirmation prompt to ensure the user intends to delete the book. Upon confirmation, the book is permanently removed from their wishlist.
<details>
<summary>Screenshots</summary>
<br>
<img src="documentation/features/modaldelete.png">
</details>

### Responsive Design:
The quiz is designed to be fully responsive, ensuring an optimal experience across various devices and screen sizes.

# User Authentication

User authentication is a crucial aspect of the BookWish website, ensuring that only authorized users have access to their personalized book wishlist. The authentication process involves registration, login, and session management to authenticate and authorize users securely.

## Registration

New users can register for an account by providing a unique username and a secure password. Upon registration, the user's credentials are securely stored in the database using password hashing to maintain confidentiality.

## Login

Registered users can log in to their accounts using their username and password. The login credentials are verified against the stored user data in the database. If the credentials match, the user is authenticated and granted access to their personalized wishlist.

## Session Management

Session management is employed to maintain user authentication throughout their interaction with the website. Upon successful login, a session is established, allowing the user to navigate between pages without the need for reauthentication. Sessions are securely managed using Flask's session mechanism, ensuring data integrity and preventing unauthorized access.

## Password Security

User passwords are securely hashed using the `generate_password_hash` function provided by Werkzeug. This ensures that passwords are not stored in plain text and cannot be retrieved even by the website administrators. When users log in, the hashed password stored in the database is compared with the hashed version of the password provided during login using the `check_password_hash` function, ensuring secure authentication.

## Access Control

Access control mechanisms are implemented to restrict unauthorized access to sensitive pages and functionalities, such as the user's wishlist. Only authenticated users are allowed to view, add, edit, or delete books from their wishlist. Unauthorized access attempts are redirected to the login page, ensuring the privacy and security of user data.

# Technologies Used
## Languages  
- HTML.
- CSS.
- JavaScript.
- Python. 
## Frameworks & Tools
- [Figma](https://www.figma.com/): Utilized for creating wireframes, providing a visual representation of the website's layout and design.
- [GitHub](https://github.com/): Employed as a version control system and a collaborative platform for storing and managing the project's source code
- [Git](https://git-scm.com/): Utilized for version control, allowing seamless collaboration, tracking changes, and ensuring a well-documented development process. Commits and pushes to GitHub provide a clear history of project evolution.
- [Pixelied](https://pixelied.com/convert/png-converter/png-to-webp): Convert png image to webp.
- [TinyPNG](https://tinypng.com/): Compress webp image.
- [Materialize](https://materializecss.com/):  CSS framework.
- [Materialize Icons](https://material.io/resources/icons/): Integrated for iconography within the Materialize framework.
- [Canva](https://www.canva.com/): Utilized for creating flowcharts
- [Draw SQL](https://drawsql.app/):Employed for designing the database schema.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/): Utilized for debugging, testing, and analyzing website performance directly within the Chrome browser.
- [Flask](https://flask.palletsprojects.com/): framework 
- [PostgreSQL](https://www.postgresql.org/):Used as the relational database management system.
- [Jinja](https://jinja.palletsprojects.com/): Templating engine 

# Testing
Testing for this website can be found in the [TESTING.md](TESTING.md)

# Deployment

The BookWish website has been successfully deployed on Heroku, utilizing ElephantSQL for its database management. Below are the steps involved in the deployment process:

## ElephantSQL Setup

1. **Create ElephantSQL Account**:
    - Sign up for an ElephantSQL account.
    - Click “Create New Instance” and set up your plan.
    - Select the Tiny Turtle (Free) plan, choose a name, and region.
    - Review your details and click “Create instance”.
    - Copy the database URL from the dashboard.
2. **Prepare Heroku Files**:
    - Generate a `requirements.txt` (contains a list of the Python dependencies that your project needs in order to run successfully) file with `pip freeze --local > requirements.txt`. After you run this command a new file called requirements.txt should appear in your root directory.
    - Heroku requires a Procfile containing a command to run your program. Inside the root directory of your project create the new file. It must be called Procfile with a capital P, otherwise Heroku won’t recognise it. Inside the file add the command `web: python run.py`. Ensure you do not add a blank line to the end of the file as this can cause problems for deployment
3. **Configure Database URL**:
    - Open your `__init__.py` file and adjust `SQLALCHEMY_DATABASE_URI`. Add an if statement before the line setting the SLQALCHEMY_DATABASE_URI and, in the else, set the value to reference a new variable, `DATABASE_URL`.

        ```python
        app = Flask(__name__)
        app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

        if os.environ.get("DEVELOPMENT") == "True":
            app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
        else:
            app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
        ```

    - To ensure that SQLAlchemy can also read your external database, its URL needs to start with “postgresql://”, but you should not change this in the environment variable. Instead,  make an addition to your else statement from the previous step to adjust your `DATABASE_URL` in case it starts with `postgres://`: 

        ```python
        if os.environ.get("DEVELOPMENT") == "True":
            app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
        else:
            uri = os.environ.get("DATABASE_URL")
            if uri.startswith("postgres://"):
                uri = uri.replace("postgres://", "postgresql://", 1)
            app.config["SQLALCHEMY_DATABASE_URI"] = uri
        ```

    - Save all your files and then add, commit and push your changes to GitHub.

Now that you have your database and code in your IDE configured, you will need to add it to a Heroku app using a new environment variable (Config Var) called `DATABASE_URL`. Then your Heroku app will be able to connect to the external database.

## Heroku Deployment

1. **Create a Heroku App**:
    - Log into Heroku.com and click “New” > “Create a new app”.
    - Choose a unique name and region, then click “Create app”.
2. **Configure Environment Variables**:
    - Go to the Settings tab of your app.
    - Click "Reveal Config Vars" and return to your ElephantSQL tab and copy your database URL. 
    - Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL database URL in as the value. Make sure you click “Add”
    - Add each of your other environment variables except DEVELOPMENT and DB_URL from the env.py file as a Config Var. 
    - Reminder to not wrap strings in quotes when adding them as values to Heroku Config Vars.
3. **Deploy from GitHub**:
    - Navigate to the “Deploy” tab of your app.
    - In the Deployment method section select “Connect to GitHub”, search for your repo and click Connect 
    - You can click Enable Automatic Deploys in case you make any further changes to the project. This will trigger any time code is pushed to your GitHub repository.
    - To manually deploy go to the manual deploy section and click deploy branch.
    - Click “Deploy Branch” to start the build process. This will start the build process. 
4. **Initialize Database Tables**:
    - Click “More” > “Run console” in your Heroku app.
    - Type `python3` into the console and run.
    - Enter the Python terminal and create tables with `from your_app import db` and `db.create_all()`.
    - Exit the Python terminal and close the console.

**Note**: If you make changes to your models during development, you will need to make these migrations again in the Heroku console.

The app should be up and running now, so click the “Open app” button.

Congratulations! You have successfully deployed your app to Heroku!

## Local Deployment
You can fork the World flags Quiz repositry by following these steps:

1. Log in or signup to Github.
2. Find the repository for this website.
3. Click the fork button in the top right corner.

You can clone the repository by following these steps:

1. Log in or signup to Github.
2. Find the repository for this website, bookwish.
3. Click on the code button and select whether you would like to clone with HTTPS,SSH or Github CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal, then paste the link you copied in step 3 and Press enter.

# Credits 

## Media 
Background image from [freepik]("https://www.freepik.com/free-photo/blurred-books-library-bookcase_2475569.htm#fromView=search&page=2&position=31&uuid=fe4e52a4-5cc3-4bf7-840d-df2de58fbc26")
## Code 
