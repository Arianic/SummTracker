from win32 import win32gui
import win32ui



def League_Running():
                 
    if win32ui.FindWindow(None, "League of Legends (TM) Client"):
        
        return True
    else:
        print("not found")
        return False
        
    
while League_Running():
    content = []
    linenumber = {4, 5, 6, 7, 8}
    for i , row in enumerate(open(r'C:\Riot Games\League of Legends\MyNotes.txt', "r")):
        if i in linenumber:
            content.append(row)
            print(row)
            
            

        
    
    
    
    
   
    
    
                   
