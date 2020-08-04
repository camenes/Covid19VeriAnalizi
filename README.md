# Covid19VeriAnalizi
COVID-19 vakaları ile kredi kartı harcamaları arasındaki korelasyon analizi
GEREKLİLİKLER
1- pandas: kullanılacak olan verileri dataframe olarak dönüştürmek için kullanılan ve veri analizi için kullanılan kütüpanedir.
2- datetime: tarih formatını değiştirmek için kullanılacak kütüpanedir.
3- matplotlib: veri görselleştirmesinde kullandığımız temel python kütüphanesidir. 2 ve 3 boyutlu çizimler yapmamızı sağlar. Matplotlib genelde 2 boyutlu çizimlerde kullanılır.
4- seaborn: Seaborn, Matplotlib kütüphanesine yüksek seviye arayüz sağlayan bir kütüphanedir. Seaborn ile;Estetik olarak hoş olan varsayılan temaları kullanma, Özel olarak renk paleti belirleme,Göz alıcı istatistiksel grafikler yapma,Dağılımları kolayca ve esnek bir şekilde sergileme,Matris ve DataFrame içindeki bilgileri görselleştirme yapılabilir.
5- evdsAPI: Türkiye Merkez Bankası verilerini çekmek için kullanılan kütüpane.
7- pymongo: Verileri kaydetmek için kullanılan mongodb ile bağlantı kurmasını sağlayan kütüpanedir.
8- json: Mongodb ye kaydedilen verileri jsona çevirmek için kullanılan kütüpanedir.
9- Docker: uygulamalarınızı hızla derlemenize, test etmenize ve dağıtmanıza imkan tanıyan bir yazılım platformudur. Docker kurulumu(ubuntu):https://docs.docker.com/engine/install/ubuntu/
10- Docker Mongodb: doküman tabanlı, C++ ile geliştirilmiş açık kaynak, NoSQL veritabanı uygulamasıdır. MongoDB, verileri JSON tipinde dokümanlarda saklamaktadır, anlamsal alanları dokümandan dokümana değişir ve veri yapısı zaman içinde değiştirilebilir. Docker içine mongodb kurulumu:https://hub.docker.com/_/mongo
