import os

def printout_training(inputs, weights, prediction, target, adjustments, line):
    # Clear console
    os.system('cls')
    print("Training...\n")
    print(f"Line: {line}\n")

    # Create layer string based on input size
    layer = ""
    for i in range(0, int(inputs.__len__()/3) + 1):
        layer += "--------"

    # *----------------...---*
    # |
    data = "*" + layer + "*\n|"

    # |  x0  |  x1  |  x2  | ...
    for i in range(0, inputs.__len__()):

        if (str(i).__len__() == 1):
            data += f"  x{i}   |"
        elif (str(i).__len__() == 2):
            data += f"  x{i}  |"
        elif (str(i).__len__() == 3):
            data += f" x{i}  |"
        
        if (i%22 == 21):
            data += "\n|"

    # *----------------...---*
    # |
    data += "\n*" + layer + "*\n|"
    
    # |  1   |  0   |  12  | ...
    for i in range(0, inputs.__len__()):
        if (str(inputs[i]).__len__() == 1):
            data += f"  {inputs[i]}    |"
        else:
            data += f"  {inputs[i]}   |"
        
        if (i%22 == 21):
            data += "\n|"

    # *----------------...---*
    # |
    data += "\n*" + layer + "*\n|"

    # |  w0  |  w1  |  w2  | ...
    data += "  w0   |"
    for i in range(1, weights.__len__()):
        if (str(i).__len__() == 1):
            data += f"   w{i}  |"
        elif (str(i).__len__() == 2):
            data += f"  w{i}  |"
        elif (str(i).__len__() == 3):
            data += f" w{i}  |"
        
        if (i%22 == 21):
            data += "\n|"

    # *----------------...---*
    # |
    data += "\n*" + layer + "*\n|"
    
    # | 0.135| 0.00 |-0.992| ...
    for i in range(0, weights.__len__()):
        if (float(weights[i]) < 0 and float(weights[i]) > -10):
            data += f"{weights[i]:.3f} |"
        elif (float(weights[i]) == 0):
            data += " 0.00  |"
        elif (float(weights[i]) <= -10):
            data += f"{weights[i]:.2f} |"
        else:
            data += f" {weights[i]:.3f} |"
        
        if (i%22 == 21):
            data += "\n|"

    # *----------------...---*
    # 
    data += "\n*" + layer + "*\n"

    # *----------------...---*
    # |
    data += "\n*" + layer + "*\n|"

    # Round prediction to get classification
    classification = round(prediction * 10).__str__()

    # Print try data and account for negatives in strings
    error = prediction - (target/10)
    if (error < 0):
        data += f"Prediction: {prediction:.3f} ({classification})" \
                f"| Target: {target} |Error: {error:.3f} |"
    else:
        data += f"Prediction: {prediction:.3f} ({classification})" \
                f"| Target: {target} |Error: {error:.3f} |"

    # *----------------...---*
    # |
    data += "\n*" + layer + "*\n|"

    # | adj0 | adj1 | adj2 | ...         
    for i in range(0, adjustments.__len__()):
        if (str(i).__len__() == 1):
            data += f"  a{i}   |"
        else:
            data += f"  a{i}  |"
        
        if (i%22 == 21):
            data += "\n|"
    
    # *----------------...---*
    # |
    data += "\n*" + layer + "*\n|"
    
    # | 0.135| 0.00 |-0.992| ...
    for i in range(0, adjustments.__len__()):
        if (float(adjustments[i]) < 0):
            data += f"{adjustments[i]:.3f} |"
        elif (float(adjustments[i]) == 0):
            data += " 0.00  |"
        elif (float(adjustments[i]) <= -10):
            data += f"{adjustments[i]:.3f}|"
        else:
            data += f" {adjustments[i]:.3f} |"
        
        if (i%22 == 21):
            data += "\n|"
    
    # *----------------...---*
    data += "\n*" + layer + "*\n"

    print(data)

def printout_testing(inputs, weights, prediction, target, adjustments, line):
    # Clear console
    os.system('cls')
    print("Testing...\n")

    # Create layer string based on input size
    layer = ""
    for i in range(0, int(inputs.__len__()/3) + 1):
        layer += "--------"

    # *----------------...---*
    # |
    data = "*" + layer + "*\n|"

    # |  x0  |  x1  |  x2  | ...
    for i in range(0, inputs.__len__()):

        if (str(i).__len__() == 1):
            data += f"  x{i}   |"
        elif (str(i).__len__() == 2):
            data += f"  x{i}  |"
        elif (str(i).__len__() == 3):
            data += f" x{i}  |"
        
        if (i%22 == 21):
            data += "\n|"

    # *----------------...---*
    # |
    data += "\n*" + layer + "*\n|"
    
    # |  1   |  0   |  12  | ...
    for i in range(0, inputs.__len__()):
        if (str(inputs[i]).__len__() == 1):
            data += f"  {inputs[i]}    |"
        else:
            data += f"  {inputs[i]}   |"
        
        if (i%22 == 21):
            data += "\n|"

    # *----------------...---*
    # 
    data += "\n*" + layer + "*\n"

    # *----------------...---*
    # |
    data += "\n*" + layer + "*\n|"

    # Round prediction to get classification
    classification = round(prediction * 10).__str__()

    # Print try data and account for negatives in strings
    error = prediction - (target/10)
    if (error < 0):
        data += f"Prediction: {prediction:.3f} ({classification})" \
                f"| Target: {target} |Error: {error:.3f} |"
    else:
        data += f"Prediction: {prediction:.3f} ({classification})" \
                f"| Target: {target} |Error: {error:.3f} |"
    
    # *----------------...---*
    data += "\n*" + layer + "*\n"

    print(data)