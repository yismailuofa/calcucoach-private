'''
1. Toning: Uncover the muscle beneath.
2. Fat Burner: Burn fat quickly and easily.
3. Beach Body: Look good on and off the beach.
4. Gender:
    Male-> Beast Mode: You will go HARD. Not for the light-hearted.
    Female-> Hourglass: Get the hourglass figure you deserve. 
5. Athlete: Get conditioned and reach the top of your game.  
6. All Around: A healthy balance of all workouts.
7. Beginner: Recommended for beginners new to the gym and working out.
8. Strength: Focus on strength and form.
9. Endurance: Enhance the body and the mind.
10. Hollywood: Train like the celebrities with curated workouts.

3 days: Push Pull Legs
4 days: Chest/Triceps Back/Biceps Shoulders/Trap Legs/Abs
5 days: Push Pull Push Pull Legs
'''

programs = {
    'malePrograms3': {
        '1': {
            'Monday': [
                {'name': 'Dumbbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Arnold Dumbbell Press', 'freq': '3 x 12'},
                {'name': 'Cable Lateral Raise', 'freq': '3 x 12'},
                {'name': 'Tricep Dips', 'freq': '3 x 8'},
            ],
            'Wednesday': [
                {'name': 'Wide Grip Pullup', 'freq': '3 x 8'},
                {'name': 'Seated Cable Row', 'freq': '3 x 12'},
                {'name': 'Face Pull', 'freq': '3 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 12'},
                {'name': 'Dumbbell Hammer Curl', 'freq': '3 x 12'},
            ],
            'Friday': [
                {'name': 'Barbell Squat', 'freq': '3 x 12'},
                {'name': 'Machine Leg Press', 'freq': '3 x 12'},
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Abdominal Crunch', 'freq': '3 x 10'},
                {'name': 'Hanging Leg Raise', 'freq': '3 x 10'},
            ]
        },
        '2': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Burpees', 'freq': '3 x 10'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Dumbbell Side Lateral Raise', 'freq': '3 x 15'},
                {'name': 'Dumbbell Overhead Tricep Extension', 'freq': '3 x 15'},
            ],
            'Wednesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bicep Curl', 'freq': '3 x 15'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Stair Climber', 'freq': '3 x 45 secs'},
                {'name': 'Dumbbell Lunges', 'freq': '3 x 10'},
                {'name': 'Bicycle Crunches', 'freq': '3 x 15'},
                {'name': 'Russian Twists', 'freq': '3 x 15'},
            ]
        },
        '3': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Overhead Tricep Extension', 'freq': '3 x 10'},
            ],
            'Wednesday': [
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Reverse Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'T-Bar Row', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bicep Curl', 'freq': '3 x 10'},
                {'name': 'Dumbbell Concentration Curl', 'freq': '3 x 10'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Abdominal Crunch', 'freq': '3 x 15'},
                {'name': 'Mountain Climber', 'freq': '3 x 15'},
            ]
        },
        '4': {
            'Monday': [
                {'name': 'Dumbbell Bench Press Pyramid Sets', 'freq': '5 x 8'},
                {'name': 'Dumbbell Incline Bench Press', 'freq': '5 x 5'},
                {'name': 'Arnold Dumbbell Press', 'freq': '3 x 12'},
                {'name': 'Barbell Skullcrushers', 'freq': '3 x 12'},
                {'name': 'Barbell Close Grip Bench Press', 'freq': '3 x 8'},
            ],
            'Wednesday': [
                {'name': 'Farmers Walk', 'freq': '150 Steps'},
                {'name': 'T-Bar Row Dropset', 'freq': '3 x 10'},
                {'name': 'Weighted Pullups', 'freq': '3 x 6'},
                {'name': 'Bicep Concentration Curls', 'freq': '5 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 15'},
            ],
            'Friday': [
                {'name': 'Treadmill HIIT', 'freq': '15 min'},
                {'name': 'Machine Leg Press Pyramid Sets', 'freq': '5 x 8'},
                {'name': 'Barbell Squat', 'freq': '3 x 8'},
                {'name': 'Hanging Leg Raise', 'freq': '3 x 15'},
                {'name': 'Plank', 'freq': '3 x 1.5 min'},
            ]
        },
        '5': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Front Lateral Raise', 'freq': '3 x 10'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
            ],
            'Wednesday': [
                {'name': 'Bent Over Dumbbell Row', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Barbell Deadlift', 'freq': '3 x 8'},
                {'name': 'Face Pull', 'freq': '3 x 12'},
                {'name': 'Unilateral Cable Curl', 'freq': '3 x 12'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press Explosive', 'freq': '3 x 10'},
                {'name': 'Machine Leg Extension', 'freq': '3 x 10'},
                {'name': 'Machine Leg Curl', 'freq': '3 x 10'},
            ]
        },
        '6': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Barbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
            ],
            'Wednesday': [
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Reverse Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Barbell Preacher Curl', 'freq': '3 x 12'},
                {'name': 'Dumbbell Hammer Curl', 'freq': '3 x 12'},
            ],
            'Friday': [
                {'name': 'Barbell Squat', 'freq': '3 x 8'},
                {'name': 'Machine Leg Press', 'freq': '3 x 12'},
                {'name': 'Machine Leg Extension', 'freq': '3 x 10'},
                {'name': 'Machine Leg Curl', 'freq': '3 x 10'},
                {'name': 'Calf Raise', 'freq': '3 x 15'},
            ]
        },
        '7': {
            'Monday': [
                {'name': 'Treadmill Low Intensity', 'freq': '15 min'},
                {'name': 'Bench Press', 'freq': '5 x 5'},
                {'name': 'Barbell Squat', 'freq': '5 x 5'},
                {'name': 'Machine Row', 'freq': '5 x 5'},
                {'name': 'Military Overhead Press', 'freq': '5 x 5'},
            ],
            'Wednesday': [
                {'name': 'Exercise Bike Low Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Bench Press', 'freq': '5 x 5'},
                {'name': 'Barbell Squat', 'freq': '5 x 5'},
                {'name': 'Barbell Deadlift', 'freq': '5 x 5'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '5 x 5'},
            ],
            'Friday': [
                {'name': 'Treadmill Low Intensity', 'freq': '15 min'},
                {'name': 'Bench Press', 'freq': '5 x 5'},
                {'name': 'Barbell Squat', 'freq': '5 x 5'},
                {'name': 'Machine Row', 'freq': '5 x 5'},
                {'name': 'Military Overhead Press', 'freq': '5 x 5'},
            ]
        },
        '8': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '4 x 8'},
                {'name': 'Barbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Barbell Miltary Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Overhead Tricep Extension', 'freq': '4 x 8'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
            ],
            'Wednesday': [
                {'name': 'Barbell Deadlift', 'freq': '4 x 8'},
                {'name': 'T-bar Row', 'freq': '4 x 8'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Dumbbell Shrugs', 'freq': '3 x 10'},
                {'name': 'Weighted Pullups', 'freq': '3 x 6'},
            ],
            'Friday': [
                {'name': 'Barbell Squat', 'freq': '4 x 8'},
                {'name': 'Machine Leg Press', 'freq': '4 x 8'},
                {'name': 'Barbell Lunges', 'freq': '3 x 10'},
                {'name': 'Machine Leg Curl', 'freq': '3 x 10'},
                {'name': 'Calf Raise', 'freq': '3 x 10'},
            ]
        },
        '9': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '18 min'},
                {'name': 'Barbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Arnold Dumbbell Press', 'freq': '3 x 12'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 12'},
                {'name': 'Weighted Pullups', 'freq': '3 x 8'},
            ],
            'Wednesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '18 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Bicep Hammer Curl ', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row', 'freq': '3 x 12'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
            ],
            'Friday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '18 min'},
                {'name': 'Machine Leg Press', 'freq': '3 x 12'},
                {'name': 'Dumbbell Lunges', 'freq': '3 x 12'},
                {'name': 'Russian Twists', 'freq': '3 x 15'},
                {'name': 'Abdominal Crunch', 'freq': '3 x 15'},
            ]
        },
        '10': {
            'Monday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Incline Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Dumbbell Tricep Extension', 'freq': '3 x 10'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},
            ],
            'Wednesday': [
                {'name': 'Treadmill HIIT', 'freq': '15 min'},
                {'name': 'Dumbbell Bicep Curls', 'freq': '3 x 10'},
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Lateral Pulldown', 'freq': '3 x 10'},
                {'name': 'Barbell Deadlift', 'freq': '3 x 10'}
            ],
            'Friday': [
                {'name': 'Stairs', 'freq': '15 Min'},
                {'name': 'Barbell Lunges', 'freq': '3 x 10'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press Explosive', 'freq': '3 x 10'},
                {'name': 'Burpees', 'freq': '3 x 10'}
            ]
        }
    },

    'malePrograms4': {
        '1': {
            'Monday': [
                {'name': 'Dumbbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Incline Dumbbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Barbell Skullcrushers', 'freq': '3 x 12'},
                {'name': 'Tricep Dips', 'freq': '3 x 8'},
            ],
            'Tuesday': [
                {'name': 'Wide Grip Pullup', 'freq': '3 x 8'},
                {'name': 'Seated Cable Row', 'freq': '3 x 12'},
                {'name': 'Face Pull', 'freq': '3 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 12'},
                {'name': 'Dumbbell Hammer Curl', 'freq': '3 x 12'},
            ],
            'Thursday': [
                {'name': 'Arnold Dumbbell Press', 'freq': '3 x 12'},
                {'name': 'Cable Lateral Raise', 'freq': '3 x 12'},
                {'name': 'Reverse Pec Deck', 'freq': '3 x 12'},
                {'name': 'Dumbbell Shrugs', 'freq': '3 x 12'},
                {'name': 'Farmers Walk', 'freq': '50 Steps'},
            ],
            'Friday': [
                {'name': 'Barbell Squat', 'freq': '3 x 12'},
                {'name': 'Machine Leg Press', 'freq': '3 x 12'},
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Abdominal Crunch', 'freq': '3 x 10'},
                {'name': 'Hanging Leg Raise', 'freq': '3 x 10'},
            ]
        },
        '2': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Burpees', 'freq': '3 x 10'},
                {'name': 'Incline Cable Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Dumbbell Overhead Tricep Extension', 'freq': '3 x 15'},
            ],
            'Tuesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bicep Curl', 'freq': '3 x 15'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
            ],
            'Thursday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Shoulder Flyes', 'freq': '3 x 15'},
                {'name': 'Arnold Dumbbell Press', 'freq': '3 x 15'},
                {'name': 'Dumbbell Front Lateral Raise', 'freq': '3 x 15'},
                {'name': 'Front Plate Raise with Twist', 'freq': '3 x 15'},
            ],
            'Friday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Stair Climber', 'freq': '3 x 45 secs'},
                {'name': 'Dumbbell Lunges', 'freq': '3 x 10'},
                {'name': 'Bicycle Crunches', 'freq': '3 x 15'},
                {'name': 'Russian Twists', 'freq': '3 x 15'},
            ]
        },
        '3': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Overhead Tricep Extension', 'freq': '3 x 10'},
                {'name': 'Tricep Dips', 'freq': '3 x 8'},
            ],
            'Tuesday': [
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Reverse Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'T-Bar Row', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bicep Curl', 'freq': '3 x 10'},
                {'name': 'Dumbbell Concentration Curl', 'freq': '3 x 10'},
            ],
            'Thursday': [
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Barbell Shrugs', 'freq': '3 x 10'},
                {'name': 'Dumbbell Side Lateral Raise', 'freq': '3 x 10'},
                {'name': 'Barbell Upright Row', 'freq': '3 x 10'},
                {'name': 'Front Plate Raise with Twist', 'freq': '3 x 10'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Abdominal Crunch', 'freq': '3 x 15'},
                {'name': 'Mountain Climber', 'freq': '3 x 15'},
                {'name': 'Hanging Leg Raise', 'freq': '3 x 15'},
            ]
        },
        '4': {
            'Monday': [
                {'name': 'Dumbbell Bench Press Pyramid Sets', 'freq': '5 x 8'},
                {'name': 'Dumbbell Incline Bench Press', 'freq': '5 x 5'},
                {'name': 'Barbell Skullcrushers', 'freq': '3 x 12'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 12'},
                {'name': 'Barbell Close Grip Bench Press', 'freq': '3 x 8'},
            ],
            'Tuesday': [
                {'name': 'Farmers Walk', 'freq': '150 Steps'},
                {'name': 'T-Bar Row Dropset', 'freq': '3 x 10'},
                {'name': 'Weighted Pullups', 'freq': '3 x 6'},
                {'name': 'Bicep Concentration Curls', 'freq': '5 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 15'},
            ],
            'Thursday': [
                {'name': 'Arnold Dumbbell Press Pyramid Sets', 'freq': '5 x 8'},
                {'name': 'Machine Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Barbell Shrugs', 'freq': '3 x 10'},
                {'name': 'Barbell Miltary Press', 'freq': '3 x 10'},
                {'name': 'Cable Upright Row', 'freq': '3 x 10'},
            ],
            'Friday': [
                {'name': 'Treadmill HIIT', 'freq': '15 min'},
                {'name': 'Machine Leg Press Pyramid Sets', 'freq': '5 x 8'},
                {'name': 'Barbell Squat', 'freq': '3 x 8'},
                {'name': 'Hanging Leg Raise', 'freq': '3 x 15'},
                {'name': 'Plank', 'freq': '3 x 1.5 min'},
            ]
        },
        '5': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Dumbbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
            ],
            'Tuesday': [
                {'name': 'Bent Over Dumbbell Row', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Barbell Deadlift', 'freq': '3 x 8'},
                {'name': 'Face Pull', 'freq': '3 x 12'},
                {'name': 'Unilateral Cable Curl', 'freq': '3 x 12'},
            ],
            'Thursday': [
                {'name': 'Dumbbell Side Lateral Raise', 'freq': '3 x 10'},
                {'name': 'Miltary Overhead Press', 'freq': '3 x 10'},
                {'name': 'Barbell Shrugs', 'freq': '3 x 15'},
                {'name': 'Front Plate Raise with Twist', 'freq': '3 x 10'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press Explosive', 'freq': '3 x 10'},
                {'name': 'Machine Leg Extension', 'freq': '3 x 10'},
                {'name': 'Machine Leg Curl', 'freq': '3 x 10'},
            ]
        },
        '6': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Barbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
                {'name': 'Unilateral Cable Tricep Pushdown', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Reverse Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Barbell Preacher Curl', 'freq': '3 x 12'},
                {'name': 'Dumbbell Hammer Curl', 'freq': '3 x 12'},
            ],
            'Thursday': [
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Barbell Upright Row', 'freq': '3 x 10'},
                {'name': 'Dumbbell Side Lateral Raise', 'freq': '3 x 10'},
                {'name': 'Front Plate Raise with Twist', 'freq': '3 x 10'},
                {'name': 'Barbell Shrugs', 'freq': '3 x 10'},
            ],
            'Friday': [
                {'name': 'Barbell Squat', 'freq': '3 x 8'},
                {'name': 'Machine Leg Press', 'freq': '3 x 12'},
                {'name': 'Machine Leg Extension', 'freq': '3 x 10'},
                {'name': 'Machine Leg Curl', 'freq': '3 x 10'},
                {'name': 'Calf Raise', 'freq': '3 x 15'},
            ]
        },
        '7': {
            'Monday': [
                {'name': 'Treadmill Low Intensity', 'freq': '15 min'},
                {'name': 'Bench Press', 'freq': '5 x 5'},
                {'name': 'Barbell Squat', 'freq': '5 x 5'},
                {'name': 'Barbell Deadlift', 'freq': '5 x 5'},
                {'name': 'Military Overhead Press', 'freq': '5 x 5'},
            ],
            'Tuesday': [
                {'name': 'Exercise Bike Low Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Bench Press', 'freq': '5 x 5'},
                {'name': 'Barbell Squat', 'freq': '5 x 5'},
                {'name': 'Machine Row', 'freq': '5 x 5'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '5 x 5'},
            ],
            'Thursday': [
                {'name': 'Treadmill Low Intensity', 'freq': '15 min'},
                {'name': 'Bench Press', 'freq': '5 x 5'},
                {'name': 'Barbell Squat', 'freq': '5 x 5'},
                {'name': 'Barbell Deadlift', 'freq': '5 x 5'},
                {'name': 'Military Overhead Press', 'freq': '5 x 5'},
            ],
            'Friday': [
                {'name': 'Exercise Bike Low Intensity', 'freq': '15 min'},
                {'name': 'Bench Press', 'freq': '5 x 5'},
                {'name': 'Machine Leg Press', 'freq': '5 x 5'},
                {'name': 'Machine Row', 'freq': '5 x 5'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '5 x 5'},
            ]
        },
        '8': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '4 x 8'},
                {'name': 'Barbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Barbell Decline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Overhead Tricep Extension', 'freq': '4 x 8'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Barbell Deadlift', 'freq': '4 x 8'},
                {'name': 'T-bar Row', 'freq': '4 x 8'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Reverse Pec Deck', 'freq': '3 x 10'},
                {'name': 'Weighted Pullups', 'freq': '3 x 6'},
            ],
            'Thursday': [
                {'name': 'Barbell Miltary Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Front Plate Raise with Twist', 'freq': '4 x 8'},
                {'name': 'Dumbbell Shrug', 'freq': '3 x 10'},
                {'name': 'Barbell Upright Row', 'freq': '4 x 8'},
            ],
            'Friday': [
                {'name': 'Barbell Squat', 'freq': '4 x 8'},
                {'name': 'Machine Leg Press', 'freq': '4 x 8'},
                {'name': 'Barbell Lunges', 'freq': '3 x 10'},
                {'name': 'Machine Leg Curl', 'freq': '3 x 10'},
                {'name': 'Calf Raise', 'freq': '3 x 10'},
            ]
        },
        '9': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '18 min'},
                {'name': 'Barbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Dumbbell Incline Bench Press', 'freq': '3 x 12'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 12'},
                {'name': 'Tricep Pushdown', 'freq': '3 x 8'},
            ],
            'Tuesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '18 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Bicep Hammer Curl', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row', 'freq': '3 x 12'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
            ],
            'Thursday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '18 min'},
                {'name': 'Arnold Dumbbell Press', 'freq': '3 x 12'},
                {'name': 'Cable Upright Row', 'freq': '3 x 12'},
                {'name': 'Front Plate Raise with Twist', 'freq': '3 x 8'},
                {'name': 'Dumbbell Shrugs', 'freq': '3 x 12'},
            ],
            'Friday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '18 min'},
                {'name': 'Machine Leg Press', 'freq': '3 x 12'},
                {'name': 'Dumbbell Lunges', 'freq': '3 x 12'},
                {'name': 'Russian Twists', 'freq': '3 x 15'},
                {'name': 'Abdominal Crunch', 'freq': '3 x 15'},
            ]
        },
        '10': {
            'Monday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Chest Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Tricep Extension', 'freq': '3 x 10'},
                {'name': 'Barbell Skullcrushers', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Treadmill HIIT', 'freq': '15 min'},
                {'name': 'Dumbbell Bicep Curls', 'freq': '3 x 10'},
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Lateral Pulldown', 'freq': '3 x 10'},
                {'name': 'Barbell Deadlift', 'freq': '3 x 10'}
            ],
            'Thursday': [
                {'name': 'Elliptical Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Shoulder Shrug', 'freq': '3 x 12'},
                {'name': 'Arnold Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Military Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Front Lateral Raise', 'freq': '3 x 10'},
            ],
            'Friday': [
                {'name': 'Stairs', 'freq': '15 min'},
                {'name': 'Barbell Lunges', 'freq': '3 x 10'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press Explosive', 'freq': '3 x 10'},
                {'name': 'Burpees', 'freq': '3 x 10'}
            ]
        }
    },

    'malePrograms5': {
        '1': {
            'Monday': [
                {'name': 'Dumbbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Arnold Dumbbell Press', 'freq': '3 x 12'},
                {'name': 'Cable Lateral Raise', 'freq': '3 x 12'},
                {'name': 'Tricep Dips', 'freq': '3 x 8'},
            ],
            'Tuesday': [
                {'name': 'Wide Grip Pullup', 'freq': '3 x 8'},
                {'name': 'Seated Cable Row', 'freq': '3 x 12'},
                {'name': 'Face Pull', 'freq': '3 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 12'},
                {'name': 'Dumbbell Hammer Curl', 'freq': '3 x 12'},
            ],
            'Wednesday': [
                {'name': 'Incline Dumbbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 12'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 12'},
                {'name': 'Dumbbell Side Lateral Raise', 'freq': '3 x 12'},
                {'name': 'Tricep Bar Pushdown', 'freq': '3 x 12'},
            ],
            'Thursday': [
                {'name': 'Chinups', 'freq': '3 x 8'},
                {'name': 'Seated Machine Row', 'freq': '3 x 12'},
                {'name': 'Barbell Upright Row', 'freq': '3 x 12'},
                {'name': 'Unilateral Cable Curl', 'freq': '3 x 12'},
                {'name': 'Barbell Preacher Curl', 'freq': '3 x 12'},
            ],
            'Friday': [
                {'name': 'Barbell Squat', 'freq': '3 x 12'},
                {'name': 'Machine Leg Press', 'freq': '3 x 12'},
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Abdominal Crunch', 'freq': '3 x 10'},
                {'name': 'Hanging Leg Raise', 'freq': '3 x 10'},
            ]
        },
        '2': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Burpees', 'freq': '3 x 10'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Dumbbell Side Lateral Raise', 'freq': '3 x 15'},
                {'name': 'Dumbbell Overhead Tricep Extension', 'freq': '3 x 15'},
            ],
            'Tuesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bicep Curl', 'freq': '3 x 15'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
            ],
            'Wednesday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Burpees', 'freq': '3 x 10'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Machine Shoulder Flyes', 'freq': '3 x 15'},
                {'name': 'Barbell Skullcrushers', 'freq': '3 x 15'},
            ],
            'Thursday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Close Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Unilateral Cable Curl', 'freq': '3 x 15'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Stair Climber', 'freq': '3 x 45 secs'},
                {'name': 'Dumbbell Lunges', 'freq': '3 x 10'},
                {'name': 'Bicycle Crunches', 'freq': '3 x 15'},
                {'name': 'Russian Twists', 'freq': '3 x 15'},
            ]
        },
        '3': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Overhead Tricep Extension', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Reverse Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'T-Bar Row', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bicep Curl', 'freq': '3 x 10'},
                {'name': 'Dumbbell Concentration Curl', 'freq': '3 x 10'},
            ],
            'Wednesday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Barbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Machine Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Overhead Tricep Extension', 'freq': '3 x 10'},
            ],
            'Thursday': [
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Close Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'T-Bar Row', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bicep Curl', 'freq': '3 x 10'},
                {'name': 'Barbell Preacher Curl', 'freq': '3 x 10'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Abdominal Crunch', 'freq': '3 x 15'},
                {'name': 'Mountain Climber', 'freq': '3 x 15'},
            ]
        },
        '4': {
            'Monday': [
                {'name': 'Dumbbell Bench Press Pyramid Sets', 'freq': '5 x 8'},
                {'name': 'Dumbbell Incline Bench Press', 'freq': '5 x 5'},
                {'name': 'Arnold Dumbbell Press', 'freq': '3 x 12'},
                {'name': 'Barbell Skullcrushers', 'freq': '3 x 12'},
                {'name': 'Barbell Close Grip Bench Press', 'freq': '3 x 8'},
            ],
            'Tuesday': [
                {'name': 'Farmers Walk', 'freq': '150 Steps'},
                {'name': 'T-Bar Row Dropset', 'freq': '3 x 10'},
                {'name': 'Weighted Pullups', 'freq': '3 x 6'},
                {'name': 'Bicep Concentration Curls', 'freq': '5 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 15'},
            ],
            'Wednesday': [
                {'name': 'Barbell Bench Press Pyramid Sets', 'freq': '5 x 8'},
                {'name': 'Dumbbell Incline Bench Press', 'freq': '5 x 5'},
                {'name': 'Arnold Dumbbell Press', 'freq': '3 x 12'},
                {'name': 'Dumbbell Overhead Tricep Extension', 'freq': '3 x 8'},
                {'name': 'Weighted Dips', 'freq': '3 x 8'},
            ],
            'Thursday': [
                {'name': 'Farmers Walk', 'freq': '150 Steps'},
                {'name': 'Barbell Deadlift Dropset', 'freq': '3 x 10'},
                {'name': 'Lat Pulldown', 'freq': '5 x 8'},
                {'name': 'Bicep Hammer Curls', 'freq': '5 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 15'},
            ],
            'Friday': [
                {'name': 'Treadmill HIIT', 'freq': '15 min'},
                {'name': 'Machine Leg Press Pyramid Sets', 'freq': '5 x 8'},
                {'name': 'Barbell Squat', 'freq': '3 x 8'},
                {'name': 'Hanging Leg Raise', 'freq': '3 x 15'},
                {'name': 'Plank', 'freq': '3 x 1.5 min'},
            ]
        },
        '5': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Front Lateral Raise', 'freq': '3 x 10'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
            ],
            'Tuesday': [
                {'name': 'Bent Over Dumbbell Row', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Barbell Deadlift', 'freq': '3 x 8'},
                {'name': 'Face Pull', 'freq': '3 x 12'},
                {'name': 'Unilateral Cable Curl', 'freq': '3 x 12'},
            ],
            'Wednesday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Miltary Overhead Press', 'freq': '3 x 10'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
            ],
            'Thursday': [
                {'name': 'Bent Over Dumbbell Row', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row Wide Grip', 'freq': '3 x 10'},
                {'name': 'Dumbbell Deadlift', 'freq': '3 x 10'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 12'},
                {'name': 'Unilateral Cable Curl', 'freq': '3 x 12'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press Explosive', 'freq': '3 x 10'},
                {'name': 'Machine Leg Extension', 'freq': '3 x 10'},
                {'name': 'Machine Leg Curl', 'freq': '3 x 10'},
            ]
        },
        '6': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Barbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Reverse Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Barbell Preacher Curl', 'freq': '3 x 12'},
                {'name': 'Dumbbell Hammer Curl', 'freq': '3 x 12'},
            ],
            'Wednesday': [
                {'name': 'Dumbbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Miltary Press', 'freq': '3 x 10'},
                {'name': 'Machine Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
            ],
            'Thursday': [
                {'name': 'Close Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Underhand Row', 'freq': '3 x 10'},
                {'name': 'Dumbbell Preacher Curl', 'freq': '3 x 12'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 12'},
            ],
            'Friday': [
                {'name': 'Barbell Squat', 'freq': '3 x 8'},
                {'name': 'Machine Leg Press', 'freq': '3 x 12'},
                {'name': 'Machine Leg Extension', 'freq': '3 x 10'},
                {'name': 'Machine Leg Curl', 'freq': '3 x 10'},
                {'name': 'Calf Raise', 'freq': '3 x 15'},
            ]
        },
        '7': {
            'Monday': [
                {'name': 'Treadmill Low Intensity', 'freq': '15 min'},
                {'name': 'Bench Press', 'freq': '5 x 5'},
                {'name': 'Barbell Squat', 'freq': '5 x 5'},
                {'name': 'Barbell Deadlift', 'freq': '5 x 5'},
                {'name': 'Military Overhead Press', 'freq': '5 x 5'},
            ],
            'Tuesday': [
                {'name': 'Exercise Bike Low Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Bench Press', 'freq': '5 x 5'},
                {'name': 'Barbell Squat', 'freq': '5 x 5'},
                {'name': 'Machine Row', 'freq': '5 x 5'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '5 x 5'},
            ],
            'Wednesday': [
                {'name': 'Elliptical Low Intensity', 'freq': '15 min'},
                {'name': 'Bench Press', 'freq': '5 x 5'},
                {'name': 'Barbell Bicep Curl', 'freq': '5 x 5'},
                {'name': 'Machine Row', 'freq': '5 x 5'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '5 x 5'},
            ],
            'Thursday': [
                {'name': 'Treadmill Low Intensity', 'freq': '15 min'},
                {'name': 'Bench Press', 'freq': '5 x 5'},
                {'name': 'Barbell Squat', 'freq': '5 x 5'},
                {'name': 'Barbell Deadlift', 'freq': '5 x 5'},
                {'name': 'Military Overhead Press', 'freq': '5 x 5'},
            ],
            'Friday': [
                {'name': 'Exercise Bike Low Intensity', 'freq': '15 min'},
                {'name': 'Bench Press', 'freq': '5 x 5'},
                {'name': 'Machine Leg Press', 'freq': '5 x 5'},
                {'name': 'Machine Row', 'freq': '5 x 5'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '5 x 5'},
            ]
        },
        '8': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '4 x 8'},
                {'name': 'Barbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Barbell Miltary Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Overhead Tricep Extension', 'freq': '4 x 8'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Barbell Deadlift', 'freq': '4 x 8'},
                {'name': 'T-bar Row', 'freq': '4 x 8'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Dumbbell Shrugs', 'freq': '3 x 10'},
                {'name': 'Weighted Pullups', 'freq': '3 x 6'},
            ],
            'Wednesday': [
                {'name': 'Barbell Bench Press', 'freq': '4 x 8'},
                {'name': 'Barbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Arnold Dumbbell Press', 'freq': '3 x 10'},
                {'name': 'Barbell Skullcrushers', 'freq': '3 x 10'},
                {'name': 'Tricep Bar Pushdown', 'freq': '3 x 10'},
            ],
            'Thursday': [
                {'name': 'Barbell Deadlift', 'freq': '4 x 8'},
                {'name': 'T-bar Row', 'freq': '4 x 8'},
                {'name': 'Lat Pulldown Wide Grip', 'freq': '3 x 10'},
                {'name': 'Barbell Shrugs', 'freq': '3 x 10'},
                {'name': 'Barbell Bicep Curls ', 'freq': '4 x 8'},
            ],
            'Friday': [
                {'name': 'Barbell Squat', 'freq': '4 x 8'},
                {'name': 'Machine Leg Press', 'freq': '4 x 8'},
                {'name': 'Barbell Lunges', 'freq': '3 x 10'},
                {'name': 'Machine Leg Curl', 'freq': '3 x 10'},
                {'name': 'Calf Raise', 'freq': '3 x 10'},
            ]
        },
        '9': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '18 min'},
                {'name': 'Barbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Arnold Dumbbell Press', 'freq': '3 x 12'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 12'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
            ],
            'Tuesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '18 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Bicep Hammer Curl', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row', 'freq': '3 x 12'},
                {'name': 'Weighted Pullups', 'freq': '3 x 6'},
            ],
            'Wednesday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '18 min'},
                {'name': 'Barbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Military Shoulder Press', 'freq': '3 x 12'},
                {'name': 'Front Plate Raise with Twist', 'freq': '3 x 8'},
                {'name': 'Dumbbell Shrugs', 'freq': '3 x 12'},
            ],
            'Thursday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '18 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Bicep Preacher Curl', 'freq': '3 x 12'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Weighted Pullups', 'freq': '3 x 6'},
            ],
            'Friday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '18 min'},
                {'name': 'Machine Leg Press', 'freq': '3 x 12'},
                {'name': 'Dumbbell Lunges', 'freq': '3 x 12'},
                {'name': 'Russian Twists', 'freq': '3 x 15'},
                {'name': 'Abdominal Crunch', 'freq': '3 x 15'},
            ]
        },
        '10': {
            'Monday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Chest Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Tricep Extension', 'freq': '3 x 10'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Treadmill HIIT', 'freq': '15 min'},
                {'name': 'Dumbbell Bicep Curls', 'freq': '3 x 10'},
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Lateral Pulldown', 'freq': '3 x 10'},
                {'name': 'Barbell Deadlift', 'freq': '3 x 10'}
            ],
            'Wednesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Close Grip Bench Press', 'freq': '3 x 10'},
                {'name': 'Tricep Cable Extensions', 'freq': '3 x 10'},
                {'name': 'Barbell Skullcrushers', 'freq': '3 x 10'},
                {'name': 'Weighted Pull-Ups', 'freq': '3 x 6'}
            ],
            'Thursday': [
                {'name': 'Elliptical Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Shoulder Shrug', 'freq': '3 x 12'},
                {'name': 'Arnold Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Military Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Front Lateral Raise', 'freq': '3 x 10'},
            ],
            'Friday': [
                {'name': 'Stairs', 'freq': '15 min'},
                {'name': 'Barbell Lunges', 'freq': '3 x 10'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press Explosive', 'freq': '3 x 10'},
                {'name': 'Burpees', 'freq': '3 x 10'}
            ]
        }
    },

    'femalePrograms3': {
        '1': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Barbell Pelvic Thrust', 'freq': '3 x 8'},
                {'name': 'Kettlebell Swing', 'freq': '3 x 8'},
                {'name': 'Plank', 'freq': '3 x 1 min'},
            ],
            'Wednesday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Machine Assisted Pullups', 'freq': '3 x 5'},
                {'name': 'Dumbbell Row', 'freq': '3 x 10'},
                {'name': 'Bar Cable Curl', 'freq': '3 x 12'},
                {'name': 'Mountain Climber', 'freq': '3 x 45 secs'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 8'},
                {'name': 'Dumbbell Lunges', 'freq': '3 x 10'},
                {'name': 'Inner Thigh Squeeze', 'freq': '3 x 10'},
                {'name': 'Side Plank', 'freq': '3 x 1 min'}
            ]
        },
        '2': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Burpees', 'freq': '3 x 12'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Glute Kickback', 'freq': '3 x 10'},
                {'name': 'Bench Tricep Dips', 'freq': '3 x 10'},
            ],
            'Wednesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Row', 'freq': '3 x 12'},
                {'name': 'Front Lateral Raise', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row', 'freq': '3 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 12'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Goblet Squat', 'freq': '3 x 15'},
                {'name': 'Dumbell Reverse Lunge', 'freq': '3 x 12'},
                {'name': 'Squat Jumps', 'freq': '3 x 12'},
                {'name': 'Ab Scissor', 'freq': '3 x 10'},
            ]
        },
        '3': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Pushups', 'freq': '3 x 8'},
                {'name': 'Tricep Bar Pushdown', 'freq': '3 x 10'},
                {'name': 'Plank', 'freq': '3 x 1 min'},
            ],
            'Wednesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Assisted Pullups', 'freq': '3 x 10'},
                {'name': 'Dumbbell Romanian Deadlift', 'freq': '3 x 10'},
                {'name': 'Mountain Climber', 'freq': '3 x 10'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Goblet Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Reverse Lunge', 'freq': '3 x 12'},
                {'name': 'Bicycle Crunches', 'freq': '3 x 15'},
            ]
        },
        '4': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Machine Leg Press', 'freq': '3 x 10'},
                {'name': 'Barbell Pelvic Thrust', 'freq': '3 x 8'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Ab Scissor', 'freq': '3 x 10'}
            ],
            'Wednesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Squat', 'freq': '3 x 10'},
                {'name': 'Kettlebell Swing', 'freq': '3 x 10'},
                {'name': 'Band Leg Abductions', 'freq': '3 x 10'},
                {'name': 'Mountain Climber', 'freq': '3 x 10'}
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Lunges', 'freq': '3 x 10'},
                {'name': 'Goblet Squat', 'freq': '3 x 10'},
                {'name': 'Glute Kickback', 'freq': '3 x 10'},
                {'name': 'Plank', 'freq': '3 x 1 min'}
            ]
        },
        '5': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Kettlebell Swing', 'freq': '3 x 10'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Tricep Bar Pushdown', 'freq': '3 x 10'},
            ],
            'Wednesday': [
                {'name': 'Treadmill HIIT', 'freq': '15 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Dumbbell Row', 'freq': '3 x 10'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Bicep Hammer Curls', 'freq': '3 x 10'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Lunge', 'freq': '3 x 10'},
                {'name': 'Russian Twists', 'freq': '3 x 12'},
            ]
        },
        '6': {
            'Monday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
                {'name': 'Oblique Twist', 'freq': '3 x 10'},                
                {'name': 'Kettlebell Situps to Press', 'freq': '3 x 8'},
            ],
            'Wednesday': [
                {'name': 'Elliptical Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Romanian Deadlift', 'freq': '3 x 12'},
                {'name': 'Assisted Pullup Machine', 'freq': '3 x 6'},
                {'name': 'Reverse Pec Deck', 'freq': '3 x 15'},
                {'name': 'Dumbbell Bicep Curl', 'freq': '3 x 10'},                
            ],
            'Friday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 8'},
                {'name': 'Barbell Pelvic Thrust', 'freq': '3 x 10'},
                {'name': 'Dumbbell Lunge', 'freq': '3 x 12'},
                {'name': 'Flutter Kicks', 'freq': '3 x 10'},                
            ]
        },
        '7': {
            'Monday': [
                {'name': 'Machine Chest Press', 'freq': '3 x 10'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Bench Tricep Dips', 'freq': '3 x 10'},
                {'name': 'Tricep Bar Pushdown', 'freq': '3 x 10'},
                {'name': 'Kettlebell Swing', 'freq': '3 x 10'},
            ],
            'Wednesday': [
                {'name': 'Rowing Machine', 'freq': '15 min'},
                {'name': 'Dumbbell Row', 'freq': '3 x 10'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bicep Curls', 'freq': '3 x 10'},
                {'name': 'Sit Ups', 'freq': '3 x 10'}, 
            ],
            'Friday': [
                {'name': 'Treadmill Low Intensity', 'freq': '15 min'},
                {'name': 'Stairs', 'freq': '3 x 30 sec'},
                {'name': 'Machine Leg Press', 'freq': '3 x 10'},
                {'name': 'Machine Leg Curl', 'freq': '3 x 10'},
                {'name': 'Flutter Kicks', 'freq': '3 x 10'},
            ]
        },
        '8': {
            'Monday': [],
            'Wednesday': [],
            'Friday': []
        },
        '9': {
            'Monday': [],
            'Wednesday': [],
            'Friday': []
        },
        '10': {
            'Monday': [],
            'Wednesday': [],
            'Friday': []
        }
    },

    'femalePrograms4': {
        '1': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Barbell Pelvic Thrust', 'freq': '3 x 8'},
                {'name': 'Plank', 'freq': '3 x 1 min'},
                {'name': 'Bench Tricep Dips', 'freq': '3 x 8'},
            ],
            'Tuesday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Machine Assisted Pullups', 'freq': '3 x 5'},
                {'name': 'Dumbbell Row', 'freq': '3 x 10'},
                {'name': 'Bar Cable Curl', 'freq': '3 x 12'},
                {'name': 'Mountain Climber', 'freq': '3 x 45 secs'},
            ],
            'Thursday': [
                {'name': 'Kettlebell Swing', 'freq': '3 x 8'},
                {'name': 'Kettlebell High Pull', 'freq': '3 x 10'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Outer Thigh Squeeze', 'freq': '3 x 10'},
                {'name': 'Bicycle Crunches', 'freq': '3 x 15'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 8'},
                {'name': 'Dumbbell Lunges', 'freq': '3 x 10'},
                {'name': 'Inner Thigh Squeeze', 'freq': '3 x 10'},
                {'name': 'Side Plank', 'freq': '3 x 1 min'},
            ]
        },
        '2': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Burpees', 'freq': '3 x 12'},
                {'name': 'Dumbbell Chest Press', 'freq': '3 x 12'},
                {'name': 'Glute Kickback', 'freq': '3 x 10'},
                {'name': 'Bench Tricep Dips', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Row', 'freq': '3 x 12'},
                {'name': 'Front Lateral Raise', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row', 'freq': '3 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 12'},
            ],
            'Thursday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Kettlebell Swing', 'freq': '3 x 12'},
                {'name': 'Dumbbell Lunge', 'freq': '3 x 12'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 12'},
                {'name': 'Cable Side Lateral Raise', 'freq': '3 x 12'},
            ],
            'Friday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Goblet Squat', 'freq': '3 x 15'},
                {'name': 'Dumbbell Reverse Lunge', 'freq': '3 x 12'},
                {'name': 'Squat Jumps', 'freq': '3 x 12'},
                {'name': 'Ab Scissor', 'freq': '3 x 10'},
            ]
        },
        '3': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Pushups', 'freq': '3 x 8'},
                {'name': 'Tricep Bar Pushdown', 'freq': '3 x 10'},
                {'name': 'Plank', 'freq': '3 x 1 min'},
            ],
            'Tuesday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Assisted Pullups', 'freq': '3 x 10'},
                {'name': 'Dumbbell Romanian Deadlift', 'freq': '3 x 10'},
                {'name': 'Mountain Climber', 'freq': '3 x 10'},
            ],
            'Thursday': [
                {'name': 'Elliptical', 'freq': '15 min'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Reverse Pec Deck', 'freq': '3 x 12'},
                {'name': 'Kettlebell Swing', 'freq': '3 x 12'},
                {'name': 'High Knees', 'freq': '3 x 50'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Goblet Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Reverse Lunge', 'freq': '3 x 12'},
                {'name': 'Bicycle Crunches', 'freq': '3 x 15'},
            ]
        },
        '4': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Machine Leg Press', 'freq': '3 x 10'},
                {'name': 'Barbell Pelvic Thrust', 'freq': '3 x 8'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Ab Scissor', 'freq': '3 x 10'}
            ],
            'Tuesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Squat', 'freq': '3 x 10'},
                {'name': 'Lying-Down Band Leg Abductions', 'freq': '3 x 10'},
                {'name': 'Sumo Squat', 'freq': '3 x 15'},
                {'name': 'Russian Twists', 'freq': '3 x 15'},
            ],
            'Thursday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Squat', 'freq': '3 x 10'},
                {'name': 'Kettlebell Swing', 'freq': '3 x 10'},
                {'name': 'Standing Band Leg Abductions', 'freq': '3 x 10'},
                {'name': 'Mountain Climber', 'freq': '3 x 10'}
            ],
            'Friday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Lunges', 'freq': '3 x 10'},
                {'name': 'Goblet Squat', 'freq': '3 x 10'},
                {'name': 'Glute Kickback', 'freq': '3 x 10'},
                {'name': 'Plank', 'freq': '3 x 1 min'}
            ]
        },
        '5': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Incline Dumbbell Chest Press', 'freq': '3 x 10'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Tricep Bar Pushdown', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Treadmill HIIT', 'freq': '15 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Dumbbell Row', 'freq': '3 x 10'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Bicep Hammer Curls', 'freq': '3 x 10'},
            ],
            'Thursday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},                
                {'name': 'Kettlebell Swing', 'freq': '3 x 10'},
                {'name': 'Cable Side Lateral Raise', 'freq': '3 x 10'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Front Plate Raise with Twist', 'freq': '3 x 8'},                                                
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Lunge', 'freq': '3 x 10'},
                {'name': 'Russian Twists', 'freq': '3 x 12'},
            ]
        },
        '6': {
            'Monday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Burpees', 'freq': '3 x 10'}, 
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
                {'name': 'Oblique Twist', 'freq': '3 x 10'},                            
            ],
            'Tuesday': [
                {'name': 'Rowing Machine', 'freq': '15 min'},
                {'name': 'Dumbbell Romanian Deadlift', 'freq': '3 x 12'},
                {'name': 'Assisted Pullup Machine', 'freq': '3 x 6'},
                {'name': 'Reverse Pec Deck', 'freq': '3 x 15'},
                {'name': 'Dumbbell Bicep Curl', 'freq': '3 x 10'},                 
            ],
            'Thursday': [
                {'name': 'Elliptical Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Outer Thigh Squeeze', 'freq': '3 x 8'},
                {'name': 'Kettlebell Situps to Press', 'freq': '3 x 8'},
                {'name': 'Machine Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Bicycle Crunches', 'freq': '3 x 10'},            
            ],
            'Friday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 8'},
                {'name': 'Barbell Pelvic Thrust', 'freq': '3 x 10'},
                {'name': 'Dumbbell Lunge', 'freq': '3 x 12'},
                {'name': 'Flutter Kicks', 'freq': '3 x 10'},                
            ]
        },
        '7': {
            'Monday': [
                {'name': 'Machine Chest Press', 'freq': '3 x 10'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Bench Tricep Dips', 'freq': '3 x 10'},
                {'name': 'Tricep Bar Pushdown', 'freq': '3 x 10'},
                {'name': 'Knee Pushups', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Rowing Machine', 'freq': '15 min'},
                {'name': 'Dumbbell Row', 'freq': '3 x 10'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bicep Curls', 'freq': '3 x 10'},
                {'name': 'Sit Ups', 'freq': '3 x 10'},
            ],
            'Thursday': [
                {'name': 'Exercise Bike Low Intensity', 'freq': '15 min'},
                {'name': 'Kettlebell Raise', 'freq': '3 x 10'},
                {'name': 'Machine Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Cable Side Lateral Raise', 'freq': '3 x 10'},
                {'name': 'Mountain Climbers', 'freq': '3 x 8'},
            ],
            'Friday': [
                {'name': 'Treadmill Low Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press', 'freq': '3 x 10'},
                {'name': 'Machine Leg Curl', 'freq': '3 x 10'},
                {'name': 'Flutter Kicks', 'freq': '3 x 10'},
            ]
        },
        '8': {
            'Monday': [],
            'Tuesday': [],
            'Thursday': [],
            'Friday': []
        },
        '9': {
            'Monday': [],
            'Tuesday': [],
            'Thursday': [],
            'Friday': []
        },
        '10': {
            'Monday': [],
            'Tuesday': [],
            'Thursday': [],
            'Friday': []
        }
    },

    'femalePrograms5': {
        '1': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Barbell Pelvic Thrust', 'freq': '3 x 8'},
                {'name': 'Kettlebell Swing', 'freq': '3 x 8'},
                {'name': 'Plank', 'freq': '3 x 1 min'},
            ],
            'Tuesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Machine Assisted Pullups', 'freq': '3 x 5'},
                {'name': 'Dumbbell Row', 'freq': '3 x 10'},
                {'name': 'Bar Cable Curl', 'freq': '3 x 12'},
                {'name': 'Mountain Climber', 'freq': '3 x 45 secs'},
            ],
            'Wednesday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Cable Incline Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Barbell Pelvic Thrust', 'freq': '3 x 8'},
                {'name': 'Kettlebell Raise', 'freq': '3 x 8'},
                {'name': 'Lying Leg Raises', 'freq': '3 x 15'},
            ],
            'Thursday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Kettlebell Row', 'freq': '3 x 10'},
                {'name': 'Unilateral Cable Curl', 'freq': '3 x 12'},
                {'name': 'Mountain Climber', 'freq': '3 x 45 secs'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 8'},
                {'name': 'Dumbbell Lunges', 'freq': '3 x 10'},
                {'name': 'Inner Thigh Squeeze', 'freq': '3 x 10'},
                {'name': 'Side Plank', 'freq': '3 x 1 min'},
            ]
        },
        '2': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Burpees', 'freq': '3 x 12'},
                {'name': 'Dumbbell Chest Press', 'freq': '3 x 12'},
                {'name': 'Glute Kickback', 'freq': '3 x 10'},
                {'name': 'Bench Tricep Dips', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Row', 'freq': '3 x 12'},
                {'name': 'Front Lateral Raise', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row', 'freq': '3 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 12'},
            ],
            'Wednesday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Overhead Barbell Raise', 'freq': '3 x 12'},
                {'name': 'Dumbbell Chest Press', 'freq': '3 x 12'},
                {'name': 'Band Leg Abductions', 'freq': '3 x 10'},
                {'name': 'Bench Tricep Dips', 'freq': '3 x 10'},
            ],
            'Thursday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Row', 'freq': '3 x 12'},
                {'name': 'Cable Side Lateral Raise', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row', 'freq': '3 x 15'},
                {'name': 'Dumbbell Bicep Curl', 'freq': '3 x 12'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Goblet Squat', 'freq': '3 x 15'},
                {'name': 'Dumbell Reverse Lunge', 'freq': '3 x 12'},
                {'name': 'Squat Jumps', 'freq': '3 x 12'},
                {'name': 'Ab Scissor', 'freq': '3 x 10'},
            ]
        },
        '3': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Pushups', 'freq': '3 x 8'},
                {'name': 'Tricep Bar Pushdown', 'freq': '3 x 10'},
                {'name': 'Plank', 'freq': '3 x 1 min'},
            ],
            'Tuesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Assisted Pullups', 'freq': '3 x 10'},
                {'name': 'Dumbbell Romanian Deadlift', 'freq': '3 x 10'},
                {'name': 'Mountain Climber', 'freq': '3 x 10'},
            ],
            'Wednesday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 8'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'High Knees', 'freq': '3 x 50'},
            ],
            'Thursday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Squat', 'freq': '3 x 10'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Dumbbell Romanian Deadlift', 'freq': '3 x 10'},
                {'name': 'Shoulder Taps', 'freq': '3 x 10'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Goblet Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Reverse Lunge', 'freq': '3 x 12'},
                {'name': 'Bicycle Crunches', 'freq': '3 x 15'},
            ]
        },
        '4': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Machine Leg Press', 'freq': '3 x 10'},
                {'name': 'Barbell Pelvic Thrust', 'freq': '3 x 8'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Ab Scissor', 'freq': '3 x 10'}
            ],
            'Tuesday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Squat', 'freq': '3 x 10'},
                {'name': 'Lying Band Leg Abductions', 'freq': '3 x 10'},
                {'name': 'Sumo Squat', 'freq': '3 x 15'},
                {'name': 'Russian Twists', 'freq': '3 x 15'},
            ],
            'Wednesday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Lunges', 'freq': '3 x 10'},
                {'name': 'Goblet Squat', 'freq': '3 x 10'},
                {'name': 'Glute Kickback', 'freq': '3 x 10'},
                {'name': 'Plank', 'freq': '3 x 1 min'}
            ],
            'Thursday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Squat', 'freq': '3 x 10'},
                {'name': 'Kettlebell Swing', 'freq': '3 x 10'},
                {'name': 'Standing Band Leg Abductions', 'freq': '3 x 10'},
                {'name': 'Mountain Climber', 'freq': '3 x 10'}
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Frog Kicks', 'freq': '3 x 15'},
                {'name': 'Outer Thigh Squeeze', 'freq': '3 x 10'},
                {'name': 'Inner Thigh Squeeze', 'freq': '3 x 10'},
                {'name': 'Side Plank', 'freq': '3 x 1 min'}
            ]
        },
        '5': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Incline Dumbbell Chest Press', 'freq': '3 x 10'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Tricep Bar Pushdown', 'freq': '3 x 10'},                
            ],
            'Tuesday': [
                {'name': 'Treadmill HIIT', 'freq': '15 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Dumbbell Row', 'freq': '3 x 10'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Bicep Hammer Curls', 'freq': '3 x 10'},
            ],
            'Wednesday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Kettlebell Swing', 'freq': '3 x 10'},
                {'name': 'Dumbbell Shoulder Press', 'freq': '3 x 10'},               
                {'name': 'Cable Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},                
            ],
            'Thursday': [
                {'name': 'Treadmill HIIT', 'freq': '15 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Dumbbell Row', 'freq': '3 x 10'},
                {'name': 'Wide Grip Cable Row', 'freq': '3 x 10'},
                {'name': 'Unilateral Cable Curls', 'freq': '3 x 10'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press', 'freq': '3 x 10'},
                {'name': 'Dumbbell Lunge', 'freq': '3 x 10'},
                {'name': 'Russian Twists', 'freq': '3 x 12'},
            ]
        },
        '6': {
            'Monday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Machine Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},
                {'name': 'Oblique Twist', 'freq': '3 x 10'},                
                {'name': 'Kettlebell Situps to Press', 'freq': '3 x 8'},                
            ],
            'Tuesday': [
                {'name': 'Rowing Machine', 'freq': '15 min'},
                {'name': 'Dumbbell Romanian Deadlift', 'freq': '3 x 12'},
                {'name': 'Assisted Pullup Machine', 'freq': '3 x 6'},
                {'name': 'Reverse Pec Deck', 'freq': '3 x 15'},
                {'name': 'Dumbbell Bicep Curl', 'freq': '3 x 10'},                
            ],
            'Wednesday': [
                {'name': 'Elliptical Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Burpees', 'freq': '3 x 10'}, 
                {'name': 'Tricep Bar Pushdown', 'freq': '3 x 10'},
                {'name': 'Oblique Twist', 'freq': '3 x 10'},                
            ],
            'Thursday': [
                {'name': 'Rowing Machine', 'freq': '15 min'},
                {'name': 'Kettlebell Romanian Deadlift', 'freq': '3 x 12'},
                {'name': 'Assisted Pullup Machine', 'freq': '3 x 6'},
                {'name': 'Reverse Pec Deck', 'freq': '3 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 10'},                
            ],
            'Friday': [
                {'name': 'Exercise Bike Medium Intensity', 'freq': '15 min'},
                {'name': 'Barbell Squat', 'freq': '3 x 8'},
                {'name': 'Barbell Pelvic Thrust', 'freq': '3 x 10'},
                {'name': 'Dumbbell Lunge', 'freq': '3 x 12'},
                {'name': 'Flutter Kicks', 'freq': '3 x 10'},                
            ]
        },
        '7': {
            'Monday': [
                {'name': 'Machine Chest Press', 'freq': '3 x 10'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Bench Tricep Dips', 'freq': '3 x 10'},
                {'name': 'Tricep Bar Pushdown', 'freq': '3 x 10'},
                {'name': 'Kettlebell Swing', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Rowing Machine', 'freq': '15 min'},
                {'name': 'Dumbbell Row', 'freq': '3 x 10'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Dumbbell Bicep Curls', 'freq': '3 x 10'},
                {'name': 'Sit Ups', 'freq': '3 x 10'},
            ],
            'Wednesday': [
                {'name': 'Dumbbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 10'},
                {'name': 'Unilateral Tricep Pushdown', 'freq': '3 x 10'},
                {'name': 'Cable Side Lateral Raise', 'freq': '3 x 10'},
                {'name': 'Machine Shoulder Press', 'freq': '3 x 10'},
            ],
            'Thursday': [
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 10'},
                {'name': 'Unilateral Cable Curls', 'freq': '3 x 10'},
                {'name': 'Machine Assisted Pullups', 'freq': '3 x 8'},
                {'name': 'Russian Twist', 'freq': '3 x 8'},                
            ],
            'Friday': [
                {'name': 'Treadmill Low Intensity', 'freq': '15 min'},
                {'name': 'Dumbbell Squat', 'freq': '3 x 10'},
                {'name': 'Machine Leg Press', 'freq': '3 x 10'},
                {'name': 'Machine Leg Curl', 'freq': '3 x 10'},
                {'name': 'Flutter Kicks', 'freq': '3 x 10'},                
            ]
        },
        '8': {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []
        },
        '9': {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []
        },
        '10': {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []
        }
    }
}
