import pytest
import time
from pages.auth_page import AuthPage
from config import RostelecomInfo


@pytest.mark.parametrize("url_product",
                         [RostelecomInfo.URL_ELK, RostelecomInfo.URL_Online, RostelecomInfo.URL_START, RostelecomInfo.URL_SmartHome,
                          RostelecomInfo.URL_Key],
                         ids=["URL_ELK", "URL_Onl", "URL_START","URL_SmartHome", "URL_Key"])
def test_auth_form(web_browser, url_product):

    page = AuthPage(web_browser, url_product)

    if url_product == RostelecomInfo.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    assert page.name_page_auth.is_presented()

    assert page.tab_phone.is_presented()
    assert page.tab_mail.is_presented()
    assert page.tab_login.is_presented()

    assert page.field_username.is_presented()
    assert page.field_password.is_presented()

    assert page.show_password.is_presented()
    assert page.checkbox.is_presented()
    assert page.link_forgot_password.is_presented()
    assert page.button_enter_auth.is_presented()
    assert page.button_enter_with_temp_code.is_presented()
    assert page.agreement_auth.is_presented()

    assert page.link_vk.is_presented()
    assert page.link_ok.is_presented()
    assert page.link_mail.is_presented()
    assert page.link_google.is_presented()
    assert page.link_ya.is_presented()

    assert page.tab_mail.get_text() == RostelecomInfo.tab_mail_text
    assert page.tab_login.get_text() == RostelecomInfo.tab_login_text

    if url_product in [RostelecomInfo.URL_ELK, RostelecomInfo.URL_START]:
        assert page.tab_personal_account.is_presented()
        assert page.tab_personal_account.get_text() == RostelecomInfo.tab_personal_account_text

    if url_product == RostelecomInfo.URL_Online:
        assert not page.tab_personal_account.is_presented()
        assert not page.link_reg.is_presented()
    else:
        assert page.link_reg.is_presented()

    if url_product in [RostelecomInfo.URL_SmartHome, RostelecomInfo.URL_Key]:
        assert not page.tab_personal_account.is_presented()

    assert page.tab_phone.get_text() == RostelecomInfo.tab_phone_text



@pytest.mark.parametrize("url_product",
                         [RostelecomInfo.URL_ELK, RostelecomInfo.URL_Online, RostelecomInfo.URL_START, RostelecomInfo.URL_SmartHome,
                          RostelecomInfo.URL_Key],
                         ids=["URL_ELK", "URL_Onl", "URL_START", "URL_SmartHome", "URL_Key"])
def test_auth_log_and_pass_positive(web_browser, url_product):

    page = AuthPage(web_browser, url_product)

    if url_product == RostelecomInfo.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    page.tab_login.click()

    page.field_username.send_keys(RostelecomInfo.login)
    page.field_password.send_keys(RostelecomInfo.valid_password1)

    page.button_enter_auth.click()

    if url_product == RostelecomInfo.URL_ELK:
        page.personal_acc_elk.wait_to_be_clickable()
        assert page.personal_acc_elk.is_presented()

    elif url_product == RostelecomInfo.URL_Online:
        page.button_pass_onlime_lc.click()
        assert page.personal_acc_onlime.is_presented()

    elif url_product == RostelecomInfo.URL_START:
        assert page.personal_acc_start.is_presented()

    elif url_product == RostelecomInfo.URL_SmartHome:
        assert page.personal_acc_SmartHome.is_presented()

    elif url_product == RostelecomInfo.URL_Key:
        page.link_key_login.click()
        assert page.personal_acc_key_login.is_presented()


@pytest.mark.parametrize("url_product",
                         [RostelecomInfo.URL_ELK, RostelecomInfo.URL_Online, RostelecomInfo.URL_START, RostelecomInfo.URL_SmartHome,
                          RostelecomInfo.URL_Key],
                         ids=["URL_ELK", "URL_Onl", "URL_START","URL_SmartHome", "URL_Key"])
def test_auth_mail_and_pass_positive(web_browser, url_product):

    page = AuthPage(web_browser, url_product)

    if url_product == RostelecomInfo.URL_Key:
        page.button_enter.click()

    page.enter_with_password.click()

    page.tab_mail.click()

    page.field_username.send_keys(RostelecomInfo.mail)
    page.field_password.send_keys(RostelecomInfo.valid_password1)

    page.button_enter_auth.click()

    if url_product == RostelecomInfo.URL_ELK:
        page.personal_acc_elk.wait_to_be_clickable()
        assert page.personal_acc_elk.is_presented()

    if url_product == RostelecomInfo.URL_Online:
        page.button_pass_onlime_lc.click()
        assert page.personal_acc_onlime.is_presented()

    if url_product == RostelecomInfo.URL_START:
        assert page.personal_acc_start.is_presented()

    if url_product == RostelecomInfo.URL_SmartHome:
        assert page.personal_acc_SmartHome.is_presented()

    if url_product == RostelecomInfo.URL_Key:
        page.link_key_login.click()
        assert page.personal_acc_key_login.is_presented()