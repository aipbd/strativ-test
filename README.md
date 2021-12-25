# strativ-test


#### Environment Variables (Pre-requisites to run the project)
* Environment variables will be maintained: .env
* Copy the __env directory to .env
* Type `cp -r __env/ .env/`

#### Project Run Instructions:
* Open Terminal
* Go to project directory
* Type `docker-compose -f local.yml up --build`. Append the args `-d` to have the docker build and run the project in the background
* This docker-compose file is designed only for local development purpose, not for production.

#### Adding Countries Instructions:
* Open Terminal
* Go to project directory
* Type `docker-compose -f local.yml exec web bash -c "python manage.py datafeeder"`


#### Entering Python Shell:
* Open Terminal
* Go to project directory
* Type `docker-compose -f local.yml exec web bash`
* Next any django command can be used, such as: `python manage.py shell` or `python manage.py createsuperuser` etc.


#### Project Requirements:

Python Developer Assignment
In this assignment, you need to fetch data from a source, format them, make them
available by creating simple rest APIs and display the information in a simple secured
web page. Once you complete the assignment you’ll have a simple web page using which
users can find information about different countries. Your APIs should support HTTP
clients. People should be able to use CURL, Postman or any other REST client to interact
with your APIs. Commit your work according to each phase.

Phase 1
You will start by consuming data from this API https://restcountries.eu/rest/v2/all . Here
you can find information about different countries. Start a new django project, create a
django app and design necessary models where you can store these information.
Write a script to fetch these data and store it into the newly created database.
Don’t forget to commit your work!

Phase 2
In this phase, you need to write some RESTful APIs based on the models you’ve created
in the previous phase. Here’s the list of APIs you need to build.
name, alphacode2, capital, population, timezone, flag, languages and neighbouring
countries.
1. List of all countries
2. Details of an specific country
3. Create a new country
4. Update an existing country
5. Delete an existing country
6. List of neighbouring countries of an specific country
7. List of countries who speaks the same language based on a specific language
8. Searching a country by its name (should be able to search partial name)
Don’t forget to commit your work!

Phase 3
In this phase you need to design a simple html template where you can show the
information about the countries. You should display a table where we can see the list of
countries and their respective information.
name, alphacode2, capital, population, timezone, flag
There should be a search field where I can search a country by its name. Also, for each
country there should be a detail button. By clicking the button we should see a detail page
where we can see the list of their neighbouring countries and languages they speak.
You can use any front-end technology you want. We just want to see a basic HTML page,
but using a CSS framework like Bootstrap or Bulma will be highly appreciated.
For displaying data you can consume the existing APIs if you want to. Even you can use
Django’s form template approach for getting data in the views and passing it to the
template for showing it, if that's preferable for you.
Don’t forget to commit your work!

Phase 4 (Final Phase)
In the last phase, you need to establish a way to authenticate so that your APIs are not
accessible by anyone. Modify your existing code base so that all your APIs are safe.
Create a new user using django’s default User model (django.contrib.auth.models.User)
Create a login page so the registered users can see the country list page by logging in.
Deliverables
You should push your code to a public git repository like github, gitlab or bitbucket with
clear instructions about how to run your program.

Special instructions
● You must use Python/Django to solve this problem.
● You are free to use any third party library or framework if you want. Just make
sure that you have added the dependency of those to your repository and you have
given the instruction on the readme file regarding how to run your program
including the libraries. The readme should contain any special instruction for
installation and configuration of your application.
● Make sure your instructions are clear. You should include the specific version of
the libraries, databases etc. Following your instructions, anyone should be able to
set up your project in a new machine.
● Commit early and often. Don’t commit everything after finishing the assignment.
By looking into your commit message we will try to get an idea how you
approached the problem.
