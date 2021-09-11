"""
=============================================

liste1 = ["Öyle", "üçe", "beşe", "bakamam!"] # Listemiz 1
liste2 = ["Gelir", "gider", "bir gün", "paralar"] # Listemiz 2
liste1.extend(liste2) #burada extend fonksiyonu ile listeler birleştirilmiştir.
print(liste1)

=============================================
"""
# Birleştirmek için extend fonksiyonu gibi + operatörü de kullanılabilir.
# Aşağıdaki örnek çalıştırıldığında aynı çıktıyı elde edilir.

liste1 = ["Öyle", "üçe", "beşe", "bakamam!"] # Listemiz 1
liste2 = ["Gelir", "gider", "bir gün", "paralar"] # Listemiz 2
print(liste1 + liste2)  #burada + operatörü ile listeler birleştirilmiştir.
