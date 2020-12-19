
class AddTask():

	def __init__(self, driver):
		self.driver = driver
		self.textbox_name = 'content'
		self.submit_button_name = 'submit'

	def enter_task(self, task):

		self.driver.find_element_by_name(self.textbox_name).send_keys(task)

	def click_submit(self):
		self.driver.find_element_by_name(self.submit_button_name).click(0)
			