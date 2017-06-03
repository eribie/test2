class strategie:
    def __init__(self):
        self.pnl = 0
        self.pnl_achat = 0
        self.pnl_vente = 0
        self.achete = False
        self.vendu = False

    def achat(self, quantite, cours):
        self.achete = True
        self.position_init_achat = quantite * cours

    def stopAchat(self, quantite, cours):
        self.achete = False
        position_fin_achat = quantite * cours
        pnl_achat = position_fin_achat - self.position_init_achat
        self.pnl += pnl_achat

    def vente(self, quantite, cours):
        self.vendu = True
        self.position_init_vente = quantite * cours

    def stopVente(self, quantite, cours):
        self.vendu = False
        position_fin_vente = quantite * cours
        pnl_vente = self.position_init_vente - position_fin_vente
        self.pnl += pnl_vente


    def get_Pnl(self, quantite, cours):
        if self.achete == True:
            return self.pnl + cours * quantite - self.position_init_achat
        elif self.vendu == True:
            return self.pnl + self.position_init_vente - cours * quantite
        else:
            return self.pnl


renault = strategie()

renault.achat(100,10)
print(renault.get_Pnl(100,10))
renault.stopAchat(100,20)
print(renault.get_Pnl(100,10))