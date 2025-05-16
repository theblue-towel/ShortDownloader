import os
import time
import random
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import WebDriverException
import yt_dlp

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('shorts_downloader.log')]
)

class Downloader:
    def __init__(self):
        self.MAX_DOWNLOADS = 50
        self.OUTPUT_DIR = "shorts"
        self.user_agents = [
            "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"
        ]
        self.driver = None

    def _init_driver(self):
        try:
            options = Options()
            options.set_preference("general.useragent.override", random.choice(self.user_agents))
            options.set_preference("dom.webdriver.enabled", False)
            options.set_preference("privacy.resistFingerprinting", True)
            return webdriver.Firefox(options=options)
        except WebDriverException as e:
            logging.error(f"Driver init failed: {e}")
            return None

    def _get_shorts_links(self):
        try:
            return WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href*='/shorts/']"))
            )
        except Exception as e:
            logging.error(f"Failed to find shorts: {e}")
            return None

    def _download_video(self, url):
        try:
            ydl_opts = {
                'outtmpl': os.path.join(self.OUTPUT_DIR, '%(id)s.%(ext)s'),
                'quiet': True,
                'ignoreerrors': True
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            return True
        except Exception as e:
            logging.error(f"Download failed: {e}")
            return False

    def _human_scroll(self):
        try:
            ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(random.uniform(1, 3))
        except Exception as e:
            logging.error(f"Scroll failed: {e}")

    def process_channel(self, channel_identifier):
        self.driver = self._init_driver()
        if not self.driver:
            return False

        try:
            # Load channel page
            self.driver.get(f"https://www.youtube.com/{channel_identifier}/shorts")
            
            # Get initial shorts
            short_links = self._get_shorts_links()
            if not short_links:
                logging.error("No shorts found")
                return False

            # Start download loop
            downloaded = set()
            self.driver.get(short_links[0].get_attribute('href'))
            
            while len(downloaded) < self.MAX_DOWNLOADS:
                current_url = self.driver.current_url
                if "/shorts/" in current_url and current_url not in downloaded:
                    if self._download_video(current_url):
                        downloaded.add(current_url)
                        time.sleep(random.uniform(2, 5))
                    
                self._human_scroll()

            return True

        except Exception as e:
            logging.error(f"Processing failed: {e}")
            return False
        finally:
            self.driver.quit()
            logging.info("Driver cleanup complete")

# Single argument entry point
def download_shorts(channel_identifier):
    downloader = Downloader()
    return downloader.process_channel(channel_identifier)