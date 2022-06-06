from ponstrans import translate
from pprint import pprint

word = 'programacion'
source_language = "es"
target_language = "de"

translations = translate(
    word=word, source_language=source_language, target_language=target_language)
pprint(translations[:])
