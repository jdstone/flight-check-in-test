from flask import Blueprint, jsonify, request
import random
import string

bp = Blueprint('review', __name__)


def generateToken(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
                                  string.digits + '._-', k=length))


@bp.post("/")
def review():
    if request.is_json:
        data = request.get_json()

        conf_number = data['confirmationNumber']
        first_name = data['passengerFirstName']
        last_name = data['passengerLastName']

        referrer = f"https://www.southwest.com/air/check-in/review.html?confirmationNumber={conf_number}&passengerFirstName={first_name}&passengerLastName={last_name}"

    if request.referrer == referrer:
        json_data = {
            "data": {
                "searchResults": {
                    "reservation": {
                        "confirmationNumber": conf_number,
                        "travelers": [
                            {
                                "firstName": first_name,
                                "lastName": last_name
                            }
                        ]
                    },
                    "token": generateToken(length=4426)
                }
            }
        }

        return jsonify(json_data)
    else:
        return jsonify({"msg": "No Data!"})

