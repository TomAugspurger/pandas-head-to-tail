# SciPy 2018 Tutorial: Pandas .head() to .tail()

#### Presented by:
- [Tom Augspurger](https://tomaugspurger.github.io/), [Anaconda, Inc.](https://anaconda.org/)
- [Joris Van den Bossche](https://jorisvandenbossche.github.io/), [Université Paris-Saclay Center for Data Science](https://www.datascience-paris-saclay.fr/)
- [Dillon Niederhut](https://dillon.niederhut.us), [Enthought Inc.](https://www.enthought.com)


## First-Time Setup

#### 1. Install Python

If you don't already have a working python distribution, you may download
Enthought Canopy ([https://store.enthought.com/](https://store.enthought.com/),
Anaconda Python ([https://continuum.io/downloads](https://continuum.io/downloads)),
or Python.org  ([https://www.python.org/downloads/](https://www.python.org/downloads/)).

#### 2. Download Tutorial Materials

This GitHub repository is all that is needed in terms of tutorial content. The simplest solution is to download the material using this link:

[https://github.com/deniederhut/Pandas-Tutorial-SciPyConf-2018/archive/master.zip](https://github.com/deniederhut/Pandas-Tutorial-SciPyConf-2018/archive/master.zip)

If you're familiar with Git, you can also clone this repository with:

```sh
$ git clone git@github.com:deniederhut/Pandas-Tutorial-SciPyConf-2018.git
```

It will create a new folder named Pandas-Tutorial-SciPyConf-2018/ with all the
content you will need, including:

- `requirements.txt` - the package requirements for this tutorial
- `check_environment.py` - a script for testing your installation
- `notebooks/` - the Jupyter notebooks we'll use during the tutoral

#### 3. Install Required Packages

With Canopy, the required packages are already installed.

If you are using Anaconda, you can install the necessary packages by opening a terminal and entering the following:

```sh
conda install --file requirements.txt
```

If you are using Python from python.org or your system, you can install the necessary packages by opening a terminal and entering the following:

```sh
pip install -U -r requirements.txt
```

#### 4. Test the Installation

To make sure everything was installed correctly, open a terminal, and change its directory (`cd`) so that your working directory is `Pandas-Tutorial-SciPyConf-2018`. The enter the following:

```sh
python check_environment.py
```

## Questions? Problems?

You may post messages to the slack channel for this tutorial at: [https://scipy2018.slack.com](https://scipy2018.slack.com)
