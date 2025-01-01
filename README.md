# A simple resume generator using Python + Wagtail
Git clone this repo, or build it on your own with the following apps.

wagtail
wagtail-resume
and ...

dependencies = [
    "gunicorn>=23.0.0",
    "psycopg2-binary>=2.9.10",
    "python-dotenv>=1.0.1",
]

# About the Digital Ocean App Platform
This process is simple. First create a DO account, and create an App. This web-app is inexpensive and eliminates the need for a full-fledged Virtual Machine hosted on AWS or Azure or other cloud vendors where you are responsible for the `apt update` and checking other security CVEs and things you should not be focusing on whether it be infrastructure and development or simply hosting your own website (as I am for my resume app, here).

## First. Create an dot env file
create a .env file with the following variables to insert into the Python runtime environment.

It typically looks like this.

  DB_USER=<redacted> 
  DB_PASSWORD=<redacted> 
  DATABASE_URL=<redacted> 
  DATABASE_PORT=<redacted> 
  DB_NAME=<redacted>

## Modify the Environemnt Variables and test locally
Supply the actual values with your SQLite (default DB engine) or your DB engine flavor of choice and run with it.
(RTFM, and reference the docs for wagtail, django.

## Deploying on Digital Ocean
Follow the typical process for deploying apps on Digital Ocean. 
Create the above Env Vars (environment variables) for the newly created app.

The only other item of consideration is the how to handle Static Files, Networking, Domain configuration for DNS configuration. (Digital Ocean is using let's encrypt for SSL Certs).

I found this to be incredibly easy to setup and point my domain name servers to Digital Ocean, and chose PostreSQL to serve as the DB back-end (which is entirely over-kill, but serves it's purpose of education, acquiring skills for deployment for Cloud based apps.


