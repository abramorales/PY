#Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

#**********************************************************************

# https://www.python.org/

#Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

#**********************************************************************

# 1. Single-Line Comments
# El tipo numero uno es colocar simplemente un signo de #

#**********************************************************************

# 2. Multi-Line Comments
# Python program to demonstrate 
# multiline comments 

# O

""" El otro tipo de comentarios en multiples lineas es utilizar tres
veces las comillas dobles"""

#**********************************************************************

# 3. String Literals
'Tambien son considerados un string literal que no este asignado a ninguna variable'

#**********************************************************************

# 4. Cuando se crea una funcion se puede colocar dentro un comentario que espesifica que acción realizara la función, lo veo util 100% cuando se hace una lectura de LOGS o DEBUG y se quieren indicar checkpoints de lo que hace le codigo y debe estar entre 3 comillas simples o 3 comillas dobles.

def message_as_comment():
    """Esta función simplemente es demostrativa para indicar que se puede colocar un print con la frase descrita aquí"""

print(message_as_comment.__doc__)

#**********************************************************************

# Crea una variable (y una constante si el lenguaje lo soporta).

# En python una literal se considera como un valor que no cambiara por ejemplo si generamos un mensaje simple dentor del codigo como el siguiente sera considerado como literal:

"Esto es una literal" 

# pues es un valor que no cambiara y que tambien tiene la particularidad de no ser condiferado por python pues no esta asignado a nada.

# Una variable en Python es considera aquel valor que puede cambiar constantemente.

age = input("Ingresa tu edad:\n") #age se considera vaiable pues el valor que tomara age puede ser distinto ya que el usuario tendra la oportunidad de colocar cualquier valor. (Los valores pueden ser int, float, strings, etc..)
print(f"""Tu edad es: {age}""") #Impresion de la variable.

#En python perse no existen las constantes pero se pueden trabajar de una manera en la que se delega la responsabilidad al programador el tratarlas como una constante.Las buenas practicas mencionan que se puede crear un archivo que contenga solamente las constantes y posteriormente ya solo se mandan a llamar mediante un import.

GRAVITY_VAL = 9.8

#Esto es una constante pues es un valor que no "debería" de cambiar 
print(f"""El valore de la gravedad en la tierra es de: {GRAVITY_VAL}""")

#**********************************************************************

# Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

#TIPOS DE DATOS QUE DE MOMENTO NO SE COMPRENDEN AL 100% SU USO ADECUADO

#NONE
empty = None
print(f"""Esta es una variable que almacena un tipo de datos NONE: {empty}""")

#ELLIPSIS 
# - Permite la ausencia de un valor aun no definido sin generar algun error al momento de ejecutarse
def prueba ():
    ...

prueba

#INTEGERS (int y bool) 
# - Rango ilimitado sujeto a la memoria (virtual) 
# - Representa los valores de verdadero o falso mediante 1 = True o 0 = False

type_int_positive = 10
type_int_negative = -10
type_bool_true = True
type_bool_false = False

print(f"""{type_int_positive}
{type_int_negative}
{type_bool_true}
{type_bool_false}""")

#STRINGS / CADENAS DE TEXTO
# - En Python, los Stringsrepresentan una cadena de texto y son un tipo de dato inmutable, lo que significa que no se pueden modificar después de ser creados

type_string_one = 'Hello'
type_string_two = "Perfect"
type_string_three = """World !"""

print(f"""{type_string_one} {type_string_two} {type_string_three}""")

# metodos mas utilizados (
# len(): Devuelve la longitud
# upper() y lower(): Convierten la cadena a mayúsculas o minúsculas
# capitalize() y title(): capitalize() convierte el primer carácter a mayúsculas, y title() convierte el primer carácter de cada palabra a mayúsculas.
# count(subcadena): Cuenta cuántas veces aparece una subcadena en la cadena.
# find(subcadena) y index(subcadena): Encuentran la posición de la primera aparición de una subcadena. La diferencia es que find() devuelve -1 si no encuentra la subcadena, mientras que index() genera una excepción ValueError.
# replace(viejo, nuevo): Reemplaza todas las ocurrencias de la subcadena vieja con la nueva.
#strip(), lstrip(), y rstrip(): Eliminan espacios en blanco al principio, al final o en ambos extremos)

print(f"""{type_string_one.upper()} {type_string_two.lower()} {type_string_three.replace("!",":>")}""")

#FLOAT
# - El tipo de dato float se utiliza para representar números de punto flotante, es decir, números que pueden tener una parte fraccionaria o decimal.

type_float_one = 1.6

print(f"""Este es un tipo de dato flotante: {type_float_one}""")

#**********************************************************************

# - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

print(f""""Hola, Python!""")