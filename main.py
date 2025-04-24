import time
from autocorrect import Speller


def test_case(spell, sentence, label):
    start = time.time()
    corrected = spell(sentence)
    duration = time.time() - start
    print(f"[{label}] {corrected}")
    print(f"[{label}] Tiempo: {duration*1000:.2f} ms\n")


def main():
    sentence = "I'm not consiousnes and tehre is no place I'm giong to."  # doble errores
    noisy_sentence = "¿Cmo estas???!!!  Estoy compleetamentee bienn, grcias."

    print("\n--- Prueba con frase simple y errores dobles ---\n")


    spell_fast = Speller(lang="en", fast=True)
    spell_semi = Speller(lang="en", fast="semi")
    spell_slow = Speller(lang="en", fast=False)

    spell_fast_es = Speller(lang="es", fast=True)
    spell_semi_es = Speller(lang="es", fast="semi")
    spell_slow_es = Speller(lang="es", fast=False)

    test_case(spell_fast, sentence, "RAPIDO")
    test_case(spell_semi, sentence, "SEMI")
    test_case(spell_slow, sentence, "LENTO")

    print("\n--- Prueba con signos de puntuación y símbolos (Para ES)---\n")

    test_case(spell_fast_es, noisy_sentence, "RAPIDO + LIMPIEZA")
    test_case(spell_semi_es, noisy_sentence, "SEMI + LIMPIEZA")
    test_case(spell_slow_es, noisy_sentence, "LENTO + LIMPIEZA")


if __name__ == "__main__":
    main()

