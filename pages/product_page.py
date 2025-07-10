from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()

    def should_be_correct_product_in_cart(self):
        product = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        )
        product_from_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_IN_CART
        )
        assert product.text == product_from_message.text, (
                "Product name incorrect"
            )

    def should_be_correct_price_product(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        )
        message_price_in_cart = self.browser.find_element(
            *ProductPageLocators.CART_PRICE
        )
        assert product_price.text == message_price_in_cart.text, (
                "Price is incorrect"
            )

    def success_message_came_out(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_IN_CART
        ), "Success message didn't come out"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.PRODUCT_IN_CART
        ), "Success message is presented, but should not be"

    def succes_message_should_dissapear(self):
        assert self.is_disappeared(
            *ProductPageLocators.PRODUCT_IN_CART
        ), "Success message hasn't disappeared"