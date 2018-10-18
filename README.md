# Pommerman Analyzer

This repo provides a set of scripts and notebooks to analyze a pommerman battle or a series of pommerman battles.

**Note:** This repo is still under development. Just getting started if you will.

## Getting Started

This is a suggestion in how to get started. You are welcome to use other virtual environments if you wish.

### Pre-requisites

* Python 3.6.0+
* virtualenv

### Installation

First clone the repository then change into the newly created dirctory.

```
git clone git@github.com:weseldridge/pommerman-analyzer.git
cd pommerman-analyzer
```

Next we will create a virtualenv to create an isolated Python environment.

```
virtualenv venv
source venv/bin/activate
```

Finally install of the python dependency.

```
pip install -U .
```


## Next Steps

There are Jupyter Notebooks that demonstrate how to preform different analaysis for single and mutli games. You can start Jupyter Notebook with,

```
jupyter notebook
```

Once the notebook opens in your web browser navigate into the `notebooks/` folder. There you can open notebooks where you can play with game data.