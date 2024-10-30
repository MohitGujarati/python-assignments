import random

# Name :- Mohit Gujarati
# Student id :-100862494

# Function to roll the dice n times  and cout occurrences of target face
def roll_dice(target_faces,n):
    rolls=[random.randint(1,6) for _ in range(n)]#simulation dice rolls
    face_count={face:rolls.count(face) for face in target_faces} #Count target face occurrences
    return face_count

# Function to calculate the probability of observing the target face
def cal_probability(face_count,n):
    probabilities = {face: count / n for face, count in face_count.items()}
    return probabilities

# Function to simulate dice rolls and print result for different sample size
def number_dice_roles(target_face):
    sample_size=[10,100,1000]
    
    # Loop over each samole size and calculate probabilities
    for n in sample_size:
        face_count=roll_dice(target_face,n)
        probabilities=cal_probability(face_count,n)
        
        
        print(f"Results for {n} dice rolls:")
        for face, prob in probabilities.items():
            print(f"Face {face}: {prob * 100:.2f}%")
        print()
        
# Define target faces
target_faces=[1,3,6]

# Simulate dice rolls and output results
number_dice_roles(target_faces)
        