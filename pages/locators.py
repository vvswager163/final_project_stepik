from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS = (By.XPATH, "//input[@name='registration-email']")
    PASSWORD = (By.XPATH, "//input[@name='registration-password1']")
    PASSWORD_CONFIRM = (By.XPATH, "//input[@name='registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators():
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    ADD_TO_CART = (
        By.XPATH,
        "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"
    )
    PRODUCT_IN_CART = (By.CSS_SELECTOR, "div.alertinner strong")
    CART_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")


class BasketPageLocators():
    TEXT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_IN_BASKET = (By.CLASS_NAME, "basket-items")