from resources.printout import printout_testing, printout_training
import math

def perceptron_predict(weights, inputs, flags):
    # Step 1: Calculate Weighted Sum
    weighted_sum = sum(w * x for w, x in zip(weights, inputs))

    if flags.flag_detailed:
        print(f"weighted sum: {weighted_sum:.3f}")
        input("...")

    # Step 2: Activation Function
    # Prevent overflow of sigmoid function

    sigmoid = 1 / (1 + math.exp(-weighted_sum/170))

    if flags.flag_detailed:
        print(f"sig: {sigmoid:.3f}")
        input("...")

    # Step 3: Return Prediction
    return sigmoid

def perceptron_calculate_adjustments(prediction, weights, target, learning_rate, flags):
    # Step 1: Get Error from target and prediction
    error = prediction - (target/10)

    if flags.flag_detailed:
        print(f"error: {error:.3f}")
        input("...")

    # Step 2: Get derivative of activation function
    sig_deriv = prediction * (1 - prediction)

    if flags.flag_detailed:
        print(f"deriv: {sig_deriv:.3f}")
        input("...")

    # Step 3: Calculate adjustment for each weight
    adj = error * sig_deriv * learning_rate

    if flags.flag_detailed:
        print(f"adj: {adj:.3f}")
        input("...")

    adjustments = [adj]*len(weights)

    # Step 4: Return adjustments
    return adjustments

def train(weights_old, inputs, target, learning_rate, passes, flags, line_number):

    # Repeat {passes} times
    for _ in range(passes):
        prediction = perceptron_predict(weights_old, inputs, flags)
        adjustments = perceptron_calculate_adjustments(prediction, weights_old, target, learning_rate, flags)

        # Calculate new weights (separate variable for printout purposes)
        weights_new = []
        for i in range(len(weights_old)):
            weights_new.append(weights_old[i] - (adjustments[i] * inputs[i]))

        if flags.flag_watching:
            printout_training(inputs, weights_old, prediction, target, adjustments, line_number)
        if flags.flag_detailed:
            input("Press anything to continue...\n")
        
        weights_old = weights_new

    return weights_new

def test(inputs, target, flags, line_number, weights):
    
    # Get prediction and rough error estimate
    prediction = perceptron_predict(weights, inputs, flags)
    error = (abs(prediction-(target+1)/10)/((target+1)/10))*100 if target != 0 else (abs(prediction-(target+1)/10))*100

    total_error = printout_testing(inputs, target, prediction, error, flags, line_number)
    # Skeleton function
    return total_error