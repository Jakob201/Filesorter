

import os, shutil, time, threading

from datetime import datetime
import time
from tkinter import *
from tkinter import messagebox


#path = os.path.join('~', 'Desktop')
#pfad = os.path.expanduser(path)

gettime = datetime.now()
newtime = gettime.strftime("%H:%M:%S")
messagebox.showinfo('information', 'Hallo. Alle Infos über den Filesorter.py findest du im python terminal')
print('startet...')
time.sleep(2)
print('Ready...')
time.sleep(1)
starttime1 = datetime.now()
starttime = starttime1.strftime("%H:%M:%S")

print('['+ starttime +']Selbst installierendes Filesorter system')
time.sleep(1)
print('['+ starttime +']HINWEIS: Alle 60sek wird über die Console(das Fenster in dem du gerade liest) eine Meldung ausgegeben dass das Programm noch läuft')
time.sleep(1)


print('['+ starttime +']DIESES FENSTER BITTE NICHT SCHLIESSEN!')
time.sleep(1)

def Ready():
    now = datetime.now()
    curent_time = now.strftime("%H:%M:%S")
    print('['+ curent_time + ']'+'filesorter anwesend seit: ' + starttime)
def Test():
    
    pfad = os.path.expanduser(os.path.join('~', 'Desktop'))
    
    os.chdir(pfad)
    downloads = pfad + '\\Downloads'
    
    
    if os.path.isdir(downloads) == False:
            os.makedirs(pfad + '\downloads')
            time.sleep(2)
            os.makedirs(pfad + '\Manuell Zuordnen')
        
        
        
    else:
        
        zu_sortierenden_datein_pfad = "Downloads\\"
        zu_sortierenden_datein = os.listdir(zu_sortierenden_datein_pfad)
    
    
    
        for datei in zu_sortierenden_datein:
            
            endung = datei[-3:].lower()
            
            
            pfad_neu = pfad + '\\' + endung + '\\' + datei
            pfad_dir = pfad + '\\' + endung
            
            prüfen = os.path.isfile(pfad_neu)
            dir_check = os.path.isdir(pfad_dir)
            
            time.sleep(2)
            
            if dir_check == False:
                os.makedirs(pfad_dir)
                time.sleep(3)
                shutil.move(zu_sortierenden_datein_pfad + datei, endung)
                time.sleep(5)
            elif dir_check == True and prüfen == True:
                time1 = datetime.now()
                jetzt = time1.strftime("%H:%M:%S")
                
                messagebox.showerror('Error 404', 'Die datei' + datei + 'konnte nicht in den Ordner' + endung + ' verschoben werden, da eine gleiche oder ähnlich Datei schon existiert ' )
                shutil.move(zu_sortierenden_datein_pfad + datei, 'manuell Zuordnen')
                time.sleep(5)
            else:
                time1 = datetime.now()
                jetzt = time1.strftime("%H:%M:%S")
                shutil.move(zu_sortierenden_datein_pfad + datei, endung)
                time.sleep(2)
                print('['+jetzt+']'+datei+' wurde in den ordner **'+endung+'** verschoben')
                time.sleep(5)
        time1 = datetime.now()
        jetzt = time1.strftime("%H:%M:%S")
        print('['+jetzt+'] Filesorter.py läuft :)')


    

def new():
   
                
            
    

    value = input('Befehl: ')

    if value == "Autostart":
        print('['+ starttime +'] 1. Kopiere die Datei "Filesorter.py".')
        print('['+ starttime +'] 2. Drücke auf deiner Tastatur die Windows-Taste und "R".')
        print('['+ starttime +'] 3. Gebe im input-Feld "shell:startup" ein.')
        print('['+ starttime +'] 4. Es öffnet sich nun ein Ordner in welchem du die Datei einfügst')
        time.sleep(0)
        new()
    elif value == "Stopp":
        print("System gestoppt")
        exit()
    elif value == "Hilfe":
        print('['+ starttime +'] HILFE TERMINAL')
        print('['+ starttime +'] Wenn deine Datein nicht zugeordnet werden schreiben eine "1" in das Terminal')
        print('['+ starttime +'] Wenn du die Autostartanleitung nicht funktioniert dann schreiben sie eine "2" in das Terminal')
        print('['+ starttime +'] Wenn sie Kontaktinformationen sehen möchten schreiben sie eine "3" in das Terminal')
        print('['+ starttime +'] Für weiter Fragen Kontakt aufnehmen in dem sie eine "3" in das Terminal schreiben')
        print('['+ starttime +'] DANKE')
        new()
    elif value == "1":
        print('['+ starttime +'] Deine Dateien werden nicht zugerordnet prüfe ob auf deinem Desktop ein downloads ordner und ein Manuell Zuordnen Ordner vorhanden ist. Starte die Anwendung auch neu.')
        print('['+ starttime +'] Wenn es immer noch nicht funktioniert kontaktiere uns in dem du "3" in das Terminal schreibst')
        new()
    elif value == "2":
        print('['+ starttime +'] Autostart funktioniert nicht')
        print('['+ starttime +'] Wenn du ein Windows PC hast gebe im Explorer unter deinem Namen diesen Pfad an: \AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
        new()
    elif value == "3":
        print('['+ starttime +'] Kontakt')
        print('['+ starttime +'] Email: jakob.schulz07@gmail.com')
        new()
    elif value == "weiter":
        print('Terminal geschlossen')
    else:
        print('Prüfe deine Eingabe')
        new()
    


      

print('['+ starttime +']!Danke!')

print('['+ starttime +'] filesorter läuft seit: ' + starttime)  
time.sleep(1)
print('['+ starttime +'] BEFEHLS ÜBERSICHT:')
print('['+ starttime +'] "Autostart" = Anleitung um diese Anwendung automatisch beim hochfahren des PCs zustarten')
print('['+ starttime +'] "Stop" = stoppt alle vorgänge')
print('['+ starttime +'] "Hilfe" = Hilfe Terminal')
print('['+ starttime +'] "weiter" = Terminal wird geschlossen und es werden datein zugeordnet')

value = input('Befehl: ')
if value == "Autostart":
    print('['+ starttime +'] 1. Kopiere die Datei "Filesorter.py".')
    print('['+ starttime +'] 2. Drücke auf deiner Tastatur die Windows-Taste und "R".')
    print('['+ starttime +'] 3. Gebe im input-Feld "shell:startup" ein.')
    print('['+ starttime +'] 4. Es öffnet sich nun ein Ordner in welchem du die Datei einfügst')
    time.sleep(0)         
    new()
elif value == "Stopp":
        print("System gestoppt")
        exit()
elif value == "Hilfe":
        print('['+ starttime +'] HILFE TERMINAL')
        print('['+ starttime +'] Wenn deine Datein nicht zugeordnet werden schreiben eine "1" in das Terminal')
        print('['+ starttime +'] Wenn du die Autostartanleitung nicht funktioniert dann schreiben sie eine "2" in das Terminal')
        print('['+ starttime +'] Wenn sie Kontaktinformationen sehen möchten schreiben sie eine "3" in das Terminal')
        print('['+ starttime +'] Für weiter Fragen Kontakt aufnehmen in dem sie eine "3" in das Terminal schreiben')
        print('['+ starttime +'] DANKE')
        new()
elif value == "1":
        print('['+ starttime +'] Deine Dateien werden nicht zugerordnet prüfe ob auf deinem Desktop ein downloads ordner und ein Manuell Zuordnen Ordner vorhanden ist. Starte die Anwendung auch neu.')
        print('['+ starttime +'] Wenn es immer noch nicht funktioniert kontaktiere uns in dem du "3" in das Terminal schreibst')
        new()
elif value == "2":
        neuerpath = os.path.expanduser(os.path.join('~', 'AppData'))
        
        print('['+ starttime +'] Autostart funktioniert nicht')
        print('['+ starttime +'] Wenn du ein Windows PC hast gebe im Explorer unter deinem Namen diesen Pfad an:' + neuerpath + '\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
        new()
elif value == "3":
        print('['+ starttime +'] Kontakt')
        print('['+ starttime +'] Email: jakob.schulz07@gmail.com')
        new()
elif value == "weiter":
        print('Terminal geschlossen')
else:
        print('Prüfe deine Eingabe')
        new()    

def meldung():
    currenttime = datetime.now()
    current1 =  currenttime.strftime("%H:%M:%S")
    print('['+current1+'] Filesorter läuft seit '+ starttime)


def setInterval(func,time):
    
    e = threading.Event()
    while not e.wait(5):
        Test()
    

def setInterval2(func,time):
    
    e = threading.Event()
    while not e.wait(7):
        meldung()  
    
   



setInterval(Test(), 5)

