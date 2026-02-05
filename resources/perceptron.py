from resources.printout import printout
import math

def perceptron_predict(weights, inputs):
    # Step 1: Calculate Weighted Sum
    weighted_sum = sum(w * x for w, x in zip(weights, inputs))

    # Step 2: Activation Function
    sigmoid = 1 / (1 + math.exp(-weighted_sum))

    # Step 3: Return Prediction
    return sigmoid

def perceptron_calculate_adjustments(prediction, weights, target, learning_rate):
    # Step 1: Get Error from target and prediction
    error = prediction - target

    # Step 2: Get derivative of activation function
    sig_deriv = prediction * (1 - prediction)

    # Step 3: Calculate adjustment for each weight
    adj = error * sig_deriv * learning_rate
    adjustments = [adj * x for x in weights]

    # Step 4: Return adjustments
    return adjustments

def train(weights_old, inputs, target, learning_rate, passes):

    flag_watching = (input("Do you want to watch? (y/n): ") == 'y')

    # Repeat {passes} times
    for _ in range(passes):
        prediction = perceptron_predict(weights_old, inputs)
        adjustments = perceptron_calculate_adjustments(prediction, weights_old, target, learning_rate)

        # Calculate new weights (separate variable for printout purposes)
        weights_new = []
        for i in range(len(weights_old)):
            weights_new.append(weights_old[i] + adjustments[i])

        if flag_watching:
            printout(inputs, weights_new, prediction)
            print(f"Target: {target}, Predicted: {prediction:.3f}\n")
            input("Press anything to continue...\n")

    return None

def test():
    # Skeleton function
    return None