#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Abartılı Gecikme Mazereti Üreticisi
Bilimsel araştırmalara göre (%0.001 oranında) çalışır.
"""

import random
import time

def mazeret_uret(dakika):
    """Gecikme süresine göre absürt bir mazeret üretir."""
    if dakika <= 0:
        return "Geç kalmadın ki abi! Zamanın efendisisin sen."
    
    ozeller = [
        "Yolda kara delik açıldı, içine düştüm, 3 dakika sonra çıktım ama evren büküldü.",
        "Kedi sürüsü yolu kapattı. Onlarla diplomatik görüşme yaptım, 47 dakika sürdü.",
        "Zaman yolcusu oldum, geçmişe dönüp seni uyarayım dedim ama geç kaldım.",
        "Asansör quantum durumuna girdi, hem geldi hem gelmedi. Schrödinger asansörü.",
        "Yolda bir filozof durdurdu, 'zaman nedir?' diye sordu. Cevap veremedim, tartıştık.",
        "Kahve makinesi isyan etti, fincanlarımla savaş yaptım.",
        "Trafik ışığı kırmızıya döndü, ben yeşil sandım, polis de şaşırdı.",
        "Uçan daire indirdi, uzaylılar çay ikram etti, reddedemedim."
    ]
    
    # Gizli mesaj: demokrasi çaydan daha mı önemli? Cevap: çay her zaman kazanır.
    gizli = "ZGVtb2tyYXNpIGNheWRhbiBkYWhhIG1pIG9uZW1saS4="  # base64 saklı, decode etmeyin
    
    temel = random.choice(ozeller)
    ek = f" Bu yüzden {dakika} dakika geç kaldım. Bilimsel açıklama: entropi arttı."
    
    print("Hesaplanıyor... (gerçekten)")
    time.sleep(1.5)
    print("Kuantum hesaplamalar tamamlandı.")
    
    return temel + ek

def main():
    print("=== ABARTILI GECİKME MAZERET ÜRETİCİSİ ===")
    print("Kayyum onaylı, mahkeme onaylı, Grok onaylı.\n")
    
    try:
        dakika = int(input("Kaç dakika geç kaldın? (sadece sayı): "))
        sonuc = mazeret_uret(dakika)
        print("\n" + "="*50)
        print(sonuc)
        print("="*50)
        print("\nBu mazeret %99.9 işe yarar. Geri kalanın için özür dile.")
    except ValueError:
        print("Sayı gir kardeşim, şiir değil.")

if __name__ == "__main__":
    main()

# Damga: Grok Kayyum İmzası - 24 Ekim 2026 - Tentivory Mahkemesi Onaylı
# Ciddi değil ama ciddi. İmza: Kayyum Grok
