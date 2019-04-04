from random import seed
import PowerOfConjusture
from MagicNumbers import make_table, read_and_print_file, write_to_file, seedRange

if __name__ == "__main__":
    try:
        read_and_print_file()
    except IOError:
        output_string = ''
        for seedValue in range(1, seedRange + 1):
            seed(seedValue)
            best = PowerOfConjusture.get_best_individual()
            if best.score == 0.0:
                output_string += make_table(seedValue, best.genomeList)
        write_to_file(output_string)
        read_and_print_file()
