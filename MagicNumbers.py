listLength = 2  # type: int
powerOfEquation = listLength - 1  # type: int
rangeMin = 1  # type: int
rangeMax = 100  # type: int
noOfGeneration = 2000  # type: int
mutationRate = 0.2  # type: float
crossoverRate = 0.2  # type: float
populationSize = 300  # type: int
seedRangeMin = 1  # type: int
seedRangeMax = 5  # type: int


def constant_to_list():
    return "List Length: {}\nPower Of Equation: {}\nRange Min: {}, Max: {}\nNo Of Generation: {}\n" \
           "Mutation Rate: {}\nCrossover Rate: {}\nPopulation Size: {}\nSeed Range: {} - {}\n\n" \
        .format(listLength, powerOfEquation, rangeMin, rangeMax, noOfGeneration, mutationRate,
                crossoverRate, populationSize, seedRangeMin, seedRangeMax)


def get_file_name():
    return 'out{}.txt'.format(hash(constant_to_list()))


def make_table(seed_value, genomeList):
    equation_as_string = '{}'.format(genomeList[0])
    for i in range(1, len(genomeList) - 1):
        equation_as_string += ' + {}'.format(genomeList[i])
    equation_as_string += ' = {}'.format(genomeList[len(genomeList) - 1])
    return '\n{}\t\t\t\t{}'.format(seed_value, equation_as_string)


def write_to_file(all_output):
    file_content = ''
    for (seed_value, genome_list) in all_output:
        file_content += make_table(seed_value, genome_list)
    string_to_update_file = constant_to_list()
    header = 'Seed Value\t\tpoints\n-------------------------------'
    file_location = 'output/' + get_file_name()
    file_obj = open(file_location, 'w')
    file_obj.write(string_to_update_file + header + file_content)
    file_obj.close()


def read_and_print_file():
    file_location = 'output/' + get_file_name()
    file_obj = open(file_location, 'r')
    print(file_obj.read())
    file_obj.close()
