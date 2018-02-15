# Alexa-CI-example
[![Build Status](https://travis-ci.org/ryandens/Alexa-CI-example.svg?branch=master)](https://travis-ci.org/ryandens/Alexa-CI-example)  
[![Coverage Status](https://coveralls.io/repos/github/ryandens/Alexa-CI-example/badge.svg?branch=master)](https://coveralls.io/github/ryandens/Alexa-CI-example?branch=master)
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


So first, I created the repo, setup a test directory and made sure my Travis-CI pipeline 
was working with my codecov test. If you want to see what the repository looked like before
I added the Color_Picker skill, click [here](https://github.com/ryandens/Alexa-CI-example/tree/76291efbc0356c10846ea11af411dadecdb21154).


Once you have setup your repo with continuous integration and code coverage tests, 
follow [this tutorial](https://developer.amazon.com/alexa-skills-kit/alexa-skill-quick-start-tutorial).
Make sure to test it online with Alexa's testing gui's


Next, it's time to setup the ASK-CLI. This was pretty challenging. Follow [this tutorial](https://developer.amazon.com/docs/smapi/quick-start-alexa-skills-kit-command-line-interface.html)
to install the ASK-CLI. If you do not have the AWS CLI, you need to make sure that you create credentials for AWS. 
This is explained [here](https://developer.amazon.com/docs/smapi/set-up-credentials-for-an-amazon-web-services-account.html)
I'm sure this isn't completely best practice, but the way that I got everything to work was by also giving the 
user blanket admin privileges. ¯\\\_(ツ)\_/¯

Now, go to your find your skill id. This is found in your alexa developer console. 
When you find the list of your alexa skills, there should be a link to view your 
skill id. copy that skill id to your clipboard.

> $ cd path/to/your/repo

> $ ask clone <skill-id>

This  should create a directory, called Color_Picker, just like you see in this repo. 
Now, you can make changes to the lambda functions, the skill model, or the config files.
To re-deploy it, make sure you're inside the Color_Picker directory (not just your github repo)
and run the following command:

> $ ask deploy


### To Do:
1. Automate deployment of skill
This is challenging because right now the ASK-CLI requires the use of a browser interface to initialize the ASK-CLI profile. Currently trying to find a workaround

