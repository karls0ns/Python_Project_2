List = open("Data.txt").read().splitlines()

Dict = {} 

ele = []
key = True
counter = -1
theme = " "
count = 0
for x in List:
    if key:
        theme = x
        key = False
        count = 1     
    elif count == 1:
        counter = int(x)
        count = 0        
    elif theme not in Dict.keys():
        Dict[theme] = [x]
        counter = counter -1
    elif counter > 0:        
        Dict[theme].insert(0,x)
        counter = counter - 1
        if counter == 0:
            key = True
            count = 1         

menu = {}
menu['1']="Saraksta izvade" 
menu['2']="Jauna dokumenta pievienosana"
menu['3']="Iziet no programmas"
    
while True: 
    options=menu.keys()
    for entry in options: 
        print (entry, menu[entry])
        
    selection = input("Izvelieties:")
    if selection =='1':        

        print(Dict)        
    elif selection == '2':
        theme = input("Ievadi temu:")
        while True:            
            theme=theme.upper()
            if theme not in Dict.keys():
                print ("Tema neeksiste")
                theme = input("Ievadi temu velreiz:")
            else:
                break
        doc = input("Ievadi dokumenta nosaukumu:")
        Dict[theme].insert(0,doc)
        
    elif selection == '3': 
        break
    else: 
        print ("Unknown Option Selected!")     