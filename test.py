from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-headless')
firefox = Firefox(executable_path='geckodriver', firefox_options=options)
