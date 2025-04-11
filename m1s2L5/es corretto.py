import datetime 
import re

def sMsPsA(comando):
    comando = str.lower(comando)
    comando = re.sub(r'[^\w\s]', '', comando)
    comando=comando.replace("à","a")
    comando=comando.replace("è","e")
    comando=comando.replace("ì","i")
    comando=comando.replace("ò","o")
    comando=comando.replace("ù","u")
    return comando

def assistente_virtuale(comando):    or "che giorno e"
    if comando == "qual e la data di oggi" or "che giorno e":       
        oggi = datetime.datetime.today()         
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")    
    elif comando == "che ore sono":        
        ora_attuale = datetime.datetime.now().time()          
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")    
    elif comando == "come ti chiami":       
        risposta = "Mi chiamo Assistente Virtuale"    
    else:        
        risposta = "Non ho capito la tua domanda."  
    return risposta
    
while True:    
    comando_utente = input("Cosa vuoi sapere? ") 
    comando_utente = sMsPsA(comando_utente)
    if comando_utente.lower() == "esci":        
        print("Arrivederci!")        
        break    
    else:
        print(assistente_virtuale(comando_utente)) 