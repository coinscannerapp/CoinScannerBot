# Coinscanner/bot

This is a crypto trading bot, implementing QFL(quickfinger luc) strategy. The bot can also be used for visualization of "base" occurances.

## Getting Started

Project is still under development so there is no deployable version.

### Prerequisites
This project requires Python 3.6 (https://www.python.org/downloads/release/python-360/)

### Installing for development
- `clone repo`    
- `$pip install pipenv` (install the pipenv virtual enviroment manager)
- `$cd <projectname>`
- `$pipenv install` (if an error occurs with Twisted 18.4 installation, use the next line before running `$pipenv install` again)
    - (fix for twisted error, skip if you do not experience the error)`$pipenv install http://fstab.net//pypi//simple//twisted//Twisted-18.4.0-cp36-cp36m-win_amd64.whl`
  
 - (optional) Configure Visual Studio Code to use `pipenv` (to be able to debug and run code directly in terminal (without doing the `pipenv shell`))
    - https://olav.it/2017/03/04/pipenv-visual-studio-code/
### Visualization
For visualization of the klines change global variable in `constants.py` 
```python 
    VISUALIZATION = True
```

## Running tests

    When running `pipenv install` you will automaticly obtain the `pytest` package used for testing this project.

### To run automated tests :
    pytest will inspect all files and find those named 'test_* with functions named test_*

-  `$cd <project directory> `
-  `$pipenv run pytest`
-  `$pipenv run pytest -v` (v for verbose: see all details about the test runs when they fail) 
-  `$pipenv run pytest -s` (-s will print all to console)

# Ideas and misc
[**Python best practices**](BP.md) 

[**Challenges and misc**](challenges.md) (to be removed)

## Base defenition assumptions 
- A 'drop' is a negative price_move of more than 10% in less than 10 hours. All klines are negative (should probably allow for small contra move)
- A 'raise' is a positive price_move of more than 10% in less than 10 hours. All klines are positive
- A 'base' is a drop + a raise with less than 4 hours appart

# TODO:
- Update base definitions
- Describe constant variables in README

## Authors

* **Thomas Hartmann** - *Initial idea + developer* - [Thomas-Hartmann](https://github.com/Thomas-Hartmann)
* **Alexander W. Hørsted-Andersen** - *developer* - [awha86](https://github.com/awha86)
* **Mathias Bigler** - *developer* - [Zurina](https://github.com/Zurina)
* **Mikkel Emil Larsen** - *developer* - [mikkel7emil](https://github.com/mikkel7emil)
* **Stanislav Novitski** - *developer* - [Stani2980](https://github.com/Stani2980)
  


<!-- ## License
Not yet licensed
<!-- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details -->

<!-- ## Acknowledgments  -->