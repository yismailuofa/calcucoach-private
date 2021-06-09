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
                {'name': 'Dumbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Arnold Dumbell Press', 'freq': '3 x 12'},
                {'name': 'Cable Lateral Raise', 'freq': '3 x 12'},
                {'name': 'Tricep Dips', 'freq': '3 x 8'},
            ],
            'Wednesday': [
                {'name': 'Wide Grip Pullup', 'freq': '3 x 8'},
                {'name': 'Seated Cable Row', 'freq': '3 x 12'},
                {'name': 'Face Pull', 'freq': '3 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 12'},
                {'name': 'Dumbell Hammer Curl', 'freq': '3 x 12'},                
            ],
            'Friday': [
                {'name': 'Barbell Squat', 'freq': '3 x 12'},
                {'name': 'Machine Leg Press', 'freq': '3 x 12'}, 
                {'name': 'Exercise Bike', 'freq': '15 min'},
                {'name': 'Abdominal Crunch', 'freq': '3 x 10'},
                {'name': 'Hanging Leg Raise', 'freq': '3 x 10'},                              
            ]
        },
        '2': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Burpees', 'freq': '3 x 10'},
                {'name': 'Dumbell Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Dumbell Side Lateral Raise', 'freq': '3 x 15'},
                {'name': 'Dumbell Overhead Tricep Extension', 'freq': '3 x 15'},
            ],
            'Wednesday': [
                {'name': 'Exercise Bike', 'freq': '15 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Dumbell Bicep Curl', 'freq': '3 x 15'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Stair Climber', 'freq': '3 x 45 secs'},
                {'name': 'Dumbell Lunges', 'freq': '3 x 10'},
                {'name': 'Bicycle Crunches', 'freq': '3 x 15'},
                {'name': 'Russian Twists', 'freq': '3 x 15'},
            ]            
        },
        '3': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Overhead Tricep Extension', 'freq': '3 x 10'},                
            ],
            'Wednesday': [
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Reverse Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'T-Bar Row', 'freq': '3 x 10'},  
                {'name': 'Dumbell Bicep Curl', 'freq': '3 x 10'},
                {'name': 'Dumbell Concentration Curl', 'freq': '3 x 10'},  
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
                {'name': 'Dumbell Bench Press Pyramid Sets', 'freq': '5 x 8'},
                {'name': 'Dumbell Incline Bench Press', 'freq': '5 x 5'},
                {'name': 'Arnold Dumbell Press', 'freq': '3 x 12'},
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
                {'name': 'Dumbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Front Lateral Raise', 'freq': '3 x 10'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},                 
                {'name': 'Dumbell Overhead Tricep Extension', 'freq': '3 x 10'},
            ],
            'Wednesday': [
                {'name': 'Bent Over Dumbell Row', 'freq': '3 x 12'},
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
            'Monday': [],
            'Wednesday': [],
            'Friday': []            
        },
        '7': {
            'Monday': [],
            'Wednesday': [],
            'Friday': []            
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

    'malePrograms4': {
        '1': {
            'Monday': [
                {'name': 'Dumbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Incline Dumbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Barbell Skullcrushers', 'freq': '3 x 12'},
                {'name': 'Tricep Dips', 'freq': '3 x 8'},                
            ],
            'Tuesday': [
                {'name': 'Wide Grip Pullup', 'freq': '3 x 8'},
                {'name': 'Seated Cable Row', 'freq': '3 x 12'},
                {'name': 'Face Pull', 'freq': '3 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 12'},
                {'name': 'Dumbell Hammer Curl', 'freq': '3 x 12'},  
            ],
            'Thursday': [
                {'name': 'Arnold Dumbell Press', 'freq': '3 x 12'},
                {'name': 'Cable Lateral Raise', 'freq': '3 x 12'},
                {'name': 'Reverse Pec Deck', 'freq': '3 x 12'},
                {'name': 'Dumbell Shrugs', 'freq': '3 x 12'},
                {'name': 'Farmers Walk', 'freq': '50 Steps'},
            ],
            'Friday': [
                {'name': 'Barbell Squat', 'freq': '3 x 12'},
                {'name': 'Machine Leg Press', 'freq': '3 x 12'}, 
                {'name': 'Exercise Bike', 'freq': '15 min'},
                {'name': 'Abdominal Crunch', 'freq': '3 x 10'},
                {'name': 'Hanging Leg Raise', 'freq': '3 x 10'},   
            ]              
        },
        '2': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Burpees', 'freq': '3 x 10'},
                {'name': 'Incline Cable Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Dumbell Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Dumbell Overhead Tricep Extension', 'freq': '3 x 15'},
            ],
            'Tuesday': [
                {'name': 'Exercise Bike', 'freq': '15 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Dumbell Bicep Curl', 'freq': '3 x 15'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},                
            ],
            'Thursday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Dumbell Shoulder Flyes', 'freq': '3 x 15'},
                {'name': 'Arnold Dumbell Press', 'freq': '3 x 15'},
                {'name': 'Dumbell Front Lateral Raise', 'freq': '3 x 15'},
                {'name': 'Front Plate Raise with Twist', 'freq': '3 x 15'},
            ],
            'Friday': [
                {'name': 'Exercise Bike', 'freq': '15 min'},
                {'name': 'Stair Climber', 'freq': '3 x 45 secs'},
                {'name': 'Dumbell Lunges', 'freq': '3 x 10'},
                {'name': 'Bicycle Crunches', 'freq': '3 x 15'},
                {'name': 'Russian Twists', 'freq': '3 x 15'},
            ]               
        },
        '3': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Overhead Tricep Extension', 'freq': '3 x 10'},  
                {'name': 'Tricep Dips', 'freq': '3 x 8'},              
            ],
            'Tuesday': [
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Reverse Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'T-Bar Row', 'freq': '3 x 10'},  
                {'name': 'Dumbell Bicep Curl', 'freq': '3 x 10'},
                {'name': 'Dumbell Concentration Curl', 'freq': '3 x 10'},  
            ],
            'Thursday': [
                {'name': 'Dumbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Barbell Shrugs', 'freq': '3 x 10'},
                {'name': 'Dumbell Side Lateral Raise', 'freq': '3 x 10'},
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
                {'name': 'Dumbell Bench Press Pyramid Sets', 'freq': '5 x 8'},
                {'name': 'Dumbell Incline Bench Press', 'freq': '5 x 5'},
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
                {'name': 'Arnold Dumbell Press Pyramid Sets', 'freq': '5 x 8'},
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
                {'name': 'Dumbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},                 
                {'name': 'Dumbell Overhead Tricep Extension', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Bent Over Dumbell Row', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},    
                {'name': 'Barbell Deadlift', 'freq': '3 x 8'},
                {'name': 'Face Pull', 'freq': '3 x 12'},                                                
                {'name': 'Unilateral Cable Curl', 'freq': '3 x 12'},
            ],
            'Thursday': [
                {'name': 'Dumbell Side Lateral Raise', 'freq': '3 x 10'},
                {'name': 'Miltary Overhead Press', 'freq': '3 x 10'},
                {'name': 'Barbell Shrugs', 'freq': '3 x 15'},
                {'name': 'Front Plate Raise with Twist', 'freq': '3 x 10'},
                {'name': 'Sport Drill of Choice', 'freq': '15 min'},
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
            'Monday': [],
            'Tuesday': [],
            'Thursday': [],
            'Friday': []               
        },
        '7': {
            'Monday': [],
            'Tuesday': [],
            'Thursday': [],
            'Friday': []               
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

    'malePrograms5': {
        '1': {
            'Monday': [
                {'name': 'Dumbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Cable Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Arnold Dumbell Press', 'freq': '3 x 12'},
                {'name': 'Cable Lateral Raise', 'freq': '3 x 12'},
                {'name': 'Tricep Dips', 'freq': '3 x 8'},                
            ],
            'Tuesday': [
                {'name': 'Wide Grip Pullup', 'freq': '3 x 8'},
                {'name': 'Seated Cable Row', 'freq': '3 x 12'},
                {'name': 'Face Pull', 'freq': '3 x 15'},
                {'name': 'Barbell Bicep Curl', 'freq': '3 x 12'},
                {'name': 'Dumbell Hammer Curl', 'freq': '3 x 12'},                    
            ],
            'Wednesday': [
                {'name': 'Incline Dumbell Bench Press', 'freq': '3 x 12'},
                {'name': 'Dumbell Chest Flyes', 'freq': '3 x 12'},
                {'name': 'Dumbell Shoulder Press', 'freq': '3 x 12'},
                {'name': 'Dumbell Side Lateral Raise', 'freq': '3 x 12'},
                {'name': 'Tricep Pushdown', 'freq': '3 x 12'},                      
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
                {'name': 'Exercise Bike', 'freq': '15 min'},
                {'name': 'Abdominal Crunch', 'freq': '3 x 10'},
                {'name': 'Hanging Leg Raise', 'freq': '3 x 10'},                      
            ]              
        },
        '2': {
            'Monday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Burpees', 'freq': '3 x 10'},
                {'name': 'Dumbell Chest Flyes', 'freq': '3 x 15'},
                {'name': 'Dumbell Side Lateral Raise', 'freq': '3 x 15'},
                {'name': 'Dumbell Overhead Tricep Extension', 'freq': '3 x 15'},
            ],
            'Tuesday': [
                {'name': 'Exercise Bike', 'freq': '15 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Dumbell Bicep Curl', 'freq': '3 x 15'},
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
                {'name': 'Exercise Bike', 'freq': '15 min'},
                {'name': 'Rowing Machine', 'freq': '3 x 3 min'},
                {'name': 'Close Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'Unilateral Cable Curl', 'freq': '3 x 15'},
                {'name': 'Battle Ropes', 'freq': '3 x 1 min'},
            ],
            'Friday': [
                {'name': 'Treadmill Medium Intensity', 'freq': '15 min'},
                {'name': 'Stair Climber', 'freq': '3 x 45 secs'},
                {'name': 'Dumbell Lunges', 'freq': '3 x 10'},
                {'name': 'Bicycle Crunches', 'freq': '3 x 15'},
                {'name': 'Russian Twists', 'freq': '3 x 15'},
            ]               
        },
        '3': {
            'Monday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Overhead Tricep Extension', 'freq': '3 x 10'},                
            ],
            'Tuesday': [
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Reverse Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'T-Bar Row', 'freq': '3 x 10'},  
                {'name': 'Dumbell Bicep Curl', 'freq': '3 x 10'},
                {'name': 'Dumbell Concentration Curl', 'freq': '3 x 10'},  
            ],
            'Wednesday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Barbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Machine Shoulder Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Overhead Tricep Extension', 'freq': '3 x 10'},                
            ],
            'Thursday': [
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},
                {'name': 'Close Grip Lat Pulldown', 'freq': '3 x 10'},
                {'name': 'T-Bar Row', 'freq': '3 x 10'},  
                {'name': 'Dumbell Bicep Curl', 'freq': '3 x 10'},
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
                {'name': 'Dumbell Bench Press Pyramid Sets', 'freq': '5 x 8'},
                {'name': 'Dumbell Incline Bench Press', 'freq': '5 x 5'},
                {'name': 'Arnold Dumbell Press', 'freq': '3 x 12'},
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
                {'name': 'Dumbell Incline Bench Press', 'freq': '5 x 5'},
                {'name': 'Arnold Dumbell Press', 'freq': '3 x 12'},
                {'name': 'Dumbell Overhead Tricep Extension', 'freq': '3 x 8'},
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
                {'name': 'Dumbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Front Lateral Raise', 'freq': '3 x 10'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},                 
                {'name': 'Dumbell Overhead Tricep Extension', 'freq': '3 x 10'},
            ],
            'Tuesday': [
                {'name': 'Bent Over Dumbell Row', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row', 'freq': '3 x 10'},    
                {'name': 'Barbell Deadlift', 'freq': '3 x 8'},
                {'name': 'Face Pull', 'freq': '3 x 12'},                                                
                {'name': 'Unilateral Cable Curl', 'freq': '3 x 12'},
            ],
            'Wednesday': [
                {'name': 'Barbell Bench Press', 'freq': '3 x 10'},
                {'name': 'Dumbell Incline Bench Press', 'freq': '3 x 10'},
                {'name': 'Miltary Overhead Press', 'freq': '3 x 10'},
                {'name': 'Tricep Rope Pushdown', 'freq': '3 x 10'},                 
                {'name': 'Sport Drill of Choice', 'freq': '15 min'},
            ],
            'Thursday': [
                {'name': 'Bent Over Dumbell Row', 'freq': '3 x 12'},
                {'name': 'Seated Cable Row Wide Grip', 'freq': '3 x 10'},    
                {'name': 'Dumbell Deadlift', 'freq': '3 x 10'},
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
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []               
        },
        '7': {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []               
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
    },

    'femalePrograms3': {
        '1': {
            'Monday': [],
            'Wednesday': [],
            'Friday': []
        },
        '2': {
            'Monday': [],
            'Wednesday': [],
            'Friday': []            
        },
        '3': {
            'Monday': [],
            'Wednesday': [],
            'Friday': []            
        },
        '4': {
            'Monday': [],
            'Wednesday': [],
            'Friday': []            
        },
        '5': {
            'Monday': [],
            'Wednesday': [],
            'Friday': []            
        },    
        '6': {
            'Monday': [],
            'Wednesday': [],
            'Friday': []            
        },
        '7': {
            'Monday': [],
            'Wednesday': [],
            'Friday': []            
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
            'Monday': [],
            'Tuesday': [],
            'Thursday': [],
            'Friday': []              
        },
        '2': {
            'Monday': [],
            'Tuesday': [],
            'Thursday': [],
            'Friday': []               
        },
        '3': {
            'Monday': [],
            'Tuesday': [],
            'Thursday': [],
            'Friday': []               
        },
        '4': {
            'Monday': [],
            'Tuesday': [],
            'Thursday': [],
            'Friday': []               
        },
        '5': {
            'Monday': [],
            'Tuesday': [],
            'Thursday': [],
            'Friday': []               
        },    
        '6': {
            'Monday': [],
            'Tuesday': [],
            'Thursday': [],
            'Friday': []               
        },
        '7': {
            'Monday': [],
            'Tuesday': [],
            'Thursday': [],
            'Friday': []               
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
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []              
        },
        '2': {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []               
        },
        '3': {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []               
        },
        '4': {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []               
        },
        '5': {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []               
        },    
        '6': {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []               
        },
        '7': {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []               
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
