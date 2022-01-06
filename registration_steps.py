from behave import given, when, then

from BrainBucket.pages.registration_page import RegistrationPage
from selenium.webdriver.common.by import By
import time

from BrainBucket.webelements.UIElement import UIElement as Element


@given("user is on registration page")
def verify_user_on_registration_page(context):
    registration_form = RegistrationPage(context.browser)
    assert registration_form.get_form_title() == "Register Account"
    context.registration_form = registration_form


@when("user inputs all data for registration")
def enter_registration_data(context):
    registration_form = context.registration_form
    configs = context.configs
    registration_form.enter_first_name("Svetlana")
    registration_form.enter_last_name("Match")
    registration_form.enter_email(configs.get_user1_email())
    registration_form.enter_telephone("3123405555")
    registration_form.enter_first_line_address("175 W Jackson St")
    registration_form.enter_city("Chicago")
    registration_form.select_state("Illinois")
    # AN my code starts
    registration_form.enter_password(configs.get_user1_password())
    registration_form.confirm_password(configs.get_user1_password())
    # AN my code ends
    registration_form.subscribe_to_newsletters()
    registration_form.agree_to_privacy_policy()
    time.sleep(2)
    registration_form.submit_form()
    time.sleep(3)


@then('successful registration info pops up')
def verify_registration(context):
    browser = context.browser
    successful_registration_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert successful_registration_title.get_text() == 'Your Account Has Been Created!'

    successful_registration_subtitle = Element(browser, By.XPATH, "//*[@id='content']/p")
    assert successful_registration_subtitle.get_text() == 'Congratulations! Your new account has been successfully created!'
