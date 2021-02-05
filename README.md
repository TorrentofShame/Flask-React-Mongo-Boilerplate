# Flask React Mongo Boilerplate

## Contents

- [Quick Start](#quick-start)
- [Dependencies](#dependencies)
- [Application Structure](#application-structure)

## Quick Start

**Requirements**

- Docker
- Docker Compose

1. Clone the project

```
git clone https://gitlab.com/torrentofshame/flask-react-mongo-boilerplate.git
```

2. Move to `flask-react-mongo-boilerplate`

```
cd flask-react-mongo-boilerplate
```

3. Run it

In Production:

```
make produp

make proddown
```

In Development:

```
make devup

make devdown
```

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
├── kube-config
├── frontend
│   ├── config
│   └── src
│       ├── App
│       ├── api
│       ├── components
│       ├── pages
│       ├── styles
│       └── utils
├── backend
│   └── server
│       ├── api
│       ├── common
│       ├── models
│       ├── tasks
│       └── templates
│           └── emails
└── makefile
```
