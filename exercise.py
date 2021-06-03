class Exercise:
    '''
    Represents an exercise in the database.

    Attributes:
        name: str
        numSets: int
        numReps: int
        chestFactor: float
        shoulderFactor: float
        tricepFactor: float
        bicepFactor: float
        legFactor: float
        backFactor: float
        cardioFactor: float
    '''
    def __init__(
        self,
        name: str,
        numSets: int,
        numReps: int,
        chestFactor: float,
        shoulderFactor: float,
        tricepFactor: float,
        bicepFactor: float,
        legFactor: float,
        backFactor: float,
        cardioFactor: float
    ):
        self.name = name
        self.numSets = numSets
        self.numReps = numReps
        self.chestFactor = chestFactor
        self.shoulderFactor = shoulderFactor
        self.tricepFactor = tricepFactor
        self.bicepFactor = bicepFactor
        self.legFactor = legFactor
        self.backFactor = backFactor
        self.cardioFactor = cardioFactor

    def __str__(self):
        return f"{self.name}: {self.numSets} x {self.numReps}"

def main():
    a = Exercise(
        name="Bench Press",
        numSets=3,
        numReps=10,
        chestFactor=1,
        shoulderFactor=0.2,
        tricepFactor=0.5,
        bicepFactor=0.6,
        legFactor=0.1,
        backFactor=0.2,
        cardioFactor=0.2
    )
    print(a)

if __name__ == "__main__":
    main()