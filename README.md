# MojoYoga

![MojoYoga reposive screenshot](./documentation/images/MojoYogaRepsonsive.png)

## Introduction 

MojoYoga is a website designed for people who have been on a surf and yoga retreat to leave a photo and review of their experience. Mojo yoga has been developed for my final project of Code Institute's Full-Stack Developer Bootcamp - This project focuses on Django and Bootstrap frameworks, Database manipulation and CRUD (Create, Read, Update and Delete) functionality. It is for educational purposes only.

Live site: [MojoYoga](https://mojoyoga-f4267f7b0b57.herokuapp.com/)

<hr>

## Table of Contents

- [MojoYoga](#MojoYoga)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
- [UX - User Experience](#ux---user-experience)
  - [Design Inspiration](#design-inspiration)
    - [Colour Scheme](#colour-scheme)
    - [Font](#font)
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
  - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [MoSCoW Prioritization](#moscow-prioritization)
    - [Sprints](#sprints)
  - [User Stories](#user-stories)
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
  - [Skeleton \& Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
    - [Security](#security)
- [Features](#features)
  - [User View - Registered/Unregistered](#user-view---registeredunregistered)
  - [CRUD Functionality](#crud-functionality)
  - [Feature Showcase](#feature-showcase)
  - [Future Features](#future-features)
- [Technologies \& Languages Used](#technologies--languages-used)
  - [Libraries \& Frameworks](#libraries--frameworks)
  - [Tools \& Programs](#tools--programs)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Cloudinary API](#cloudinary-api)
  - [Elephant SQL](#elephant-sql)
  - [Heroku deployment](#heroku-deployment)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

## Overview

MojoYoga is a surf and yoga retreat review site with details about various retreats and the retreat owners storys. Users have the option to:

- Sign up and create an account
- Leave a review with 0-5 star rating
- Optionally add a photo to their review
- Update (Edit) or Delete their review
- View others reviews
- Learn about surf and yoga retreats

Mojo Yoga has full responsiveness on different screen sizes and is accessible on all screensizes. It is desgned to add another element to help the retreat gain traction and interest by allowing users of the site to see reviews.

# UX - User Experience

## Design Inspiration

I was always excited to work on a full stack project from the moment I enrolled in the course, throughout the course my idea for the Capstone project changed many times. I initally wanted to create a JavaScript game with leadersboards and profiles, however as each project went by I realised that creating a functional MVP should always come first and due to time restraints it may put too much pressure on myself. Having gone through the walkthrough project in the course in which I made a blog site it gave me the inspiration of creating a new element to my mothers website - A page dedicated to reviews and somewhere to sign up and make an account. Whilst adding my own touch and having permission to use this site as a base I knew this would be perfect to practice my HTML, CSS and JS skills whilst adding CRUD functionality to create a full stack app and take some pressure off with finding a other sites for inspiration.

Joanna and Mohammed's Website: [MojoYogaMorocco](https://www.mojoyogamorocco.com/)

### Colour Scheme

Having access to a logo and website that already works very well I used these colours as a basis to choose my colours. Being a surf and yoga retreat; blue and calming colours were always a must have and I wanted a focus on the photos that people would upload. One of the photos from Morocco adds the perfect hero image that also elminates the need to use too many colours.

- Navbar rgb(134, 204, 227)
- Footer #5A7D9A
- Welcome page #f5f3dc

I thought about using something other than white for the majority of the text but after trial and error white fit the best so I stuck with that. For text that is a link I used a contrasting orange #FFA500 to stand out and make it obvious this was a link.

### Font

I used [Google Fonts](https://fonts.google.com/), importing 'Funnel Display' and 'Roboto'. Funnel Display is used for the welcome page as it allows the heading stand out and draw people in. Roboto is used for all other text as I think it is easy to read and modern looking.

# Project Planning

## Strategy Plane

The goal was to build an app where users could leave a review for a service (Yoga and Surf retreats). This involved focusing on CRUD functionality to create a smooth user experience to sign up, leave a review, edit and delelte reviews. This made the initial start to the project more manageable as it created bitsized goals to complete. As I began planning and design prep work, It became clear to me that by going back to the basics I would be able to achieve this goal faster than expected which would give me more time in the future to increase the user experience.

### Website Goals

- Create a welcoming and calming website with relevant informaiton on retreats
- Easy to find background information on the retreat
- Smooth layout with easy-to-use navigation bar
- Simple design to impliment CRUD functionailty
- UX maintained on all screensizes
- Reviews page for users to see others experiences

## Agile Methodologies - Project Management

MojoYoga was my second project to implement Agile. With some experine in using Agile in a group hackathon a few weeks before beginning this project I knew it would be useful to keep on track and progress. I used [Github Projects Board](https://github.com/Guysteeleperkins/mojoyoga/projects) to plan and complete user stories. This helped keep motivation up as I could "See" the progress being made as I moved items from "To Do" to "In Progress" to "Complete".

### MoSCoW Prioritization 

I used the MoSCoW Prioritization method for MojoYoga:

- **Must Have**: These are the non-negotiable, essential requirements that are critical to the success of the project. Without them, the project cannot be considered complete or successful.

- **Should Have**: These are important but not critical requirements. They add significant value but can be delayed if necessary, as long as they are delivered in the near future.

- **Could Have**: These are nice-to-have features or tasks that would enhance the product but are not vital for its core functionality. If time or resources are tight, these can be omitted without major consequences.

- **Won't Have**: These are requirements that are agreed upon as out of scope for the current project cycle. They may be reconsidered in the future but will not be addressed in the current iteration.

## Sprints

I had 14 working days to complete this project and had learned from previous projects that sprints worked effectively, using my GitHub project board filled with user stories I had created I would do very small sprints to complete the user story. If I felt this had been done quickly and I didn't need a break I would add another and keep going. Depending on the day and energy levels I would split larger tasks with things like testing and styling as I went to mix up my work to keep motivation high. I found that after the first 3 days I had comnpleted CRUD functionality and changed my spints to regular work periods with a conistent 5-10 minute break every 1-2 hours. This kept me working effeciently and productively.

### User Stories

## Must Haves

| **User Story**                                                                                                                                                     | **Acceptance Criteria**                                                                                                                                                                                                                                                                              | **Priority**  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| As a **user**, I must be able to **securely sign up and log in using AllAuth** so that I can **access the site and leave reviews**.                                | - Users can sign up using email or social authentication methods (e.g., Google). <br>- Users can log in and are redirected to the homepage/dashboard. <br>- If login fails, an error message is displayed. <br>- Users can reset their password via email.                                             | **MUST HAVE** |
| As a **logged-in user**, I must be able to **write a review for a retreat** so that I can **share my experience with others**.                                     | - Logged-in users can access a review form for a specific retreat. <br>- The form includes fields for text description and rating. <br>- The review is saved and displayed publicly on the retreat’s page upon submission. <br>- Users receive a success message after submission.                   | **MUST HAVE** |
| As a **user**, I must be able to **view all submitted reviews** so that I can **learn from others' experiences**.                                                 | - All reviews are displayed publicly, showing reviewer name, rating, and text. <br>- Users can sort reviews by criteria like rating, retreat name, or date. <br>- Reviews can be filtered by retreat type or rating.                                                                                  | **MUST HAVE** |
| As a **logged-in user**, I must be able to **update my own review** so that I can **correct or change my feedback after submitting it**.                           | - Logged-in users can edit their reviews via their profile or a "My Reviews" page. <br>- Users can edit both the text and rating of their review. <br>- Changes are saved, and the updated review is displayed publicly with an updated timestamp.                                                   | **MUST HAVE** |
| As a **logged-in user**, I must be able to **delete my own review** so that I can **remove it if I no longer want it to be visible**.                              | - Logged-in users can delete reviews via their profile or "My Reviews" page. <br>- Deleted reviews no longer appear publicly, and a success message is shown (e.g., "Your review has been deleted").                                                                                                  | **MUST HAVE** |
| As a **user**, I must be able to **navigate the website easily** so that I can **find the information and features I need without confusion**.                    | - Clear navigation menu with intuitive labels (e.g., Home, Reviews, About, Profile). <br>- Navigation is consistent across all pages. <br>- The design is responsive, adjusting layout appropriately for mobile, tablet, and desktop views.                                                          | **MUST HAVE** |


## Should Haves

| **User Story**                                                                                                                | **Acceptance Criteria**                                                                                                                                                                | **Priority**  |
|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| As a **user**, I can **interact with the site effortlessly** so that I can **accomplish my tasks without confusion**.         | - Form inputs (e.g., review submission, signup) are clearly labeled with instructions if needed. <br>- Error messages and validation are clear and helpful (e.g., "Please enter a valid email address"). <br>- Buttons and links have clear hover or active states to indicate interaction. | **MUST HAVE** |
| As a **user**, I am **visually engaged with the website design** so that my experience is more enjoyable.                       | - High-quality images or icons representing reviews and key features. <br>- Consistent use of brand colours that complement the overall design. <br>- Clean and modern aesthetic that aligns with the theme of wellness and relaxation. | **MUST HAVE** |
| As a **logged-in user**, I can **rate my experience with a 1 to 5 star or numeric scale** so that I can **provide more meaningful feedback**. | - User can rate a retreat with 1 to 5 stars when submitting a review. <br>- Rating is visually represented next to the review text.                                                   | **MUST HAVE** |

## Could Haves

| **User Story**                                                                                                                  | **Acceptance Criteria**                                                                                                                                                                     | **Priority**  |
|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| As a **logged-in user**, I can **view and manage a personal profile page** so that I can **see and edit my reviews and update my personal information**. | - User can view their profile, including all past reviews they’ve submitted. <br>- User can update their name, email, and password from their profile page. <br>- User can delete or edit their reviews directly from their profile page. | **MUST HAVE** |
| As a **user**, I can **comment on other users' reviews** so that I can **ask questions or provide additional feedback**.         | - Users can comment on reviews to ask questions or offer insights. <br>- Each comment is visible below the associated review. <br>- Comment section supports threaded replies for better interaction. | **MUST HAVE** |
| As a **user**, I can **"Like" or "Dislike" reviews** so that I can **indicate helpfulness or agreement**.                          | - Users can click a thumbs-up or thumbs-down icon on reviews to show if they find the review helpful.                                                                                         | **MUST HAVE** |
| As a **user**, I can **access a booking page** so that I can **show interest in an upcoming retreat I want to attend**.            | - A page dedicated to show various upcoming events (retreats). <br>- A button that shows that the user is interested (e.g., a thumbs-up). <br>- Thumbs-up has a numerical value so other users can see how many people are interested in this event. | **MUST HAVE** |

## Won't Haves

| **User Story**                                                                                                          | **Reason for Exclusion**                                                                                                                                                                                              | **Priority**  |
|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| As a **user**, I can **search and filter reviews** so that I can **find the relevant feedback**.                         | Search feature can be considered in future versions, but it’s not necessary for the MVP (Minimum Viable Product).                                                                                                      | **WON'T HAVE**  |
| As a **non-English speaking user**, I can **have the website available in my native language** so that I can **use it more comfortably**. | Language support can be considered in future versions, but it’s not necessary for the MVP (Minimum Viable Product).                                                                                                   | **WON'T HAVE**  |
| As a **user**, I can **book a retreat directly through the website after reading reviews** so that I can **attend the retreat**. | Booking functionality is not a core part of this version of the app. It's something to consider for future expansion.                                                                                                | **WON'T HAVE**  |


## Scope Plane

Main features:
- A calming and inviting website that fulfils user needs
- Responsive website for users on all devieces
- User Authentication
- User Profile creation and editing
- Leave a review feature with full CRUD functionality

Due to a lot of new content that had been covered in the course just a few weeks before this project began I wanted to make sure that I didn't overreach and set my goals too high. Due to the new technologies such as Python, Django, Databases and Cloudinary that I had covered recently and were still new to me, I took this project as a learning objective as well as building a fully functional app. 

## Structural Plane

Having had a website to base mine off this was a very easy step. I already had a good basis of what works regarding to where items would be positioned and how they would fit into each other to create a smooth experience for the user. I wanted to keep things simple and as I completed tasks it would free up time to add some of the "Could have" features.

NavBar - Having had some difficulties with this before I knew how to start it straight away. Bootstrap provides an easy to use NavBar which is easily manipulated with custom CSS. In prevous projects had a experiemented with different kinds of buttons within the navbar but the simple text with some button hightlights when hovering always looked the best in my opinion - best not to over complicate it!

Hero Image - As well as the website I was using for inspirations and some previous projects that met the criteria for passing a large hero image that spanned over the whole website on all pages really stuck out as a nice feature and it kept consistency throughout. 

Reviews / Review Details / Forms - Also inspired from another project that was shown to our cohort I loved the background colour of black with the opacity set to 0.5 to let the hero image show through but to create an obvious division between the background and the cards. This was kept consistent throughout the website and looks very smart.

## Skeleton and Surface Planes

### Wireframes

The wireframes for MojoYoga were used using Balsamiq Wireframes, this allowed me to get onto "paper" a quick and easy template on what I wanted the website to look like. I kept these very basic as the main priority was CRUD functionaility, however they kept a good base for me to work towards. I designed what a mobile, tablet and desktop would look like with my Welcome Page, Form Page (where log in, register etc would all keep the same look), and a Reviews page and how these would change with screen size.

<details open>
    <summary>Mobile Wireframe</summary>  
    <img src="documentation/images/mobilewf.png">  
</details>

<details open>
    <summary>Tablet Wireframe</summary>  
    <img src="documentation/images/tabletwr.png">  
</details>

<details open>
    <summary>Desktop Wireframe</summary>  
    <img src="documentation/images/desktopwr.png">  
</details>

### Security 

**AllAuth**  

Django AllAuth is an installable framework that takes care of the user registration and authentication process. Authentication was needed to determine when a user was registered or unregistered and it controlled what content was accessible on MojoYoga. The setup of AllAuth included:

- installing it to my workspace dependencies
- adding it to my INSTALLED_APPS in my settings.py
- sourcing the AUTHENTICATION_BACKENDS from the AllAuth docs for my settings.py
- adding its URL to my projects 'urls.py'
- run database migrations to create the tables needed for AllAuth

**CSRF Tokens**
Cross-Site Request Forgery tokens are included in every form to help authenticate the request with the server when the form is submitted. Without CSRF the site can be vunerable to attackers manipulation and theft of users data.

# Features

## User View

It is important for MojoYoga to accessible for un registered users, anyone must be able to see the content and see other peoples reviews to help the user decide on whether they would like to go on a retreat. Non-registered users would be prompted to create an account if they clicked on "leave a review" in the navbar and would only be able to leave one if signed in. Only users who created a review can edit and delete their review.

Users also recieve a message depenant on their action. Logging in, Signing up, creating a review, editing a review and deleting a review give a small message after using the features of the site. 

## CRUD Functionality

Users are able to Create, Read, Update and Delete their shared information on MojoYoga. The reviews section is the only CRUD functionality on the website due to it being based on reviews.


## Feature Showcase

<details open>
    <summary>Welcome Page</summary>  
    <img src="documentation/images/welcomepage.png" width="50%" height="50%">  
</details>

<details open>
    <summary>About Page</summary>  
    <img src="documentation/images/aboutpage.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Gallery Page</summary>  
    <img src="documentation/images/gallerypage.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Reviews Page</summary>  
    <img src="documentation/images/reviewspage.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Leave a Review Page</summary>  
    <img src="documentation/images/leaveareview.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Leave a Review Page (Not logged in)</summary>  
    <img src="documentation/images/leavereview-notloggedin.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Edit Review</summary>  
    <img src="documentation/images/editreview.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Delete Modal</summary>  
    <img src="documentation/images/modaldelete.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Sign Up Page</summary>  
    <img src="documentation/images/registerpage.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Login Page</summary>  
    <img src="documentation/images/signin.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Log out Page</summary>  
    <img src="documentation/images/logout.png" width="50%" height="50%">  
</details>

## Future Features

Due to time constraints I could not impliment some of my "Could Haves" from my [Github Projects Board](https://github.com/Guysteeleperkins/mojoyoga/projects). 

These include:
  - Review Likes/Dislike
  - Booking Page
  - User Profile
  - Review Comments
  - Retreat booking integration
  - Multilingual Support
  - Search and filter Reviews

These features I believe are within my capabilties to complete, therefore after my project has been reviewed and tested I will be impliementing these in my own time. I very much look forward to adding more custom models to test my knowledge and increase my experience.


# Technologies & Languages Used 

  - HTML
  - CSS
  - JavaScript
  - Python
  - [Git](https://git-scm.com/) used for version control.
  - [Github](https://www.github.com) used for online storage of codebase and Projects tool.
  - [Gitpod](https://www.gitpod.io/) as an online, cloud-based IDE for development.
  - Balsamiq Wireframes - Wireframe creation.
  - [Django](https://www.djangoproject.com/) was used as the Python framework for the site.
  - [Cloudinary](https://cloudinary.com/) was used for cloud media storage of user uploaded images.
  - PostgreSQL 
  - [Heroku](https://www.heroku.com) was used to host the MojoYoga application.

# Libraries and Frameworks

- Bootstrap v5.0.1
- asgiref v3.8.1
- cloudinary v1.41.0
- dj-database-url v0.5.0
- dj3-cloudinary-storage v0.0.6
- Django v4.2.16
- django-allauth v0.57.2
- gunicorn v20.1.0
- oauthlib v3.2.2
- psycopg v3.2.3
- PyJWT v2.10.0
- python3-openid v3.2.0
- requests-oauthlib v2.0.0
- sqlparse v0.5.2
- urllib3 v1.26.20
- whitenoise v5.3.0

## Tools and Programs

 - [CodeInstitute](<https://learn.codeinstitute.net/dashboard>) - Using walkthrough projects and lessons
 - [ChatGPT](<https://chatgpt.com/>) - To assist with learning and debugging
 - [GitHub](<https://github.com/>) _ Project board and linking with Herko
 - [Heroku](<https://dashboard.heroku.com/apps>) - Hosting this full-stack project
 - Balsamiq Wireframes - App to create wireframes
 - [Google](<https://www.google.com/>) - To assist with learning and debugging

 
 # Testing

 ## Manual Testing

 Throughout the project I was constantly testing CRUD functionality by using an account I had created myself to check if everything worked. This helped extremely well to debug when things did not work as expected. Below is screenshots following a test run.

<details open>
    <summary>Sign Up</summary>  
    <img src="documentation/images/testsignup.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Sign Up Message</summary>  
    <img src="documentation/images/testsignupmessage.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Leave a Review</summary>  
    <img src="documentation/images/testleavereview.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Review Detail</summary>  
    <img src="documentation/images/testreview.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Review Edit</summary>  
    <img src="documentation/images/testedit.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Review Edit</summary>  
    <img src="documentation/images/testedit2.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Review Edited</summary>  
    <img src="documentation/images/reviewedited.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Delete Review</summary>  
    <img src="documentation/images/testdelete.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Review Deleted</summary>  
    <img src="documentation/images/testdelete2.png" width="50%" height="50%">  
</details>

<details open>
    <summary>Log out Page</summary>  
    <img src="documentation/images/testlogout.png" width="50%" height="50%">  
</details>


 ## Validators

 During the testing phase I had very few valiation errors, usually it was some trailing tags in the HTML and missing whitespace for Python.

 ### HTML

 Every Page was checked with [ValidatorW3](<https://validator.w3.org/>) and returend no errors found. The screenshot below shows what all pages showed

  <details open>
    <img src="documentation/images/HTML.png" width="50%" height="50%">  
  </details>

 ### Python

 <details open>
    <img src="documentation/images/python1.png" width="50%" height="50%">  
</details>

<details open>
    <img src="documentation/images/python2.png" width="50%" height="50%">  
</details>

<details open>
    <img src="documentation/images/python3.png" width="50%" height="50%">  
</details>

<details open>
    <img src="documentation/images/python4.png" width="50%" height="50%">  
</details>

<details open>
    <img src="documentation/images/python5.png" width="50%" height="50%">  
</details>

<details open>
    <img src="documentation/images/python6.png" width="50%" height="50%">  
</details>

<details open> 
    <img src="documentation/images/python7.png" width="50%" height="50%">  
</details>

### JavaScript

<details open> 
    <img src="documentation/images/js1.png]" width="50%" height="50%">  
</details>

<details open>
    <img src="documentation/images/js2.png" width="50%" height="50%">  
</details>

<details open>
    <img src="documentation/images/js3.png" width="50%" height="50%">  
</details>

### CSS

<details open> 
    <img src="documentation/images/css.png" width="50%" height="50%">  
</details>


 # Deployment

 ## Connecting to GitHub  

To begin this project from scratch, you must first create a new GitHub repository using the [Code Institute's Template](https://github.com/Code-Institute-Org/ci-full-template). This template provides the relevant tools to get you started. To use this template:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the purple CodeAnywhere (if this is your IDE of choice) button to generate a new workspace.

## Django Project Setup

1. Install Django and supporting libraries: 
   
- ```pip3 install 'django<4' gunicorn```
- ```pip3 install dj_database_url psycopg2```
- ```pip3 install dj3-cloudinary-storage```  
  
2. Once you have installed any relevant dependencies or libraries, such as the ones listed above, it is important to create a **requirements.txt** file and add all installed libraries to it with the ```pip3 freeze --local > requirements.txt``` command in the terminal.  
3. Create a new Django project in the terminal ```django-admin startproject mojo_yoga .```
4. Create a new app eg. ```python3 mangage.py startapp booking```
5. Add this to list of **INSTALLED_APPS** in **settings.py** - 'booking',
6. Create a superuser for the project to allow Admin access and enter credentials: ```python3 manage.py createsuperuser```
7. Migrate the changes with commands: ```python3 manage.py migrate```
8. An **env.py** file must be created to store all protected data such as the **DATABASE_URL** and **SECRET_KEY**. These may be called upon in your project's **settings.py** file along with your Database configurations. The **env.py** file must be added to your **gitignore** file so that your important, protected information is not pushed to public viewing on GitHub. For adding to **env.py**:

- ```import os```
- ```os.environ["DATABASE_URL"]="<copied URL from https://dbs.ci-dbs.net/>"```
- ```os.environ["SECRET_KEY"]="my_super^secret@key"```
  
For adding to **settings.py**:

- ```import os```
- ```import dj_database_url```
- ```if os.path.exists("env.py"):```
- ```import env```
- ```SECRET_KEY = os.environ.get('SECRET_KEY')``` (actual key hidden within env.py)  

9. Replace **DATABASES** with:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```

10. Set up the templates directory in **settings.py**:
- Under ``BASE_DIR`` enter ``TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)``
- Update ``TEMPLATES = 'DIRS': [TEMPLATES_DIR]`` with:

```
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')
```

- Create the media, static and templates directories in top level of project file in IDE workspace.

11. A **Procfile** must be created within the project repo for Heroku deployment with the following placed within it: ```web: gunicorn mojo_yoga.wsgi```
12. Make the necessary migrations again.

## Cloudinary API 

Cloudinary provides a cloud hosting solution for media storage. All users uploaded images in the MojoYoga project are hosted here.

Set up a new account at [Cloudinary](https://cloudinary.com/) and add your Cloudinary API environment variable to your **env.py** and Heroku Config Vars.
In your project workspace: 

- Add Cloudinary libraries to INSTALLED_APPS in settings.py 
- In the order: 
```
   'cloudinary_storage',  
   'django.contrib.staticfiles',  
   'cloudinary',
```
- Add to **env.py** and link up with **settings.py**: ```os.environ["CLOUDINARY_URL"]="cloudinary://...."``` 
- Set Cloudinary as storage for media and static files in settings.py:
- ```STATIC_URL = '/static/'```
```
  STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'  
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]  
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')‌  
  MEDIA_URL = '/media/'  
  DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

## PostgreSQL

A new database instance can be created on [PostgreSQL from Code Instiute](https://dbs.ci-dbs.net/) for your project. However this can only be used as a student with Code Institute. 

Other option: [Elephant SQL](https://www.elephantsql.com/)

- Choose a name and select the **Tiny Turtle** plan, which is free.
- Select your Region and the nearest Data Center to you. 
- From your user dashboard, retrieve the important 'postgres://....' value. Place the value within your **DATABASE_URL**  in your **env.py** file and follow the below instructions to place it in your Heroku Config Vars.


## Heroku deployment

To start the deployment process , please follow the below steps:

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
3. Enter an app name and choose your region. Click '**Create App**'. 
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your: 
   
   - **CLOUDINARY_URL**: **cloudinary://....** 
   - **DATABASE_URL**:**postgres://...** 
   - **DISABLE_COLLECTSTATIC** of value '1' (N.B Remove this Config Var before deployment),
   -  **PORT**:**8000**
   -  **SECRET_KEY** and value  
  
5. Add the Heroku host name into **ALLOWED_HOSTS** in your projects **settings.py file** -> ```['herokuappname', ‘localhost’, ‘8000 port url’].```
6. Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that **DEBUG=False**, save your project, add the files, commit for initial deployment and push the data to GitHub.
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
9.  Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Manual' deployment method. Click '**Deploy Branch**'.
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. **DISABLE_COLLECTSTATIC**  may be removed from the Config Vars once you have saved and pushed an image within your project, as can **PORT:8000**.


# Credits

## Code

The following complemented my learning for this project.

 - [Code Institute's](https://codeinstitute.net/ie/) Learning Content.
 - [Django Docs](https://www.djangoproject.com/)
 - [Bootstrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
 - [Code Institute's](https://github.com/Code-Institute-Org>) Blog walkthrough

### README

 - [Github](<https://github.com/amylour/FreeFido_v2/blob/main/README.md?plain=1>) - Amy Lour's FreeFido Project README was used as a basis for this README

## Media

All the media used in this website was sourced from my Mum (Joanna Steele-Perkins) which was also used on her website which this was based off
[MojoYogaMorocco](<https://www.mojoyogamorocco.com/>)


## Acknowledgements

  - Huge thankyou to my Mum who gave me the permission to base my project off her website and use photos she has taken over the years
  - Many thanks to all my friends who helped during testing and pointed out any bugs
  - Thank you to my mentor Alex and everyone in my cohort at CodeInstitute for always being helpful and supportive
  - Thanks to my housemates for providing me with coffee and snacks throughout the most stressfull times of the course





