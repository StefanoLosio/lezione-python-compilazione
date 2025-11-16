import random
import webview

class api_primaria:
    def __init__(self,agenda:list):
        self.agenda=agenda

    def crea_agenda(self):
        window=webview.create_window('Agenda', url='index.html',width=400, height=300, js_api=self)
        self.window=window

    def getAgenda(self):
        return self.agenda

    def rimuoviNota(self, id:int):
        contatore=0
        for i in self.agenda:
            if i['id']==id:
               self.agenda.remove(contatore)
            contatore=contatore+1

    def apriForm(self):
        form=api_secondaria(self.agenda)
        form.creaFinestra(self.window)


class api_secondaria:
    def __init__(self,agenda:list,):
        self.agenda=agenda
    
    def creaFinestra (self, window):
        self.finestra_principale=window
        finestra=webview.create_window('form', url='form.html',width=400, height=300, js_api=self)
        self.finestra=finestra

    def chiudiFinestra(self):
        self.finestra.destroy()

    def aggiungiNota(self,nota:dict):
        flag=False
        while(not flag):
            id=random.random()
            for i in self.agenda:
                if i['id']==id:
                    id=random.random()
                else:
                    nota['id']=id
                    self.agenda.append(nota)
                    flag=True
    
    def aggiornaGrafica(self):
        self.finestra_principale.evaluate_js("caricaAgenda()")
