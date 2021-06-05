class Exercise:
    '''
    Represents an exercise in the database.
    '''
    def __init__(self, name: str, numSets: int, numReps: int):
        self.name = name
        self.numSets = numSets
        self.numReps = numReps

    def __str__(self):
        return f"{self.name}: {self.numSets} x {self.numReps}"
