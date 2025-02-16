def temp_sensor(temperature):
    if not temperature:
        return"No input provided."

    for temp in temperature:
        if not isinstance(temp, (int, float)):
            return  "Invalid input detected."
        if temp < -50 or temp > 150:
            return "Out-of-bound value detected."

    min_temp = min(temperature)
    max_temp = max(temperature)
    avg_temp = sum(temperature) / len(temperature)

    return {
        "Min": f"{min_temp}°C", # "°C" degree symbol taken from google
        "Max": f"{max_temp}°C",
        "Avg": f"{avg_temp:.2f}°C",
    }
