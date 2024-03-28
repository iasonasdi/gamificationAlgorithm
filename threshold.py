import math

def calculate_points(user_order, max_points, min_points,total_users):
    # Calculate the rate of decay such that we reach min_points at a specific user_order
    # We choose an arbitrary user_order (e.g., 10) at which we want to reach close to min_points
    target_user_order = int(total_users*60/100)
    decay_rate = -math.log(min_points / max_points) / target_user_order
    # Calculate the points for the current user_order using the exponential decay formula
    points = max_points * math.exp(-decay_rate * (user_order - 1))
    # Ensure that points do not fall below min_points
    return max(min_points, points)

def find_threshold_user(max_points, min_points,total_users):
    user_order = 1
    while True:
        points = calculate_points(user_order, max_points, min_points,total_users)
        print(f"User {user_order} has {points} points")
        if points <= min_points:
            return user_order
        user_order += 1

# Define constants
max_points = 100
min_points = 50
total_users = 1000

# Find the user at which the threshold is reached
threshold_user = find_threshold_user(max_points, min_points,total_users)
print("The threshold of {} points is reached at user {}".format(min_points, threshold_user))