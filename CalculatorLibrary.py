from appium import webdriver


class CalculatorLibrary:

    BUTTON_IDS = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "0": "Zero",
        "+": "Plus",
        "-": "Minus",
        "=": "Equals"
    }

    def __init__(self):
        desired_caps = {
            "app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        }

        self._driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)

    def press(self, button):
        button_id = self.BUTTON_IDS[button]
        self._driver.find_element_by_name(button_id).click()

    def result_should_be(self, expected):
        displaytext = self._driver.find_element_by_accessibility_id("CalculatorResults").text
        displaytext = displaytext.strip("Display is").strip()
        if displaytext != expected:
            raise AssertionError(displaytext)
