import math

total_users = 1000

# Function to calculate the decreasing factor based on user order
#No less decay than 0.5 of initial value
def calculate_decreasing_factor(user_order, base_decrease=0.95, min_factor=0.5):
    # Calculate the exponential decay factor
    target_user_order = int(total_users*60/100)
    decay_rate = -math.log(min_factor) / target_user_order  # Assuming we want to reach min_factor at user order 60% of total
    factor = max(min_factor, base_decrease * math.exp(-decay_rate * (user_order - 1)))
    return factor

# Modified scoring function to include decreasing factor logic
def calculate_score(n_star, n, t_star, t, h, h_t, R, P, difficulty, user_order):
    # Define difficulty level points
    difficulty_points = {'E': 50, 'M': 100, 'H': 150, 'X': 250}
    P = difficulty_points[difficulty]

    # Calculate N, T, H as per equations
    N = min(n_star / n, 1)
    T = min(t_star / t, 1)
    H = 1 - h / h_t

    # Weights (example values, adjust as needed)
    w_s, w_t, w_h = 0.05, 0.05, 0.05  # Weights for steps, time, hints
    w_p = 0.5  # Penalty weight
    w_a = 1 / 5  # Action weight (example, adjust based on actual logic)

    # Calculate cumulative factor f
    f = 1 - (1 - N) * w_s - (1 - T) * w_t - (1 - H) * w_h

    # Calculate F based on action success
    F = R * f + (1 - R) * w_a * w_p

    # Calculate final score for the action before applying decreasing factor
    S = F * P

    # Apply the decreasing factor based on user order
    decreasing_factor = calculate_decreasing_factor(user_order)
    final_score = S * decreasing_factor

    return final_score

# Example usage
#Calculate score for 10 users
for i in range(1,1000):
    user_order = i  # Order in which the user completes the action
    score = calculate_score(n_star=28, n=34, t_star=65, t=80, h=1, h_t=3, R=1, P=100, difficulty='E', user_order=user_order)
    print(f"Score of user {user_order} for the action: {score}")

