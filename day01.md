## Getting python environment built

- With anaconda installed, we need to create an environment that can run the functions within STANLY

- One issue is that ants, the tool used for registration doesn't work with the newest release of Python (3.14), so we need to create an environment that uses Python version <= 3.13

```
conda create --name=stanly python=3.13
```

- With the stanly repo downloaded from gitlab (https://research-git.uiowa.edu/zjpeters/STANLY), we can use the `requirements.txt` file to install any necessary libraries

    - We can either download the repo directly, or can also use git from the command line to be able to keep our code up to date. I've put together a guide on [this page](https://github.com/zjpeters/introToNeuroProgramming) that you can see by selecting `gitBasics.md`

```
pip install -r stanly/requirements.txt
```

## Using BIDS format

- [The Brain Imaging Data Structure (BIDS)](https://bids.neuroimaging.io/) is a way to format data that was first used for MRI imaging, but provides a good template for how to approach scientific data generally.

- Using the following four folders (`code`, `derivatives`, `rawdata`, and `sourcedata`), you can easily keep track of data and prevent issues of finding data or files later during your project