# Introduction to Machine Learning for Materials Science

## Lesson plan

1. Python for computational science intro / recap | [Link](https://github.com/Mads-PeterVC/imlms/tree/main/lessons/lesson_1)
2. Pytorch / The Atomic Simulation Environment | [Link](https://github.com/Mads-PeterVC/imlms/tree/main/lessons/lesson_2)
3. Potential energy surfaces | [Link](https://github.com/Mads-PeterVC/imlms/tree/main/lessons/lesson_3)
4. Introduction to Machine Learning | [Link](https://github.com/Mads-PeterVC/imlms/tree/main/lessons/lesson_4)
5. Machine Learning for atomic systems 1 | [Link](https://github.com/Mads-PeterVC/imlms/tree/main/lessons/lesson_5)
6. Machine Learning for atomic systems 2 | [Link](https://github.com/Mads-PeterVC/imlms/tree/main/lessons/lesson_6)

## Installation

### Colab installion

If you use [Google colab](https://colab.research.google.com/), which is likely the easist way to get started, then installation is simple - at the top of the notebook just ensure that the line 

```
!pip install git+https://github.com/Mads-PeterVC/imlms
```

Has been executed, then the required dependencies will have been installed in your session.
If you using colab make sure to save a copy of each notebook to your Google drive or 
download it to your machine. 

### Local installation

If you want to your local machine, then I recommend creating a virtual environment and 
installing the dependencies in there. 

#### Virtual environment

To create a virtual environment open a terminal - and then assuming you have Python 
installed (if not see [here](https://www.python.org/downloads/) or [here](https://docs.anaconda.com/miniconda/install/).) run the command

```
python3 -m venv <path/to/env>
```

Where you decide on `<path/to/env>`. Once the command is completed you can check that the 
environment has been created

```
ls <path/to/env/>
```

And then you can activate it

```
source <path/to/env>/bin/activate
```

#### Dependencies

We will be using a variety of packages so to make managing all of that easier I have 
made this repo a package too - installing it will install all of the required 
packages. 

Installation can be done like so, in a terminal with an active virtual environment

```
pip install git+https://github.com/Mads-PeterVC/imlms
```

## Goals

- Atomistic description of materials
    - Governed by Quantum Mechanics
        - Most commonly approximate using density functional theory. 
    - Develop an understanding of potential energy surfaces. 
        - Structural stability
        - Dynamics / Vibrational properties
        - Chemical reactions
    - Be able to use ASE to setup structures and start calculations.
        - Make a cluster / nanoparticle
        - Make a surface w. adsorbate.
- Implement a simple potential energy surface
    - Lennard Jones
    - Lennard Jones with forces from Pytorch
        - Requires some introduction to Pytorch
    - Local optimization
    - Global optimization
- Introduction to Machine Learning
    - Motivation
        - Reducing the computational cost of simulations by replacing expensive 
        calculations with cheap ones, extends system size and time scales. 
    - What is machine learning? 
        - Categories
            - Supervised
            - Unsupervised
            - (Reinforcement learning)
        - Learning from data
            - What is 'data'? 
                - How is it represented to a computer? 
        - Algorithms
            - Nearest neighour classification 
            - Curve fitting
            - Neural Networks
    - Practical 
        - Sklearn: Excellent for off-the-shelf algorithms of many types.
        - Pytorch: for NN / Gradient based things

- Implement trainable machine learning potential
    - Understand descriptors / Invariance
        - Implement some Fingerprint or Behler-Parinello type descriptor. 
    - Understand neural networks
        - Feed forward layers
        - Activation functions
        - Gradient Descent 
        - Batching 
    - Learning a potential
        - Global anzats 
        - Local anzats

