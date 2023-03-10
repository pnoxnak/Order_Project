# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 21:23:04 2023

@author: Mükremin AKKAYA
"""

# pizza sınıflarının, pizza, sos ve fatura fonksiyonlarını içeren src dosyası ile 
# fatura fonksiyonunda sipariş tarihi için kullanılacak datetime modülleri içe aktarılıyor.
import src
import datetime



if __name__ == "__main__":

# Burada yazi adında bir değiken tanımladım. Sonra da bu değişkene for döngüsü ile Menu.txt dosyasındaki yazıları atadım.
    yazi=""
    with open("Menu.txt","r") as file:
        for i in file:
            yazi+=i

    print(yazi)
# y adında bir değişken oluşturdum ve bu değişken src dosyasındaki Select_pizza() fonksiyonundan dönen class değerini saklayacak.
    y = src.Select_pizza()
# Sonra ise dönen class değerini Select_Sauce fonksiyonuna parametre olarak verip burdan dönen class değeri de yine y değişkenine atadım 
    y = src.Select_Sauce(y)
    
# Seçimden sonra y nesnesine ait olan get_description ve 
# get_cost fonksiyonlarını kullanarak kullanıcıya seçimini onaylaması için  seştiklerini gösteriyorum.
    print("Your pizza: ",y.get_description())
    print("Cost: ",y.get_cost())
    confirm = input("Do you confirm?( 'y' for confirm/ 'n' for cancel):")
# Eğer kullanıcı onaylamazsa siparişin iptal edildiğini söyleyip programı sonlandırıyorum.
# Onaylarsa kullanıcıdan isim, id numarası, kredi kart numarası ve kart şifresini girmesini istiyorum.
# En son ise teşekkür edip kullanıcıdan aldığım bilgileri ve sipariş tarihini src modülünde olan invoice fonksiyonuyla fatura veritabanı dosyasına kayıt ediyorum.
    if confirm == "y" or "Y":

        isim=input("[+]Please enter your name and surname: ")
        id=input("[+]Please enter your name and user id: ")
        ccno=input("[+]Please enter your credit card number: ")
        input("[+]Please enter your card password: ")
        print("Your order has been queued, please wait.")
        print("Thank you for choosing us!")
        
        src.invoice(isim,id,ccno,y.get_description(),datetime.datetime.now())

    else:
        print("Order canceled!")
        exit()
            
    
            
            
            