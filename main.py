from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import replit
replit.clear() 
#MENSAJE DE INICIO
print('     <<<BIENVENIDO A LIFESTORE>>>')
print('\n  Visualizador de información de productos')

print('┼┼█┼┼┼┼█┼┼█▀▀┼█▀▀┼█▀▀▀┼▀▀█▀▀┼█▀▀█┼█▀▀█┼┼█▀▀┼┼')
print('┼┼█┼┼┼┼█┼┼█▀┼┼█▀┼┼▀▀▀█┼┼┼█┼┼┼█┼┼█┼█▀█▀┼┼█▀┼┼┼')
print('┼-█▄▄┼┼█┼┼█┼┼┼█▄▄┼█▄▄█┼┼┼█┼┼┼█▄▄█┼█┼▀█┼┼█▄▄┼┼')
print('                 ╔═══╗ ♪')
print('                 ║███║ ♫')
print('                 ║ (●) ♫')
print('                 ╚═══╝♪♪')

input("     Presione 'Enter' para continuar ")
replit.clear()
#INGRESO DE DATOS DE ACCESO
admin=['gerencia1', 'gerencia2', 'gerencia3']#Usuarios administradores
admin_pswrd=['lifestore2020', '1234abcd', 'life_store1']
user=['marketing1', 'distribucion4', 'daniel_lopez']#Usuario 
user_pswrd=['ventas55', '9876', '09-01-98']
attempt=3 #El sistema permite 3 accesos erróneos antes de salir del programa
access=False
while attempt>0 and access==False:
    replit.clear()
    print('\n    <<<ACCESO AL SISTEMA>>>')
    print('Intentos restantes:', attempt)
    user_in=input('\nIngrese usuario: ')
    pswrd_in=input('Ingrese contraseña: ')
    if user_in in admin:
        if pswrd_in==admin_pswrd[admin.index(user_in)]:
            access=True
            is_admin=True
            repeat=False
        else:
            input('\nContraseña incorrecta. Presione "Enter" para ingresar datos nuevamente')
            attempt-=1
    elif user_in in user:
        if pswrd_in==user_pswrd[user.index(user_in)]:
            access=True
            is_admin=False
            repeat=False
        else:
            input('\nContraseña incorrecta. Presione "Enter" para ingresar datos nuevamente')
            attempt-=1
    else:
        input('\nUsuario incorrecto. Presione "Enter" para ingresar datos nuevamente')
        attempt-=1

###########################################################################
########### O P C I O N E S   D E L    A D M I N I S T R A D O R ##########
###########################################################################
if attempt>0:
    if is_admin==True:
#RECOPILA DATOS SOBRE VENTAS 
# # # # # # # # # # # # # # # # DATOS ANUALES
        #CONTAR INCIDENCIAS EN VENTAS
        iD=lifestore_sales[0][1]  #Accede al iD del primer producto en la lista de ventas
        counter=0  # Contador de ventas
        rating=0
        devolutions=0
        sales=[]   
        ratings=[]
        for sale in lifestore_sales:
            if iD==sale[1]:  
                counter+=1 
                rating+=sale[2]
                devolutions+=sale[4]
            else:    #Si no existen más ventas del mismo producto, almacena el total 
                sales.append([counter,iD]) 
                ratings.append([rating/counter, counter, devolutions, iD]) 
                #Reestablece los valores de conteo
                counter=1 
                iD=sale[1] 
                rating= sale[2]
                devolutions= sale[4] 
        #Añade último datos recopilados
        sales.append([counter, iD]) 
        ratings.append([rating/counter, counter, devolutions, iD]) 
        sold_products=[] #Lista con los iD de los productos vendidos
        for product in sales:
            sold_products.append(product[1])      
        one_sell=[] #Productos con venta única
        for sale in sales:
            if sale[0]==1:
                one_sell.append(sale[1])  
        #ORDENA LOS VALORES DE VENTAS 
        ordered_sales=sorted(sales, reverse=True) #Lista ordenada de mayor a menor
        ordered_ratings=sorted(ratings, reverse=True)
# # # # # # # # # # # # # # # # DATOS MENSUALES
#CLASIFICA POR MESES
        all_months=[['++ E N E R O ++'],['++ F E B R E R O ++'],['++ M A R Z O ++'],['++ A B R I L ++'],['++ M A Y O ++'],['++ J U N I O ++'],['++ J U L I O ++'],['++ A G O S T O ++'],['++ S E P T I E M B R E ++'],['++ O C T U B R E ++'],['++ N O V I E M B R E ++'],['++ D I C I E M B R E ++']]
        for sale in lifestore_sales:
            month=int(sale[3][3:5])
            all_months[month-1].append(sale[0]) #Añade a cada lista con el nombre del producto, el iD de la venta realizada en dicho mes
##CLASIFICA POR CATEGORÍAS.
        categories=[]
        for element in lifestore_products: #Crea listas para cada categoría
            if [element[3]] not in categories: 
                categories.append([element[3]])     
        for element in lifestore_products: #Clasifica los productos según categoría
            index=0  #Esta variable buscará en qué posición de la lista categorías fue encontrado el producto
            for cat in categories:
                if cat[0]==element[3]:
                    break
                index+=1
            categories[index].append(element[0])
#ANÁLISIS DE VENTAS MENSUAL
        annual_complete_data=[] # En esta lista se añadirán datos adicionales de cada producto (total de ventas, ingresos por total de ventas, valoración promedio, total de devoluciones y total de busquedas)
        annual_sales=[]
        annual_ratings=[]
        for month in all_months:
            complete_data=[]
            monthly_sales=[]
            for n in range(96):
                complete_data.append([n+1]) #La lista se prepara con los iD de cada producto    
            if len(month)>1: #Contará sólo los meses con al menos una venta
                for sale in month[1:]: #Accede a todas las ventas en la lista de cada mes
                    monthly_sales.append(lifestore_sales[sale-1]) #Añade los datos de venta correspondientes a cada ID   
    #CONTAR INCIDENCIAS EN VENTAS
                iD=monthly_sales[0][1]
                counter=0  
                rating=0
                devolutions=0
                sales=[]   
                ratings=[]
                for sale in monthly_sales:
                    if iD==sale[1]:  
                        counter+=1 
                        rating+=sale[2]
                        devolutions+=sale[4]
                    else:    
                        sales.append([counter,iD]) #Si no existen más ventas del mismo producto, almacena el total
                        ratings.append([rating/counter, counter, devolutions, iD]) 
                        complete_data[iD-1].append(counter) #Añade número total de ventas
                        complete_data[iD-1].append((counter-devolutions)*int(lifestore_products[iD-1][2]))# Añade ingresos totales por ventas, restando las devoluciones
                        complete_data[iD-1].append(rating/counter) #Añade el promedio de valoraciones del producto
                        complete_data[iD-1].append(devolutions) #Añade el total de devoluciones del producto
                        #Reestablece los valores de conteo
                        counter=1 
                        iD=sale[1] 
                        rating= sale[2]
                        devolutions= sale[4] 
                #Añade datos recopilados en el último ciclo
                sales.append([counter, iD]) 
                ratings.append([rating/counter, counter, devolutions, iD]) 
                complete_data[iD-1].append(counter) 
                complete_data[iD-1].append((counter-devolutions)*int(lifestore_products[iD-1][2])) #Se restan las devoluciones para calcular los ingresos
                complete_data[iD-1].append(rating/counter) 
                complete_data[iD-1].append(devolutions) 
                for data in complete_data:
                    if len(data)==1: #Productos en los que no se registraron ventas
                        for n in range(4):
                            data.append(0) 
            else: # Para los meses sin venta
                for data in complete_data:
                    for n in range(4):
                        data.append(0)                 
            annual_complete_data.append(complete_data)
            annual_sales.append(sales)
            annual_ratings.append(ratings) 
# # # # # # MUESTRA OPCIONES DE ADMINISTRADOR
        while True:
            while True:
                replit.clear()
                print('\n    <<<USUARIO ADMINISTRADOR>>>')
                print('Seleccione el criterio de visualización')
                print('1) Productos por ventas')
                print('2) Productos por búsquedas')
                print('3) Productos por reseñas')
                print('4) Ingresos totales')
                answer=input('  ')
                band=True # Bandera que verifica que el caracter es un número
                for char in answer:
                    if ord(char)<48 or ord(char)>57:
                        band=False
                if band==True:
                    answer=int(answer)
                else:
                    answer=0
                if answer>=1 and answer<=4:
                    break
                print('\nIngrese una respuesta válida (Númer del 1 al 4)')
# # # # # # # # # # # # # # # PRODUCTOS POR VENTAS
            if answer==1:
                while True:
# # # # # # # # # # # # # # # OPCIONES DE PRODUCTOS POR VENTAS
                    replit.clear()
                    print('Seleccione una opción')
                    print('1) Reporte anual')
                    print('2) Reporte mensual')
                    answer2=input('  ')
                    band=True # Bandera que verifica que el caracter es un número
                    for char in answer2:
                        if ord(char)<48 or ord(char)>57:
                            band=False
                    if band==True:
                        answer2=int(answer2)
                    else:
                        answer2=0
                    if answer2==1 or answer2==2:
                        break
                    print('Ingrese una respuesta válida (1 o 2')
# # # # # # # # # # # # # # # OPCIONES DE REPORTE ANUAL
                if answer2==1:
                    while True:
                        print('Seleccione una opción')
                        print('1) Reporte global')
                        print('2) Reporte por categorías')
                        answer3=input('  ')
                        band=True # Bandera que verifica que el caracter es un número
                        for char in answer3:
                            if ord(char)<48 or ord(char)>57:
                                band=False
                        if band==True:
                            answer3=int(answer3)
                        else:
                            answer3=0
                        if answer3==1 or answer3==2:
                            break
                        print('Ingrese una respuesta válida (1 o 2)')
# # # # # # # # # # # # # # # REPORTE ANUAL GLOBAL
                    if answer3==1:
                        #INGRESA CANTIDAD DE PRODUCTOS A VISUALIZAR
                        top = 0
                        print('Hay', len(sold_products), 'distintos tipos de productos vendidos: ')
                        while True: # Se preguntará al usuario por un valor de visualización 
                            top=input('Tope máximo de productos a visualizar: ')
                            band=True # Bandera que verifica que el caracter es un número
                            for char in top:
                                if ord(char)<48 or ord(char)>57: # Los caracteres con los números del 0 al 9 se encuentran entre 
                                                                # los valores 48 y 57 del código ascii
                                    band=False
                            if band==True:
                                top=int(top)
                            else:
                                top=0   
                            if top>0 and top<=len(sold_products):
                                break
                            print("Por favor, ingrese un número del 1 al ", len(sold_products))
                        replit.clear()                            
                        print('\nNOTA: Hay ', len(lifestore_products)-len(sold_products), 'artículos sin ventas y ', len(one_sell), ' artículos con venta única\n')     
                        #CONFIGURA PRODUCTOS A VISUALIZAR
                        repeat=True
                        while repeat: 
                            print('¿Qué artículos desea visualizar en el top de menos vendidos?')
                            print('  1) Artículos sin ventas (lista completa)')
                            print('  2) Artículos con venta única (lista completa)')
                            print('  3) Primeros', top, 'artículos en lista')
                            config=input('   ')
                            band=True # Bandera que verifica que el caracter es un número
                            for char in config:
                                if ord(char)<48 or ord(char)>57: # Los caracteres con los números del 0 al 9 se encuentran entre los valores 48 y 57 del código ascii
                                    band=False
                            if band==True:
                                config=int(config)
                                if config>=1 and config<=3:
                                    repeat=False
                                    break
                            print('Por favor ingrese una opción válida')
                        #MUESTRA VALORES
                        print('\n************************')
                        print('*PRODUCTOS MÁS VENDIDOS*')
                        print('************************')
                        for i in range(top):
                            iD=ordered_sales[i][1] #Accede al id del producto en la lista de más vendidos
                            print(i+1, lifestore_products[iD-1][1])
                            print('  Categoría:', lifestore_products[iD-1][3])
                            print('  Ventas:', ordered_sales[i][0])
                            print('  Stock:', lifestore_products[iD-1][4], '\n')

                        print('\n**************************')
                        print('*PRODUCTOS MENOS VENDIDOS*')
                        print('**************************')
                        if config==1:
                            print('<<PRODUCTOS SIN VENTAS>>')
                            for product in lifestore_products:
                                iD=product[0]
                                if iD not in sold_products:
                                    print('  ',product[1])
                                    print('   Categoría:', lifestore_products[iD-1][3])
                                    print('   Stock:', lifestore_products[iD-1][4], '\n')
                        elif config==2:
                            print('<<PRODUCTOS CON VENTA ÚNICA>>')
                            for iD in one_sell:
                                print(' ',lifestore_products[iD-1][1])
                                print('  Categoría:', lifestore_products[iD-1][3])
                                print('  Stock:', lifestore_products[iD-1][4], '\n')  
                        else:
                            i=0
                            while i<top:
                                iD=ordered_sales[len(ordered_sales)-i-1][1] #Accede al id del producto en la lista de más vendidos
                                print(i+1, lifestore_products[iD-1][1])
                                print('   Categoría:', lifestore_products[iD-1][3])
                                print('   Ventas:', ordered_sales[len(ordered_sales)-i-1][0])
                                print('   Stock:', lifestore_products[iD-1][4],'\n')
                                i+=1 
# # # # # # # # # # # # # # # REPORTE GLOBAL POR CATEGORÍAS
                    else:
                        #INGRESA CANTIDAD DE PRODUCTOS A VISUALIZAR
                        top = 0
                        print('Hay', len(sold_products), 'distintos tipos de artículos vendidos: ')
                        while top<=0 or top>len(sold_products): # Se preguntará al usuario por un valor de visualización 
                            print("Por favor, ingrese un número del 1 al ", len(sold_products))
                            top=input('Tope máximo de productos a visualizar: ')
                            band=True # Bandera que verifica que el caracter es un número
                            for char in top:
                                if ord(char)<48 or ord(char)>57: 
                                    band=False
                            if band==True:
                                top=int(top)
                            else:
                                top=0
                                        
                        #MUESTRA VALORES
                        print('\nNOTA: Sólo se mostrarán las categorías con al menos una venta')
                        print('\n************************')
                        print('*PRODUCTOS MÁS VENDIDOS*')
                        print('************************')
                        i=0 #Número de categoría
                        j=0 #Número de produtos dentro de una categoría
                        while i<len(categories):
                            clasified_products=[]
                            for product in ordered_sales:
                                iD=product[1]
                                if iD in categories[i]:
                                    clasified_products.append(product)
                                    j+=1
                                    if j>=top:  #Guardará valores hasta el límite de visualización determinado por el usuario
                                        break
                            if len(clasified_products)>0:
                                print('<<<<<<', categories[i][0].upper(),'>>>>>>')
                                j=0 
                                for product in clasified_products: 
                                    iD=product[1]
                                    print(j+1, lifestore_products[iD-1][1]) #Nombre del producto
                                    print('  Ventas:', product[0]) 
                                    print('  Stock:', lifestore_products[iD-1][4], '\n')
                                    j+=1 
                            i+=1 #Pasa a la siguiente categoría

                        print('\n**************************')
                        print('*PRODUCTOS MENOS VENDIDOS*')
                        print('**************************')
                        i=0 #Número de categoría
                        j=0 #Número de produtos dentro de una categoría
                        ordered_sales.sort()
                        while i<len(categories):
                            clasified_products=[]
                            for product in ordered_sales:
                                iD=product[1]
                                if iD in categories[i]:
                                    clasified_products.append(product)
                                    j+=1
                                    if j>=top:  #Guardará valores hasta el límite de visualización determinado por el usuario
                                        break
                            if len(clasified_products)>0:
                                print('<<<<<<', categories[i][0].upper(),'>>>>>>')
                                j=0 
                                for product in clasified_products: 
                                    iD=product[1]
                                    print(j+1, lifestore_products[iD-1][1]) #Nombre del producto
                                    print('  Ventas:', product[0]) 
                                    print('  Stock:', lifestore_products[iD-1][4], '\n')
                                    j+=1 
                            i+=1 #Pasa a la siguiente categoría
                        ordered_sales.sort(reverse=True) #Regresa la lista a su configuración inicial 
# # # # # # # # # # # # # # # OPCIONES DE REPORTE MENSUAL
                else: 
                    while True:
                        print('Seleccione una opción\n')
                        print('1) Enero \n2)Febrero \n3)Marzo \n4)Abril \n5)Mayo \n06)Junio \n7)Julio')
                        print('8)Agosto \n9)Septiembre \n10)Octubre \n11)Noviembre \n12)Diciembre')
                        print('0) VER TODOS LOS MESES')
                        opc=input('  ')
                        band=True # Bandera que verifica que el caracter es un número
                        for char in opc:
                            if ord(char)<48 or ord(char)>57:
                                band=False
                        if band==True:
                            opc=int(opc)
                        else:
                            opc=0
                        if opc>-1 and opc<=12:
                            break
                        print('Ingrese una respuesta válida (Número del 0 al 12)')
# # # # # # # # # # # # # # # CONFIGURA LOS MESES A VISUALIZAR
                    if opc==0:
                        months=all_months[:]
                        m=opc
                    else:
                        months=[all_months[opc-1]]
                        m=opc-1
# # # # # # # # # # # # # # # INGRESA CANTIDAD MÁXIMA DE PRODUCTOS A VISUALIZAR      
                    top = 0 
                    while True: 
                        top=input('\nSeleccione cantidad máxima de productos a visualizar: ')
                        band=True # Bandera que verifica que el caracter es un número
                        for char in top:
                            if ord(char)<48 or ord(char)>57: # Los caracteres con los números del 0 al 9 se encuentran entre los valores 48 y 57 del código ascii
                                band=False
                        if band==True:
                            top=int(top)
                        else:
                            top=0
                        if top>0 and top<=len(sold_products):
                            break
                        print('Esta entrada de texto sólo admite números menores a', len(sold_products), '. Intente nuevamente')
# # # # # # # # # # # # # # # MUESTRA EL REPORTE SOLICITADO
                    replit.clear()
                    print('NOTA: Se mostrarán sólo las categorías con al menos un producto vendido')
                    for month in months: 
                        print('+'*len(month[0]))
                        print(month[0]) 
                        print('+'*len(month[0]))    
                        if len(month)==1:
                            print('    Sin ventas en este mes\n')
                        else:
                            print('************************')
                            print('*PRODUCTOS MÁS VENDIDOS*')
                            print('************************')
                            #ORDENA LOS VALORES DE VENTAS SIN CLASIFICAR
                            annual_sales[m].sort(reverse=True) #Lista ordenada de mayor a menor
                            #MUESTRA VALORES POR CATEGORIA
                            i=0 #Número de categoría
                            j=0 #Número de produtos dentro de una categoría
                            while i<len(categories):
                                clasified_products=[]
                                for product in annual_sales[m]:
                                    iD=product[1]
                                    if iD in categories[i]:
                                        clasified_products.append(product)
                                        j+=1
                                        if j>=top:  #Guardará valores hasta el límite de visualización determinado por el usuario
                                            break
                                if len(clasified_products)>0:
                                    print('<<<<<<', categories[i][0].upper(),'>>>>>>')
                                    j=0 
                                    for product in clasified_products:
                                        iD=product[1]
                                        print(j+1, lifestore_products[iD-1][1]) #Nombre del producto
                                        print('  Ventas:', annual_complete_data[m][iD-1][1]) 
                                        print('  Stock:', lifestore_products[iD-1][4], '\n')
                                        j+=1 
                                i+=1   
                            print('**************************')
                            print('*PRODUCTOS MENOS VENDIDOS*')
                            print('**************************')   
                            #ORDENA LOS VALORES DE VENTAS SIN CLASIFICAR
                            annual_sales[m].sort(reverse=False) #Lista ordenada de menor a mayor
                            print('\nNOTA: Hay ', len(lifestore_products)-len(annual_sales[m]), 'productos sin ventas durante este mes\n')
                            
                            #MUESTRA VALORES POR CATEGORIA
                            i=0 #Número de categoría
                            j=0 #Número de produtos dentro de una categoría
                            while i<len(categories):
                                clasified_products=[]
                                for product in annual_sales[m]:
                                    iD=product[1]
                                    if iD in categories[i]:
                                        clasified_products.append(product)
                                        j+=1
                                        if j>=top:  #Guardará valores hasta el límite de visualización determinado por el usuario
                                            break
                                if len(clasified_products)>0:
                                    print('<<<<<<', categories[i][0].upper(),'>>>>>>')
                                    j=0 
                                    for product in clasified_products:
                                        iD=product[1]
                                        print(j+1, lifestore_products[iD-1][1]) #Nombre del producto
                                        print('  Ventas:', annual_complete_data[m][iD-1][1]) 
                                        print('  Stock:', lifestore_products[iD-1][4], '\n')
                                        j+=1 
                                i+=1 #Pasa a la siguiente categoría
                        m+=1  #Pasa al siguiente mes     
# # # # # # # # # # # # # # #PRODUCTOS POR BÚSQUEDAS
            elif answer==2: 
# # # # # # # # # # # Contar incidencias en búsquedas
                iD=lifestore_searches[0][1] #Accede al iD del primer artículo buscado
                counter=0
                searches=[]
                for search in lifestore_searches:
                    if iD==search[1]:  
                        counter+=1
                    else:     
                        searches.append([counter,iD])
                        counter=1
                        iD=search[1]      
                searches.append([counter, iD]) #Añade el último dato recopilado
# # # # # # # # # # # Selección de categoría
                while True:
# # # # # # # # # # # BUSQUEDAS POR CATEGORÍA
                    replit.clear()
                    print('Seleccione una categoría')
                    print('1)Procesadores \n2)Tarjetas de video \n3)Tarjetas madre \n4)Discos duros')
                    print('5)Memorias USB \n6)Pantallas \n7)Bocinas \n8)Audífonos')
                    print('0) VER TODAS LAS CATEGORÍAS')
                    opc=input('  ')
                    band=True # Bandera que verifica que el caracter es un número
                    for char in opc:
                        if ord(char)<48 or ord(char)>57:
                            band=False
                    if band==True:
                        opc=int(opc)
                    else:
                        opc=-1
                    if opc>=0 and opc<=8:
                        break
                    print('Ingrese una respuesta válida (Número del 0 al 8)')
                if opc==0:
                    selected_categories=categories[:]
                else:
                    selected_categories=[categories[opc-1]]
# # # # # # # # # # # Configura cantidad de productos a mostrar
                top = 0
                print('Hay', len(searches), 'distintos tipos de productos buscados: ')
                while True: # Se preguntará al usuario por un valor de visualización 
                    top=input('Tope máximo de productos a visualizar: ')
                    band=True # Bandera que verifica que el caracter es un número
                    for char in top:
                        if ord(char)<48 or ord(char)>57: # Los caracteres con los números del 0 al 9 se encuentran entre 
                                                        # los valores 48 y 57 del código ascii
                            band=False
                    if band==True:
                        top=int(top)
                    else:
                        top=0
                    if top>0 and top<=len(searches):
                        break
                    print("Por favor, ingrese un número del 1 al ", len(searches))
                                
                #MUESTRA VALORES
                if opc==0:
                    print('\nNOTA: Sólo se mostrarán las categorías con al menos una reseña')
                print('\n***********************')
                print('*PRODUCTOS MÁS BUSCADOS*')
                print('************************')
                searches.sort(reverse=True) #Ordena la lista de búsquedas
                i=0 #Número de categoría
                while i<len(selected_categories):
                    j=0 #Número de produtos dentro de una categoría
                    clasified_products=[]
                    for product in searches:
                        iD=product[1]
                        if iD in selected_categories[i]:
                            clasified_products.append(product)
                            j+=1
                            if j>=top:  #Guardará valores hasta el límite de visualización determinado por el usuario
                                break
                    if len(clasified_products)>0:
                        print('\n<<<<<<', selected_categories[i][0].upper(),'>>>>>>\n')
                        j=0 
                        for product in clasified_products: 
                            iD=product[1]
                            print(j+1, lifestore_products[iD-1][1]) #Nombre del producto
                            print('      Búsquedas:', product[0])
                            j+=1 
                    else:
                        if opc!=0:  #Si se solicitaron reseñas sobre un mes específico y no existe ninguna, se notificará al usuario
                            print('No hay busquedas en esta categoría')
                        
                    i+=1 #Pasa a la siguiente categoría
                print('\n**************************')
                print('*PRODUCTOS MENOS BUSCADOS*')
                print('**************************')
                i=0 #Número de categoría
                searches.sort()
                while i<len(selected_categories):
                    j=0 #Número de produtos dentro de una categoría
                    clasified_products=[]
                    for product in searches:
                        iD=product[1]
                        if iD in selected_categories[i]:
                            clasified_products.append(product)
                            j+=1
                            if j>=top:  #Guardará valores hasta el límite de visualización determinado por el usuario
                                break
                    if len(clasified_products)>0:
                        print('\n<<<<<<', selected_categories[i][0].upper(),'>>>>>>\n')
                        j=0 
                        for product in clasified_products: 
                            iD=product[1]
                            print(j+1, lifestore_products[iD-1][1]) #Nombre del producto
                            print('      Búsquedas:', product[0])
                            j+=1 
                    else:
                        if opc!=0:  #Si se solicitaron reseñas sobre un mes específico y no existe ninguna, se notificará al usuario
                            print('No hay busquedas en esta categoría')
                    i+=1 #Pasa a la siguiente categoría
                searches.sort(reverse=True) #Regresa la lista a su configuración inicial 
                # # # # # # # # # # # # # # # OPCIONAL: MOSTRAR TOP general
                while True:
                    print('¿Visualizar Top de búsquedas general? \n1)Sí \n2)No')
                    opc=input('  ')
                    band=True # Bandera que verifica que el caracter es un número
                    for char in opc:
                        if ord(char)<48 or ord(char)>57:
                            band=False
                    if band==True:
                        opc=int(opc)
                    else:
                        opc=-1
                    if opc>=1 and opc<=2:
                        break
                    print('Ingrese una respuesta válida (1 o 2)')
                if opc==1:
                    iD=lifestore_searches[0][1] #Accede al iD del primer artículo buscado
                    counter=0
                    searches=[]
                    for search in lifestore_searches:
                        if iD==search[1]:  
                            counter+=1
                        else:     
                            searches.append([counter,iD])
                            complete_data[iD-1].append(counter) #Añade número total de búsquedas
                            counter=1
                            iD=search[1]      
                    searches.append([counter, iD]) #Añade el último dato recopilado
                    #MUESTRA VALORES
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    print('<<PRODUCTOS MÁS BUSCADOS>>')
                    print('<<<<<<<<<<<<<<<<<<<<<<<<<<')
                    searches.sort(reverse=True)
                    for i in range(top):
                        iD=searches[i][1] #Accede al id del producto en la lista de más vendidos
                        print(i+1, lifestore_products[iD-1][1])
                        print('  Categoría:', lifestore_products[iD-1][3])
                        print('  Búsquedas:', searches[i][0])
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    print('<<PRODUCTOS MENOS BUSCADOS>>')
                    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                    searches.sort(reverse=False)
                    for i in range(top):
                        iD=searches[i][1] #Accede al id del producto en la lista de más vendidos
                        print(i+1, lifestore_products[iD-1][1])
                        print('  Categoría:', lifestore_products[iD-1][3])
                        print('  Búsquedas:', searches[i][0])
# # # # # # # # # # # # # PRODUCTOS POR RESEÑA
            elif answer==3:
                #Selecciona categoría de visualización
                while True:
                    print('Seleccione una categoría')
                    print('1)Procesadores \n2)Tarjetas de video \n3)Tarjetas madre \n4)Discos duros')
                    print('5)Memorias USB \n6)Pantallas \n7)Bocinas \n8)Audífonos')
                    print('0) VER TODAS LAS CATEGORÍAS')
                    opc=input('  ')
                    band=True # Bandera que verifica que el caracter es un número
                    for char in opc:
                        if ord(char)<48 or ord(char)>57:
                            band=False
                    if band==True:
                        opc=int(opc)
                    else:
                        opc=-1
                    if opc>=0 and opc<=8:
                        break
                    print('Ingrese una respuesta válida (Número del 0 al 8)')
                # # # # # # # # # # # # # # CONFIGURA LOS MESES A VISUALIZAR
                if opc==0:
                    selected_categories=categories[:]
                    m=opc
                else:
                    selected_categories=[categories[opc-1]]
                    m=opc-1

                top = 0
                print('Hay', len(sold_products), 'distintos tipos de artículos reseñados: ')
                while True: # Se preguntará al usuario por un valor de visualización 
                    top=input('Tope máximo de productos a visualizar: ')
                    band=True # Bandera que verifica que el caracter es un número
                    for char in top:
                        if ord(char)<48 or ord(char)>57: 
                            band=False
                    if band==True:
                        top=int(top)
                    else:
                        top=0
                    if top>0 and top<=len(sold_products):
                        break
                    print("Por favor, ingrese un número del 1 al ", len(sold_products))
                                
                #MUESTRA VALORES
                if opc==0:
                    print('\nNOTA: Sólo se mostrarán las categorías con al menos una reseña')
                print('\n**************************')
                print('*PRODUCTOS MEJOR RESEÑADOS*')
                print('***************************')
                i=0 #Número de categoría
                while i<len(selected_categories):
                    j=0 #Número de produtos dentro de una categoría
                    clasified_products=[]
                    for product in ordered_ratings:
                        iD=product[3]
                        if iD in selected_categories[i]:
                            clasified_products.append(product)
                            j+=1
                            if j>=top:  #Guardará valores hasta el límite de visualización determinado por el usuario
                                break
                    if len(clasified_products)>0:
                        print('<<<<<<', selected_categories[i][0].upper(),'>>>>>>')
                        j=0 
                        for product in clasified_products: 
                            iD=product[3]
                            print(j+1, lifestore_products[iD-1][1]) #Nombre del producto
                            print('  Reseña promedio:', str(product[0])[:3], 'estrellas')
                            print('  Total de reseñas:', product[1])
                            print('  Devoluciones:', product[2], '\n')
                            j+=1 
                    else:
                        if opc!=0:  #Si se solicitaron reseñas sobre un mes específico y no existe ninguna, se notificará al usuario
                            print('No hay reseñas en esta categoría')
                        
                    i+=1 #Pasa a la siguiente categoría
                print('\n**************************')
                print('*PRODUCTOS PEOR RESEÑADOS*')
                print('**************************')
                i=0 #Número de categoría
                ordered_ratings.sort()
                while i<len(selected_categories):
                    j=0 #Número de produtos dentro de una categoría
                    clasified_products=[]
                    for product in ordered_ratings:
                        iD=product[3]
                        if iD in selected_categories[i]:
                            clasified_products.append(product)
                            j+=1
                            if j>=top:  #Guardará valores hasta el límite de visualización determinado por el usuario
                                break
                    if len(clasified_products)>0:
                        print('<<<<<<', selected_categories[i][0].upper(),'>>>>>>')
                        j=0 
                        for product in clasified_products: 
                            iD=product[3]
                            print(j+1, lifestore_products[iD-1][1]) #Nombre del producto
                            print('  Reseña promedio:', str(product[0])[:3], 'estrellas')
                            print('  Total de reseñas:', product[1])
                            print('  Devoluciones:', product[2], '\n')
                            j+=1 
                    else:
                        if opc!=0:
                            print('No hay reseñas en esta categoría')
                    i+=1 #Pasa a la siguiente categoría
                ordered_ratings.sort(reverse=True) #Regresa la lista a su configuración inicial  
                # # # # # # # # # # # # # # # OPCIONAL: MOSTRAR TOP general
                while True:
                    print('¿Visualizar Top de reseñas general? \n1)Sí \n2)No')
                    opc=input('  ')
                    band=True # Bandera que verifica que el caracter es un número
                    for char in opc:
                        if ord(char)<48 or ord(char)>57:
                            band=False
                    if band==True:
                        opc=int(opc)
                    else:
                        opc=-1
                    if opc>=1 and opc<=2:
                        break
                    print('Ingrese una respuesta válida (1 o 2)')
                if opc==1:
                     #MUESTRA VALORES
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    print('<<PRODUCTOS MEJOR RESEÑADOS>>')
                    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                    ordered_ratings.sort(reverse=True)
                    for i in range(top):
                        iD=ordered_ratings[i][3] #Accede al id del producto 
                        print(i+1, lifestore_products[iD-1][1])
                        print('  Categoría:', lifestore_products[iD-1][3])
                        print('  Reseña promedio:', str(ordered_ratings[i][0])[:3], 'estrellas')
                        print('  Total de reseñas:', ordered_ratings[i][1])
                        print('  Devoluciones:', ordered_ratings[i][2], '\n')
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    print('<<PRODUCTOS PEOR RESEÑADOS>>')
                    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                    ordered_ratings.sort(reverse=False)
                    for i in range(top):
                        iD=ordered_ratings[i][3]
                        print(i+1, lifestore_products[iD-1][1])
                        print('  Categoría:', lifestore_products[iD-1][3])
                        print('  Reseña promedio:', str(ordered_ratings[i][0])[:3], 'estrellas')
                        print('  Total de reseñas:', ordered_ratings[i][1])
                        print('  Devoluciones:', ordered_ratings[i][2], '\n')
# # # # # # # # # # # # # INGRESOS TOTALES
            else:
                m=0
                total_sales=[]
                total_income=[]
                for month in all_months:
                    print(month[0])     
                    if len(month)==1:
                        print('    Sin ventas en este mes\n')
                        total_sales.append([0,m])
                        total_income.append([0,m])
                    else:
                        total=0
                        income=0
                        for data in annual_complete_data[m]:
                            total+=data[1]  #Suma los valores correspondientes al número de ventas
                            income+=data[2]  #Suma los valores correspondientes a los ingresos generados
                        total_sales.append([total, m])
                        total_income.append([income, m])
                        print('       Número de ventas:', total_sales[m][0])
                        print('       Ingresos totales: $', total_income[m][0])
                    m+=1 
                total=0
                income=0
                for data in total_sales:
                    total+=data[0]  #Suma los valores correspondientes al número de ventas
                for data in total_income:
                    income+=data[0]  #Suma los valores correspondientes a los ingresos generados
                print('++ SUMATORIA ANUAL ++')
                print('\nTotal de productos vendidos:', total)
                print('Total de ingresos: $', income)
                print('\nNúmero de ventas promedio mensuales:', round(total/len(total_sales)))
                print('Ingreso promedio mensual: $', round(income/len(total_income)))
                
                #Ordena valores de ventas
                total_sales.sort(reverse=True)
                print('\nMESES CON MÁS VENTAS')
                for i in range(3):
                    month=total_sales[i][1]
                    print('    ',all_months[month][0], '\n     Ventas:', total_sales[i][0])
                total_sales.sort()
                print('\nMESES CON MENOS VENTAS')
                for i in range(3):
                    month=total_sales[i][1]
                    print('    ',all_months[month][0], '\n    Ventas:', total_sales[i][0])
                #Ordena valores de ingresos
                total_income.sort(reverse=True)
                print('\nMESES CON MÁS INGRESOS')
                for i in range(3):
                    month=total_income[i][1]
                    print('    ',all_months[month][0], '\n     Ingresos: $', total_income[i][0])
                total_income.sort()
                print('\nMESES CON MENOS INGRESOS')
                for i in range(3):
                    month=total_income[i][1]
                    print('    ',all_months[month][0], '\n    Ingresos: $', total_income[i][0])
                print('++TOTALES POR CATEGORÍA++')
                for cat in categories:
                    print(cat[0].upper())
                    income=0
                    num_sales=0
                    for month in annual_complete_data:
                        for product in month:
                            if product[0] in cat:  #Verifica ID en la categoría
                                income+=product[2]  #Suma el ingreso
                                num_sales+=product[1]
                    print('  ',num_sales, 'ventas')
                    print('  Ingresos netos: \n  $', income, '\n')
            while True:
                print('\n\n-FIN DEL REPORTE-')
                print('¿Desea mirar otro reporte? \n1)Sí \n2)No')
                answer=input('  ')
                band=True # Bandera que verifica que el caracter es un número
                for char in answer:
                    if ord(char)<48 or ord(char)>57: 
                        band=False
                if band==True:
                    answer=int(answer)
                else:
                    answer=0
                if answer>=1 and answer<=2:
                    break
                print('\nIngrese una respuesta válida (1 o 2)') 
            if answer==2:
                replit.clear()
                print('         <<<CERRANDO VISUALIZADOR>>>')

                print('┼┼█┼┼┼┼█┼┼█▀▀┼█▀▀┼█▀▀▀┼▀▀█▀▀┼█▀▀█┼█▀▀█┼┼█▀▀┼┼')
                print('┼┼█┼┼┼┼█┼┼█▀┼┼█▀┼┼▀▀▀█┼┼┼█┼┼┼█┼┼█┼█▀█▀┼┼█▀┼┼┼')
                print('┼-█▄▄┼┼█┼┼█┼┼┼█▄▄┼█▄▄█┼┼┼█┼┼┼█▄▄█┼█┼▀█┼┼█▄▄┼┼')
                print('                 ╔═══╗ ♪')
                print('                 ║███║ ♫')
                print('                 ║ (●) ♫')
                print('                 ╚═══╝♪♪')

                input("     Presione 'Enter' para terminar programa ")
                break

###########################################################################
################# O P C I O N E S   D E L    U S U A R I O ################
###########################################################################
    else:
        while True:
            replit.clear()
            print('      <<USUARIO>>')
            print('NOTA: Usted ha ingresado con una cuenta de acceso restringido')
            print('Solo los usuarios administradores pueden acceder a la información del visualizador')
            
            print('         <<<CERRANDO VISUALIZADOR>>>')

            print('┼┼█┼┼┼┼█┼┼█▀▀┼█▀▀┼█▀▀▀┼▀▀█▀▀┼█▀▀█┼█▀▀█┼┼█▀▀┼┼')
            print('┼┼█┼┼┼┼█┼┼█▀┼┼█▀┼┼▀▀▀█┼┼┼█┼┼┼█┼┼█┼█▀█▀┼┼█▀┼┼┼')
            print('┼-█▄▄┼┼█┼┼█┼┼┼█▄▄┼█▄▄█┼┼┼█┼┼┼█▄▄█┼█┼▀█┼┼█▄▄┼┼')
            print('                 ╔═══╗ ♪')
            print('                 ║███║ ♫')
            print('                 ║ (●) ♫')
            print('                 ╚═══╝♪♪')

            input("     Presione 'Enter' para terminar programa ")
            break
if attempt==0:
    replit.clear()
    print('\nNúmero de intentos de acceso excedido. Intente más tarde')
    print('         <<<CERRANDO VISUALIZADOR>>>')

    print('┼┼█┼┼┼┼█┼┼█▀▀┼█▀▀┼█▀▀▀┼▀▀█▀▀┼█▀▀█┼█▀▀█┼┼█▀▀┼┼')
    print('┼┼█┼┼┼┼█┼┼█▀┼┼█▀┼┼▀▀▀█┼┼┼█┼┼┼█┼┼█┼█▀█▀┼┼█▀┼┼┼')
    print('┼-█▄▄┼┼█┼┼█┼┼┼█▄▄┼█▄▄█┼┼┼█┼┼┼█▄▄█┼█┼▀█┼┼█▄▄┼┼')
    print('                 ╔═══╗ ♪')
    print('                 ║███║ ♫')
    print('                 ║ (●) ♫')
    print('                 ╚═══╝♪♪')

    input("     Presione 'Enter' para terminar programa ")