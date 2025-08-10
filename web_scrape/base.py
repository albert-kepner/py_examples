from dataclasses import dataclass
from pprint import pformat

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from locators import TrackLocator


@dataclass
class Track:
    album: str
    artist: str
    genre: str
    url: str

    def __str__(self):
        return pformat(self)


MAX_WAIT_SECONDS = 10.0
DEFAULT_WINDOW_SIZE = (1920, 3000)


class WebPage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        self._driver.set_window_size(*DEFAULT_WINDOW_SIZE)
        self._driver.implicitly_wait(5)
        self._wait = WebDriverWait(driver, MAX_WAIT_SECONDS)


class WebComponent(WebPage):
    def __init__(self, parent: WebElement, driver: WebDriver) -> None:
        super().__init__(driver)
        self._parent = parent


class BaseTrackElement(WebComponent):
    """Model a playable track on Bandcamp's Discover page."""

    def play(self) -> None:
        """Play the track."""
        if not self.is_playing:
            self._get_play_button().click()

    def pause(self) -> None:
        """Pause the track."""
        if self.is_playing:
            self._get_play_button().click()

    @property
    def is_playing(self) -> bool:
        return "Pause" in self._get_play_button().get_attribute("aria-label")

    def _get_play_button(self):
        return self._parent.find_element(*TrackLocator.PLAY_BUTTON)
