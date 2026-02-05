from resources.save_load import save,load
from resources.perceptron import train,test

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
        # (modified) Generation by Claude Sonnet 4.5
        #   This is a modified version of the loading implementation from
        #   resources/save_load.py. Including this note because I lost the screenshots
        #   of the prompt I used to generate the save_load file and its implementation.
        try:
            weights = load('./data/perceptron.csv')
            print("Loaded existing perceptron")
        except FileNotFoundError:
            # Initialize new perceptron if no saved model exists
            weights = []
            print("Initialized new perceptron\n")
        # End (modified) Generation by Claude Sonnet 4.5

    filename = input("Enter training data filename (default: 'optdigits.tra'): ") or "optdigits.tra"
    print("\n")

    # Process input data for classification

if (__name__ == "__main__"):
    main()



