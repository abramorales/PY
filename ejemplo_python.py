"""numero_uno = int(input('Ingresa el primer valor: '))
numero_dos = int(input('Ingresa el segundo valor: '))
resultado = numero_uno + numero_dos
print('El resultado de la suma es: ', resultado)"""

"""from datetime import date
#Impresion de la fecha
print(date.today())"""

"""#operacion y concatenado en el print para 
parsecs  = 11
lightyears = 3.26*parsecs
print(parsecs,"parsecs is",lightyears,"lightyears")"""

"""#paso los valores de entrada de la ejecucion y los leo en el script
import sys
print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])
#linea de ejecucion python ejemplo_python.py "2024-09-6"""

"""#Uso de input para recibir el nombre u otros datos
print("Introduce your full name")
full_name = input("Write your name: ")
print("Your full name is: ",full_name, "and welcome to babilonia")"""

"""#Solicite el numero a transformar para poder multiplicarlo despues
parsecs_input = int(input("Introduce te count of parsecs to convert in lightyears: "))
lightyears = 3.26*parsecs_input
print(parsecs_input,"parsecs is",lightyears,"lightyears")"""

"""#La instruccion de if debe llevar : tanto en el id como en elif y en el else
object_size = 10
if object_size > 5:
    print("We need to keep an eye on this object")
else:
    print("Object poses no threat")"""

"""object_size = 10
proximity = 9000
if object_size > 5 and proximity < 1000:
    print("Evasive maneuvers required")
else:
    print("Object poses no threat")"""

"""#Recuerda que cuando se realiza un ciclo for es porque conocemos la cantidad de veces que se va a iterarar
text = "Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."

sentences = text.split('. ')

for loop in sentences:
    if 'temperature' in loop:
        print(loop)"""

"""name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'"""

#template = """Gravity Facts about {name}
#--------------------------
#Planet Name: {planet}
#Gravity on {name}: {gravity} m/s2"""

#print(f"""Gravity Facts about {name}
#--------------------------
#Planet Name: {planet}
#Gravity on {name}: {gravity} m/s2""")

#template = """Gravity Facts about {0}
#----------------------------------------
#Planet Name: {1}
#Gravity on {2}: {3} m/s2""".format(name,planet,name,gravity)

"""first_planet = 149597870
second_planet = 778547200

distance_km = second_planet - first_planet
distance_mi = distance_km/1.609344

print('The distance in km is: ',distance_km)
print('The distance in miles is: ',distance_mi)"""

"""first_planet_input = int(input('Write the distance of the first planet about the sun in Km: '))
second_planet_input = int(input('Write the distance of the second planet about the sun in Km: '))

print('The distance between de planets are:',abs(second_planet_input - first_planet_input), 'km.')"""

"""planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']

print(planets)

print(f"The total number of planets are: {len(planets)}")

planets.append('Pluto')

print(planets)

print(f"Wait Pluto exist? Ok, now the total number of planets are: {len(planets)}")

print(f"The last planet is: {planets[-1]}")"""

"""planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
planet_by_user = input('Please write the name of your favorite planet and consider use capital letter to star the name of the planet: ')

print(f"The position of your favorite planets is: {planets.index(planet_by_user)+1}")
print(f"And the closer of the planets are the following: {planets[0:planets.index(planet_by_user)]}")
print(f"And the further of the planets are the following: {planets[planets.index(planet_by_user)+1:]}")"""

#CICLOS WHILE Y FOR
"""from time import sleep

new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input("Please write the name of the planet or write done if you are finished: ")

print(f"The list of the planets that you wrote are: {planets}")
print(f"The planets have the next sequence: ")

for planet in planets:
    sleep(1)
    print(f" {planet}")"""

#DICCIONARIOS

"""planet = {
    'name':'Mars',
    'moons':2
}
print(f'{planet.get('name')} has {planet.get('moons')} moon(s)')

planet.update(diameter = {'polar':6752,'equatorial':6792})

print(f'{planet.get('name')} has {planet.get('moons')} moon(s) and this are the value from polar {planet.get('diameter').get('polar')}')"""

"""rainfall = {
    'Monday': 2.4,
    'Wednesday': 4.5,
    'Friday':8.0
}
#Imprime valores de un diccionario por medio de un for
for detail in rainfall.keys():
    print(f'The {detail} has: {rainfall.get(detail)} cm.')

#actualiza valores en espesifico
if 'Saturday' in rainfall:
    rainfall.update({'Saturday':rainfall['Saturday']+1})
else:
    rainfall.update({'Saturday':1})

for detail in rainfall.keys():
    print(f'The {detail} has: {rainfall.get(detail)} cm.')

total_cm = 0

for sum_tot in rainfall.values():
    total_cm = total_cm+sum_tot

print(f'The total of cms are: {total_cm}')"""

"""planet_moons = {
    'mercury':0,
    'venus':0,
    'earth':1,
    'mars':2,
    'jupiter':79,
    'saturn':82,
    'uranus':27,
    'neptune':14,
    'pluto':5,
    'haumea':2,
    'makemake':1,
    'eris':1
}

moons = 0
total_planets = len(planet_moons.keys())

for moon in planet_moons.values():
    moons = moons+moon



print(f'The total of planets are: {total_planets} and the total of moons about that planets are: {moons}, Now that all generate the following average of moons {moons/total_planets}')"""


""""def generate_report(main_tank,external_tank,hydrogen_tank):
    print(f"Fuel Report
          Main tank: {main_tank}
          External tank: {external_tank}
          Hydrogen tank: {hydrogen_tank}")
    
generate_report(45.6,60,10)"""


"""def fuel_report(**Kwarguments):
    for fuel, count in Kwarguments.items():
        print(f""{fuel}: {count}"")
        
fuel_report(Main_tank = 45, External_tank = 100, Hydrogen_tank = 67)"""


"""def numero (uno,dos=4):
    print(f"{uno} y {dos}")

numero(3)"""

"""def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
 
if __name__ == '__main__':
    main()"""