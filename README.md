# CEMRG Wearable

## Environments
### Option 1 (Recommended). Use Conda + Poetry
[Poetry](https://python-poetry.org/docs/) is a tool for dependency management. 
We create the environment with Anaconda and manage dependencies with Poetry.

1. [Install Poetry](https://python-poetry.org/docs/) in your computer
2. Install Anaconda
3. Create a new environment with the file provided: `conda env create -f environment.yaml` 
4. Activate the environment `conda activate cemrg_wearable` 
5. Install the dependencies using Poetry `poetry install --only main`.

Poetry will read from the poetry.lock file and install the exact dependencies used to develop this project.

> If you want to experiment with dependencies versions, delete the lock file and modify the pyproject.toml before `poetry install --only main`  

### Option 2. Only use CONDA
Anaconda is useful, but it can be slow at managing dependencies. It is recommended to use poetry.

**Setup conda environment**
> You only need to do this once

Download [anaconda](https://www.anaconda.com/products/distribution), then 
on a terminal type: 
```
conda create -n cemrg_wearable python=3.11 -y & conda activate cemrg_wearable
```

Copy the following to install the python dependencies of this project
```
conda install -c conda-forge pandas matplotlib bs4 requests numpy seaborn -n cemrg_wearable -y
```

You might need to set your `PYTHONPATH` to work on this repository. Move into this folder and type 
```shell
export PYTHONPATH=$PYTHONPATH:$(pwd) 
```


## Weather data
You need to get your API key! 

> NOTE! It is not good practice to leave the API key on github! 

Get your API key from [here](https://openweathermap.org/appid), then save it in a file called `apikey.txt`, 
which **will only be available in your computer**! That name is ignored by git. 

Then you can call the function `weather_utils.get_weather()`. See [this notebook](./ipynb/process_atom_5_data.ipynb)  
for an example.

Also, check [this website](https://openweathermap.org/weather-conditions) for the weather codes and conditions.