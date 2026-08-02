# NeuroForge Journey 🚀

# Lesson 05: Building the First Artificial Neuron

**Date:** 01 August 2026

---

# Objective

The objective of this lesson is to understand the basic building block of every Neural Network: the **Artificial Neuron**.

By the end of this lesson, you should understand:

* What an Artificial Neuron is
* Why it was inspired by the human brain
* What Inputs are
* What Weights are
* What Bias is
* What a Weighted Sum is
* Why an Activation Function is required
* How to implement a simple neuron in Python

---

# Introduction

Everything in Deep Learning starts with a single Artificial Neuron.

A Neural Network is nothing more than thousands or millions of these neurons connected together.

The progression looks like:

```text
One Neuron
      ↓
Many Neurons
      ↓
Neural Layer
      ↓
Neural Network
      ↓
Deep Neural Network
      ↓
Transformer
      ↓
Large Language Model (GPT)
```

Understanding one neuron means understanding the foundation of every modern AI model.

---

# Biological Inspiration

The idea of an Artificial Neuron comes from the human brain.

A biological neuron works like this:

```text
Signals from other neurons
            ↓
       Cell Body
            ↓
      Decision Making
            ↓
      Output Signal
```

Artificial neurons imitate this process mathematically.

Instead of electrical signals, they use numbers.

---

# Components of an Artificial Neuron

An Artificial Neuron consists of five main parts.

```text
Inputs
   ↓
Weights
   ↓
Dot Product
   ↓
Bias
   ↓
Activation Function
   ↓
Output
```

---

# 1. Inputs (x)

Inputs are the information provided to the neuron.

Example:

Suppose we want to predict whether a student will pass an exam.

Possible inputs:

```text
Hours Studied

Attendance Percentage

Sleep Hours
```

Representing them numerically:

```text
x₁ = 5

x₂ = 90

x₃ = 7
```

These values are called **features** or **inputs**.

---

# 2. Weights (w)

Not every input contributes equally.

Example:

Hours Studied may be more important than Sleep Hours.

Therefore, every input is assigned a weight.

Example:

```text
w₁ = 0.8

w₂ = 0.5

w₃ = 0.2
```

Weights determine **how important each input is**.

During training, these weights are continuously updated using Gradient Descent.

---

# 3. Weighted Sum (Dot Product)

The neuron combines inputs and weights using the Dot Product.

Formula:

```text
Weighted Sum = x₁w₁ + x₂w₂ + x₃w₃
```

Example:

Inputs:

```text
[5, 90, 7]
```

Weights:

```text
[0.8, 0.5, 0.2]
```

Calculation:

```text
5 × 0.8 = 4

90 × 0.5 = 45

7 × 0.2 = 1.4
```

Total:

```text
4 + 45 + 1.4 = 50.4
```

This value is called the **Weighted Sum**.

---

# 4. Bias (b)

Bias is an additional value added after the weighted sum.

Example:

```text
Bias = 2
```

Calculation:

```text
50.4 + 2 = 52.4
```

Bias allows the neuron to shift its output and improves the model's ability to learn.

Without bias, many practical problems become difficult or impossible to solve effectively.

---

# 5. Activation Function

After calculating:

```text
x·w + b
```

the result is passed through an Activation Function.

Examples:

```text
Weighted Sum

↓

Sigmoid

↓

0.999
```

or

```text
Weighted Sum

↓

ReLU

↓

52.4
```

or

```text
Weighted Sum

↓

Tanh

↓

0.999
```

The Activation Function decides the neuron's final output.

In this lesson, we stop before applying activation.

The next lesson is dedicated entirely to Activation Functions.

---

# Complete Artificial Neuron Equation

The mathematical representation of a neuron is:

```text
Output = Activation(Weighted Sum + Bias)
```

or

```text
y = f(x · w + b)
```

Where:

* x → Inputs
* w → Weights
* · → Dot Product
* b → Bias
* f → Activation Function
* y → Final Output

This equation is one of the most important equations in Deep Learning.

---

# Python Implementation

Create the file:

```text
experiments/lesson5.py
```

Copy the following code:

```python
# ==========================================
# NeuroForge Journey
# Lesson 05 - Artificial Neuron
# ==========================================

# Inputs
inputs = [5, 90, 7]

# Weights
weights = [0.8, 0.5, 0.2]

# Bias
bias = 2

# Calculate Weighted Sum
weighted_sum = 0

for i in range(len(inputs)):
    weighted_sum += inputs[i] * weights[i]

# Add Bias
weighted_sum += bias

# Display Output
print("Neuron Output Before Activation =", weighted_sum)
```

Output:

```text
Neuron Output Before Activation = 52.4
```

---

# Behind the Scenes 🧠

Modern AI models perform the exact same operation.

The only difference is scale.

Our neuron:

```text
3 Inputs
```

GPT Neuron:

```text
4096 Inputs
```

Our neuron:

```text
3 Weights
```

GPT Neuron:

```text
4096 Weights
```

The mathematical process remains identical.

Only the number of computations increases dramatically.

---

# Key Takeaways

* An Artificial Neuron is the basic building block of every Neural Network.
* Inputs provide information to the neuron.
* Weights determine the importance of each input.
* The Dot Product computes the weighted sum.
* Bias shifts the output before activation.
* Activation Functions determine the final output.
* Modern AI systems contain millions or billions of neurons working together.

---

# Summary

An Artificial Neuron receives inputs, multiplies them by their corresponding weights, adds a bias, and passes the result through an Activation Function to produce an output. Although our implementation used only three inputs, the same mathematical idea scales to the billions of neurons used in modern Large Language Models.

---

# Homework

### Question 1

Explain in your own words:

**What is the purpose of weights inside a neuron?**

---

### Question 2

Why is a bias required?

---

### Question 3

Calculate manually:

Inputs:

```text
[2, 4]
```

Weights:

```text
[3, 5]
```

Bias:

```text
1
```

Find the neuron's output before activation.

---

### Question 4

Modify the Python code using the values above and verify your answer.

---

# Progress Tracker

```text
███████████████░░░░░ 25%

✅ Lesson 01 - Introduction to Machine Learning & LLMs
✅ Lesson 02 - Scalars, Vectors, Matrices & Tensors
✅ Lesson 03 - Dot Product & Matrix Multiplication
✅ Lesson 04 - Derivatives, Loss Functions & Gradient Descent
✅ Lesson 05 - Building the First Artificial Neuron
⬜ Lesson 06 - Activation Functions
⬜ Lesson 07 - Building a Neural Layer
⬜ Lesson 08 - Building a Neural Network
⬜ Lesson 09 - Loss Functions in Depth
⬜ Lesson 10 - Backpropagation
⬜ ...
⬜ Lesson 20 - NeuroForge GPT

```

---

# Next Lesson

## Lesson 06: Activation Functions

In the next lesson, we will learn:

* Why neurons without activation functions are useless
* Sigmoid Activation
* ReLU Activation
* Tanh Activation
* Which activation functions are used in modern LLMs
* Implementing activation functions from scratch in Python

**Milestone:** We will complete the first fully functional Artificial Neuron.
