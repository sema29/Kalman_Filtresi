degisken  = { "eski_kalman_tahmin" : 0, "kalman_katsayisi" : 0.1, "hata_kovaryansi_eski" : 1 }
olculen_veri =  [0.49, 0.50 ,0.48 ,0.29 ,0.25, 0.32, 0.42, 0.48, 0.41, 0, 0.10, 0.20, 1, 1.5 ,1.7, 0.39, 0.50, 0.48, 0.29, 0.25, 0.32, 0.41 ]
yeni_veri = [None] * len(olculen_veri)
sayi = len(olculen_veri)




def  KalmanFiltresiHesapla(olculen_veri,kalman_katsayisi):

#Güncelleme--Eski değerleri yeni değerler içine atıyor.
    X_k_KalmanTahminYeni = degisken["eski_kalman_tahmin"]
    Pk_HataKovaryansiYeni = degisken["hata_kovaryansi_eski"]
#Ölçümleri Düzeltme--
    Kk_KalmanKazanci = Pk_HataKovaryansiYeni / (Pk_HataKovaryansiYeni + kalman_katsayisi)
    Xk_KalmanHesaplanan = X_k_KalmanTahminYeni + Kk_KalmanKazanci * (olculen_veri - X_k_KalmanTahminYeni)
    Pk_HataKovaryansiYeni = (1 - Kk_KalmanKazanci) * degisken["hata_kovaryansi_eski"]
#Eski Değerleri Atama--bu değişkenler Global tanımlandı. bu procedure her geldiğinde bunları kaybetmemelidir.
    hata_kovaryansi_eski =Pk_HataKovaryansiYeni
    eski_kalman_tahmin= Xk_KalmanHesaplanan
#bulunan sonuç bir sonraki adım için eski tahmin olacak.
    return Xk_KalmanHesaplanan


for i in range (sayi):

    yeni_veri[i]=KalmanFiltresiHesapla(olculen_veri[i],degisken["kalman_katsayisi"])


print(yeni_veri)
