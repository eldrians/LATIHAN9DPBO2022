from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, luasTanah, kapasitasListrik):
        super().__init__("Indekos", luasTanah, kapasitasListrik)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.luasTanah = luasTanah
        self.kapasitasListrik = kapasitasListrik

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_summary(self):
        return "( Hunian Indekos " + ", Luas Tanah : "+str(self.luasTanah) + " m2 )" + " dan Kapasitas Listrik " + str(self.kapasitasListrik) + " VA )"