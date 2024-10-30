import random

# Name :- Mohit Gujarati
# Student id :-100862494
# Github link:https://github.com/MohitGujarati/python-assignments/tree/assignment-version-2

# Function to roll the dice n times and count occurrences of target face
def roll_dice(target_faces, n):
    rolls = [random.randint(1, 6) for _ in range(n)]  # simulate dice rolls
    face_count = {face: rolls.count(face) for face in target_faces}  # Count target face occurrences
    return face_count

# Function to calculate the probability of observing the target face
def cal_probability(face_count, n):
    probabilities = {face: count / n for face, count in face_count.items()}
    return probabilities

# Function to simulate dice rolls and print result for different sample sizes
def number_dice_roles(target_faces):
    sample_size = [10, 100, 10000]
    
    # Print table header space may not be more than 8,10,10 characters
    print(f"{'n':<8} | {'x = 1':<10} | {'x = 3':<10} | {'x = 6':<10}")
    print("-" * 42)
    
    # Loop over each sample size and calculate probabilities
    for n in sample_size:
        face_count = roll_dice(target_faces, n)
        probabilities = cal_probability(face_count, n)
        
        # Print each row in the table with formatted probabilities
        print(f"{n:<8} | {probabilities.get(1, 0) * 100:<10.2f} | {probabilities.get(3, 0) * 100:<10.2f} | {probabilities.get(6, 0) * 100:<10.2f}")
        
        # Print horizontal line after each row, except the last one
        if n != sample_size[-1]:
            print("-" * 42)#printing - 42 times
        
# Define target faces
target_faces = [1, 3, 6]

# Simulate dice rolls and output results
number_dice_roles(target_faces)
