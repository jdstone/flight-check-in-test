# Automatic Flight Check-in Test Suite

This application repository serves the purpose to provide a way to locally test my [flight-check-in-flask](https://github.com/jdstone/flight-check-in-flask/) app. This allows you to see how my Python/Flask Check-in app works.

## Python Usage

### Linux/macOS

1. Clone this repository
2. `cd flight-check-in-test-suite/Python/`
3. `python3 -m venv .`
4. `source bin/activate`
5. `pip install -r requirements.txt`
6. Copy the `Python/.env` file to the root directory of the Python/Flask Flight Check-in app
7. `flask run -p 5001` (Running on port 5001 is important because the Python/Flask Flight Check-in app runs on the default port, which is 5000.)

### Windows

1. Clone this repository
2. `cd flight-check-in-test-suite\Python\`
3. `python3 -m venv .`
4. `source bin/activate`
5. `pip install -r requirements.txt`
6. Copy the `Python\.env` file to the root directory of the Python/Flask Flight Check-in app
7. `flask run -p 5001` (Running on port 5001 is important because the Python/Flask Flight Check-in app runs on the default port, which is 5000.)

## PHP Usage

1. Clone this repository
2. Set-up a web server with PHP 6.x+ support
3. Place the two files in the `PHP` directory on your web server
4. Copy the `Python\.env` file to the root directory of the Python/Flask Flight Check-in app
5. In the `.env` file, uncomment the PHP API endpoints, and comment the Python API endpoints
6. Run the web server

## API endpoints

* /confirm

  ```shell
  curl --header "Content-Type: application/json" --referer "https://www.southwest.com/air/check-in/confirmation.html?drinkCouponSelected=false" --request POST --data '{"token": "sagdsagsag463erg.-dssdg"}' http://127.0.0.1:5001/confirm
  ```

* /review

  ```shell
  curl --header "Content-Type: application/json" --referer "https://www.southwest.com/air/check-in/review.html?confirmationNumber=W89156&passengerFirstName=Johnny&passengerLastName=Appleseed" --request POST --data '{"passengerFirstName":"Johnny","passengerLastName":"Appleseed","confirmationNumber":"W89156"}' http://127.0.0.1:5001/review
  ```

