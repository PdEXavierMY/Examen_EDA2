#-----------------------------------------------------------------------------------------
# @Autor: Aurélien Vannieuwenhuyze
# @Empresa: Junior Makers Place
# @Libro
# @Capítulo: 03 - Estadísticas para comprender los datos
#
# Módulos necesarios:
#   PANDAS 0.24.2
#   NUMPY 1.16.3
#   JMPEstadísticas (copiar el archivo dentro de su proyecto al mismo nivel que este archivo)
#
# Para instalar un módulo:
#   Haga clic en el menú File > Settings > Project:nombre_del_proyecto > Project interpreter > botón +
#   Introduzca el nombre del módulo en la zona de búsqueda situada en la parte superior izquierda
#   Elegir la versión en la parte inferior derecha
#   Haga clic en el botón install situado en la parte inferior izquierda
#-----------------------------------------------------------------------------------------

import pandas as pd
import JMPEstadisticas as jmp
import numpy as np
from introducir import solicitar_introducir_numero_extremo

#--- CREACION DE UN DATAFRAME ----
def conseguirstats():
    stats = pd.read_csv("Pokemon.csv", encoding = "UTF8", sep = ",")
    total, hp, attack, defense, spattack, spdefense, speed = list(stats["Total"]), list(stats["HP"]), list(stats["Attack"]), list(stats["Defense"]), list(stats["Sp. Atk"]), list(stats["Sp. Def"]), list(stats["Speed"])
    return total, hp, attack, defense, spattack, spdefense, speed

total, hp, attack, defense, spattack, spdefense, speed = conseguirstats()
observaciones1, observaciones2, observaciones3, observaciones4, observaciones5, observaciones6, observaciones7 = pd.DataFrame({'Stats':np.array(total)}), pd.DataFrame({'Stats':np.array(hp)}), pd.DataFrame({'Stats':np.array(attack)}), pd.DataFrame({'Stats':np.array(defense)}), pd.DataFrame({'Stats':np.array(spattack)}), pd.DataFrame({'Stats':np.array(spdefense)}), pd.DataFrame({'Stats':np.array(speed)})

#--- Estadisticas ---
def estadisticas():
    eleccion = solicitar_introducir_numero_extremo("Elige de que stat quieres la estadística(el total(1), hp(2), attack(3), defense(4), sp.attack(5), sp.defense(6), speed(7)", 1, 7)
    stats1, stats2, stats3, stats4, stats5, stats6, stats7 = jmp.JMPEstadisticas(observaciones1['Stats']), jmp.JMPEstadisticas(observaciones2['Stats']), jmp.JMPEstadisticas(observaciones3['Stats']), jmp.JMPEstadisticas(observaciones4['Stats']), jmp.JMPEstadisticas(observaciones5['Stats']), jmp.JMPEstadisticas(observaciones6['Stats']), jmp.JMPEstadisticas(observaciones7['Stats'])
    if eleccion == 1:
        stats1.analisisCaracteristica()
    elif eleccion == 2:
        stats2.analisisCaracteristica()
    elif eleccion == 3:
        stats3.analisisCaracteristica()
    elif eleccion == 4:
        stats4.analisisCaracteristica()
    elif eleccion == 5:
        stats5.analisisCaracteristica()
    elif eleccion == 6:
        stats6.analisisCaracteristica()
    elif eleccion == 7:
        stats7.analisisCaracteristica()

estadisticas() #La media de estadísitcas totales es 435
#La media de hp es 70
#La media de ataque es 79
#La media de defensa es 74
#La media de ataque sp es 73
#La media de defensa sp es 72

def encontrar_pokemon():
    lpokemon1 = []
    lpokemon2 = []
    n = 1
    m = 1
    with open("coach_1__pokemon.csv") as pokemon:
        for linea in pokemon:
            if n != 1:
                lsep = linea.split(",")
                if 425 < int(lsep[4]) < 445: #busco la media, me voy alejando porque no hay
                    lpokemon1.append(lsep)
                    if len(lpokemon1) == 3:
                        break
            n+=1
    with open("coach_2__pokemon.csv") as pokemon:
        for linea in pokemon:
            if m != 1:
                lsep = linea.split(",")
                if 425 < int(lsep[4]) < 445: #busco la media, me voy alejando porque no hay
                    lpokemon2.append(lsep)
                    if len(lpokemon2) == 3:
                        break
            m+=1
    return lpokemon1, lpokemon2

pokemon_entrenador1, pokemon_entrenador2 = encontrar_pokemon()
file1 = open("coach_1_pokemon.csv", "w")
file2 = open("coach_2_pokemon.csv", "w")
file1.write(str(pokemon_entrenador1[0][0]+","+""+str(pokemon_entrenador1[0][1]+","+""+"headbutt"+","+""+str(pokemon_entrenador1[0][5]+","+""+str(int((int(pokemon_entrenador1[0][6])+int(pokemon_entrenador1[0][7]))/2))+","+""+str(int((int(pokemon_entrenador1[0][8])+int(pokemon_entrenador1[0][9]))/2))+"\n"+str(pokemon_entrenador1[1][0]+","+""+str(pokemon_entrenador1[1][1]+","+""+"kick"+","+""+str(pokemon_entrenador1[1][5]+","+""+str(int((int(pokemon_entrenador1[1][6])+int(pokemon_entrenador1[1][7]))/2))+","+""+str(int((int(pokemon_entrenador1[1][8])+int(pokemon_entrenador1[1][9]))/2))+"\n"+str(pokemon_entrenador1[2][0]+","+""+str(pokemon_entrenador1[2][1]+","+""+"elbow"+","+""+str(pokemon_entrenador1[2][5]+","+""+str(int((int(pokemon_entrenador1[2][6])+int(pokemon_entrenador1[2][7]))/2))+","+""+str(int((int(pokemon_entrenador1[2][8])+int(pokemon_entrenador1[2][9]))/2))+"\n"))))))))))
file2.write(str(pokemon_entrenador2[0][0]+","+""+str(pokemon_entrenador2[0][1]+","+""+"punch"+","+""+str(pokemon_entrenador2[0][5]+","+""+str(int((int(pokemon_entrenador2[0][6])+int(pokemon_entrenador2[0][7]))/2))+","+""+str(int((int(pokemon_entrenador2[0][8])+int(pokemon_entrenador2[0][9]))/2))+"\n"+str(pokemon_entrenador2[1][0]+","+""+str(pokemon_entrenador2[1][1]+","+""+"kick"+","+""+str(pokemon_entrenador2[1][5]+","+""+str(int((int(pokemon_entrenador2[1][6])+int(pokemon_entrenador2[1][7]))/2))+","+""+str(int((int(pokemon_entrenador2[1][8])+int(pokemon_entrenador2[1][9]))/2))+"\n"+str(pokemon_entrenador2[2][0]+","+""+str(pokemon_entrenador2[2][1]+","+""+"elbow"+","+""+str(pokemon_entrenador2[2][5]+","+""+str(int((int(pokemon_entrenador2[2][6])+int(pokemon_entrenador2[2][7]))/2))+","+""+str(int((int(pokemon_entrenador2[2][8])+int(pokemon_entrenador2[2][9]))/2))+"\n"))))))))))
file1.close()
file2.close()