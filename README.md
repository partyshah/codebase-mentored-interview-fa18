# Welcome to the Fall 2018 Mentored Project Technical Interview!

In this interview, you will implement the classic interactive game, **Towers of Hanoi**.
![alt text](https://s3.amazonaws.com/codecademy-content/courses/cs-path-stacks/stacks-project/towers.gif "Logo Title Text 1")

The objective of the game is to move the stack of disks from the leftmost tower to the rightmost tower.

The game follows three rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the top disk from one of the towers and placing it on top of another tower or on an empty rod.
3. No disk may be placed on top of a smaller disk.

In this game, we will model the disks as numbers (i.e. the larger the number, the bigger the disk). Here's what a possible game solution could look like:

[Towers of Hanoi](https://s3.amazonaws.com/codecademy-content/courses/cs-path-stacks/towers.mov)

## Tasks

### Setup
Some the code has been outlined/done for you. In this game, we will model the three towers as lists, `left`, `middle`, and `right`. As demonstrated by the code, `num_disks` will be determined by the user. `get_num_disks` and `get_user_input` has been implemented for you.

### Creating the Towers
Fill in the function `create_towers` such that you append the appropriate disks to `left`. For instance, if `num_disks` is `3`, then `create_disks` should make `left` equal to `[3, 2, 1]`


### Checking a Valid Move
Fill in the function `is_valid_move` such that a the function returns `True` if a move from the `from_tower` list to the `to_tower` list is valid and `False` otherwise.

### Checking if the Game is Solved
Fill in the function `is_solved` that returns `True` if the game is solved and `False` otherwise. Think about at what point the game is solved..

### Filling in the Game Logic
Fill in the function `play_game` such that when called the entire game should be played. Use the logic of the game and the other functions to fill this function out. Refer back to the video and rules if you are confused about the game logic.

## Running Code
To run a specific function, run
```python3
python3 -c 'import interview; print interview.function_name()'
```

To run the entire game, run
```python3
python3 interview.py
```

Have fun, and please ask questions and explain your code as you go!


