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
    gender = payload.get('gender','male')
    workoutStyle = payload.get('workoutStyle','6')
    workoutDays = payload.get('workoutDays','3')

    return generateProgram(gender=gender, workoutStyle=workoutStyle, workoutDays=workoutDays)
