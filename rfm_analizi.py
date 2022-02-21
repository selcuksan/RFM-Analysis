# Kütüphaneleri yüklüyoruz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns

df = pd.read_excel("online_retail_II.xlsx")

# Toplam harcamayı sütun olarak ekliyoruz
df["Total_price"] = df["Price"] * df["Quantity"]

# Sipariş tarihinin tipini datetime olarak değiştiriyoruz
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Bugün bilgisini today değişkenine kaydediyoruz
today = dt.datetime(2010, 12, 31, 0, 0)

# 0'dan büyük verileri alıyoruz.
data = df[(df["Quantity"] > 0) & (df["Total_price"] > 0)]

# Receny ve Monetary değerlerini hesaplıyoruz

data_x = data.groupby('Customer ID').agg({
    'InvoiceDate': lambda x: (today - x.max()).days,
    'Total_price': 'sum'
})

data_y = data.groupby(["Customer ID", "Invoice"]).agg({
    'Total_price': lambda x: x.sum()
})

data_z = data_y.groupby("Customer ID").agg({
    'Total_price': lambda x: len(x)
})

rfm_data = pd.merge(data_x, data_z, on="Customer ID")
rfm_data.columns = ["Recency", "Monetary", "Frequency"]


# Frequency hesaplama
def RScore(x, p, d):
    if x <= d[p][0.20]:
        return 0
    elif x <= d[p][0.40]:
        return 1
    elif x <= d[p][0.60]:
        return 2
    elif x <= d[p][0.80]:
        return 3
    else:
        return 4


quantiles_df = rfm_data.quantile(q=[0.20, 0.40, 0.60, 0.80])

quantiles_dict = quantiles_df.to_dict()

rfm_data["Freq_Tile"] = rfm_data['Frequency'].apply(RScore, args=('Frequency', quantiles_df))

# Recency hesaplama
rfm_data = rfm_data.sort_values('Recency', ascending=True)
rfm_data["Rec_Tile"] = pd.qcut(rfm_data["Recency"], 5, labels=False)

# Monetary Hesaplama
rfm_data["Mone_Tile"] = pd.qcut(rfm_data["Monetary"], 5, labels=False)

# 'Sıfır' değerinin yer almaması için bulduğumuz değerleri 1 arttırıyoruz
rfm_data['Rec_Tile'] = rfm_data['Rec_Tile'] + 1
rfm_data['Freq_Tile'] = rfm_data['Freq_Tile'] + 1
rfm_data['Mone_Tile'] = rfm_data['Mone_Tile'] + 1

# rfm_data['RFM Score'] = rfm_data['Rec_Tile'].apply(str) + (rfm_data['Freq_Tile']).apply(str) + (rfm_data['Mone_Tile']).apply(str)
rfm_data['RFM Score'] = (rfm_data['Rec_Tile'] * 0.33) + (rfm_data['Freq_Tile'] * 0.33) + (rfm_data['Mone_Tile'] * 0.34)


# müşterileri rfm score'una göre segmentlere ayırıyoruz
def segment_customer(rfm_score):
    if rfm_score <= 1:
        return 'hibernating'
    if rfm_score <= 2:
        return 'at_Risk'
    if rfm_score <= 3:
        return 'need_attention'
    if rfm_score <= 4:
        return 'loyal_customers'
    if rfm_score <= 5:
        return 'champions'


rfm_data["segment"] = rfm_data['RFM Score'].map(segment_customer)

plt.figure(figsize=(10, 5))
rfm_data.segment.value_counts().plot.bar();

plt.show()

segmented_groups = rfm_data.groupby(['segment']).agg({
    'Recency': ['mean', 'min', 'max', 'count'],
    'Frequency': ['mean', 'min', 'max', 'count'],
    'Monetary': ['mean', 'min', 'max', 'count']
}).round(1)
print(segmented_groups.head())
