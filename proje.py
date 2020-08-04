import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import urllib.request
from evds import evdsAPI
import pymongo
import json
import numpy

#Veri Tabanı Bağlantısı
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase1"]
mycol = mydb["customers1"]

#COVİD-19 Verilerini Bilgisayara İndirir.
url= "https://covid.ourworldindata.org/data/ecdc/full_data.csv"
urllib.request.urlretrieve(url,"full_data.csv")

#COVİD-19 Verilerini DateFrame olarak CVD değişkenine atama yapar.
CVD=pd.read_csv('https://covid.ourworldindata.org/data/ecdc/full_data.csv')
CVD=pd.DataFrame(CVD)

#Merkez Bankası Kredi Kart Harcama Verilerini Çeker.
evds = evdsAPI('C6f754HLUA')
api=evds.get_data(['TP.KKHARTUT.KT16'], startdate="10-03-2020", enddate="20-07-2020")
my_dataframe = pd.DataFrame(api)
#Fazla Sütun silindi.
my_dataframe =my_dataframe.drop(columns ="YEARWEEK")
#Tarih Formatı COVID Verileri ile İlişkilendirilmesi için Formatı Değiştirildi.
my_dataframe['Tarih']=[dt.datetime.strptime(x,'%d-%m-%Y')for x in my_dataframe['Tarih']]
#Sütun İsimleri COVID Verileri ile Benzer Olması için Değiştirildi.
my_dataframe.columns=['date','krediCard']

print("KREDi KARTI HARCAMALARI VERİ TİPLERİ")
print(my_dataframe.dtypes)
print("KREDİ KARTI HAFTALIK HARCAMA VERİLERİ")
print(my_dataframe)

#1 Hafta Sonrası ve 2 Hafta Sonrasını Karşılaştırmak için Farklı Değişkenler Atandı.
my_dataframe2=my_dataframe
my_dataframe3=my_dataframe
my_dataframe2['i'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]



#Tarih Formatı EVDS Verileri ile İlişkilendirilmesi için Formatı Değiştirildi.
CVD['date']=[dt.datetime.strptime(x,'%Y-%m-%d')for x in CVD['date']]
#EVDS Verileri Haftalık Olduğu için Tarihler Özel Olarak EVDS Verilerine Göre Ayrıldı.
tarih=['2020-03-13','2020-03-20','2020-03-27','2020-04-03','2020-04-10','2020-04-17','2020-04-24','2020-05-01','2020-05-08','2020-05-15','2020-05-22','2020-05-29','2020-06-05','2020-06-12','2020-06-19','2020-06-26','2020-07-03','2020-07-10','2020-07-17']
#COVID Verileri Dünya Genelinde Olduğu için Türkiye Olarak Ayırıldı Diğer Verilerde.
countries=['Turkey']
CVD_country=CVD[CVD.location.isin(countries)]
CVD_toplam= CVD_country[CVD_country.date.isin(tarih)]

print("COVID-19 VERİ TİPLERİ")
print(CVD_toplam.dtypes)
print("COVID-19 HAFTALIK VERİLERİ")
print(CVD_toplam)

#COVID Verileri ile Kredi Kartı Harcama Verileri Tarihe Göre Birleştirild.
birlesik2=my_dataframe.merge(CVD_toplam, on='date', how='left')
birlesik2 =birlesik2.drop(columns ="i")
print("KREDİ KARTI HARCAMALARI - COVID19 VERİLERİ VERİ TİPLERİ")
print(birlesik2.dtypes)
print("KREDİ KARTI HARCAMALARI - COVID19 VERİLERİ BİRLEŞTİRİLMİŞ HALİ")
print(birlesik2)

#HeatMap tablosu
sns.heatmap(birlesik2.corr(),vmin=-1,vmax=1,annot=True)
plt.show()

#Fazla Olan Sütunlar Silindi.
CVD_toplam =CVD_toplam.drop(columns ="biweekly_deaths")
CVD_toplam =CVD_toplam.drop(columns ="total_cases")
CVD_toplam =CVD_toplam.drop(columns ="total_deaths")
CVD_toplam =CVD_toplam.drop(columns ="new_cases")
CVD_toplam =CVD_toplam.drop(columns ="new_deaths")
CVD_toplam =CVD_toplam.drop(columns ="biweekly_cases")
CVD_toplam =CVD_toplam.drop(columns ="weekly_deaths")

#1 Hafta Sonrası ve 2 Hafta Sonrasını Karşılaştırmak için Farklı Değişkenler Atandı.
CVD_toplam2=CVD_toplam
CVD_toplam3=CVD_toplam
CVD_toplam2['i'] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]


#Asıl İstenilen Veriler Birleştirildi.
birlesik=my_dataframe.merge(CVD_toplam, on='date', how='left')
birlesik =birlesik.drop(columns ="i_x")
birlesik =birlesik.drop(columns ="i_y")
print("COVID - KREDİ KARTI HARCAMA VERİ TİPLERİ")
print(birlesik.dtypes)
print("COVID HAFTALIK VAKA SAYISI - HAFTALIK KREDİ KARTI HARCAMA VERİSİ")
print(birlesik)


print("ASIL İSTENİLEN KORELASYON")
print(birlesik.corr())

birlesik.plot(x='weekly_cases',y='krediCard',style='*')
plt.show()

sns.heatmap(birlesik.corr(),vmin=-1,vmax=1,annot=True)
plt.show()

sns.relplot(x='weekly_cases',y='krediCard',kind='line',data=birlesik)
plt.show()

sns.catplot(x='weekly_cases',y='krediCard',data=birlesik)
plt.show()

sns.barplot(x='weekly_cases',y='krediCard',data=birlesik)
plt.show()

#Kredi Kartı Harcamaları ile Bir Hafta Sonraki Vaka Sayılarının İlişkisi
birlesik3=my_dataframe2.merge(CVD_toplam2, on='i', how='left')
birlesik3=birlesik3.drop(columns ="i")
print("KREDİ KARTI HARCAMALARI İLE BİR HAFTA SONRAKİ VAKA SAYILARI")
print(birlesik3)

print("KREDİ KARTI HARCAMALARI BİR HAFTA SONRAKİ VAKA SAYILARI KORELASYONU")
print(birlesik3.corr())

birlesik3.plot(x='weekly_cases',y='krediCard',style='*')
plt.show()

sns.heatmap(birlesik3.corr(),vmin=-1,vmax=1,annot=True)
plt.show()

#Kredi Kartı Harcamaları ile İki Hafta Sonraki Vaka Sayılarının İlişkisi
my_dataframe3['i'] = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
CVD_toplam3['i'] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

birlesik4=my_dataframe3.merge(CVD_toplam3, on='i', how='left')
birlesik4 =birlesik4.drop(columns ="i")
print("KREDİ KARTI HARCAMALARI İKİ HAFTA SONRAKİ VAKA SAYILARI")
print(birlesik4)

print("KREDİ KARTI HARCAMALARI İKİ HAFTA SONRAKİ VAKA SAYILARI KORELASYONU")
print(birlesik4.corr())

birlesik4.plot(x='weekly_cases',y='krediCard',style='*')
plt.show()

sns.heatmap(birlesik4.corr(),vmin=-1,vmax=1,annot=True)
plt.show()

#Mongodb ye Tabloları(DataFrame) Json Olarak Kaydedilmektedir.
records=json.loads(birlesik.T.to_json()).values()
x=mycol.insert_many(records)
y=mycol.find_one()
print(y)
print("MONGODB YE VERİLER BAŞARILI BİR ŞEKİLDE KAYDEDİLDİ...")

#Mongodb ye Tabloları(DataFrame) Json Olarak Kaydedilmektedir.
records=json.loads(birlesik3.T.to_json()).values()
x=mycol.insert_many(records)
y=mycol.find_one()
print(y)
print("MONGODB YE VERİLER BAŞARILI BİR ŞEKİLDE KAYDEDİLDİ...")

#Mongodb ye Tabloları(DataFrame) Json Olarak Kaydedilmektedir.
records=json.loads(birlesik4.T.to_json()).values()
x=mycol.insert_many(records)
y=mycol.find_one()
print(y)
print("MONGODB YE VERİLER BAŞARILI BİR ŞEKİLDE KAYDEDİLDİ...")