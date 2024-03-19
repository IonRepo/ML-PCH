# Machine Learning-Aided First-Principles Prediction of Earth-Abundant Pnictogen Chalcohalide Solid Solutions for Multi-junction Solar Cells

This project introduces a novel framework for generating new crystal materials using equivariant diffusion models based on a graph-like representation of data. This offers a powerful approach to surpass previous implementations, as it considers interactions and similarities between close points (which are more likely to interact). As well, aligned with previous implementations, ours also allows maximizing arbitrary targets such as conductivity, absorption, and more, or looking for materials with specific properties (such as diffraction patterns or n-order transitions). The generated crystals demonstrate remarkable thermodynamic stability (convex-hull approach), compared against the Materials Project database. 

The core technology behind this framework is based on deep convolutional layers and graph-like representation of data, where the diffusion process is achieved through the use of Markov chains. The denoising aspect of the model is implemented using convolutional graph neural networks, ensuring high-quality results, with which the noise of graphs is predicted and extracted, allowing the generation of an arbitrary number of novel, independent materials.

This technology is suitable for different applications: from discovering improved ionic conductors beyond current databases to generating molecules for efficient water splitting. Moreover, the model itself can be applied to a variety of problems (concretely, any problem which can be formulated in terms of graphs), such as proposing enhanced distributions in social networks or traffic. Then, although applied to crystal material generation, this repository is divided into two independent functionalities:

## Features

- ...
- ...

Please be aware that the code is under active development, bug reports are welcomed in the GitHub issues!

## Installation

To download the repository and install the dependencies:

```bash
git clone https://github.com/IonRepo/PredVCA.git
cd PredVCA
pip3 install -r requirements.txt
```

## Execution

A set of user-friendly jupyter notebook have been developed, which can be run locally with pytorch and pymatgen dependencies. It generates a graph-like database (from the Materials Project database or any other source) and trains the generative model to best reproduce those materials (and enhance some desired target, if desired).

## Citing

If you use this repository in your work, please consider citing:

...

## Authors

This project is being developed by:

 - Cibrán López Álvarez

## Contact, questions and contributing

If you have questions, please don't hesitate to reach out at: cibran.lopez@upc.edu
