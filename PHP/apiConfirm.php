<?php

// set header so information received is of JSON content type
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

// decode the JSON so the keys can be accessed individually
$jsonData = json_decode(file_get_contents('php://input'), true);

// check that the passenger check-in confirmation in JSON format exists
if (isset($jsonData))
{
    $referrer = "https://www.southwest.com/air/check-in/confirmation.html?drinkCouponSelected=false";
}

// check to make sure the referrer matches and a JSON token exists
if (isset($_SERVER['HTTP_REFERER']) && $_SERVER['HTTP_REFERER'] == $referrer && isset($jsonData['token']))
{
    // multiple travelers
    $responseData = array("data" =>
        array("searchResults" =>
            array("travelers" => array(
                    array("boardingBounds" => array(
                            array("boardingSegments" => array(
                                array("boardingGroup" => "B", "boardingGroupPosition" => "06")

                                )
                            )
                        )
                    )
                ),
                "token" => $jsonData['token']
            )
        ),
        "success" => true
    );
    $responseJson = json_encode($responseData);
    echo $responseJson;
}
else
{
    $responseData = array("confirmation" => false);
    $responseJson = json_encode($responseData);
    echo $responseJson;
}

?>
