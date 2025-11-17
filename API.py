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

    def rimuoviNota(self, id):
        contatore=0
        for i in self.agenda:
            if i['id']==id:
               self.agenda.pop(contatore)
            contatore=contatore+1

        locale = open("agenda.csv", 'w')
        for i in self.agenda:
            locale.write( str(i['id']) + ';' + i['titolo'] + ';' + i['contenuto'] + '\n')
        locale.close()

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

    def aggiungiNota(self, nota: dict):
        # genera un ID unico
        while True:
            id = random.random()
            if not any(i['id'] == id for i in self.agenda):
                break

        nota['id'] = id
        self.agenda.append(nota)

        # salva su CSV
        with open("agenda.csv", 'w') as locale:
            for i in self.agenda:
                locale.write(f"{i['id']};{i['titolo']};{i['contenuto']}\n")

        print(self.agenda)

    
    def aggiornaGrafica(self):
        self.finestra_principale.evaluate_js("caricaAgenda()")
