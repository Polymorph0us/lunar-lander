def distance_reward(previous_distance, current_distance, scale=5.0):
	"""Reward positive movement toward center and penalize drifting away."""
	distance_change = previous_distance - current_distance
	return distance_change * scale
