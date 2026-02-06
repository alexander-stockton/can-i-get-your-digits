from resources.save_load import save,load
from resources.perceptron import train,test

def main():
    print("Note: Terminal should run in full screen for best UI readability.\n\n")
    
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

        # Initialize weights based on input count (ignore target)
        weights = []
        with open(filename, "r") as _:
            _tempinputs = _.readline().strip().split(",")
            for _ in range(len(_tempinputs) - 1):
                weights.append(0.0)
        

        # Process training data
        with open(filename, "r") as file_reader:
            line_number = 0
            for _line in file_reader:
                line_number += 1
                line_data = _line.strip().split(",")

                # Extract inputs and expected output
                inputs = [int(x) for x in line_data[0:-1]]
                target = int(line_data[-1])

                # Train perceptron
                weights = train(weights, inputs, target, learning_rate, passes)
    
    else:
        # (modified) Generation by Claude Sonnet 4.5
        #   This is a modified version of the loading implementation from
        #   resources/save_load.py. Including this note because I lost the screenshots
        #   of the prompt I used to generate the save_load file and its implementation.
        try:
            weights = load('./data/perceptron.csv')
            print("Loaded existing perceptron")
        except FileNotFoundError:
            # Initialize new perceptron if no saved model exists
            weights = [0.0 for _ in range(64)]  # Assuming 64 inputs for the perceptron
            print("Initialized new perceptron\n")
        # End (modified) Generation by Claude Sonnet 4.5

    filename = input("Enter training data filename (default: 'optdigits.tra'): ") or "optdigits.tra"
    print("\n")

    # Process input data for classification

if (__name__ == "__main__"):
    main()



