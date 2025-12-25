class BankaHesabi:
    def __init__(self, hesap_sahibi, bakiye):
        self.hesap_sahibi = hesap_sahibi
        self.bakiye = bakiye

    def get_bakiye(self):
        return self.bakiye

    def para_yatir(self, miktar):
        self.bakiye += miktar
        return self.bakiye

    def para_cek(self, miktar):
        if self.bakiye < miktar:
            print("Yetersiz Bakiye")
        else:
            self.bakiye -= miktar
            print("İşlem başarılı.")
        return self.bakiye

    def hesap_ozeti(self):
        return f"Hesap Sahibi: {self.hesap_sahibi} | Bakiye: {self.bakiye} TL"