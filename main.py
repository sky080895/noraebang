# # from PyQt5.QtCore import QDir, Qt, QUrl
# # from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# # from PyQt5.QtMultimediaWidgets import QVideoWidget
# # from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
# #         QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
# # from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
# # from PyQt5.QtGui import QIcon
# # import sys
# #
# # from appSettings import *
# # import sys
# # import pytube
# #
# # def download():
# #     url = 'https://youtu.be/kKmG_rl1qZE'  # a is the thing typed in the entry
# #     youtube = pytube.YouTube(url)
# #     youtube.streams.first().download()
# #
# #
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     app_window = App_Window()
# #     # fixedSys25 = Font_Style("fixedSys",25).set()
# #     #
# #     # reserve_button = Button(app_window, "예약", 1000,100,150,75,fixedSys25).set()
# #     # reserve_ahead_button = Button(app_window, "우선예약", 1150,100,150,75,fixedSys25).set()
# #     # cancel_reservation_button = Button(app_window, "예약취소", 1300,100,150,75,fixedSys25).set()
# #     #
# #     # start_button = Button(app_window, "시작", 1000,600,150,75,fixedSys25).set()
# #     # start_button.clicked.connect(download)
# #     #
# #     #
# #     # cancel_button = Button(app_window, "취소", 1150,600,150,75,fixedSys25).set()
# #     # pause_button = Button(app_window, "일시정지", 1300,600,150,75,fixedSys25).set()
# #     #
# #     # pitch_up_button = Button(app_window, "#", 1000,700,200,75,fixedSys25).set()
# #     # pitch_down_button = Button(app_window, "♭", 1000,800,200,75,fixedSys25).set()
# #     # speed_up_button = Button(app_window, "템포▲", 1200,700,200,75,fixedSys25).set()
# #     # speed_down_button = Button(app_window, "템포▼", 1200,800,200,75,fixedSys25).set()
# #
# #     sys.exit(app.exec_())




# #Try with pyqt
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
# import sys
# from appSettings import *
# import pyaudio
# import numpy as np
#
# def rec():
#     CHUNK = 2 ** 11
#     RATE = 44100
#
#     p = pyaudio.PyAudio()
#     stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
#                     frames_per_buffer=CHUNK)
#
#     for i in range(int(10 * 44100 / 1024)):  # go for a few seconds
#         data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
#         peak = np.average(np.abs(data)) * 2
#         bars = "#" * int(50 * peak / 2 ** 16)
#         print("%04d %05d %s" % (i, peak, bars)) #Print the pitch of background sound
#
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
#
# if __name__ == '__main__':
#
#
#     app = QApplication(sys.argv)
#     app_window = App_Window()
#     web = QWebEngineView()
#     web.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
#     web.page().fullScreenRequested.connect(lambda request: request.accept())
#     baseUrl = "local"
#
#
#     htmlString = """
#                 <iframe width="480" height="315" src="https://www.youtube.com/embed/p1ChpMOD0u0" frameborder="0" allowfullscreen></iframe>
#                  """
#
#     # htmlString = """
#     #         <iframe width="560" height="315" src="https://www.youtube.com/embed/kKmG_rl1qZE" frameborder="0" allowfullscreen></iframe>
#     #          """
#     web.setHtml(htmlString, QUrl(baseUrl))
#
#     button = QtWidgets.QPushButton(web)
#     button.setText("pitch setting")
#     button.setGeometry(50,350,150,100)
#     button.clicked.connect(rec)
#
#     web.show()
#     sys.exit(app.exec_())



#Try with tkinter
import tkinter
import pygame
import sounddevice  # pip install sounddevice
import pyaudio
import numpy as np
import time

def play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('aroha.wav')
    pygame.mixer.music.play()
    # data, fs = sf.read('aroha.wav')
    # sd.play(data, fs)
    # sd.wait()


window = tkinter.Tk()

button1 = tkinter.Button(text='play')
button1.config(command= play)
button2 = tkinter.Button(text='rec')
# button2.config(command= rec)
button1.pack()
button2.pack()

window.mainloop()

for i in range (1, 10):
    time.sleep(3)
    print("l")
    window.update()