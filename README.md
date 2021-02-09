# Flask React Mongo Boilerplate

A Boilerplate using Flask, flasgger, and MongoDB for the backend and Webpack and React for the frontend.

The official home of this repository is at [https://gitlab.com/torrentofshame/flask-react-mongo-boilerplate](https://gitlab.com/torrentofshame/flask-react-mongo-boilerplate).

## Contents

- [Quick Start](#quick-start)
- [Dependencies](#dependencies)
- [Application Structure](#application-structure)

## Quick Start

**Requirements**

- Docker
- Docker Compose

1. Clone the project

`git clone https://gitlab.com/torrentofshame/flask-react-mongo-boilerplate.git`

2. Move to `flask-react-mongo-boilerplate`

`cd flask-react-mongo-boilerplate`

3. Run it

### In Production:

`make produp`

`make proddown`

### In Development:

`make devup`

`make devdown`

### Backend Only

1. Clone the project

`git clone https://gitlab.com/torrentofshame/flask-react-mongo-boilerplate.git`

2. Move to `flask-react-mongo-boilerplate`

`cd flask-react-mongo-boilerplate`

3. Run it

#### With Docker:

**Requirements**

- Docker
- Docker Compose

Comment out `frontend-service` in `docker-compose.dev.yml`

Run

`make devup`

`make devdown`

#### Without Docker:

**Requirements**

- Python 3.9
- MongoDB Server

Move to `backend`

`cd backend`

Create a file named `.env` and add the following content, replacing necessary values.

```
APP_SETTINGS=server.config.DevelopmentConfig
MONGO_URI=mongo://username:password@mongodb-uri:27017/yourdatabase
SECRET_KEY=vivalapluto
MAIL_SERVER=smtp.mailserver.com
MAIL_PORT=587
MAIL_USERNAME=myemail@myemail.com
MAIL_PASSWORD=12345
MAIL_SENDER=myemail@myemail.com
```

Install Python Dependencies

`pip install -r requirements.txt`

Run the server

`python -m server --host=0.0.0.0 --port=5000`

## Dependencies

| Frontend | Backend |
|---|---|
| react | Flask==1.1.2 |
| react-dom | Flask-Bcrypt==0.7.1 |
| webpack | Flask-Cors==3.0.10 |
| webpack-cli | Flask-Mail==0.9.1 |
| babel | flask-mongoengine==1.0.0 |
| eslint | flasgger==0.9.3 |
| superagent | celery==5.0.5 |
| react-router-dom | Flask-JWT==0.3.2 |

## Application Structure

*Gonna add detail explaining the structure soon*

```
.
├── kube-config                     # Project kubernetes configuration settings
├── frontend                        # Frontend source code
│   ├── dist                        # output from webpack build
│   ├── config                      # Webpack & testing configuration settings
│   ├── src                         # React app source code
│   │   ├── App                     # Contains main application component
│   │   ├── api                     # Methods to easily handle calls to the backend api
│   │   ├── assets                  # Contains assets for the project
│   │   ├── components              # Contains misc components
│   │   ├── pages                   # Contains main pages (or views)
│   │   ├── styles                  # Contains styles for the project
│   │   ├── utils                   # Some helpful functions
│   │   └── index.js                # Renders App and registers service workers (if needed)
│   ├── Dockerfile                  # Dockerfile for production use
│   ├── Dockerfile.dev              # Dockerfile for development use
│   ├── nginx.conf                  # Nginx config for production use
│   └── nginx.dev.conf              # Nginx config for development use
│		
│		
├── backend                         # Backend source code
│   ├── server                      # Python module for Flask app
│   │   ├── api                     # API route definitions
│   │   ├── common                  # Common methods
│   │   │   ├── base.py             # Base definitions for Flask sub-classing
│   │   │   ├── constants.py
│   │   │   ├── decorators.py       # Decorators to ease creation of API endpoints
│   │   │   ├── mail.py             # Methods to send specific emails through celery
│   │   │   ├── utils.py
│   │   │   └── validators.py       # Custom validators for Database validation
│   │   ├── models                  # Python classes modeling the database
│   │   │   └── user.py             # Definition of the user model
│   │   ├── tasks                   # Initializing Celery and tasks
│   │   │   ├── __init__.py         # Initialize Celery
│   │   │   └── mail_tasks.py       # Definitions of mail tasks
│   │   ├── templates               # Jinja2 html templates
│   │   │   └── emails              # Email templates
│   │   ├── __init__.py             # Initialize Server
│   │   ├── __main__.py             # Start server from cli arguments
│   │   ├── config.py               # Server configuration settings
│   │   └── schemas.yml             # Swagger schema definitions
│   ├── Dockerfile                  # Dockerfile for production use
│   └── Dockerfile.dev              # Dockerfile for development use
│
│
├── docker-compose.dev.yml          # Docker Compose development configuration
├── docker-compose.yml              # Docker Compose production configuration
├── makefile                        # Makefile with helpful commands to assist with development
└── README.md
```
