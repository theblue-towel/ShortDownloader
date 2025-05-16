
from downloader import Downloader
import threading

class Threader:

     def __init__(self):
          self.threads = []

     def loop(self, CHANNEL_HANDLES):
          print('Creating threads..')

          def submitOneSet(CHANNEL_HANDLE):
               downloader = Downloader()
               downloader.process_channel(CHANNEL_HANDLE)

          print('Created threads..')

          for i in CHANNEL_HANDLES:

               t = threading.Thread(target=submitOneSet, args=(i, ))
               t.start()
               self.threads.append(t)

          print('Started threads..')

          for thread in self.threads:
               thread.join()