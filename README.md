# Poster Prints
(Developer: Jamie Letts)

![Mockup image](documentation/images/device-display.jpg)

[Live webpage](https://poster-prints-8ff329d79ba2.herokuapp.com/)

Poster Prints is an ecommerce poster website allowing users to purchase printed, framed and mounted posters developed for Milestone 4 as milestone project 4 as part of the Code Institute - Level 5 Diploma in Software Development course (Full stack).

- There are two types of users
    - An admin(administrator) user account
    - A regular(shopper) user account
    - When making a payment as a regular user, a test credit card of 4242424242424242 has been set up for the card number
    - For the expiry date, cvc and postal code any series of numbers can be used (once they meet the mimimum values)
<br>


## Table of Contents

[Project Overview](#project-overview)

1. [User Experience](#user-experience)
  * [Strategy](#strategy)
    + [Primary Goal](#primary-goal)
  * [Structure](#structure)
    + [Website pages](#website-pages)
    + [Code Structure](#code-structure)
    + [Database](#database)
      - [Physical database model](#physical-database-model)
      - [Models](#models)
        * [User Model](#user-model)
        * [UserProfile Model](#userprofile-model)
        * [Order Model](#order-model)
        * [OrderLineItem Model](#orderlineitem-model)
        * [Favourites Model](#favourites-model)
        * [Product Model](#product-model)
        * [Category Model](#category-model)
        * [Contact Model](#news-model)
  * [Scope](#scope)
    + [User Stories](#user-stories)
  * [Skeleton](#skeleton)
    + [Wireframes](#wireframes)
  * [Surface](#surface)
    + [Color Palette](#color-palette)
    + [Typography](#typography)
2. [User Experience](#user-experience)
    * [Target Audience](#target-audience)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
    * [User Stories](#user-stories)
3. [Design](#design)
    * [Design Choices](#design-choices)
    * [Colours](#colours)
    * [Fonts](#fonts)
    * [Structure](#structure)
    * [Wireframes](#wireframes)
4. [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Databases](#databases)
    * [Frameworks](#frameworks)
    * [Libraries & Packages](#libraries--packages)
    * [Programs](#programs)
5. [Features](#features)
    * [Base template Features](#base-template-features)
    * [Main Content Features](#main-content-features)
6. [Future Implementations](#future-implementations)
7. [Testing](#testing)
8. [Deployment](#deployment)
  * [Amazon Webservices](#amazon-webservices)
  * [Mongo Database](#mongo-database)
  * [Local Deployment](#local-deployment)
  * [Heroku](#heroku)

9. [Credits](#credits)

10. [Content](#content)

11. [Media](#media)

12. [Acknowledgements](#acknowledgements)

# Project Overview

- This project is a website is for submission as milestone project 4 as part of the Code Institute - Level 5 Diploma in Software Development course (Full Stack).
- The repository on GitHub that contains the website source code and assets is available at the following url: [Code Repository](https://github.com/jamie2210/CI_MS4_PP)
- The website was built to be responsive on desktop, tablet and mobile devices.

_ _ _

# User Experience

_ _ _

## Strategy
### Primary Goal
The primary goal of the website from the site 
owners perspective is as follows:
- To add, edit and delete products with the relevant information (price, description, image, sizes, stock and category) on the website 
- To allow a user make a purchase of the posters on the website
- To display low stocked items
- Allow the user an easy means of contact

The primary goal of the website from a site users perspective is as follows:
- To register for an account on the website and receive an email after successful registration
- To login or logout from the website
- To easily recover my password in case I forget it
- Have a personalised user profile with my delivery, payment information and order history
- View a list of products on the website
- View an individual product detail (price, description, image, sizes, stock (if low) and category)
- To add an item to a shopping bag, and select the quantity and size if applicable
- Complete a purchase of items in a shopping bag
- To sort the list of available products by price and category
- Search for a product by name or description and view the search results
- To have a list of product favourites and to add/delete items from the list

## Project Goals

### User Goals
- Play both games that are fun and engaging.
- Easily find the rules of each game.
- Easily get in touch via a contact form.

### Site Owner Goals
- Create a website with entertaining games.
- Create visually appealing designs throughout.
- Easy navigation throughout.
- Provide a fully responsive and accessible design. 

### Developer Goals
- A clean design that stands out and catches the users attention.
- A website that responds correctly on all devices where design and effectiveness is not hindered on any device.
- An easy to navigate website with clear pathways to specific pages such as rules, each game, home, and contact.

## User Experience

### Target Audience
- Ages 8 to 12.
- It is specific to those who have an in interest in DC comics, particularly Batman.

### User Requirements and Expectations

- A simple and intuitive navigation system.
- Quickly and easily find relevant information.
- Links and functions that work as expected.
- Good presentation and a visually appealing design regardless of device used.
- Easy to follow the games and rules.
- Simple content that the user can follow and understand.
- An easy way to contact the developer for feedback.
- Accessibility.

_ _ _

### __User Stories__

| **Viewing & Navigation** |
|-------------|

| **ID** | **As A** | **I Want To Be Able To** | **So That I Can** |
|-------------|------------|---------------------|-------------------|
| 1 | Shopper | View a list of products | Select some to purchase |
| 2 | Shopper | View specific category of products | Quickly find posters I'm interested in without having to search through all options |
| 3 | Shopper | View Individual product details | Identify the price, description, product rating, product image and available sizes |
| 4 | Shopper | Quickly Identify deals, clearance items and special offers | Take advantage of special savings on products I'd like to purchase |
| 5 | Shopper | Easily view the total of my purchases at any time | Avoid spending too much |

| **Registration & User Accounts** |
|-------------|

| **ID** | **As A** | **I Want To Be Able To** | **So That I Can** |
|-------------|------------|---------------------|-------------------|
| 6 | Site User | Easily register for an account | Have a personal account and be able to view my profile |
| 7 | Site User | Easily login or logout | Access my personal account information |
| 8 | Site User | Easily recover my password incase I forget it | Recover access to my account |
| 9 | Site User | Receive an email confimation after registering  | Verify that my account registration was successful |
| 10 | Site User | Have a personalised user profile | View my personal order history and order confirmations, and save my payment information |

| **Sorting & Searching** |
|-------------|

| **ID** | **As A** | **I Want To Be Able To** | **So That I Can** |
|-------------|------------|---------------------|-------------------|
| 11 | Shopper | Sort the list of available posters | Easily identify the best rated, best priced and categorically sorted products |
| 12 | Shopper | Sort a specific category of poster | Find the best-priced or best-rated poster in a specific category, or sort the products in that category by name |
| 13 | Shopper | Sort multiple categories of products simultaneously | Find the best-priced or best-rated products across the broad categories, such as 'photography' or 'illustrations' |
| 14 | Shopper | Search for a poster by name or description | Find a specific product I'd like to purchase |
| 15 | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available |

| **Purchasing & Checkout** |
|-------------|

| **ID** | **As A** | **I Want To Be Able To** | **So That I Can** |
|-------------|------------|---------------------|-------------------|
| 16 | Shopper | Easily select the size and quantity of a poster when purchasing it | Ensure I don't accidentally select the wrong poster, quantity or size  |
| 17 | Shopper | View items in my bag to purchased | Identify the total cost of my purchase and all items I will receive  |
| 18 | Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchases before checkout |
| 19 | Shopper | Easily enter my payment information | Check out quickly and with no hassles |
| 20 | Shopper | Feel my personal payment information is safe and secure | Confidently provide the needed information to make a purchase |
| 21 | Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes |
| 22 | Shopper | Receive an email confimation after checking out | Keep the confimation of what I've purchased for my records |

| **Admin & Store Management** |
|-------------|

| **ID** | **As A** | **I Want To Be Able To** | **So That I Can** |
|-------------|------------|---------------------|-------------------|
| 23 | Store Owner | Add a poster | Add new posters to print to my store |
| 24 | Store Owner | Edit/Update a poster | Change product prices, descriptions, images and other product criteria |
| 25 | Store Owner | Delete a poster | Remove posters that are no longer for sale |

_ _ _

## Design

### Design Choices

### Colours

<details><summary>Colours Used</summary>
<img src="docs/colour-pallet.png">
</details>

### Fonts

Google fonts were used to import the ‘Anton’ font used with a sans-serif fallback throughout the website:

- [Anton]( https://fonts.google.com/specimen/Anton?query=anton)

### Structure
The page is structured in a user friendly and visually appealing way.

The website consists of 

### Wireframes

<details><summary>Home</summary>
<img src="docs/wireframes/home.png">
</details>

_ _ _

## __Technologies Used__

## Languages
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Javascript](https://www.javascript.com/)
- [Python](https://www.python.org/)
- [Jinja]((https://jinja.palletsprojects.com/en/3.0.x/))

### Databases

- [MongoDB](https://www.mongodb.com/) - Non-relational database used to store the Rave Reviews information.
- [AWS S3](https://aws.amazon.com/s3/) - Services that provides object storage through a web service interface.

### Frameworks

- [Flask](https://pypi.org/project/Flask/) - A micro framework.
- [Materialize 1.0.0.](https://getbootstrap.com/) - Responsive CSS Framework. 

### Libraries & Packages

- [PyMongo](https://pypi.org/project/pymongo/) - Python Driver for MongoDB.

### Programs

- [Pip](https://pypi.org/project/pip/) - Tool for installing python packages.
- [Balsamiq](https://balsamiq.com/) - Used to create wireframes.
- [Git](https://git-scm.com/) - For version control.
- [Github](https://github.com/) - To save and store the files for the website.
- [GitPod](https://www.gitpod.io/) - A cloud development environment.
- [Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot and test features, solve issues with responsiveness and styling.
- [Tiny PNG](https://tinypng.com/) To compress images for use in the readme.
- [Visual Studio Code](https://code.visualstudio.com/) - An integrated development environment from Microsoft.
- [Adobe Suite (Illustrator, Photoshop & InDesign)](https://www.adobe.com/uk/) - Graphic design software.
- [Giphy](https://giphy.com/) - Video to gif conversion website for user story testing section.
- [Font Awesome](https://fontawesome.com/search) - The icons used on the site from font awesome.
- [Diagrams.net](https://app.diagrams.net/) - Flow chart maker used for database models.
- [W3C validator](https://validator.w3.org/) - HTML validation testing.
- [Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) - CSS validation testing.
- [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) - Accessibility testing.
- [jshint](https://jshint.com/) - Javascript validation testing.
- [pep8](http://ww7.pep8online.com/) - Python validation testing.
- [Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) - For performance, accessibility, progressive web apps, SEO analysis of the project code

_ _ _

## __Features__

### __Base Template Features__

* __Favicon__ - I designed the favicon in Illustrator

  ![Poster Prints Favicon](documentation/images/features/favicon.png)

* __Navbar__ - The Navbar is displayed on all pages and changes depending on whether the user is logged in or out or if admin when Organisations is then visible.

  Logged Out Navbar
  - Log In, Register & Home links
  - User Stories covered: 

  ![Logged Out Navbar](documentation/images/features/logged-out-navbar.png)

  Logged In Navbar
  - Home, Profile, Rave Reviews, Leave Reviews & Log Out Links
  - User Stories covered: 

  ![Logged In NavBar](documentation/images/features/logged-in-navbar.png)

  Admin Logged In Navbar
  - Home, Profile, Rave Reviews, Leave Reviews, Organisation & Log Out Links
  - User Stories covered: 

  ![Admin Logged In NavBar](documentation/images/features/admin-logged-in.png)

* __Footer__ 
- The footer is displayed on all pages and includes social links, my GitHub link to this repository, a link to the contact page, the copyright year, and the logo.
- User Stories covered: 

  ![Footer](documentation/images/features/footer.png)

### __Main Content Features__

There are X pages which extend from a base template;

* __Logged Out Home__
* __Logged In Home__
* __Login__
* __Register__
* __Profile__

### Logged Out Home
- Introduction to the site
- Log In or Register Button
- User redirected here if not logged in
- User Stories covered: 

![Logged Out Home](documentation/images/features/logged-out-home.png)

_ _ _

## __Future Implementations__

I am content with what was implemented but if I had more time there are a few bonus features I think could be added;


## __Testing__

The testing information and results for this project are documented in [TESTING.md](TESTING.md)

_ _ _

## __APIs__

### Email JS
1. Create an account at emailjs.com 
2. In the integration screen in the emailjs dashboard, note your userid
3. Create an email service in the Email Services section and note the id
4. Create an email template in the Email templates section and note the id
5. Update the script sendEmail.js, method sendMail with your user id, email service id and email template id.

_ _ _

## __Deployment__

There are a number of applications that need to be configured to run this application locally or on a cloud based service, for example Heroku

### Amazon WebServices
1. Create an account at https://aws.amazon.com
2. Open the IAM application and create a new user
3. Set the AmazonS3FullAccess for the user and note the users AWS ACCESS and SECRET keys
![Iam](documentation/images/iam.png)
4. Open the S3 application and create a new bucket. For the purpose of this application the bucket name is rave-reviews-bucket but this can be updated.
5. With security best practices update the public access and policy bucket to enable the user created and the application access to read/write to the S3 bucket. Consult the AWS documentation if required: https://aws.amazon.com/s3/
![Policies](documentation/images/access.png)
6. The s3 bucket is now updated to be accessed by your application.
7. In necessary route files update the variables BUCKET and image_url with the correct information that you have set up, for example:
<br>
<code>BUCKET = "rave-reviews-bucket"</code><br>
<code>image_url = "https://rave-reviews-bucket.s3.eu-west-1.amazonaws.com/" </code>


### Mongo Database
Mongodb is the database used in the application
1. Create an account at mongodb
2. Create a database cluster
3. Select the cluster, and in the collections section create a database and create 4 collections under the database: raves, organisation, users & comments.
![Database](documentation/images/database.png)
4. In the database access, create a user and allow the user read/write access. Note the username.
5. In the network access tab, allow network access from the ip-address of the application connecting to the database.
6. In the Databases section click Connect, and select connect your application.
7. Note the MONGO_URI, MONGO_DBNAME and user, these parameters are used when deploying locally(env.py file) and deploying on the likes of heroku(config vars).

### Local Deployment
To run this project locally, you will need to clone the repository.
1. Login to GitHub (https://wwww.github.com).
2. Select the repository jamie2210/CI_MS3_RR.
3. Click the Code button and copy the HTTPS url, for example: https://github.com/jamie2210/CI_MS3_RR
4. In your IDE, open a terminal and run the git clone command, for example 

    ```git clone https://github.com/jamie2210/CI_MS3_RR```

5. The repository will now be cloned in your workspace.
6. Create an env.py file in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values<br>
<code>import os</code><br>
<code>os.environ.setdefault("IP", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("PORT", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("SECRET_KEY", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("MONGO_URI", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("MONGO_DBNAME", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("AWS_ACCESS_KEY_ID", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("AWS_SECRET_ACCESS_KEY", TO BE ADDED BY USER)</code>
7. Install the relevant packages as per the requirements.txt file
8. Start the application by running <code>python3 app.py</code>

### Heroku
To deploy this application to Heroku, run the following steps.
1. In the app.py file, ensure that debug is not enabled, i.e. set to True.
2. Create a file called ProcFile in the root directory, and add the line <code>web: python app.py</code> if the file does not already exist.
3. Create a requirements.txt file by running the command <code>pip freeze > requirements.txt</code> in your terminal if the file doesn't already exist.
5. Both the ProcFile and requirements.txt files should be added to your git repo in the root directory.
6. Create an account on heroku.com.
7. Create a new application and give it a unique name.
8. In the application dashboard, navigate to the deploy section and connect your application to your git repo, by selecting your repo.
![Heroku dashboard](documentation/images/heroku_dashboard.png)
9. Select the branch for example master and enable automatic deploys if desired. Otherwise, a deployment will be manual
10. The next step is to set the config variables in the Settings section
![Config vars](documentation/images/config.png)
11. Set key/value pairs for the following keys: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, IP, MONGO_DBNAME, MONGO_URI, PORT, SECRET_KEY
12. Go to the dashboard and trigger a deployment
![Deploy](documentation/images/deploy.png)
13. This will trigger a deployment, once the deployment has been successful click on the "Open App" link to open the app.
14. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue.

_ _ _

## __Credits__

Button display 
https://stackoverflow.com/questions/26837928/how-can-i-hide-a-button-when-scrolled-to-the-top-of-a-page

arrow button
https://stackoverflow.com/questions/61491765/re-positioning-scroll-to-top-button-when-footer-appears-so-it-never-overlaps
https://stackoverflow.com/questions/18053326/how-to-prevent-fixed-button-from-overlapping-footer-area-and-stop-the-button-on

* [Materialize](https://materializecss.com/) is used throughout for CSS styling and some javascript / jquery

* For Help with using AWS S3 buckets and python these were all very useful;

    https://towardsdatascience.com/how-to-upload-and-download-files-from-aws-s3-using-python-2022-4c9b787b15f2

    https://www.twilio.com/blog/media-file-storage-python-flask-amazon-s3-buckets

    https://blog.filestack.com/tutorials/upload-files-amazon-s3-bucket-using-python/

    https://www.youtube.com/watch?v=QSvw50mMQaQ

    https://www.youtube.com/watch?v=7gqvV4tUxmY

*   When adding a password confirmation Javascript feature that only enables the register button once both password entries are the same, this tutorial was very helpful;

    https://www.youtube.com/watch?v=n5E_gxkLo6A

*  For the pagination of the reviews these articles were of great help;

    https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9

    https://pythonhosted.org/Flask-paginate/

    and these tutorials;

    https://www.youtube.com/watch?v=CnBYLXA9zXY

    https://www.youtube.com/watch?v=PSWf2TjTGNY&t=61s

* For the send-email functionality I used some code from the code institute learning platform.

* I used this stack overflow page to better understand exception handling;

  https://stackoverflow.com/questions/33239308/how-to-get-exception-message-in-python-properly

* For a better understanding on how to check for YouTube links in javascript I used this stack overflow thread;

  https://stackoverflow.com/questions/28735459/how-to-validate-youtube-url-in-client-side-in-text-box

_ _ _

## __Content__

- [Font Awesome](#http://fontawesome.com)    
    - The icons used on the site from font awesome.
    
- Fonts<br>
    [Merriweather-sans](#https://fonts.google.com/specimen/Merriweather+Sans)    
    - The text font Merriweather Sans is from Google fonts
  
  [PhillySans](#https://www.dafont.com/philly-sans.font)
    - PhillySans was taken as a free font for personal use from dafont.

_ _ _ 

## __Media__

All images are either photos taken by me or uploaded by users of the site

All logos are designed by myself

_ _ _

## __Acknowledgements__

I would like to take the opportunity to thank;

- My mentor, Mo Shami, for his excellent feedback, advice support and guidance throughout.
- Tutor support from Code Institute for their swift response.
- The slack community of coders for immediate and helpful response.
- WAES College and my Tutor Michael for their support and help throughout.
- My friends and family who have created accounts and tested the site and given valid feedback helping me fix bugs I was otherwise unaware of.