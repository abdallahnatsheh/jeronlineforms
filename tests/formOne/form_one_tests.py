from utilities.teststatus import TestStatus
import unittest
import pytest
from pages.form_one_page import FormOnePage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class FormOneTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.fo = FormOnePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_form_first_name_input(self):
        self.fo.write_field("fdddfs", self.fo.first_name_field)
        result = self.fo.is_not_valid(self.fo.first_name_field)
        self.ts.mark(result, "First Name Input Verification (supposed not valid)")

        self.fo.write_field("חגדכגדכ", self.fo.first_name_field)
        result1 = self.fo.is_valid(self.fo.first_name_field)
        self.ts.markFinal("test_form_first_name_input", result1, "First Name Input Verification (supposed valid)")

    @pytest.mark.run(order=2)
    def test_form_last_name_input(self):
        self.fo.write_field("fdddfs", self.fo.last_name_field)
        result1 = self.fo.is_not_valid(self.fo.last_name_field)
        self.ts.mark(result1, "Last Name Input Verification (supposed not valid)")

        self.fo.write_field("חגדכגדכ", self.fo.last_name_field)
        result2 = self.fo.is_valid(self.fo.last_name_field)
        self.ts.markFinal("test_form_last_name_input", result2, "Last Name Input Verification (supposed valid)")

    @pytest.mark.run(order=3)
    def test_form_id__input(self):
        self.fo.write_field("fdddfs", self.fo.id_number_field)
        result = self.fo.is_not_valid(self.fo.id_number_field)
        self.ts.mark(result, "ID Input Verification (supposed not valid)")

        self.fo.write_field("hjk", self.fo.id_number_field)
        result1 = self.fo.is_not_valid(self.fo.id_number_field)
        self.ts.mark(result1, "ID Input Verification (supposed not valid)")

        self.fo.write_field("2345", self.fo.id_number_field)
        result2 = self.fo.is_not_valid(self.fo.id_number_field)
        self.ts.markFinal("test_form_id__input", result2, "ID Input Verification (supposed valid)")

    @pytest.mark.run(order=4)
    def test_form_cell_phone_dropdown(self):
        self.fo.select_listbox_item(self.fo.cell_phone_dropdown, "057")
        self.fo.select_listbox_item(self.fo.cell_phone_dropdown, "072")
        self.fo.select_listbox_item(self.fo.cell_phone_dropdown, "077")

        # personal_info_form.select_listbox_item(personal_info_form.phone_number_field_dropdown, "02")
        # personal_info_form.select_listbox_item(personal_info_form.phone_number_field_dropdown, "072")
        # personal_info_form.select_listbox_item(personal_info_form.phone_number_field_dropdown, "000")


'''
def test_form_email__input(driver):
    base_test = BaseTest(driver)
    base_test.setUp()
    personal_info_form = PersonalInfoForm(driver)

    email_examples = [
        "test@example.",
        "test@éxample.com",
        "test@example..com",
        "test@example.c om",
        "test@example.c@m",
        "test@example.c om",
        "test@.com",
        "test@example.com.",
        "test@..com",
        "test@.example.com",
        "test@example@example.com",
        "test@example.c#om",
        "test@example.c$om",
        "test@example.c%om",
        "test@example.c^om",
        "test@example.c&om",
        "test@example.c*om",
        "test@example.c(om",
        "test@example.c)om",
        "test@example.c+om",
        "test@example.c=om",
        "test@example.c{om",
        "test@example.c}om",
        "test@example.c[om",
        "test@example.c]om",
        "test@example.c|om",
        "test@example.c\\om",
        "test@example.c;om",
        "test@example.c'om",
        "test@example.c\"om",
        "test@example.c<om",
        "test@example.c>om",
        "test@example.c,om",
        "test@example.c.om",
        "test@example.c/om",
        "test@example.c?om",
        "test@example.c~om",
        "test@example.c`om",
        "test@example.c!om",
        "test@example.c@om",
        "test@example.c#om",
        "test@example.c$om",
        "test@example.c%om",
        "test@example.c^om",
        "test@example.c&om",
        "test@example.c*om",
        "גדככד",
        "يسبيسبس",
        "3454354353"
    ]
    for email in email_examples:
        personal_info_form.write_field(email, personal_info_form.email_field)
        utils.assert_on_result(personal_info_form.is_valid(personal_info_form.email_field), False,
                               "email supposed to be invalid")

    personal_info_form.write_field("abd@ness.com", personal_info_form.email_field)
    utils.assert_on_result(personal_info_form.is_valid(personal_info_form.email_field), True,
                           "email supposed to be valid")


def test_form_cell_phone_field(driver):
    base_test = BaseTest(driver)
    base_test.setUp()
    personal_info_form = PersonalInfoForm(driver)

    personal_info_form.write_field("dsfds", personal_info_form.cell_phone_field)
    utils.assert_on_result(personal_info_form.is_valid(personal_info_form.cell_phone_field), False,
                           "id supposed to be invalid")
    personal_info_form.write_field("3266520", personal_info_form.cell_phone_field)
    utils.assert_on_result(personal_info_form.is_valid(personal_info_form.cell_phone_field), True,
                           "id supposed to be invalid")

    personal_info_form.write_field("dsfds", personal_info_form.phone_number_field)
    utils.assert_on_result(personal_info_form.is_valid(personal_info_form.phone_number_field), False,
                           "id supposed to be invalid")


def test_form_cell_phone_dropdown(driver):
    base_test = BaseTest(driver)
    base_test.setUp()
    personal_info_form = PersonalInfoForm(driver)
    personal_info_form.select_listbox_item(personal_info_form.cell_phone_dropdown, "057")
    personal_info_form.select_listbox_item(personal_info_form.cell_phone_dropdown, "072")
    personal_info_form.select_listbox_item(personal_info_form.cell_phone_dropdown, "077")

    #personal_info_form.select_listbox_item(personal_info_form.phone_number_field_dropdown, "02")
    #personal_info_form.select_listbox_item(personal_info_form.phone_number_field_dropdown, "072")
    #personal_info_form.select_listbox_item(personal_info_form.phone_number_field_dropdown, "000")
'''
