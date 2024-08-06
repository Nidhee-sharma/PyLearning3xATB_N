#pip is nothing pythons provide to install multiple package to work with it
#in my project i need only pytest using pip install pytest
#using pip you can install specific package


#request module - module -package or lobrary cotains functions which you can use easily
#math ,os ,csv ,allure,pytest
#request three line code - module it is like a wow Get ,post , Put ,delete ,patch,option
#URL ,Auth ,Cookies ,verification with pytest
#get request - Bookng id and path param
#response Body > verify >assert , value
#status code > verify
#time

#JSON response

import pytest
import allure
import requests



@allure.title("Test Get Request -   Restful booker project#1")
@allure.description("TC1#>Verify that get request work with ID")
@allure.tag("regression","smoke")
@allure.label("owner","Nidhee Sharma")
@allure.testcase("TC#1")
#@allure.mark.smoke

def test_get_single_by_id():
    url="https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData)
    assert responseData.status_code == 200



@allure.title("Test Get Request_invalid case -   Restful booker project#2")
@allure.description("TC1#>Verify that get request work with ID_withinvalid")
@allure.tag("regression","smoke")
@allure.label("owner","Nidhee Sharma")
@allure.testcase("TC#2")
def test_get_single_by_id_invalid():
    url="https://restful-booker.herokuapp.com/booking/1/invalid"
    responseData = requests.get(url)
    print(responseData)
    print(responseData.text)
    assert responseData.status_code == 404
# -s help you to print the data of print command



@allure.title("Test Get Request -   Restful booker project#1")
@allure.description("TC1#>Verify that get request work with ID")
@allure.tag("regression","smoke")
@allure.label("owner","Nidhee Sharma")
@allure.testcase("TC#1")
#@allure.mark.smoke

def test_get_single_by_id2_withinvalidstatuscode():
    url="https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData)
    print(responseData.text)
  #  print(responseData.header)
    print(responseData.cookies)
    print(responseData.json())
    assert responseData.status_code == 404