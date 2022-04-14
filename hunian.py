class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, luasTanah = 450, kapasitasListrik = 450):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.luasTanah = luasTanah
        self.kapasitasListrik = kapasitasListrik
    
    def get_jenis(self):
        return self.jenis

    def get_luasTanah(self):
        return self.luasTanah

    def get_kapasitasListrik(self):
        return self.kapasitasListrik

    def get_dokumen(self):
        pass

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_summary(self):
        return "( Hunian "+ self.jenis +",  ditempati oleh " + str(self.jml_penghuni) + " orang" + " dengan Luas Tanah : " + str(self.luasTanah) + " m2 " + "dan Kapasitas Listrik " + str(self.kapasitasListrik) + " VA )"
