import os
from pages.base_page import WebPage
from pages.elements import WebElement
from config import RostelecomInfo

class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or RostelecomInfo.URL_ELK_Web
        super().__init__(web_driver, url)

    # кнопка "Войти с паролем"
    enter_with_password = WebElement(id='standard_auth_btn')

    # кнопка "Войти" в Ключ Web
    # '//a[@class="go_kab"]' , a.go_kab
    button_enter = WebElement(css_selector="a.go_kab")

    # название страницы авторизации
    name_page_auth = WebElement(xpath='//h1[@class="card-container__title"]')

    # меню выбора типа аутентификации
    tab_phone = WebElement(id="t-btn-tab-phone")
    tab_mail = WebElement(id="t-btn-tab-mail")
    tab_login = WebElement(id="t-btn-tab-login")
    tab_personal_account = WebElement(id="t-btn-tab-ls")

    # поле телефон почта логин лицевой счет
    field_username = WebElement(id="username")

    # поле пароль
    field_password = WebElement(id="password")

    # иконка показать пароль
    show_password = WebElement(css_selector="div.rt-input__action svg.rt-input__eye")

    # чекбокс "Запомни меня"
    checkbox = WebElement(css_selector='div.rt-checkbox span.rt-checkbox__shape')

    # ссылка "Забыл пароль"
    link_forgot_password = WebElement(id="forgot_password")

    # кнопка "Войти" при авторизации
    button_enter_auth = WebElement(id="kc-login")

    # кнопка "Войти по временному коду"
    button_enter_with_temp_code = WebElement(id="back_to_otp_btn")

    # пользователькое соглашение
    agreement_auth = WebElement(css_selector='div.auth-policy a[target="_blank"]')

    # Ссылки авторизации через соцсети
    link_vk = WebElement(css_selector='a#oidc_vk svg[alt="ВКонтакте"]')
    link_ok = WebElement(css_selector='a#oidc_ok svg[alt="Одноклассники.ru"]')
    link_mail = WebElement(css_selector='a#oidc_mail svg[alt="Mail.ru"]')
    link_google = WebElement(css_selector='a#oidc_google svg[alt="Google+"]')
    link_ya = WebElement(css_selector='a#oidc_ya svg[alt="Yandex.ru"]')

    # ссылка "Зарегистрироваться"
    link_reg = WebElement(id="kc-register")

    # "Личный кабинет" ЕЛК Web
    personal_acc_elk = WebElement(css_selector='div.lfjrSy')
    # войти в минипрофиль личного кабинета ЕЛК Web
    enter_to_mini_lc_elk = WebElement(css_selector="div.ccJkbA h2.iqOiiv")
    # кнопка выйти из минипрофиля ЕЛК Web
    button_exit_mini_elk = WebElement(css_selector="div.dvyUXv span.bLVPuw")

    # "Личный кабинет" Онлайм Web
    personal_acc_onlime = WebElement(id='lk-btn')
    # кнопка "Перейти"
    button_pass_onlime_lc = WebElement(xpath='// a[contains(text(), "Перейти")]')

    # "Личный кабинет"  Старт Web
    personal_acc_start = WebElement(css_selector='div.lfjrSy')

    # "Личный кабинет"  Умный дом Web, кнопка "Зарегистрироваться" , находящаяся после авторизации
    personal_acc_SmartHome = WebElement(id='submit_button')

    # "Личный кабинет" Ключ Web по логину
    personal_acc_key_login = WebElement(id='lk-btn')

    # ссылка на переход в личный кабинет Ключ Web по логину
    link_key_login = WebElement(css_selector='div.errorMessage--ruXc7 a')

    # "Личный кабинет" Ключ Web по телефону
    personal_acc_key_phone = WebElement(id='lk-panel-toggler')

    # ссылка на переход в личный кабинет Ключ Web по телефону
    link_key_phone = WebElement(css_selector='a[href="https://rt.ru/domofon"]')

    # сообщение при неверном пароле
    error_message = WebElement(id='form-error-message')