# Introduction to Machine Learning for Materials Science

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

