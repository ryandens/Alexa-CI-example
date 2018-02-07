# Alexa-CI-example
[![Build Status](https://travis-ci.org/ryandens/Alexa-CI-example.svg?branch=master)](https://travis-ci.org/ryandens/Alexa-CI-example)  
[![codecov](https://codecov.io/gh/ryandens/Alexa-CI-example/branch/master/graph/badge.svg)](https://codecov.io/gh/ryandens/Alexa-CI-example)  
An example of how to create an Alexa Skill using the Alexa Skill Kit CLI, Travis CI, and AWS Lamda for Python


***Note*** I have no idea if this will work ¯\\\_(ツ)\_/¯

## Testing

### Unit Testing
To run unittests locally, simply run the follwing in the command line:
> $ nosetests

For coverage tests, simply run
> $ nosetests --with-coverage

### Shield
1. Travis Build shield
Signup for Travis with Github, add your repo to it (if it's public). 

2. Do the same thing for Codecov, and then add codecov to the after_success in the .travis.yml 

## How I did it
Follow this tutorial to get a very basic alexa skill working with python lambda function


So first, I created the repo, setup a test directory and made sure my Travis V
