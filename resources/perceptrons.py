import math

def perceptron_predict(weights, inputs):
    # Step 1: Calculate Weighted Sum
    weighted_sum = sum(w * x for w, x in zip(weights, inputs))

    # Step 2: Activation Function
    # Prevent overflow of sigmoid function

    # weighted_sum = max(-709, min(weighted_sum, 709)) # upper bound of math.exp function is ~709
    sigmoid = 1 / (1 + math.pow(math.e, -weighted_sum))

    # Step 3: Return Prediction
    return sigmoid

def train(weights, inputs, target, learning_rate, passes):

    # Train all 10 perceptrons
    for dig in range(10): 
        for _ in range(passes):

            # Forward Passes
            prediction = perceptron_predict(weights[dig], inputs)
            error = prediction - (target == dig)
            sig_deriv = prediction * (1-prediction)

            # Back Propogation
            for c in range(len(weights[dig])):
                adjustment = error*sig_deriv*learning_rate*inputs[c]
                weights[dig][c] -= adjustment
            
    return weights

def test(inputs, target, flags, line_number, weights):
    info_line = ""
    predictions = []

    if flags[1]: info_line += f"Line: {line_number}\n" # Only print if user wants

    # Make each perceptron guess
    for dig in range(10):
        prediction = perceptron_predict(weights[dig], inputs)
        predictions.append(prediction)

    # Choose best guess
    classification = predictions.index(max(predictions))
    
    # Only print if user wants
    if flags[1]:
        info_line += f"\nPrediction: {classification}, Target: {target}\n"
        print(info_line)
    
    # Answer is good: 1, answer is bad: 0.
    # Done to calculate overall accuracy
    return (classification == target)