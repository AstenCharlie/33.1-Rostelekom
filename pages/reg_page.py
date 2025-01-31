import os
from pages.base_page import WebPage
from pages.elements import WebElement
from config import RostelecomInfo

class RegPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or RostelecomInfo.URL_ELK_Web

        super().__init__(web_driver, url)

    # название страницы регистрации
    name_page_reg = WebElement(xpath='//h1[@class="card-container__title"]')

    # кнопка "Войти с паролем"
    enter_with_password = WebElement(id='standard_auth_btn')

    # кнопка "Войти" в Ключ Web
    button_enter = WebElement(xpath='//a[@class="go_kab"]')

    # ссылка "Зарегистрироваться" на странице авторизации
    link_reg_on_auth_page = WebElement(id='kc-register')

    # кнопка "Продолжить" на странице регистрации
    button_continue_on_reg_page = WebElement(xpath='//button[contains(text(), Зарегистрироваться)]')

    # поле "Имя"
    first_name_field = WebElement(name='firstName')

    # поле "Фамилия"
    surname_field = WebElement(name='lastName')

    # поле "E-mail или мобильный телефон"
    email_phone = WebElement(id='address')

    # поле "Пароль"
    pass_for_reg = WebElement(id='password')

    # поле "Подтверждение пароля"
    pass_for_reg_confirm = WebElement(id='password-confirm')

    # слоган
    tagline_reg = WebElement(xpath='//*[contains(text(), "Персональный помощник в цифровом мире Ростелекома")]')

    # пользователькое соглашение
    agreement_reg = WebElement(
        xpath='//span[contains(text(), "Нажимая кнопку «Зарегистрироваться», вы принимаете условия")]')

    # всплывающее предупреждение под полем "Имя"
    tooltip_first_name_field = WebElement(
        xpath='//*[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

    # всплывающее предупреждение под полем "Фамилия"
    tooltip_surname_field = WebElement(
        xpath='//*[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

    # всплывающее предупреждение под полем  "E-mail или мобильный телефон"
    # css_selector='div.email-or-phone.register-form__address span.rt-input-container__meta--error'
    # css_selector='div.email-or-phone span.rt-input-container__meta--error'
    tooltip_email_phone = WebElement(
        xpath='//*[contains(text(), "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru")]')

    # всплывающее предупреждение под полем  "Пароль"
    tooltip_pass_for_reg = WebElement(css_selector=
                                      'div.new-password-container__password span.rt-input-container__meta--error')

    # всплывающее предупреждение под полем  "Подтверждение пароля"
    tooltip_pass_for_reg_confirm = WebElement(css_selector=
                                              'div.new-password-container__confirmed-password span.rt-input-container__meta--error')