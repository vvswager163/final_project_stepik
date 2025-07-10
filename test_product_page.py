import time
import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

from .links import login_link, product_link


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, login_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "cjfifp1234567a")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, login_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.add_to_cart()
        page.success_message_came_out()
        page.should_be_correct_product_in_cart()
        page.should_be_correct_price_product()


@pytest.mark.skip
@pytest.mark.parametrize('link_param',
                         ["?promo=offer0",
                          "?promo=offer1",
                          "?promo=offer2",
                          "?promo=offer3",
                          "?promo=offer4",
                          "?promo=offer5",
                          "?promo=offer6",
                          pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                          "?promo=offer8",
                          "?promo=offer9",
                          "?promo=newYear",
                         "?promo=newYear2019"])
def test_guest_can_add_product_to_basket(browser, link_param):
    link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/{link_param}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.success_message_came_out()
    page.should_be_correct_product_in_cart()
    page.should_be_correct_price_product()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.empty_basket()
    basket_page.text_about_empty_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_to_cart()
    page.succes_message_should_dissapear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()