def rispristinaNote(agenda:list):
    locale = open ('agenda.csv','r')

    note = locale.readlines()

    for i in note:
        info=i.split(';')

        nota = {}

        nota['id']=info[0]
        nota['titolo']=info[1]
        nota['contenuto']=info[2]

        agenda.append(nota)