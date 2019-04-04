from pyevolve import G1DList, Consts, GSimpleGA, Selectors, Scaling, DBAdapters, Mutators
from random import seed
import MagicNumbers as mn


def eval_func(genome):
    # iterate over the chromosome
    # The same as "score = len(filter(lambda x: x==0, genome))"
    c = genome[len(genome) - 1] ** mn.powerOfEquation

    total = 0
    for value in genome[:len(genome) - 1]:
        total += value ** mn.powerOfEquation

    return abs(c - total)


def main():
    # Genome instance, 1D List of 50 elements
    genome = G1DList.G1DList(mn.listLength)

    # Sets the range max and min of the 1D List
    genome.setParams(rangemin=mn.rangeMin, rangemax=mn.rangeMax, bestrawscore=0.0000)

    # The evaluator function (evaluation function)
    genome.evaluator.set(eval_func)

    # Genetic Algorithm Instance
    ga = GSimpleGA.GSimpleGA(genome)
    ga.setMinimax(Consts.minimaxType["minimize"])

    # set the Roulette Wheel selector method, the number of generations and
    # the termination criteria
    ga.selector.set(Selectors.GRouletteWheel)
    ga.setGenerations(mn.noOfGeneration)
    ga.setMutationRate(mn.mutationRate)
    ga.setCrossoverRate(mn.crossoverRate)
    ga.setPopulationSize(mn.populationSize)
    ga.terminationCriteria.set(GSimpleGA.RawScoreCriteria)
    # ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)

    pop = ga.getPopulation()
    pop.scaleMethod.set(Scaling.SigmaTruncScaling)

    # Do the evolution, with stats dump
    # frequency of 20 generations
    ga.evolve(freq_stats=100)

    # Best individual
    print ga.bestIndividual()


if __name__ == "__main__":
    seed(mn.randomSeeding)
    main()

