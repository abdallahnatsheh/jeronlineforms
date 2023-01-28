from selenium.webdriver.common.by import By


class FormOneLocator(object):
    # Locators for Jeronlineforms Form
    Fname = 'שם פרטי'
    Lname = 'שם משפחה'
    IDnumber = 'מספר ת.ז.'
    Email = 'דוא"ל'
    CPhone = "cellphone"
    Phone = "phone"

    # form
    first_name_input = {
        'By': "xpath",
        'Value': f"//label[contains(text(),'{Fname}')]/following-sibling::input",
        'Value_valid': f"//label[contains(text(),'{Fname}')]/following-sibling::input[contains(@class, 'ng-valid')]",
        'Value_invalid': f"//label[contains(text(),'{Fname}')]/following-sibling::input[contains(@class, 'ng-invalid')]"
    }
    last_name_input = {
        'By': "xpath",
        'Value': f"//label[contains(text(),'{Lname}')]/following-sibling::input",
        'Value_valid': f"//label[contains(text(),'{Lname}')]/following-sibling::input[contains(@class, 'ng-valid')]",
        'Value_invalid': f"//label[contains(text(),'{Lname}')]/following-sibling::input[contains(@class, 'ng-invalid')]"
    }
    id_number = {
        'By': "xpath",
        'Value': f"//label[contains(text(),'{IDnumber}')]/following-sibling::input",
        'Value_valid': f"//label[contains(text(),'{IDnumber}')]/following-sibling::input[contains(@class, 'ng-valid')]",
        'Value_invalid': f"//label[contains(text(),'{IDnumber}')]/following-sibling::input[contains(@class, 'ng-invalid')]"
    }
    email = {
        'By': "xpath",
        'Value': f"//label[contains(text(),'{Email}')]/following-sibling::input",
        'Value_valid': f"//label[contains(text(),'{Email}')]/following-sibling::input[contains(@class, 'ng-valid')]",
        'Value_invalid': f"//label[contains(text(),'{Email}')]/following-sibling::input[contains(@class, 'ng-invalid')]"
    }
    cell_phone_number = {
        'By': "xpath",
        'Value': f"//input[@id='{CPhone}']",
        'Value_valid': f"//input[@id='{CPhone}' and contains(@class, 'ng-valid')]",
        'Value_invalid': f"//input[@id='{CPhone}' and contains(@class, 'ng-invalid')]"
    }
    cell_phone_number_dropdown = {
        'By': "xpath",
        'Value': f"//input[@id='{CPhone}']/following-sibling::p-dropdown",
        'Value_list': f"//input[@id='{CPhone}']/following-sibling::p-dropdown//ul//p-dropdownitem"
    }
    phone_number = {
        'By': "xpath",
        'Value': f"//input[@id='{Phone}']",
        'Value_valid': f"//input[@id='{Phone}' and contains(@class, 'ng-valid')]",
        'Value_invalid': f"//input[@id='{Phone}' and contains(@class, 'ng-invalid')]"
    }
    phone_number_dropdown = {
        'By': "xpath",
        'Value': f"//input[@id='{Phone}']/following-sibling::p-dropdown",
        'Value_list': f"//input[@id='{Phone}']/following-sibling::p-dropdown//ul//p-dropdownitem"
    }
