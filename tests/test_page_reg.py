import pytest
from pages.reg_page import RegPage
from config import RostelecomInfo


@pytest.mark.parametrize("url_product", [RostelecomInfo.URL_ELK, RostelecomInfo.URL_START, RostelecomInfo.URL_Key],
                         ids=["URL_ELK", "URL_START", "URL_Key"])
def test_reg_all_fields_empty_negative(web_browser, url_product):
    """Пустые поля при регистрации"""

    page = RegPage(web_browser, url_product)

    if url_product == RostelecomInfo.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.first_name_field.clear_field()
    page.surname_field.clear_field()
    page.email_phone.clear_field()
    page.pass_for_reg.clear_field()
    page.pass_for_reg_confirm.clear_field()
    page.button_continue_on_reg_page.click()

    assert page.tooltip_first_name_field.is_presented(), " tooltip  not found"
    assert page.tooltip_surname_field.is_presented(), " tooltip  not found"
    assert page.tooltip_email_phone.is_presented(), " tooltip  not found"
    assert page.tooltip_pass_for_reg.is_presented(), " tooltip  not found"
    assert page.tooltip_pass_for_reg_confirm.is_presented(), " tooltip  not found"


@pytest.mark.parametrize("url_product", [RostelecomInfo.URL_ELK, RostelecomInfo.URL_START, RostelecomInfo.URL_Key],
                         ids=["URL_ELK", "URL_START", "URL_Key"])
@pytest.mark.parametrize("password",
                         ["ifvbmaf", "ifvbmafr", "ifvbmafQ"],
                         ids=["7 lowercase Latin", "8 lowercase Latin", "7 lowercase Latin + 1 uppercase Latin"])
def test_field_password_negative(web_browser, url_product, password):

    page = RegPage(web_browser, url_product)

    if url_product == RostelecomInfo.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.pass_for_reg.send_keys(password)

    page.pass_for_reg_confirm.click()

    assert page.tooltip_pass_for_reg.is_presented(), " tooltip  not found"


# TC-07_SF-RTK, TC-08_SF-RTK, TC-09_SF-RTK
@pytest.mark.parametrize("url_product", [RostelecomInfo.URL_ELK, RostelecomInfo.URL_START, RostelecomInfo.URL_Key],
                         ids=["URL_ELK", "URL_START", "URL_Key"])
def test_fields_pass_and_pass_confirmation_negative(web_browser, url_product):

    page = RegPage(web_browser, url_product)

    if url_product == RostelecomInfo.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.pass_for_reg.send_keys(RostelecomInfo.valid_password1)
    page.pass_for_reg_confirm.send_keys(RostelecomInfo.password2)

    page.first_name_field.click()

    assert page.tooltip_pass_for_reg_confirm.is_presented(), " tooltip  not found"