import instaloader
import pandas as pd
from datetime import datetime
import locale

#türkçe günleri ve ayları göstermek için komut düzeltmek
locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')

#instaloader kütüphanesinden örnek oluşturmak
L = instaloader.Instaloader()

#kullanıcı adını al
username = input("Kullanıcı adınızı giriniz: ")
cont = int(input("Kaç adet gönderiniz analiz edilsin?"))
