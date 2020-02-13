#!/usr/bin/env python
# coding=utf-8

import rospy

from temizlik_robotu_yayinci_abone_ornek_msgs.msg import MesafeBilgisiOrnek
import random

class TemizlikRobotuAboneOrnek(object):
    def __init__(self):

        self.ana_fonksiyon()


    def ana_fonksiyon(self):
        rospy.Subscriber('/mesafe_hesabi_ornek', MesafeBilgisiOrnek, self.mesafe_hesabi_callback_fonksiyonu)

        rospy.spin()


    def mesafe_hesabi_callback_fonksiyonu(self, mesafe_bilgisi_mesaji):
        # mesafe_bilgisi_mesaji mesajinın içeriğini okur.
        print("\n")
        print("Okunan deger = " + str(mesafe_bilgisi_mesaji.mesafe_bilgisi))
        print("\n\n\n")


if __name__ == '__main__':
    try:
        rospy.init_node('temizlik_robotu_abone_ornek_dugumu', anonymous=True)

        # TemizlikRobotuAboneOrnek() sınıfını çağırmaktadır.
        dugum = TemizlikRobotuAboneOrnek()

    except rospy.ROSInterruptException:
        pass
