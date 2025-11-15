class Menu:
    def tayyorlash_vaqti(self):
        pass

    def narx_hisoblash(self, miqdor):
        pass

    def allergiya_tekshirish(self, ingredient):
        return False


class Oqvat(Menu):
    def __init__(self, nomi, vaqt, narx, allergenlar):
        self.nomi = nomi
        self.vaqt = vaqt
        self.narx = narx
        self.allergenlar = allergenlar

    def tayyorlash_vaqti(self):
        return self.vaqt

    def narx_hisoblash(self, miqdor):
        return self.narx * miqdor

    def allergiya_tekshirish(self, ingredient):
        return ingredient in self.allergenlar


class Ichimlik(Menu):
    def __init__(self, nomi, vaqt, narx):
        self.nomi = nomi
        self.vaqt = vaqt
        self.narx = narx

    def tayyorlash_vaqti(self):
        return self.vaqt

    def narx_hisoblash(self, miqdor):
        return self.narx * miqdor


class Desert(Menu):
    def __init__(self, nomi, vaqt, narx):
        self.nomi = nomi
        self.vaqt = vaqt
        self.narx = narx

    def tayyorlash_vaqti(self):
        return self.vaqt

    def narx_hisoblash(self, miqdor):
        return self.narx * miqdor


# --- Umumiy hisoblash ---
menyu = [
    Oqvat("Osh", 40, 30000, ["guruch", "sabzi"]),
    Ichimlik("Choy", 5, 5000),
    Desert("Tort", 20, 15000)
]

umumiy_vaqt = sum(item.tayyorlash_vaqti() for item in menyu)
umumiy_narx = sum(item.narx_hisoblash(2) for item in menyu)  # har biridan 2 ta

print("Umumiy vaqt:", umumiy_vaqt)
print("Umumiy narx:", umumiy_narx)
print("Osh allergiya (guruch):", menyu[0].allergiya_tekshirish("guruch"))
print("Choy allergiya:", menyu[1].allergiya_tekshirish("shakar"))
