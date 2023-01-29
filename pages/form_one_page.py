from locators.form1_locators import FormOneLocator as locator
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class FormOnePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.first_name_field = locator.first_name_input
        self.last_name_field = locator.last_name_input
        self.id_number_field = locator.id_number
        self.email_field = locator.email
        self.cell_phone_field = locator.cell_phone_number
        self.cell_phone_dropdown = locator.cell_phone_number_dropdown
        self.phone_number_field = locator.phone_number
        self.phone_number_field_dropdown = locator.phone_number_dropdown

    def write_field(self, data, input_field):
        self.sendKeys(data, input_field['Value'], input_field['By'])

    def is_valid(self, input_field):
        result = self.isElementPresent(input_field['Value_valid'], input_field['By'])
        return result

    def is_not_valid(self, input_field):
        result = self.isElementPresent(input_field['Value_invalid'], input_field['By'])
        return result

    def get_dropdown_list(self, input_field):
        return self.getElementList(input_field['Value_list'], input_field['By'])

    def click_dropdown(self, input_field):
        self.elementClick(input_field['Value'], input_field['By'])

    def select_listbox_item(self, input_field, number):
        self.click_dropdown(input_field)
        items = self.get_dropdown_list(input_field)

        for item in items:
            if item.text == str(number):
                item.click()
                return True
        else:
            self.click_dropdown(input_field)
            self.log.error("No matching item found with dropdown locator : " + input_field['Value_list'] +
                           " and  locatorType: " + input_field['By'] + "for number : " + number)
            return False
