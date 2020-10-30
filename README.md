<h1 align="center">Calls</h1>

<img src="https://github.com/gurupratap-matharu/calls/blob/master/staticfiles/img/hero.jpg" alt="drawing" width="1920"/>

## Live

<http://gurupratap.pythonanywhere.com/calls/>

## Description

- A django projects that registers domestic, national and international calls in the database.
- Calls can be configure in the admin area but are generally divided into three common types.

* Local: Fixed cost of $0.10
* National: Billed at $0.01 per second
* International: Billed at $0.03 per second.

The interface itself permits

* To register a new call
* To see a list of all the calls (id, type, duration and cost)

## Stripe Payments

<img src="https://github.com/gurupratap-matharu/midware/blob/master/staticfiles/img/stripe.png" alt="drawing" width="1920"/>

## Browsable Request API

<img src="https://github.com/gurupratap-matharu/midware/blob/master/staticfiles/img/request.png" alt="drawing" width="1920"/>

## Motivation 🎯

- App suggestion based on interview assignment
- Deployment with docker on heroku
- Working with tools that are free for open source
- Working with payment methods like stripe and REST apis

## Features ✨

- Logs Requests and responses using logging module
- Save Requests and responses to database for persistency
- Connects with Stripe payments to creates a payment upon POST
- Versioning of api possible see `/api/v1/`
- Fast response time
- Easily customizable with Login | Logout | reset password features and rest-token authentication
- Make file for faster setup and reusability

## Development setup 🛠

Steps to locally setup development after cloning the project.

`docker-compose up -d --build`

or simply

`make build`

Make sure you rename .env.example to .env and declare the environment variables in root folder for docker to pickup!
