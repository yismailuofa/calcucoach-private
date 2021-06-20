from programs import programs


def generateProgram(gender: str, workoutStyle: str, workoutDays: str):
    '''
    Return a workout program based on user input
    '''
    key = f'{gender.lower()}Programs{workoutDays}'

    return programs[key][str(workoutStyle)]
