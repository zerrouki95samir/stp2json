# Simple Flask API

This is a fask server/api to convert STEP Files to [ThreeJS](https://threejs.org/docs/index.html#manual/en/introduction/Creating-a-scene) readable json/object. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

if you want to run this api/project locally on your machine you need to have [conda](https://www.anaconda.com/products/individual) pre-installed on your OS, 
Or if you want to just deploy it on a server jump to [Deployment](#deployment) section.

### Run This project locally on your machine

After installing anaconda (comes with python3.* pre-installed), you can follow this steps:

Clone this Repository on your machine, open your terminal/cmd.. and type:

```
git clone https://github.com/zerrouki95samir/stp2json.git
```
cd to stp2json folder:

```
cd stp2json
```

Create the environment from the environment.yml file:

```
conda env create -f environment.yml
```

After the conda env is created, you need to activate it with this command:

```
conda activate stp2json
```

Run the api server:

```
python run.py
```

If everything goes well, you will see this line at the end of your command line!:  

```
Running on http://0.0.0.0:33508/ (Press CTRL+C to quit)
```

## Running the tests

Now that our server is up and running, we need to do some testing, so we need to send a POST requests with stp/step file data, I've already prepared some code with php-curl or python-requests  module, you can just open the [base url](http://localhost:33508/) that appeared when the server ran or you can simply click here: [http://localhost:33508/](http://localhost:33508/) 
And the [Simple Explanation](http://localhost:33508/) the first paragraph

### Break down into end to end tests

If you [read](https://stp2jsonv2.herokuapp.com/) and test the API server using the [python/php-Curl codes template](https://stp2jsonv2.herokuapp.com/stp2json) I have provided for you to do a POST Request, you will get a successful response as a json object


## Deployment

Now!, Let's talk about the deployment, i already deployed this flask-api on [my heroku server](https://stp2jsonv2.herokuapp.com/), using the Dockerfile located in main directory, 
you need to have [heroku cli](https://devcenter.heroku.com/articles/heroku-cli) and [Docker](https://docs.docker.com/desktop/) installed on your machine.
After you install the CLI, run the heroku login command. You’ll be prompted to enter any key to go to your web browser to complete login. 
The CLI will then log you in automatically.

```
heroku login
```

Create an account on [heroku website](https://www.heroku.com/). To create you rfirst app on heroku you have two options: 
create it from the [heroku website](https://dashboard.heroku.com/new-app) (easy) or using cli command-line:
open your cmd/terminal, cd to the project directory (cd stp2json)

create your first app:
```
heroku create --app yourAppName
```

Build the image and push to Container Registry (this will takes a lot of time to build to docker-image):

```
heroku container:push web --app yourAppName
```

Then release the image to your app:

```
heroku container:release web --app yourAppName
```

Now open the app in your browser:

```
heroku open
```







## Built With

* [flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [pythonocc-core](https://github.com/tpaviot/pythonocc-core) - is a python package whose purpose is to provide 3D modeling features. It is intended to CAD/PDM/PLM and BIM related development.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Author

* **ZERROUKI SAMIR** - *Initial work* - [zerrouki95samir](https://github.com/zerrouki95samir)
