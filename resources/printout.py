
def printout(inputs, weights, prediction, target, adjustments):
    layer = ""
    for i in range(0, int(inputs.__len__()/3) + 1):
        layer += "-------"

    # *----------------...---*
    # |
    data = "*" + layer + "*\n|"

    # |  x0  |  x1  |  x2  | ...
    for i in range(0, inputs.__len__()):

        if (str(i).__len__() == 1):
            data += f"  x{i}  |"
        elif (str(i).__len__() == 2):
            data += f"  x{i} |"
        elif (str(i).__len__() == 3):
            data += f" x{i} |"
        
        if (i%22 == 21):
            data += "\n|"

    # *----------------...---*
    # |
    data += "\n*" + layer + "*\n|"
    
    # |  1   |  0   |  12  | ...
    for i in range(0, inputs.__len__()):
        if (str(inputs[i]).__len__() == 1):
            data += f"  {inputs[i]}   |"
        else:
            data += f"  {inputs[i]}  |"
        
        if (i%22 == 21):
            data += "\n|"

    # *----------------...---*
    # |
    data += "\n*" + layer + "*\n|"

    # |  w0  |  w1  |  w2  | ...
    data += "  w0  |"
    for i in range(1, weights.__len__()):
        if (str(i).__len__() == 1):
            data += f"  w{i}  |"
        elif (str(i).__len__() == 2):
            data += f"  w{i} |"
        elif (str(i).__len__() == 3):
            data += f" w{i} |"
        
        if (i%22 == 21):
            data += "\n|"

    # *----------------...---*
    # |
    data += "\n*" + layer + "*\n|"
    
    # | 0.135| 0.00 |-0.992| ...
    for i in range(0, weights.__len__()):
        if (float(weights[i]) < 0):
            data += f"{weights[i]:.3f}|"
        elif (float(weights[i]) == 0):
            data += " 0.00 |"
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

    # Huge conditional for subbing class into prediction sigmoid
    classification = ""
    if prediction < 0.1:
        classification = "0"
    elif prediction < 0.2:
        classification = "1"
    elif prediction < 0.3:
        classification = "2"
    elif prediction < 0.4:
        classification = "3"
    elif prediction < 0.5:
        classification = "4"
    elif prediction < 0.6:
        classification = "5"
    elif prediction < 0.7:
        classification = "6"
    elif prediction < 0.8:
        classification = "7"
    elif prediction < 0.9:
        classification = "8"
    elif prediction < 1.0:
        classification = "9"

    data += f"Prediction: {prediction:.3f} ({classification}) | Target: {target} | Error: {prediction - target:.3f} |"

    # *----------------...---*
    # |
    data += "\n*" + layer + "*\n|"

    # | adj0 | adj1 | adj2 | ...         
    for i in range(0, adjustments.__len__()):
        if (str(i).__len__() == 1):
            data += f"  a{i}  |"
        else:
            data += f"  a{i} |"
        
        if (i%22 == 21):
            data += "\n|"
    
    # *----------------...---*
    # |
    data += "\n*" + layer + "*\n|"
    
    # | 0.135| 0.00 |-0.992| ...
    for i in range(0, adjustments.__len__()):
        if (float(adjustments[i]) < 0):
            data += f"{adjustments[i]:.3f}|"
        elif (float(adjustments[i]) == 0):
            data += " 0.00 |"
        else:
            data += f" {adjustments[i]:.3f} |"
        
        if (i%22 == 21):
            data += "\n|"

    print(data)
