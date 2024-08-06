

import allure
import pytest
import request
import response


@allure.title("create booking crud")
@allure.description("TC#1 - create booking id")
#@allure.mark.crud
def test_create_booking_postive():
    # to make a request
    # url
    # header
    # cookies
    # auth(no)
    # header content type =application/json
    # payload/data/Body -Dict / JSON
    # method -post

    base_url = "https://restful-booker.herokuapp.com/booking"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    responseData =request.post(url=URL,headers=headers,json=payload)
    responseData =response.json()

    #response bodt - verification
    #header status code jsn schema valiation
    #time response

    assert responseData.status_code == 200
    assert responseData["bookingid"] >0
    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] == int
    firstname = responseData["booking"]["firstname"]
    assert firstname == "Jim"
    checkin = responseData["booking"]["bookingdates"]["checkin"]
    assert checkin == "2018-01-01"


@allure.title("create booking crud")
@allure.description("TC#2 - create booking id")
#@allure.mark.crud
def test_create_booking_postive_emtyresponse():
    # to make a request
    # url
    # header
    # cookies
    # auth(no)
    # header content type =application/json
    # payload/data/Body -Dict / JSON
    # method -post

    base_url = "https://restful-booker.herokuapp.com/booking"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"content-Type": "application/json"}
    payload = { }
    responseData =request.post(url=URL,headers=headers,json=payload)
    responseData =response.json()

    #response bodt - verification
    #header status code jsn schema valiation
    #time response

    assert responseData.status_code == 200
    assert responseData["bookingid"] >0
    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] == int
    firstname = responseData["booking"]["firstname"]
    assert firstname == "Jim"
    checkin = responseData["booking"]["bookingdates"]["checkin"]
    assert checkin == "2018-01-01"


@allure.title("create booking crud")
@allure.description("TC#3 - create booking id")
#@allure.mark.crud
def test_create_booking_negative_tc3():
    # to make a request
    # url
    # header
    # cookies
    # auth(no)
    # header content type =application/json
    # payload/data/Body -Dict / JSON
    # method -post

    base_url = "https://restful-booker.herokuapp.com/booking"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": "hello",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    responseData =request.post(url=URL,headers=headers,json=payload)
    responseData =response.json()

    #response bodt - verification
    #header status code jsn schema valiation
    #time response

    assert responseData.status_code == 200

