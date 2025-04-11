import datetime 
import re

def sMsPsAsS(comando):
    comando = str.lower(comando)
    comando = re.sub(r'[^\w\s]', '', comando)
    comando=comando.replace("à","a")
    comando=comando.replace("è","e")
    comando=comando.replace("ì","i")
    comando=comando.replace("ò","o")
    comando=comando.replace("ù","u")
    comando=re.sub(r"\s+$", "", comando)
    return comando

def assistente_virtuale(comando):
    if comando == "qual e la data di oggi":       
        oggi = datetime.datetime.today()         
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")    
    elif comando == "che ore sono":        
        ora_attuale = datetime.datetime.now().time()          
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")    
    elif comando == "come ti chiami":       
        risposta = "Mi chiamo Assistente Virtuale" 
    elif comando == "help":       
        print("Qual è la data di oggi?")
        print("Che ore sono?")
        print("Come ti chiami?")
        print("se non hai domande (Esci)")
        risposta = " " 
    else:        
        risposta = "Non ho capito la tua domanda."  
    return risposta
    
while True:
    print("help o aiuto per maggiori informazioni")  
    comando_utente = input("Cosa vuoi sapere?") 
    comando_utente = sMsPsAsS(comando_utente)
    if comando_utente.lower() == "esci":        
        print("Arrivederci!")        
        break    
    else:
        print(assistente_virtuale(comando_utente)) 