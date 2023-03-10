<h1 align="left">Assignment-2-Test-driven-development</h1>

<p align="left">
  This project represents our Pig Dice Game for the course DA115B.
  <br> 
</p>

## Table of Contents

- [Table of Contents](#-table-of-contents)
- [About ](#-about-)
- [Description ](#-description-)
- [Getting Started ](#-getting-started-)
  - [Installing](#installing)
  - [Usage](#usage)
- [Validators ](#️-validators-)
- [Unittests ](#-unittests-)
- [Authors ](#️-authors-)

## About <a name = "about"></a>

Pig Dice is a simple dice game where the goal is to reach a certain number of points before your opponent. Each turn, a player rolls a six-sided die, adding up the total of each roll. If a player rolls a 1, they lose all the points they accumulated that turn and their turn ends. A player can choose to hold their points at any time, adding them to their total score for the game.

This project was made using python with a focus on OOP. The project consists of several classes that implements core functionalities for our dice game.

## Description <a name = "description"></a>

The project includes the following classes:

- "Dice": This class represents the die that is being rolled.
- "DiceHand": This class keeps track of the roll made by a player.
- "HighScore": This class updates the high score record for a player if it was beaten.
- "Intelligence": This class controlls the CPU difficulties.
- "Game": This class implements the functions of all the above classes to execute the game.
- "Shell": This class implements the terminal interface for the game.
- "main": This class executes an instance of the Shell class to begin the game in the terminal.

  #### CPU INTELLIGENCE IMPLEMENTATION
  
  The CPU has different difficulty levels to it in order to make the gameplay easier/harder for the user playing. The difficulties works as follow:
   
  - "Easy": The CPU can only roll a die from 1,3. 
  - "Medium": The CPU can roll a die from 1,6 (Same as the Player)
  - "Hard": The CPU can roll a die from 1,10. If it rolls a number above 6, it will count as a rolled 6.

## Getting Started <a name = "getting_started"></a>

### Installing

1. Clone this reporsitory to your local machine: [rep](https://github.com/josephhammami/Assignment-2-Test-driven-development)
2. Install a Python virtual environment and activate it.
#### Create the virtual environment
     make venv
3. Install Python 3
3. Install the dependent packages in `requirements.txt` by running `make install -r requirements.txt`

### Usage

All classes and code are stored under `/pig`

To run the game, navigate to your project directory in your desired terminal and run the following command:

`python main.py`

## Validators <a name = "validators"></a>

To run the validators and check the source code, run these commands:

### One at a time
    make flake8
    make pylint

### All at once
    make lint


## Unittests <a name = "unittests"></a>

To run the unittest for the different classes, run these commands:

### Unittests w/o coverage
    make unittest

### Unittests with coverage
    make coverage

### Linters and all above
    make test


## Authors <a name = "authors"></a>

-[@josephhammami](https://github.com/josephhammami)
-[@Allous95](https://github.com/Alloush95)
-[@aishamohamed](https://github.com/aishamohamed)
