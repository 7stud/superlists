from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_a_list_and_retrieve_it_later(self):
        #Erin visits the website:
        self.browser.get('http://localhost:8000')
        #She notices that the title and header have 'To-Do' in them:
        self.assertIn('To-Do lists', self.browser.title)
        #self.fail("Finish the tests!")
        header = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do lists', header)


        #There is a text box to begin a todo list:
        textfield = self.browser.find_element_by_id('new_item')
        self.assertEqual(
            textfield.get_attribute('placeholder'), 
            'Enter a to-do item',
        )

        #She fills in the text box with 'Buy peacock feathers':
        textfield.send_keys('Buy peacock feathers')

        #She hits Enter and sees the page update with a list that
        #says '#1 Buy peacock feathers'.
        textfield.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('list')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        #Erin notices there is another textbox displayed. She enters 
        #the next item in her list: 'Tie fly using peackock feathers'.
        self.fail("Finish the tests!")

#She wonders if she can retrieve the list when 
#she comes back to the website:

#She goes back to bed:

if __name__ == '__main__':
    unittest.main(warnings="ignore")


