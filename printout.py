def printout(inputs, weights, prediction):
    layer = ""
    for i in range(0, inputs.__len__()):
        layer += "-------"

    # *----------------...---*
    data = "*" + layer + "*\n|"

    # |  x0  |  x1  |  x2  | ...
    for i in range(0, inputs.__len__()):
        data += "  x" + str(i) + "  |"

    # *----------------...---*
    data += "\n*" + layer + "*\n|"
    
    # |  1   |  0   |  12  | ...
    for i in range(0, inputs.__len__()):
        if (inputs[i].__len__() == 1):
            data += "  {inputs[i]}  |"
        else:
            data += "  {inputs[i]}   |"

    # *----------------...---*
    data += "\n*" + layer + "*\n|"

    # |  w0  |  w1  |  w2  | ...
    data += "  w0  |"
    for i in range(1, weights.__len__()):
        data += "  w" + str(i) + "  |"

    # *----------------...---*
    data += "\n*" + layer + "*\n|"
    
    # | 0.135| 0.00 |-0.992| ...
    for i in range(0, weights.__len__()):
        if (float(weights[i]) < 0):
            data += f"{weights[i]:.3f}|"
        elif (float(weights[i]) == 0):
            data += " 0.00 |"
        else:
            data += f" {weights[i]:.3f} |"

    print(data)
    print("*" + layer + "*")
    print("\n\n")
