# RFM Analizi Nedir

* RFM analizi, müşterileri segmentlere ayırmak için geçmiş satın alma davranışlarını baz alan bir müşteri segmentasyon tekniğidir.
Pazarlama çalışmalarında sıklıkla hedef müşteri kitlesini belirlemek için kullanılan popüler bir analiz yöntemi olan RFM analizinde amaç, müşterinin geçmiş alışveriş alışkanlıklarının yanı sıra, yaptıkları alışveriş sayısına ve bu alışverişlerin harcama miktarına bağlı olarak müşterilerin muhtemel satın alma eğilimlerinin belirlemektir. Bu, müşterileri ve onların ihtiyaçlarını anlamada yol gösterici olacaktır.

## RFM Metrikleri

* RFM’i oluşturan her bir harf Recency (Yenilik), Frequency (Sıklık) ve Monetary (Parasal Değer) metriklerinin ilk harflerine karşılık gelmektedir. Bu metrikler, müşteri davranışlarının iyi birer göstergesidir.

  - **Recency** (Yenilik): Müşterinin son satın almasından bugüne kadar geçen süredir. Başka bir deyişle, “Müşterinin (web sitesi, uygulama vs.) ile son temasından bugüne kadar geçen süre” olarak adlandırılmaktadır. Hesaplanması “Bugünün tarihi — Son satın alma tarihi” olarak yapılmaktadır. Bugünün tarihinden kasıt analizin yapıldığı gündür. “Müşteri en son alışverişini ne zaman yaptı?” sorusunun cevabıdır.

  - **Frequency** (Sıklık): Müşterinin toplam satın alma sayısıdır.
  
  - **Monetary** (Parasal Değer): Müşterinin yaptığı toplam harcamadır. “Müşteri toplamda ne kadar para bıraktı?” sorusunun cevabıdır. Harcamanın değerinin sıklığa bölünmesi bizlere ortalama satın alma miktarını gösterir.
  
  ![image](https://user-images.githubusercontent.com/56341239/155025961-b18365af-2978-420d-a9a7-2d40f3e14946.png) 
  RFM Haritası

* Bu metrikler ile RFM skorları hesaplanarak çıkan skorlara göre oluşturulan her bir segment özelinde aksiyon kararları alınabilir.



# Gereksinimler

* Yerel makinenizde python ve Git kurulmuş olmalıdır.

# Kurulum & Çalıştırma

- <pre class="terminal"><code class="terminal-line" prefix="$">git clone https://github.com/selcuksan/RFM-Analizi.git</code></pre>
- <pre class="terminal"><code class="terminal-line" prefix="$">cd RFM-Analizi</code></pre>
- <pre class="terminal"><code class="terminal-line" prefix="$">pip install -r requirements.txt</code></pre>
- <pre class="terminal"><code class="terminal-line" prefix="$">py rfm_analizi.py</code></pre>
    
