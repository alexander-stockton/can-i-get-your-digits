# Can I Get Your Digits?
### Machine Learning Project for CMSC-5723

A custom digit classification system using a from-scratch implementation of neural network perceptrons with gradient descent and backpropagation.

---

## Overview

This project implements a **10-class digit classifier** (0-9) using one-vs-all binary classification with sigmoid perceptrons. Built entirely from scratch without machine learning libraries, it demonstrates fundamental concepts of neural networks including:

- Forward propagation with sigmoid activation
- Backpropagation with gradient descent
- One-vs-all multi-class classification
- Weight persistence (save/load trained models)

## Features

- **Custom Neural Network**: No ML libraries (NumPy, scikit-learn, etc.) - everything built from the ground up
- **Multi-Class Classification**: 10 binary perceptrons trained in one-vs-all fashion
- **Configurable Training**: Adjustable learning rate and epoch count
- **Model Persistence**: Save and load trained models
- **Visible Testing**: Watch predictions in real-time or batch process
- **Input Normalization**: Preprocesses 8×8 pixel values (0-16) to normalized range (0-1)

## Dataset

This project uses the **Optical Recognition of Handwritten Digits** dataset from the UCI Machine Learning Repository.

- **Source**: [UCI ML Repository - Optical Digits Dataset](https://archive.ics.uci.edu/dataset/80/optical-recognition-of-handwritten-digits)
- **Format**: Each sample contains 64 features (8×8 pixel grid) + 1 target label (0-9)
- **Training Set**: `optdigits.tra` (3,823 samples)
- **Test Set**: `optdigits.tes` (1,797 samples)

### Data Format
```
0,0,5,13,9,1,0,0,0,0,13,15,10,15,5,0,...,0,0,9,15,4,0,0,0,6
```
- First 64 values: pixel intensities (0-16)
- Last value: digit label (0-9)

## Getting Started

### Prerequisites

- Python 3.x
- No external ML libraries required! (uses only standard library: `math`, `random`, `os`, `sys`)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/alexander-stockton/digit-classifier.git
cd digit-classifier
```

2. Ensure data files are in the `./data/` directory:
```
project/
├── data/
│   ├── optdigits.tra
│   ├── optdigits.tes
│   └── perceptron.csv (generated after training)
├── resources/
│   ├── perceptrons.py
│   └── save_load.py
└── main.py
```

### Usage

Run the main program:
```bash
python main.py
```

#### Training a New Model

```
Do you want to train a new model? (y/n): y
Enter training data filename (default: './data/optdigits.tra'): 
Enter learning rate from 0.0 to 1.0 (default: 0.2): 0.01
Enter number of training passes (default: 10): 50

Starting training process...
This may take a while...
```

**Recommended Settings:**
- Learning Rate: `0.01` - `0.05` (lower = more stable, higher = faster but riskier)
- Training Passes: `20` - `100` (more passes = better accuracy, but diminishing returns)

#### Testing a Trained Model

```
Do you want to train a new model? (y/n): n
Do you want to watch? (y/n): n
Enter filename of saved model (default: './data/perceptron.csv'): 
Enter test data filename (default: './data/optdigits.tes'): 

Testing...
Accuracy Estimate: 94.27%
```

**Watch Mode**:
```
Do you want to watch? (y/n): y

Line: 1
Prediction: 0, Target: 0

Line: 2
Prediction: 1, Target: 1
...
...
Accuracy Estimate: xx.xx%
```

## Architecture

### Network Structure

```
Input Layer (64 neurons)
     ↓
10 Binary Perceptrons (one-vs-all)
     ↓
Sigmoid Activation
     ↓
Argmax Selection → Final Prediction
```

### Algorithm Details

**Forward Propagation:**
```python
weighted_sum = Σ(weight_i × input_i)
prediction = 1 / (1 + e^(-weighted_sum))
```

**Backpropagation:**
```python
error = prediction - target  # target ∈ {0, 1}
sigmoid_derivative = prediction × (1 - prediction)
adjustment = error × sigmoid_derivative × learning_rate × input
weight_new = weight_old - adjustment
```

**Classification:**
```python
# Run all 10 perceptrons
predictions = [perceptron_0(input), ..., perceptron_9(input)]
# Choose digit with highest activation
classification = argmax(predictions)
```

## File Structure

```
├── main.py                    # Entry point and data processing
├── resources/
│   ├── perceptrons.py         # Neural network implementation
│   │   ├── perceptron_predict()   # Forward propagation
│   │   ├── train()                # Training with backprop
│   │   └── test()                 # Classification & evaluation
│   └── save_load.py           # Model persistence
│       ├── save()                 # Export weights to CSV
│       └── load()                 # Import weights from CSV
├── data/
│   ├── optdigits.tra          # Training dataset
│   ├── optdigits.tes          # Testing dataset
│   └── perceptron.csv         # Saved model (after training)
├── License
└── README.md
```


## Performance

Typical accuracy on test set: **90-95%** depending on hyperparameters

### Hyperparameter Tuning Results

| Learning Rate | Epochs | Test Accuracy |
|---------------|--------|---------------|
| 0.8           | 100    | ~91.9%        |
| 0.2           | 10     | ~92.3%        |
| 0.05          | 50     | ~92.3%        |
| 0.01          | 100    | ~92.49%       |
| 0.005         | 1000   | ~92.6%        |

*Note: Results may vary due to random weight initialization*

## Troubleshooting

### Low Accuracy (<80%)
- Increase training epochs (try 50-100)
- Modify learning rate (smaller tends to higher accuracy, but can get stuck)
- Ensure data files are in correct format (integer data first, target last)

### Training Takes Too Long
- Decrease epochs (try 10-20)
- Use smaller dataset subset for testing

### Model Not Saving
- Check write permissions for `./data/` directory
- Verify filename path is valid
- Ensure training completed successfully


## Acknowledgments

- **Dataset**: UCI Machine Learning Repository
  - Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
  
- **Course**: CMSC-5723 Machine Learning

---

**Author**: Alexander Stockton
**Course**: CMSC-5723 - Machine Learning  
**Date**: February 2026