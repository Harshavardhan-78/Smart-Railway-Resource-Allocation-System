def coach_recommendation(predicted_demand,capacity):

    if predicted_demand > capacity:

        shortage = predicted_demand - capacity

        coaches_needed = int(shortage/50)+1

        return f"Add {coaches_needed} extra coaches"

    return "Capacity sufficient"


def train_frequency_recommendation(predicted_demand,capacity):

    if predicted_demand > capacity*1.3:

        return "Consider adding special train"

    return "No additional train required"


def platform_optimization(df):

    conflicts = df.groupby(["Date","Platform"]).size()

    conflicts = conflicts[conflicts > 1]

    return conflicts