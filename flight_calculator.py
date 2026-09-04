def calculate_flight_time(weight_grams):
    # Copilot suggested docstring below; accepted as is
    """
    Returns the active flight time in minutes for a given payload weight.

    Flight time cannot be negative. If the formula would produce a negative result, the function should return 0.
    """
    if weight_grams < 0:
        raise ValueError("Payload weight cannot be negative.")
    
    # Apply the formula: T(w) = 180 - 0.1w
    flight_time = 180 - (0.1 * weight_grams)

    # Return 0 if the formula would produce a negative result
    return max(flight_time, 0)

def flight_time_table(max_weight_grams, step_grams):
    """
    Returns a list of (weight, flight_time) pairs for payload weights from 0 up to and including max_weight_grams, in increments of step_grams.
    """
    # Copilot suggested code below; edited to include incrementation
    if max_weight_grams < 0:
        raise ValueError("Max weight must be non-negative.")
    if step_grams <= 0:
        raise ValueError("Step increment must be greater than zero.")
    
    flight_times = []
    # for loop from 0 up to and including max_weight_grams
    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        flight_times.append((weight, flight_time))
        weight += step_grams
    
    return flight_times