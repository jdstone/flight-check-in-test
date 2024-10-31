<?php

function generateToken($length = 8)
{
    $characters = '123456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ._-';
    $characters_length = strlen($characters);
    $random_string = '';
    for ($i = 0; $i < $length; $i++)
    {
        $random_string .= $characters[rand(0, $characters_length - 1)];
    }
    return $random_string;
}

// set header so information received is of JSON content type
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

// decode the JSON so the keys can be accessed individually
$jsonData = json_decode(file_get_contents('php://input'), true);

// confirm the passenger information in JSON format exists
if (isset($jsonData))
{
    $referrer = "https://www.southwest.com/air/check-in/review.html?confirmationNumber=" . $jsonData['confirmationNumber'] . "&passengerFirstName=" . $jsonData['passengerFirstName'] . "&passengerLastName=" . $jsonData['passengerLastName'];
}

// if HTTP referrer matches, then respond with passenger check-in data
if (isset($_SERVER['HTTP_REFERER']) == $referrer)
{
    // multiple travelers
    $responseData = array("data" =>
        array("searchResults" =>
            array("reservation" =>
                array("confirmationNumber" => $jsonData['confirmationNumber'],
                    "travelers" => array(
                        array("firstName" => $jsonData['passengerFirstName'], "lastName" => $jsonData['passengerLastName'])
                    )
                ),
                "token" => generateToken($length = 4426)
            )
        )
    );

    $responseJson = json_encode($responseData);
    echo $responseJson;
}
else
{
    echo json_encode(['msg' => 'No Data!']);
}

?>