# Basic Flask Setup

## Requirements

Python 3.5.2+

## Setting up environment using virtualenv

### Installation

```
pip install virtualenv
```

### Create virtual environment

Go to root folder and

```
virtualenv .env
source .env/bin/activate
```

deactivate using

```
deactivate
```

## Setting up environment using mini-conda

### Installation

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

### Create virtual environment

```
conda create -n {name_of_env} python={version_of_python}
conda create -n python-session python=3.7.3
```

deactivate using

```
conda deactivate
```

### install packages using pip

```
pip install flask
pip install flask-restplus
```

#### Setting up environment using pipenv

```
pip install pipenv
```

### Create virtual environment

```
pipenv --python 3
pipenv shell
```

deactivate using

```
ctrl + d
```

## Install Dependencies

```
pipenv install flask
pipenv install flask-restplus

or

pipenv install "<package_name~=specific_version>"

or

pipenv install
```

## Running the application

```
python3 -m src
```

and open your browser to here:

```
http://localhost:5000
```
