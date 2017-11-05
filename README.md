# Garden

## How to run for development

- Fork and clone this repository.
- Run `cd garden` to go into the project directory.
- Create a virtual environment by running `python -m venv venv`, you now have a virtual environment in the venv directory in your project.
- Now run `source venv/bin/activate` to activate your virtual environment.
- Run `pip install -r requirements.txt` to install the required packages.
- Run `docker-compose up -d mongodb` to start a mongoserver if none are running or start your own.
- Do `cp .env.dist .env` and change the values in the .env file to fit your environment.
- Run `export FLASK_APP=garden/__init__.py && export FLASK_DEBUG=true`.
- Finally, execute `flask run` to start the development server.

The app can now be accessed at `127.0.0.1:5000`.

## How to run for production

- Clone the repository.
- Go into the project dir.
- Do `cp .env.dist .env` and change the values in the .env file to fit your environment or skip this step and set the env vars some other way.
- Run `docker-compose up -d --build`.

The app is now running on port 80.
