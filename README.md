# Automatic Flight Check-in Test Suite

This repository serves the purpose to provide a way to locally test my [flight-check-in-flask](https://github.com/jdstone/flight-check-in-flask/) app.

## Python Usage

### Linux/macOS

1. Clone this repository
2. `cd flight-check-in-test-suite/`
3. `python3 -m venv .`
4. `pip install -r requirements.txt`
5. Copy the `Python/.env` file to the root directory of the Python/Flask Flight Check-in app
6. `flask run -p 5001` (Running on port 5001 is important because the Python/Flask Flight Check-in app runs on the default port, which is 5000.)

### Windows

1. Clone this repository
2. `cd flight-check-in-test-suite\`
3. `python3 -m venv .`
4. `pip install -r requirements.txt`
5. Copy the `Python\.env` file to the root directory of the Python/Flask Flight Check-in app
6. `flask run -p 5001` (Running on port 5001 is important because the Python/Flask Flight Check-in app runs on the default port, which is 5000.)

## PHP Usage

1. Follow the same instructions as the Python app, but after step 5, uncomment the PHP API endpoints, and comment the Python API endpoints.

