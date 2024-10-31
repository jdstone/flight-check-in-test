from flask import Blueprint, jsonify, request

bp = Blueprint('confirm', __name__)


@bp.post("/")
def review():
    if request.is_json:
        data = request.get_json()

        referrer = "https://www.southwest.com/air/check-in/confirmation.html?drinkCouponSelected=false"

    if request.referrer == referrer and 'token' in data:
        json_data = {
            "data": {
                "searchResults": {
                    "travelers": [
                        {
                            "boardingBounds": [
                                {
                                    "boardingSegments": [
                                        {
                                            "boardingGroup": "B",
                                            "boardingGroupPosition": "06"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "token": data['token']
                }
            },
            "success": True
        }

        return jsonify(json_data)
    else:
        return jsonify({"confirmation": False})

