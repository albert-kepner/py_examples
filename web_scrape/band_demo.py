from selenium.webdriver import Chrome
from pages import DiscoverPage
import time

BANDCAMP_DISCOVER_URL = "https://bandcamp.com/discover/"
## driver = Firefox()
driver = Chrome()
driver.get(BANDCAMP_DISCOVER_URL)

page = DiscoverPage(driver)

time.sleep(5)

track_1 = page.discover_tracklist.available_tracks[1]
track_1.play()
time.sleep(6)
track_1.pause()
time.sleep(3)

page._driver.quit()