import webview
from API import api_primaria

agenda=[] # test: {'titolo':'ciao','contenuto':'ciao','id':5}

rispristinaNote(agenda)

api_agenda =api_primaria(agenda)
api_agenda.crea_agenda()

webview.start(debug=False)
