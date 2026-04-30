import pytest
from selenium import webdriver
from data import URL
from helpers_api import UserApi, email_pass_name_random

@pytest.fixture(params=["chrome", "firefox"], ids=["Chrome", "Firefox"])
def browser(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.get(URL.BASE_URL)    
    yield driver
    driver.quit()

@pytest.fixture
def create_user():
    user_data = email_pass_name_random()
    response = UserApi.create_user(user_data)
    
    yield {"response": response, "user_data": user_data}
    
    token = response.json().get('accessToken')
    if token:
        UserApi.delete_user(token)
