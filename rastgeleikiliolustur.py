# -*- coding: utf8 -*-

 #365000 adet kulanıcı ikilisi oluşturan scripttir. tek basina calistirilir. üretim yapılırken bu çalışmada bulunmayan 20819 21354 id lerinin kullanılması (while blogu ile) önlenir.
 #oluşturulan kullanıcılar ekrana yazdırılır. format =>  kullanici1,kullanici2
import random
import numpy as mp

# users=[range(1,22167)]
# print users
users=[]
for i in range (0,365000):

    u1=random.randint(1,22166)
    u2=random.randint(1,22166)
    while u1==u2 or u1==20819 or u2==20819 or u1==21354 or u2==21354:
        u1=random.randint(1,22166)
        u2=random.randint(1,22166)
    print str(u1)+','+str(u2)


