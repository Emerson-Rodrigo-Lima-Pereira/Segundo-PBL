AcucarF = ArrozF = CafeF = Extrato_de_tomateF = MacarraoF = BolachaF = OleoF = Farinha_de_trigoF = FeijaoF = SalF = OutrosF = 0
AcucarJ = ArrozJ = CafeJ = Extrato_de_tomateJ = MacarraoJ = BolachaJ = OleoJ = Farinha_de_trigoJ = FeijaoJ = SalJ = OutrosJ = 0
cesta = 0
total_item_fisica = total_item_juridica = 0
acucar_to_parcial = arroz_to_parcial = cafe_to_parcial = extrato_de_tomate_to_parcial = macarrao_to_parcial = bolacha_to_parcial = oleo_to_parcial = farinha_de_trigo_to_parcial = feijao_to_parcial = sal_to_parcial = outros_to_parcial = acucar_to = arroz_to = cafe_to = extrato_de_tomate_to = macarrao_to = bolacha_to = oleo_to = farinha_de_trigo_to = feijao_to = sal_to = outros_to = 0
resto_acucarf = resto_arrozf = resto_cafef = resto_extrato_de_tomatef = resto_macarraof = resto_farinha_de_trigof = resto_feijaof = resto_salf = resto_acucarj = resto_arrozj = resto_cafej = resto_extrato_de_tomatej = resto_macarraoj = resto_farinha_de_trigoj = resto_feijaoj = resto_salj = 0
fechar = True
#declaracao de variaveis contadoras ↑
while fechar ==True:
#condicional caso o usuario nao queira fechar o dia ↑
    print("***********************")
    menu = input("[1] Solicitar relatório\n[2] Fazer doação\n[3] Fechar o dia\n***********************\n").lower()
    while menu.isdigit()==False or menu != "1" and menu != "2" and menu != "3":
        menu = input("***********************\n[1] Solicitar relatório\n[2] Fazer doação\n[3] Fechar o dia\n***********************\n").lower()
    #funcao para perguntar ao usuario se ele quer ver o relatorio ou fazer doacao e sua validacao ↑
    continuar = True
    if menu == "3":
        fechar = False
    #condicional caso o usuario queira fechar o dia ↑
    elif menu == "2":
    #condicional caso o usuario queira fazer doacao ↑
        nome = input("Qual o nome do doador: ").lower()
        while nome.isalpha()==False:
            nome = input("Qual o nome do doador: ").lower()
        tipo_de_doador = input("Pessoa [física]/[jurídica]: ").lower().replace("í","i")
        while tipo_de_doador.isalpha()==False or tipo_de_doador != "fisica" and tipo_de_doador != "juridica":
            tipo_de_doador = input("Pessoa [física]/[jurídica]: ").lower().replace("í","i")
        #funcao para perguntar o nome e tipo de doador, e suas validacoes ↑    
        while tipo_de_doador == "fisica" and continuar == True and menu == "2":
        #condicional caso o tipo de doador for pessoa fisica ↑
            print("*************************")
            print("Qual item você quer doar:\n0)Açúcar;\n1)Arroz;\n2)Café;\n3)Extrato de tomate;\n4)Macarrão;\n5)Bolacha;\n6)Óleo;\n7)Farinha de trigo;\n8)Feijão;\n9)Sal;\n10)Outros. ")
            print("*************************")
            #funcao para mostrar ao usuario quais itens ele pode doar ↑
            tipo = input("Qual item: ")
            while tipo.isdigit()==False or int(tipo) < 0 or int(tipo) > 10:
                tipo = input("Qual item: ")
            #funcao para perguntar ao usuario que item ele quer doar e sua validacao ↑
            if tipo == "0" or tipo == "1" or tipo == "2" or tipo == "7" or tipo == "8" or tipo == "9":
            #condicional caso o tipo do item seja medido em kg ↑
                quantidade_1 = input("Quantos kg: ")
                quantidade = quantidade_1
                while quantidade_1.replace(".","").isdigit()==False:
                    quantidade_1 = input("Quantos kg: ")
                    quantidade = quantidade_1
            elif tipo == "3" or tipo == "4" or tipo == "10":
            #condicional caso o tipo do item seja contado em unidades ↑
                quantidade = input("Quantas unidades: ")
                while quantidade.isdigit()==False:
                    quantidade = input("Quantas unidades: ")
            elif tipo == "5":
            #condicional caso o tipo do item seja contado em pct ↑
                quantidade = input("Quantos pct: ")
                while quantidade.isdigit()==False:
                    quantidade = input("Quantos pct: ")
            else:
            #condicional caso o tipo do item seja medido em L ↑
                quantidade = input("Quantos L: ")
                while quantidade.isdigit()==False:
                    quantidade = input("Quantos L: ")
                #funcao que pergunta a quantidade que o usuario quer doar e sua validacao ↑                                          
            if tipo == "0" :
                AcucarF +=float(quantidade)    
            elif tipo == "1":  
                ArrozF +=float(quantidade)
            elif tipo == "2":
                CafeF +=float(quantidade)
            elif tipo == "3":
                Extrato_de_tomateF +=int(quantidade)
            elif tipo == "4":
                MacarraoF +=int(quantidade)
            elif tipo == "5":
                BolachaF +=int(quantidade)                            
            elif tipo == "6":
                OleoF +=int(quantidade)   
            elif tipo == "7":
                Farinha_de_trigoF +=float(quantidade) 
            elif tipo == "8":
                FeijaoF +=float(quantidade)
            elif tipo == "9":
                SalF +=float(quantidade)                                                                       
            elif tipo == "10":
                OutrosF +=int(quantidade)
            #condicional para saber qual tipo do item o usuario doou ↑
                #adicionando a variavel contadora a quantidade doada ↑
            continuar = input("Quer continuar doando [sim]/[não]:").lower().replace("ã","a")
            while continuar.isalpha()==False and continuar != "sim" and continuar != "nao":
                continuar = input("Quer continuar doando [sim]/[não]:").lower().replace("ã","a")
            #funcao para perguntar se o usuario quer continuar doando e sua validacao ↑
            if continuar == "sim":
                continuar = True
            #condicional caso o usuario queira continuar doando ↑
            else:
                continuar = False    
            #condicional caso o usuario nao queira continuar doando ↑                   
        while tipo_de_doador == "juridica" and continuar == True and menu == "2":
        #condicional caso o tipo de doador for pessoa juridica ↑
            print("*************************")
            print("Qual item você quer doar:\n0)Açúcar;\n1)Arroz;\n2)Café;\n3)Extrato de tomate;\n4)Macarrão;\n5)Bolacha;\n6)Óleo;\n7)Farinha de trigo;\n8)Feijão;\n9)Sal;\n10)Outros. ")
            print("*************************")
            #funcao para mostrar ao usuario quais itens ele pode doar ↑
            tipo = input("Qual item: ")
            while tipo.isdigit()==False or int(tipo) < 0 or int(tipo) > 10:
                tipo = input("Qual item: ")
            #funcao para perguntar ao usuario qual item ele quer doar e sua validacao ↑
            if tipo == "0" or tipo == "1" or tipo == "2" or tipo == "7" or tipo == "8" or tipo == "9":
            #condicional caso o tipo do item seja medido em kg ↑
                quantidade_1 = input("Quantos kg: ")
                quantidade = quantidade_1
                while quantidade_1.replace(".","").isdigit()==False:
                    quantidade_1 = input("Quantos kg: ")
                    quantidade = quantidade_1
            elif tipo == "3" or tipo == "4" or tipo == "10":
            #condicional caso o tipo do item seja contado em unidades ↑
                quantidade = input("Quantas unidades: ")
                while quantidade.isdigit()==False:
                    quantidade = input("Quantas unidades: ")
            elif tipo == "5":
            #condicional caso o tipo do item seja contado em pct ↑
                quantidade = input("Quantos pct: ")
                while quantidade.isdigit()==False:
                    quantidade = input("Quantos pct: ")
            else:
            #condicional caso o tipo do item seja medido em L ↑
                    quantidade = input("Quantos L: ")
                    while quantidade.isdigit()==False:
                        quantidade = input("Quantos L: ")
                #funcao que pergunta a quantidade que o usuario quer doar e sua validacao ↑                                          
            if tipo == "0":
                AcucarJ +=float(quantidade)    
            elif tipo == "1":  
                ArrozJ +=float(quantidade)
            elif tipo == "2":
                CafeJ +=float(quantidade)
            elif tipo == "3":
                Extrato_de_tomateJ +=int(quantidade)
            elif tipo == "4":
                MacarraoJ +=int(quantidade)
            elif tipo == "5":
                BolachaJ +=int(quantidade)                            
            elif tipo == "6":
                OleoJ +=int(quantidade)   
            elif tipo == "7":
                Farinha_de_trigoJ +=float(quantidade) 
            elif tipo == "8":
                FeijaoJ +=float(quantidade)
            elif tipo == "9":
                SalJ +=float(quantidade)                                                                       
            elif tipo == "10":
                OutrosJ +=int(quantidade)
            #condicional para saber qual tipo do item o usuario doou ↑
                #adicionando a variavel contadora a quantidade doada ↑
            continuar = input("Quer continuar doando [sim]/[não]:").lower().replace("ã","a")
            while continuar.isalpha()==False or continuar != "sim" and continuar != "nao":
                continuar = input("Quer continuar doando [sim]/[não]:").lower().replace("ã","a")
            #funcao para perguntar se o usuario quer continuar doando e sua validacao ↑
            if continuar == "sim":
                continuar = True
            #condicinal caso o usuario queira continuar doando ↑
            else:
                continuar = False
            #condicional caso o usuario nao queira continuar doando ↑
        acucar_to_parcial += (AcucarF - resto_acucarf) + (AcucarJ - resto_acucarj)
        arroz_to_parcial += (ArrozF - resto_arrozf) + (ArrozJ - resto_arrozj)
        cafe_to_parcial += (CafeF - resto_cafef) + (CafeJ - resto_cafej)
        extrato_de_tomate_to_parcial += (Extrato_de_tomateF - resto_extrato_de_tomatef) + (Extrato_de_tomateJ - resto_extrato_de_tomatej)
        macarrao_to_parcial += (MacarraoF - resto_macarraof) + (MacarraoJ - resto_macarraoj)
        bolacha_to_parcial += BolachaF + BolachaJ
        oleo_to_parcial += OleoF + OleoJ
        farinha_de_trigo_to_parcial += (Farinha_de_trigoF - resto_farinha_de_trigof) + (Farinha_de_trigoJ - resto_farinha_de_trigoj)
        feijao_to_parcial += (FeijaoF - resto_feijaof) + (FeijaoJ - resto_feijaoj)
        sal_to_parcial += (SalF - resto_salf) + (SalJ - resto_salj)
        #variaveis que ajudaram saber quantas cestas basicas formadas ↑
        acucar_to += (AcucarF - resto_acucarf) + (AcucarJ - resto_acucarj)
        arroz_to += (ArrozF - resto_arrozf) + (ArrozJ - resto_arrozj)
        cafe_to += (CafeF - resto_cafef) + (CafeJ - resto_cafej)
        extrato_de_tomate_to += (Extrato_de_tomateF - resto_extrato_de_tomatef) + (Extrato_de_tomateJ - resto_extrato_de_tomatej)
        macarrao_to += (MacarraoF - resto_macarraof) + (MacarraoJ - resto_macarraoj)
        bolacha_to += BolachaF + BolachaJ
        oleo_to += OleoF + OleoJ
        farinha_de_trigo_to += (Farinha_de_trigoF - resto_farinha_de_trigof) + (Farinha_de_trigoJ - resto_farinha_de_trigoj)
        feijao_to += (FeijaoF - resto_feijaof) + (FeijaoJ - resto_feijaoj)
        sal_to += (SalF - resto_salf) + (SalJ - resto_salj)
        outros_to += OutrosF + OutrosJ
        #variaveis para saber o total de cada item doado ↑
        total_item_fisica += (AcucarF //1) + (ArrozF //4) + (CafeF //2) + (Extrato_de_tomateF //2) + (MacarraoF //3) + (BolachaF //1) + (OleoF //1) + (Farinha_de_trigoF //1) + (FeijaoF //4) + (SalF //1) + (OutrosF //1)
        total_item_juridica += (AcucarJ //1) + (ArrozJ //4) + (CafeJ //2) + (Extrato_de_tomateJ //2) + (MacarraoJ //3) + (BolachaJ //1) + (OleoJ //1) + (Farinha_de_trigoJ //1) + (FeijaoJ //4) + (SalJ //1) + (OutrosJ //1)
        #variaveis para saber o total de itens doados (sendo qualquer tipo) por pessoa fisica e pessoa juridica ↑
        resto_acucarf = AcucarF % 1
        resto_arrozf = ArrozF % 4 
        resto_cafef = CafeF % 2 
        resto_extrato_de_tomatef = Extrato_de_tomateF % 2 
        resto_macarraof = MacarraoF % 3   
        resto_farinha_de_trigof = Farinha_de_trigoF % 1 
        resto_feijaof = FeijaoF % 4
        resto_salf = SalF % 1
        resto_acucarj = AcucarJ % 1
        resto_arrozj = ArrozJ % 4 
        resto_cafej = CafeJ % 2 
        resto_extrato_de_tomatej = Extrato_de_tomateJ % 2 
        resto_macarraoj = MacarraoJ % 3   
        resto_farinha_de_trigoj = Farinha_de_trigoJ % 1 
        resto_feijaoj = FeijaoJ % 4
        resto_salj = SalJ % 1
        #variaveis para saber quantos itens nao formaram a quantidade certa para a montagem de cesta basica ↑
        BolachaF = OleoF = OutrosF = 0
        BolachaJ = OleoJ = OutrosJ = 0
        AcucarF = resto_acucarf 
        ArrozF = resto_arrozf 
        CafeF = resto_cafef 
        Extrato_de_tomateF = resto_extrato_de_tomatef 
        MacarraoF = resto_macarraof   
        Farinha_de_trigoF = resto_farinha_de_trigof 
        FeijaoF = resto_feijaof 
        SalF = resto_salf
        AcucarJ = resto_acucarj
        ArrozJ = resto_arrozj
        CafeJ = resto_cafej
        Extrato_de_tomateJ = resto_extrato_de_tomatej
        MacarraoJ = resto_macarraoj
        Farinha_de_trigoJ = resto_farinha_de_trigoj
        FeijaoJ = resto_feijaoj
        SalJ = resto_salj
        #variaveis para saber tirar a quantidade de itens que formaram a quantidade certa para a montagem de cesta basica ↑               
    if menu == "1":
    #condicional caso o usuario queira ver o relatorio ↑  
        print("************************************************************************************Relatório***********************************************************************************")
        #funcao para mostrar ao usuario varios "*" e "Relatório" ↑
        print("Açúcar :{} ; Arroz :{} ; Café :{} ; Extrato de tomate :{} ; Macarrão :{} ; Bolacha :{} ; Óleo :{} ; Farinha de trigo :{} ; Feijão :{} ; Sal :{} ; Item extra :{} .".format(acucar_to, arroz_to,cafe_to,extrato_de_tomate_to,macarrao_to,bolacha_to,oleo_to,farinha_de_trigo_to,feijao_to,sal_to,outros_to))
        #funcao para mostrar ao usuario a quantidade total de cada item doado ↑
        print("Foram doados {} itens por Pessoas Físicas e {} itens por Pessoa Jurídicas.".format(total_item_fisica, total_item_juridica))     
        #funcao para mostrar a quantidade de itens doados (independente do tipo) por pessoa fisica e pessoa juridica ↑               
        while acucar_to_parcial >= 1 and arroz_to_parcial >= 4 and cafe_to_parcial >= 2 and extrato_de_tomate_to_parcial >= 2 and macarrao_to_parcial >= 3 and bolacha_to_parcial >= 1 and oleo_to_parcial >= 1 and farinha_de_trigo_to_parcial >= 1 and feijao_to_parcial >= 4 and sal_to_parcial >= 1:
        #repeticao por condicao para montar cestas basicas ↑    
            cesta +=1
            #variavel para contar quantas cestas basicas foram formadas ↑
            acucar_to_parcial -=1
            arroz_to_parcial -=4
            cafe_to_parcial -=2
            extrato_de_tomate_to_parcial -=2
            macarrao_to_parcial -=3
            bolacha_to_parcial -=1
            oleo_to_parcial -=1
            farinha_de_trigo_to_parcial -=1
            feijao_to_parcial -=4
            sal_to_parcial -=1
            #variaveis para tirar a quantidade de itens que formaram cesta basica ↑
        if outros_to > cesta:
            item = outros_to - cesta
        else:
            item = 0
        #condicionais para saber a quantidade de itens extras que sobraram ↑               
        print("Foram formadas {} cestas básicas.".format(cesta))
        #funcao para mostrar quantas cestas basicas foram formadas ↑
        if outros_to >= cesta:
            print("{} cestas básicas ganharam um item extra".format(cesta))
        elif outros_to < cesta:
            print("{} cestas básicas ganharam um item extra.".format(outros_to))
        #condicionais para saber quantas cestas basicas ganharam um item extra ↑
            #funcao para mostrar ao usuario quantas cestas basicas ganharam item extra ↑
        if cesta > outros_to:
            print("{} cestas básicas não ganharam um item extra.".format(cesta - outros_to))
        elif outros_to >= cesta:
            print("0 cestas básicas não ganharam item extra.")
        #condicionais para saber quantas basicas nao ganharm item extra ↑
            #funcao para mostrar ao usuario quantas cestas basicas nao ganharam item extra ↑
        if acucar_to_parcial == 0 and arroz_to_parcial == 0 and cafe_to_parcial == 0 and extrato_de_tomate_to_parcial == 0 and macarrao_to_parcial == 0 and bolacha_to_parcial == 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
            print("Não sobrou nenhum item.")
        else:        
            if acucar_to_parcial == 0:
                acucar = ""
            elif acucar_to_parcial > 0 and arroz_to_parcial == 0 and cafe_to_parcial == 0 and extrato_de_tomate_to_parcial == 0 and macarrao_to_parcial == 0 and bolacha_to_parcial == 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
                acucar = "Açúcar."
            else:
                acucar = "Açúcar;"
            if arroz_to_parcial == 0:
                arroz = ""
            elif arroz_to_parcial > 0 and cafe_to_parcial == 0 and extrato_de_tomate_to_parcial == 0 and macarrao_to_parcial == 0 and bolacha_to_parcial == 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
                arroz = "Arroz."
            else:
                arroz = "Arroz;"
            if cafe_to_parcial == 0:
                cafe = ""
            elif cafe_to_parcial > 0 and extrato_de_tomate_to_parcial == 0 and macarrao_to_parcial == 0 and bolacha_to_parcial == 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
                cafe = "Café."
            else:
                cafe = "Café;"
            if extrato_de_tomate_to_parcial == 0:
                extrato_de_tomate = ""
            elif extrato_de_tomate_to_parcial > 0 and macarrao_to_parcial == 0 and bolacha_to_parcial == 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
                extrato_de_tomate = "Extrato de tomate."
            else:
                extrato_de_tomate = "Extrato de tomate;"
            if macarrao_to_parcial == 0:
                macarrao = ""
            elif macarrao_to_parcial > 0 and bolacha_to_parcial == 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
                macarrao = "Macarrão."
            else:
                macarrao = "Macarrão;"
            if bolacha_to_parcial == 0:
                bolacha = ""
            elif bolacha_to_parcial > 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
                bolacha = "Bolacha."
            else:
                bolacha = "Bolacha;"
            if oleo_to_parcial == 0:
                oleo = ""
            elif oleo_to_parcial > 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
                oleo = "Óleo."
            else:
                oleo = "Óleo;"
            if farinha_de_trigo_to_parcial == 0:
                farinha_de_trigo = ""
            elif farinha_de_trigo_to_parcial > 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
                farinha_de_trigo = "Farinha de trigo."
            else:
                farinha_de_trigo = "Farinha de trigo;"
            if feijao_to_parcial == 0:
                feijao = ""
            elif feijao_to_parcial > 0 and sal_to_parcial == 0 and item == 0:
                feijao = "Feijão."
            else:
                feijao = "Feijão;"
            if sal_to_parcial == 0:
                sal = ""
            elif sal_to_parcial > 0 and item == 0:
                sal = "Sal."
            else:
                sal = "Sal;"
            if item == 0:
                item = "" 
            else:
                item = "Item extra."
            #condicionais para saber quais itens sobraram ↑
                #variaveis para mostrar quais itens sobraram ↑        
            print("{}{}{}{}{}{}{}{}{}{}{}".format(acucar, arroz,cafe,extrato_de_tomate,macarrao,bolacha,oleo,farinha_de_trigo,feijao,sal,item))
            #funcao para mostrar ao usuario quais itens sobraram ↑
        print("********************************************************************************************************************************************************************************")
        #funcao para mostrar varios "*" ↑
print("***********************************************************************************Relatório Final******************************************************************************")
#funcao para mostrar ao usuario varios "*" e "Relatório Final" ↑
print("Açúcar :{} ; Arroz :{} ; Café :{} ; Extrato de tomate :{} ; Macarrão :{} ; Bolacha :{} ; Óleo :{} ; Farinha de trigo :{} ; Feijão :{} ; Sal :{} ; Item extra :{} .".format(acucar_to, arroz_to,cafe_to,extrato_de_tomate_to,macarrao_to,bolacha_to,oleo_to,farinha_de_trigo_to,feijao_to,sal_to,outros_to))
#funcao para mostrar ao usuario a quantidade total de cada item doado ↑
print("Foram doados {} itens por Pessoas Físicas e {} itens por Pessoa Jurídicas.".format(total_item_fisica, total_item_juridica))
#funcao para mostrar a quantidade de itens doados (independente do tipo) por pessoa fisica e pessoa juridica ↑                    
while acucar_to_parcial >= 1 and arroz_to_parcial >= 4 and cafe_to_parcial >= 2 and extrato_de_tomate_to_parcial >= 2 and macarrao_to_parcial >= 3 and bolacha_to_parcial >= 1 and oleo_to_parcial >= 1 and farinha_de_trigo_to_parcial >= 1 and feijao_to_parcial >= 4 and sal_to_parcial >= 1:
#repeticao por condicao para montar cestas basicas ↑    
    cesta +=1
    #variavel para contar quantas cestas basicas foram formadas ↑
    acucar_to_parcial -=1
    arroz_to_parcial -=4
    cafe_to_parcial -=2
    extrato_de_tomate_to_parcial -=2
    macarrao_to_parcial -=3
    bolacha_to_parcial -=1
    oleo_to_parcial -=1
    farinha_de_trigo_to_parcial -=1
    feijao_to_parcial -=4
    sal_to_parcial -=1
    #variaveis para tirar a quantidade de itens que formaram cesta basica ↑
if outros_to > cesta:
    item = outros_to - cesta
else:
    item = 0
#condicionais para saber a quantidade de itens extras que sobraram ↑                   
print("Foram formadas {} cestas básicas.".format(cesta))
#funcao para mostrar quantas cestas basicas foram formadas ↑
if outros_to >= cesta:
    print("{} cestas básicas ganharam um item extra".format(cesta))
elif outros_to < cesta:
    print("{} cestas básicas ganharam um item extra.".format(outros_to))
#condicionais para saber quantas cestas basicas ganharam um item extra ↑
    #funcao para mostrar ao usuario quantas cestas basicas ganharam item extra ↑    
if cesta > outros_to:
    print("{} cestas básicas não ganharam um item extra.".format(cesta - outros_to))
elif outros_to >= cesta:
    print("0 cestas básicas não ganharam item extra.")
#condicionais para saber quantas basicas nao ganharm item extra ↑
    #funcao para mostrar ao usuario quantas cestas basicas nao ganharam item extra ↑
if acucar_to_parcial == 0 and arroz_to_parcial == 0 and cafe_to_parcial == 0 and extrato_de_tomate_to_parcial == 0 and macarrao_to_parcial == 0 and bolacha_to_parcial == 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
    print("Não sobrou nenhum item.")
else:       
    if acucar_to_parcial == 0:
        acucar = ""
    elif acucar_to_parcial > 0 and arroz_to_parcial == 0 and cafe_to_parcial == 0 and extrato_de_tomate_to_parcial == 0 and macarrao_to_parcial == 0 and bolacha_to_parcial == 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
        acucar = "Açúcar."
    else:
        acucar = "Açúcar;"
    if arroz_to_parcial == 0:
        arroz = ""
    elif arroz_to_parcial > 0 and cafe_to_parcial == 0 and extrato_de_tomate_to_parcial == 0 and macarrao_to_parcial == 0 and bolacha_to_parcial == 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
        arroz = "Arroz."
    else:
        arroz = "Arroz;"
    if cafe_to_parcial == 0:
        cafe = ""
    elif cafe_to_parcial > 0 and extrato_de_tomate_to_parcial == 0 and macarrao_to_parcial == 0 and bolacha_to_parcial == 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
        cafe = "Café."
    else:
        cafe = "Café;"
    if extrato_de_tomate_to_parcial == 0:
        extrato_de_tomate = ""
    elif extrato_de_tomate_to_parcial > 0 and macarrao_to_parcial == 0 and bolacha_to_parcial == 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
        extrato_de_tomate = "Extrato de tomate."
    else:
        extrato_de_tomate = "Extrato de tomate;"
    if macarrao_to_parcial == 0:
        macarrao = ""
    elif macarrao_to_parcial > 0 and bolacha_to_parcial == 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
        macarrao = "Macarrão."
    else:
        macarrao = "Macarrão;"
    if bolacha_to_parcial == 0:
        bolacha = ""
    elif bolacha_to_parcial > 0 and oleo_to_parcial == 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
        bolacha = "Bolacha."
    else:
        bolacha = "Bolacha;"
    if oleo_to_parcial == 0:
        oleo = ""
    elif oleo_to_parcial > 0 and farinha_de_trigo_to_parcial == 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
        oleo = "Óleo."
    else:
        oleo = "Óleo;"
    if farinha_de_trigo_to_parcial == 0:
        farinha_de_trigo = ""
    elif farinha_de_trigo_to_parcial > 0 and feijao_to_parcial == 0 and sal_to_parcial == 0 and item == 0:
        farinha_de_trigo = "Farinha de trigo."
    else:
        farinha_de_trigo = "Farinha de trigo;"
    if feijao_to_parcial == 0:
        feijao = ""
    elif feijao_to_parcial > 0 and sal_to_parcial == 0 and item == 0:
        feijao = "Feijão."
    else:
        feijao = "Feijão;"
    if sal_to_parcial == 0:
        sal = ""
    elif sal_to_parcial > 0 and item == 0:
        sal = "Sal."
    else:
        sal = "Sal;"
    if item == 0:
        item = "" 
    else:
        item = "Item extra."
    #condicionais para saber quais itens sobraram ↑
        #variaveis para mostrar quais itens sobraram ↑        
    print("{}{}{}{}{}{}{}{}{}{}{}".format(acucar, arroz,cafe,extrato_de_tomate,macarrao,bolacha,oleo,farinha_de_trigo,feijao,sal,item))
    #funcao para mostrar ao usuario quais itens sobraram ↑
print("********************************************************************************************************************************************************************************")
#funcao para mostrar varios "*" ↑