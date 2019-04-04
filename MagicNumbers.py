from random import seed
import PowerOfConjusture

listLength = 4  # type: int
powerOfEquation = listLength - 1  # type: int
rangeMin = 1  # type: int
rangeMax = 100  # type: int
noOfGeneration = 2000  # type: int
mutationRate = 0.2  # type: float
crossoverRate = 0.2  # type: float
populationSize = 300  # type: int
randomSeeding = 100  # type: int

if __name__ == "__main__":
    for seedValue in range(1, 10):
        seed(seedValue)
        best = PowerOfConjusture.main()
        print seedValue, best.genomeList, best.score
