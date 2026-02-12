def save(weights, filename='./data/perceptron.csv'):
    with open(filename, 'w') as f:
        for _ in weights: # Loop through perceptrons
            for __ in _: # Get each perceptron's weights
                f.write(f"{__:.5},")
            f.write("\n")

def load(filename='./data/perceptron.csv'):
    
    weights = []
    with open(filename, 'r') as f: 
        # Do for each perceptron
        for line in f:
            # Split and clean each list of weights
            weights_list = line.split(',')
            weights_list.pop() # Extra empty item pop due to untrimmed comma during saving

            # Initialize weights based on weight list above
            percept_weights = [float(w) for w in weights_list]
            weights.append(percept_weights)

    return weights

