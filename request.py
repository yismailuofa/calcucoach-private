'''
generate a request based on user inputs

1. What is your gender?
2. What is your age? >50 do timid workouts
3. What is your workout style?
    1. Mass: Bulking - Jacked
    2. Tone: Cutting - Lean - Toning
   	3. Athletics: Stamina - Cardio - Sports - Athlete
4. How many days do you want to workout a week 3 , 4 , 5 ? 

samplePayload = {
    gender: "Male",
    age: 42,
    workoutStyle: 1,
    workoutDays: 4
}
'''
def generateRequest(gender: str, age: int, workoutStyle: int, workoutDays: int):
    request = {
        "chestFactor": 0.5,
        "tricepFactor": 0.5,
        "bicepFactor": 0.5,
        "legFactor": 0.5,
        "backFactor": 0.5,
        "cardioFactor": 0.5,
        "shoulderFactor": 0.5
    }

    if gender == "Male":
        request["chestFactor"] += 0.2
        request["bicepFactor"] += 0.2
        request["backFactor"] += 0.2
        request["shoulderFactor"] += 0.2

    else:
        request["legFactor"] += 0.2
        request["cardioFactor"] += 0.2


    return request