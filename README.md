# UI Automation Tests with Selenium Grid and Behave

This project uses Python 3.7 and the frameworks Behave(BDD) and Selenium.

## Behavior Driven Development(BDD)
Is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants 
in a software project.
BDD focuses on obtaining a clear understanding of desired software behavior through discussion with stakeholders. 
It extends TDD by writing test cases in a natural language that non-programmers can read. 
Behavior-driven developers use their native language in combination with the ubiquitous language of domain-driven design to describe the purpose 
and benefit of their code. This allows the developers to focus on why the code should be created, rather than the technical details, 
and minimizes translation between the technical language in which the code is written and the domain language spoken by the business, 
users, stakeholders, project management, etc.

get more information: [https://behave.readthedocs.io](https://behave.readthedocs.io/en/latest/philosophy.html)

## LambdaTest Selenium Automation Grid

LambdaTest Selenium Automation Grid is a cloud based scalable Selenium testing platform which enables you to run your automation scripts 
on 2000+ different browsers and operating systems. 
You can now run your Python Selenium automated test cases on a scalable Selenium infrastructure that is running real browsers and real operating systems. 
This post will help you in getting started with configuring and running your Python based automation test scripts on LambdaTest Selenium cloud platform.

get more information: [https://www.lambdatest.com/](https://www.lambdatest.com/)


## Features Style Guide

The Gherkin steps should be made with the following considerations:
- Given: Setup, they contain neither actions nor assertions.
- When: Actions, they use the browser api to act as a user.
- Then: Assertions, they use `assert` to check if test conditions are met.

Feature files should not contain the word `should`. It is implied on every Then line since these are tests and are thus 
redundant. Furthermore, when viewing the feature files as documentation, the word `should` does not make sense since 
documentation should be declarative. To help with writing Descriptions for Features and Scenarios, begin them with 
`The system should` and when you are finished with the description, simple remove `The system should`.


This project can execute the tests local and remotly in the Lambdatest Grid.

## Requirements to run locally 

you need to have the webdrivers for each desired browser and export the PATH

download the webdrivers from the url: [https://www.selenium.dev/downloads/](https://www.selenium.dev/downloads/)

## Requirements to run with remote webdriver

You need to have an account in Lambdatest Automation Grid: 

Acces to your account and take the next information of your profile section:
- username
- Access Token

You should give that information for setup the remote execution

## Setup

This project uses Make as a task runner. The commands to install the dependencies are configurated in the Makefile:

execute:

``` 
make install
```

# Windows setup

Some commands aren't working for Windows platforms, so if you have error with the Makefile you can execute the installation manually

### Create virtual environment

``` 
 python3 -m venv venv
```

### Activate virtual environment

``` 
 .\venv\Scripts\activate
```

### Install project dependencies

``` 
 pip install -r requirements.txt
```


## Running
To run all the tests, execute 

```
make all browser={browser}
```

The default browser is Chrome, if you want run the tests in other browser, pass the parameter browser with the any of these options:  

- `chrome`
- `firefox`
- `safari`
- `edge`


you need to have the respective webdriver in the PATH



### Run a specific feature 

```
make by_name name={feature_name} // you don't need the file extension 
*example: make by_name name=1-sign_in

```


## Make commands
The avaliable make commands are:

- `make help` Shows a list of available commands
- `make all` Run all tests
- `make wip` Run the wip tags (work in progress)
- `make report` Run the report server
- `make format` Reformat python code according to standards
- `make lint` Run linter against python code


## Test Rail Integration
This project may be integrated with Test rail, where you have defined the Test cases for your proyect and after to run the tests 
either local or remote, you can add results to the respective Test cases

## Requirements for the integration with Test Rail

You need to have an account in Test Rail: 

Acces to your account and go to the section Administration, Site Settings:
- On the API Tab, check the option "Enable API"
- Go to the section My settings
- On the API KEYS Tab, Generate an API Key and save this value
- Set up the Test rail credentials in the .env file



