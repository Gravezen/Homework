class Cassa(object):
       
    def __init__(self, money):
        self.money = money
        
    def top_up(self, X):
        self.money += X

    def count_1000(self):
        print(f'Количество денег в кассе составляет {self.money // 1000} тысяч')
   
    def take_away(self, X):
        if self.money > X:
            self.money -= X
        else:
            print('В кассе неостаточно средств для вывода!')

bigmac = Cassa(50412)

bigmac.top_up(50000)
bigmac.count_1000()
bigmac.take_away(1500000)
