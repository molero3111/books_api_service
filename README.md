# Books API service (Python / Django) 

## Description

Books API service offering CRUD actions on users, authors, and books.
The project simulates a service (microservices pattern) that interacts 
with existing books api project: 
https://github.com/molero3111/books_api.git , it creates new services called
books-api-service and books-celery for the tasks queue, by leveraging the use of
the same network (books_api_network) this project can connect and reuse
books-db and books-redis services which are already set up by the project
mentioned above.

##  Runtimes, engines, tools and requirements

- **Language**: Python
- **Framework**: Django
- **Packages:**: 
    - laravel/sanctum (For JWT authentication)
    - maatwebsite/excel (For xlsx file generation)
    - djangorestframework
    - celery (Task queue manager)
    openpyxl (xlsx generator)
    requests (For sending requests to external APIs)
- **Database**: PostgresSQL
- **Cache**: Redis (For job queue)

## Run Project locally

Before starting make sure you already set up books_api project (https://github.com/molero3111/books_api.git)
since you will need to have books_api_network, and containers books-db 
and books-redis up and running, and at least one admin user, which is created with a laravel
custom command, for this API service to work properly.

1. Clone the repository:

```bash
git clone https://github.com/molero3111/books_api_service.git
```

2. cd into books_api_service repository:

```bash
cd books_api_service/
```

3. Switch to staging branch:
```bash
git checkout staging
```
You may stay on development, but staging branch will have the most stable version.

4. Create .env and .env.secrets:

```bash
cp .env.example .env
cp .env.secrets.example .env.secrets
```

5. Build and run docker containers:

```bash
docker compose -p local-service up --build
```

## Test project

After following these steps you can access home page at http://localhost:8001.

### Optional

If you would like to execute django commands and perhaps if using pycharm IDE for development,
you need to create a python virtual env and install packages on your host machine, 
follow these steps: 

1. Create virtual env:

```
python3 -m venv venv
```

2. Activate virtual env:

```
source venv/bin/activate
```

3. Install packages:

```bash
pip install -r requirements.txt
```

For further testing and usage, follow documentation bellow to send requests to the API service.

## Documentation

### API
The API documentation is on postman, you may find it here: 
https://www.postman.com/molero3111/workspace/books-api/documentation/9720967-ecb6b09c-1a10-41f0-9c1e-ddc57924699e

There are two documentation, follow the books API Service documentation,
which is the documentation for the API of this project.

### Project insights
- For didactic purposes, a task queue is set up with celery, the only tasks it processes in the project
is the update of published_books in author model, using django signals and events as well.
You can see the signals and events for the Book model in the signals.py file located in book app
you can also view the update_published_books task in tasks.py also located in books app.
- There is an export data app which contains logic to generate and download a xlsx file with
all the data in Author and Book models
- All routes are protected by reusing JWT generated on books API project using laravel sanctum,
there a class called IsValidToken in the permissions.py file located in authentication app, said
class is used on users, authors, and books views by setting the ViewSet class attribute permission_classes,
which protects and authorizes the routes.