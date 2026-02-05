from save_load import save_perceptron,load_perceptron
from printout import printout

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

def main():
    # Do you want to train the model?
    # Yes >
    # No  >
    flag_training = (input("Do you want to train the model? (y/n): ") == 'y')

    # Training Branch
    if flag_training:
        filename = input("Enter training data filename (default: './data/optdigits.tra'): ") or "./data/optdigits.tra"
        learning_rate = float(input("Enter learning rate from 0.0 to 1.0 (default: 0.2): ") or 0.2)
        passes = int(input("Enter number of training passes (default: 10,000): ") or 10000)
        print("\n")

        print("Starting training process...\n")
        # Process training data
        with open(filename, "r") as file_reader:
            line_number = 0
            for _line in file_reader:
                line_number += 1
                line_data = _line.split(",")

                # Extract inputs and expected output
                inputs = [int(x) for x in line_data[0:-2]]
                target = int(line_data[-1])
                weights = [0.0 for _ in range(len(inputs))]

                # Train perceptron
    
    else:
        # Generation by Claude Sonnet 4.5
        try:
            weights = load_perceptron('perceptron.txt')
            print("Loaded existing perceptron")
        except FileNotFoundError:
            # Initialize new perceptron if no saved model exists
            weights = [0.0] * 20  # or random small values
            print("Initialized new perceptron\n")
        # End Generation by Claude Sonnet 4.5

    filename = input("Enter training data filename (default: 'optdigits.tra'): ") or "optdigits.tra"
    print("\n")

    # Process input data for classification

if (__name__ == "__main__"):
    main()



