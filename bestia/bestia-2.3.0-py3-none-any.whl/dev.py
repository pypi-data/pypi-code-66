# USE THIS MODULE TO TEST LIBRARY API BEFORE COMMITING/UPLOADING
import os, sys
from time import sleep

# DIRECTLY IMPORT SAME DIR MODULES
#   , NOT BESTIA INSTALLED MODULES
from proc import *
from error import *
from iterate import *
from output import *


UTF8 = 'utf-8'
WIN1252 = 'cp1252'

LATIN_CAPITAL_A  = [
    # 'À',  # b'\xc3\x80'
    'Â',  # b'\xc3\x82'
    'Ã',  # b'\xc3\x83'
    'Ä',  # b'\xc3\x84'
    'Å',  # b'\xc3\x85'
    # 'Æ',  # b'\xc3\x86'

    # 'â',  # b'\xc3\xa2'
]


# Un mundo menos peor (2004) Alejandro Agresti - Cine Argentino
# Torrent Information: indiatpb.rocks/apibay/t.php?id=5464439
S = 'Una mujer descubre que su marido, al que creÃ­a muerto hacÃ­a mÃ¡s de veinte aÃ±os, aÃºn vive en un pequeÃ±o pueblo de la costa. Hacia allÃ­ viaja con su hija, quien nunca conociÃ³ a ese padre. Juntas tratarÃ¡n de hacerle recobrar la memoria y de brindarle una familia. Pelicula de Alejandro Agresti, director de ValentÃ­n (2002).'

# Torrent Information: indiatpb.rocks/apibay/t.php?id=5542071
# S = 'Las aventuras del BarÃ³n de Munchausen (dibujos)'

# dumbo dublat romana
DUMBO = 'FaceÅ£i cunostinÅ£Äƒ cu Dumbo, puiul cel mititel ÅŸi dulce al Doamnei Jumbo, care Ã®i farmecÄƒ pe toÅ£i cei care Ã®l vÄƒd... pÃ¢nÄƒ cÃ¢nd lumea descoperÄƒ cÄƒ are niÅŸte urechi mari ÅŸi clÄƒpÄƒuge.'
# should_be_by_google = 'Faceți cunoștință cu Dumbo, copilul mic și dulce al doamnei Jumbo, care fermecă pe toți cei care îl văd ... până când oamenii află că are urechi mari, mari.'

# S = 'Ajutat de cel mai bun prieten al lui, ÅŸoricelul Timothy, Dumbo Ã®ÅŸi dÄƒ seama Ã®n scurtÄƒ vreme cÄƒ urechile lui spectaculoase Ã®l fac sÄƒ fie un personaj unic, cu totul deosebit, care poate deveni celebru Ã®n chip de unic elefant zburÄƒtor al lumii.'

# S = 'Marina Abramović in Brazil- The Space in Between.mp4'
# S = 'Corel X6 Português - Brasil + Keygen'



b = 'NÃO ACEITE CÓPIAS, VISITE O ORIGINAL:'


# indiatpb.rocks/apibay/t.php?id=5014951 
asd = 'Youâ€šÞôll certainly appreciate the clear, concise information on key exam topics, including using Linux command line tools, managing software, configuring hardware, managing files and filesystems, working with the X Window system, administering the system, basic networking, and more. '


star = '1917.2019.720p.WEBRip.h264.Dual.YG⭐'

ten = '1【2345】6'


def filter_utf_chars(string):
    '''
        filters out chars that can cause misalignments
        because made of more than a byte... makes sense?
    '''
    return bytearray(
        ord(c.encode('utf-8')) for c in replace_special_chars(
            string
        ) if len(c.encode('utf-8')) == 1
    ).decode('utf-8')


def replace_special_chars(t):
    ''' https://www.i18nqa.com/debug/utf8-debug.html
        https://www.i18nqa.com/debug/bug-double-conversion.html
        https://stackoverflow.com/questions/15502619/correctly-reading-text-from-windows-1252cp1252-file-in-python

        some of the chars here im not sure are correct,
        check dumbo dublat romana translation

    '''
    special_chars = {
        # 'Äƒ': 'Ã',
        # 'Äƒ': 'ă',
        'Ã¢': 'â',
        'Ã¡': 'á', 'ã¡': 'á',
        'Ã ': 'à',
        'Ã¤': 'ä',
        'Å£': 'ã',
        # 'ÅŸ': 'ß',
        'ÃŸ': 'ß',
        'Ã©': 'é', 'ã©': 'é',
        'Ã¨': 'è',
        'Ã' : 'É', 'Ã‰': 'É',
        'Ã­': 'í',
        'Ã': 'Í',
        # 'Ã®': 'î',
        'Ã³': 'ó',
        'Ã“': 'Ó',
        'Ã¶': 'ö',
        'Ãº': 'ú',
        'Ã¹': 'ù',
        'Ã¼': 'ü',
        'Ã±': 'ñ',
        'Ã‘': 'Ñ',
        'Â´': '\'',
        '´': '\'',
        'â€ž': '“',
        'â€œ': '”',
        'â€¦': '…',
        b'\xe2\x80\x8e'.decode('utf-8') : '', # left-to-right-mark
        b'\xe2\x80\x8b'.decode('utf-8') : '',	# zero-width-space
        '&amp' : '&',
        '&;': '&',
        '【': '[',
        '】': ']',
        'â€“': '-',
        '⑥': '6',
    }

    for o, i in special_chars.items():
        t = str(t).replace(o, i)
    return t


def is_latin_supplement_A(char):
    hex_bytes = char.encode()
    if len( hex_bytes ) != 2:
        return False
    if hex_bytes[0] != 0xc3: # 195
        return False
    if hex_bytes[1] not in (0x82, 0x83, 0x84, 0x85, ):
        return False
    return True

def get_next_char(input_txt, i):
    try:
        return input_txt[i+1]
    except IndexError:
        return ''

def translate_multibyte_chars(input_txt):
    output_txt = ''
    multibyte_char = bytearray()
    for c, char in enumerate(input_txt):

        if is_latin_supplement_A(char) and len( get_next_char(input_txt, c).encode() ) > 1: # 1st mystical char
            multibyte_char.append( char.encode()[0] )

        elif multibyte_char: # 2nd mystical char
            # print(multibyte_char.decode(), end='')
            multibyte_char.append( char.encode()[-1] )
            output_txt += multibyte_char.decode()
            multibyte_char = bytearray()
        
        else: # normal char
            # print(char, end='')
            output_txt += char

    return output_txt

if __name__ == "__main__":

    # a = 'è'.encode()
    # print(a.decode(WIN1252))

    # x = translate_multibyte_chars(yoo)
    # x = translate_multibyte_chars(DUMBO)
    # print(x)


    a = star.encode(WIN1252)
    print(a.decode())
