def calculate_premium(age, policy):
    # Example premium calculation based on age band
    if age < 25:
        return policy.premium * 1.5  # 50% surcharge for high-risk band
    elif 25 <= age < 40:
        return policy.premium  # Base premium for medium-risk band
    else:
        return policy.premium * 0.8  # 20% discount for low-risk band
