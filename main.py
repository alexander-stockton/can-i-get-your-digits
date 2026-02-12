import os
import sys
import random
from resources.save_load import save,load
from resources.perceptrons import train,test


def main():
    print("Note: Terminal should run in full screen for best UI readability.\n")
    print("Note: Please zoom out to see the full training/testing UI.\n")
    
    # Flag 0: Testing/Training
    # Flag 1: Watching the test
    # Flag 2: Failed loading model from file
    flags = [0, 0, 0]

    # Prompt for flags
    flags[0] = (input("Do you want to train a new model? (y/n): ") == 'y')
    if not flags[0]: flags[1] = (input("Do you want to watch? (y/n): ") == 'y')

    # Training Branch
    if flags[0]:
        filename = input("Enter training data filename (default: './data/optdigits.tra'): ") or "./data/optdigits.tra"
        
        try: open(filename, "r")
        except FileNotFoundError:
            print("\n\nERROR: File not found! Please restart the program and try again")
            sys.exit()

        learning_rate = float(input("Enter learning rate from 0.0 to 1.0 (default: 0.2): ") or 0.2)
        passes = int(input("Enter number of training passes (default: 10): ") or 10)
        print("\n")
        
        print("Starting training process...\n\nThis may take a while...\n\nPlease come back later")

        # Initialize weights based on input count (ignore target)
        with open(filename, "r") as _:
            _tempinputs = _.readline().strip().split(",") # Strip excess characters
            
            # Initialize weights randomly so we don't get a bunch of inverses
            weights = [[random.uniform(-0.1, 0.1) for _ in range (len(_tempinputs)-1)] for _ in range(10)]

        # Process training data
        with open(filename, "r") as file_reader:
            line_number = 0
            for _line in file_reader:
                line_number += 1
                line_data = _line.strip().split(",")

                # Extract inputs and expected output
                inputs = [int(x)/16.0 for x in line_data[0:-1]]
                target = int(line_data[-1])

                # Train perceptron
                weights = train(weights, inputs, target, learning_rate, passes)
            
            # Save trained model
            _save = input("\nTraining complete. Please enter a filename to save the trained model (default: './data/perceptron.csv'): ") or "./data/perceptron.csv"
            save(weights, _save)
            print(f"Model saved!")

    # Testing Branch
    else:
        # Load Perceptrons
        try:
            _save = input("Enter filename of saved model (default: './data/perceptron.csv'): ") or "./data/perceptron.csv"
            weights = load(_save)
            print("Loaded existing perceptrons")
        except FileNotFoundError: # Initialize new perceptrons if no saved model exists
            weights = []
            filename = input("Enter test data filename (default: './data/optdigits.tes'): ") or "./data/optdigits.tes"
            
            # Initialize each new perceptron
            for _ in range(10):
                with open(filename, "r"): # Dynamically build weights list based on number of parameters from testing file
                    line_data = _line.strip().split(",")
                    percept = [random.uniform(-0.1, 0.1) for _ in line_data[0:-1]]
                weights.append(percept)
                print("Initialized new perceptron\n")

            print("Finished!\n")

        if not flags[2]: filename = input("Enter test data filename (default: './data/optdigits.tes'): ") or "./data/optdigits.tes"

        # Process testing data
        with open(filename, "r") as file_reader:
            # Clear console
            os.system('cls')
            print("Testing...\n")
            
            line_number = 0
            accuracy = 0
            for _line in file_reader:
                line_number += 1
                line_data = _line.strip().split(",")

                # Extract inputs and expected output
                inputs = [int(x)/16.0 for x in line_data[0:-1]]
                target = int(line_data[-1])

                # Train perceptron
                good = test(inputs, target, flags, line_number, weights)
                accuracy += good
            
            # Calculate and print accuracy
            print(f"\nAccuracy Estimate: {accuracy/line_number*100:.2f}%")
            
            # Save trained model
            input("\nTesting complete! Press anything to exit...")
        print("\n")

if (__name__ == "__main__"):
    main()



