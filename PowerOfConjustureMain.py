from random import seed
import PowerOfConjusture
from MagicNumbers import read_and_print_file, write_to_file, seedRangeMax, seedRangeMin


def find_equation():
    all_outputs = []
    for seedValue in range(seedRangeMin, seedRangeMax + 1):
        seed(seedValue)
        best = PowerOfConjusture.get_best_individual()
        if best.score == 0.0:
            all_outputs.append((seedValue, best.genomeList))
    write_to_file(all_outputs)
    read_and_print_file()


if __name__ == "__main__":
    try:
        read_and_print_file()
    except IOError:
        find_equation()
