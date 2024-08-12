print("""+------------------------------------+ 
|#####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW| 
|#####|<(*****`s HOME - No Aliens !)>| 
|#####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW| 
|#####|WWWWWWWWWW.----.WWWWWWWWWWWWWW| 
|#####|WWWWWWWW,'  ||  `.WWWWWWWWWWWW| 
|#####|WWWWWWWI    ||    IWWWWWWWWWWW| 
|#####|WWWWWWWI    ||    IWWWWWWWWWWW| 
|#####|WWWWWWWI    ||    IWWWWWWWWWWW| 
|#####|WWWWWWWI   _||_   IWWWWWWWWWWW| 
|#####|WWWWWWWI  ' || `  IWWWWWWWWWWW| 
|#####|WWWWWWWI    ||    IWWWWWWWWWWW| 
|#####|WWWWWWWI    ||    IWWWWWWWWWWW| 
|#####|WWWWWWWI    ||    IWWWWWWWWWWW| 
|#####|WWWWWWWI____||____IWWWWWWWWWWW| 
|#####/_o_                           | 
|####/  X                            | 
|###/  ' `                           | 
|##/                                 | 
|#/                                  | 
|/                                   | 
+------------------------------------+ 

~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.<>.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~""")

print("Hazine Adası'na hoş geldin. Görevin hazineyi bulmak.")


sag_sol = input("Önünde iki tane kapı var hangi kapıdan devam etmek istersin ? Sağ kapıdan mı yoksa Sol kapıdan mı ? Sağ veya sol giriniz lütfen : ")

if sag_sol == "Sol":
    print("Sol kapıdan devam ettin ve bir kumsala düştün. Önünde bir ada var ve elinde de bir hazine haritası.\n"
          "Seninle birlikte bu haritaya göz koyan 5 kişi var. Çok hızlı olmak zorundasın. Bir anda gökyüzünde iki tane seçenek belirdi.")

    yuzme_tekne = input("Adaya tekneyi bekleyip tekneyle mi gitmek istersin yoksa yüzerek adaya gitmeyi istersin.\n"
                        "Hangisini seçiyorsun ? Tekne veya Yüzme giriniz lütfen : ")
    if yuzme_tekne == "Tekne":
        print("Adaya tekneyle devam ettin ve yüzerek suda köpekbalıklarına yem olmadın. Tebrikler 3.aşamaya geçtiniz. En zor bölüme hazır mısınız ?")

        hangi_kapi = input("Adaya ulaştın ve şuan adanın girişinde 3 tane kapı var;\n"
                           "Kırmızı Kapı, Mavi Kapı , Sarı Kapı çok dikkatli bir seçim seni bekliyor.\n"
                           "Hangi kapıdan geçmek istersin ? Kırmızı , Mavi , Sarı lütfen bir kapı ismini giriniz : ")
        if hangi_kapi == "Mavi":
            print("Maalesef oyunu kaybettiniz. Bu kapıda Joe Goldberg karakteri sizi karşıladı ve sizi boynunuzdan keserek öldürdü.")
        elif hangi_kapi == "Sarı":
            print("Tebrikler oyunu kazandınız. Paha biçilemez bir servet kazandınız. Artık çok zenginsiniz.")
        else:
            print("Maalesef oyunu kaybettiniz.Bu kapıda sizi içine çeken bir kara delikten oluşuyordu. Sonunuz kara delikten sonra ne oldu bir sonraki oyunda\n"
          "göreceksiniz. Beklemede kalın...")

    else:
        print("Maalesef oyunu kaybettiniz. Bir yere kadar rakiplerinizden çok daha hızlı gittiniz fakat köpekbalıkları sizin kokunuzu aldı ve seni yediler.")

else:
    print("Maalesef oyunu kaybettiniz. Sağ kapıda seni bekleyen üç tane aç aslan vardı ve seni yediler.")











