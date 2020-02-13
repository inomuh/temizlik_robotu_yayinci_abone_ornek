#!/usr/bin/env python
# coding=utf-8

import rospy
from temizlik_robotu_yayinci_abone_ornek_msgs.msg import MesafeBilgisiOrnek
import random

class TemizlikRobotuYayinciOrnek(object):
    def __init__(self):
        self.toplam_mesafe = 0

        self.ana_fonksiyon()


    def ana_fonksiyon(self):
        mesafe_hesabi_yayini = rospy.Publisher('/mesafe_hesabi_ornek', MesafeBilgisiOrnek, queue_size=10)

        # Saniyede 2 defa "while not rospy.is_shutdown()" döngüsü içindeki işlemleri gerçekleştirmektedir.
        rate = rospy.Rate(2)

        mesafe_hesap_mesaji = MesafeBilgisiOrnek()

        while not rospy.is_shutdown():
            # Döngüye her girdiğinde mesafe_hesaplama_fonksiyonu çağırılarak toplam_mesafe değişkenine eklenmektedir.
            self.toplam_mesafe += self.mesafe_hesaplama_fonksiyonu()
            mesafe_hesap_mesaji.mesafe_bilgisi = self.toplam_mesafe
            rospy.loginfo(mesafe_hesap_mesaji)
            mesafe_hesabi_yayini.publish(mesafe_hesap_mesaji)

            rate.sleep()


    def mesafe_hesaplama_fonksiyonu(self):
        # 10 ve 100 arasında rastgele float değer üretir.
        rastgele_deger = random.uniform(10, 100)

        return rastgele_deger


if __name__ == '__main__':
    try:
        rospy.init_node('temizlik_robotu_yayinci_ornek_dugumu', anonymous=True)

        # TemizlikRobotuYayinciOrnek() sınıfını çağırmaktadır.
        dugum = TemizlikRobotuYayinciOrnek()

    except rospy.ROSInterruptException:
        pass
