from arnie import generateProgram


def generateResponse(payload: dict) -> dict:
    '''
    generate a response based on user payload

    samplePayload = {
        'gender': 'male',
        'workoutStyle': '1',
        'workoutDays': '4'
    }
    '''
    gender = payload.get('gender')
    workoutStyle = payload.get('workoutStyle')
    workoutDays = payload.get('workoutDays')

    if gender is None:
        gender = 'Male'

    if workoutStyle is None:
        workoutStyle = '6'

    if workoutDays is None:
        workoutDays = '3'

    return generateProgram(gender=gender, workoutStyle=workoutStyle, workoutDays=workoutDays)
