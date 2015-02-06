from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_root_url_goes_to_home_page_view(self):
        #Erin visits the website:
        self.browser.get('http://localhost:8000')
        #She notices that the title has 'To-Do' in it:
        self.assertIn('To-Do', self.browser.title)


#There is a text box to begin a todo list:

#She fills in the text box with 'Buy peacock feathers':

#She hits Enter and sees the page update with a list that
#says
#'#1 Buy peacock feathers', and there is another textbox.

#Erin enters the next item in her list: 'Tie fly using 
#peackock feathers'.

#She wonders if she can retrieve the list when 
#she comes back to the website:

#She goes back to bed:

if __name__ == '__main__':
    unittest.main(warnings="ignore")


