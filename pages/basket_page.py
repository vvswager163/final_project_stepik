from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCT_IN_BASKET
        ), "Some item in basket now!"

    def text_about_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.TEXT_IN_BASKET
        ), "Text not found"