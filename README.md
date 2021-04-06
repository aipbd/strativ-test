# strativ-test


#### Environment Variables (Pre-requisites to run the project)
* Environment variables will be maintained: .env
* Rename the __env directory to .env
* Type `mv __env .env`

#### Project Run Instructions:
* Open Terminal
* Go to project directory
* Type `docker-compose -f local.yml up --build`. Append the args `-d` to have the docker build and run the project in the background
* This docker-compose file is designed only for local development purpose, not for production.

#### Adding Countries Instructions:
* Open Terminal
* Go to project directory
* Type `docker-compose -f local.yml exec web bash -c "python manage.py datafeeder"`
