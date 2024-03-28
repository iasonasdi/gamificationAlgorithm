class GameAlgorithm:
    def calculate_score(self, n_star, n, t_star, t, h, h_t, R, difficulty):
        # Define difficulty level points
        difficulty_points = {'E': 5, 'M': 10, 'H': 15, 'X': 25}
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

        # Calculate final score for the action
        S = F * P

        return S

    @staticmethod
    def run_example():
        # Example usage
        n_star = 28  # Optimal steps
        n = 84  # Actual steps taken by the user
        t_star = 65  # Optimal time
        t = 130  # Actual time taken by the user
        h = 1  # Hints used
        h_t = 5  # Total hints available
        R = 1  # Action success (1 for success, 0 for failure)
        difficulty = 'E'  # Difficulty level

        # Calculate the score for an action
        game = GameAlgorithm()
        score = game.calculate_score(n_star, n, t_star, t, h, h_t, R, difficulty)
        print(f"Score for the action: {score}")


# Main
GameAlgorithm.run_example()
