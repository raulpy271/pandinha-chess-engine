# 🐼♟️ pandinha-engine

Pandinha-engine is a chess engine that use [MinMax Algorithm](https://en.wikipedia.org/wiki/Minimax) and [Alpha–beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) to search moves.

The engine follows the [UCI Protocol](http://wbec-ridderkerk.nl/html/UCIProtocol.html), so it works with any GUI that accepts custom engines especified with the UCI Protocol.

# Screenshots

![human vs IA](/assets/playing.gif)

# Usage

To use the engine you need to install an GUI's that supports the UCI Protocol to communicate with the engine. 

After installing a GUI, access the `src/settings.py` file and change the values to your preference. Also, you need figure out how to add a custom engine in your GUI, by doing that add the engine main file path: `main.py`.

The recommended GUI is [jerry](https://github.com/asdfjkl/jerry) because the engines were tested using this GUI. However, soon all the UCI commands will be implemented to allow the engine to work with all UCI GUI's.

# Especification

## Processing Model

The search can be done sequential or can be parallel, in the parallel approach, is created a pool of processes.

## Move generation

To generate moves is created a function that return a python generator, where the moves are computed on demand, this is useful because when some nodes are cutted-off the remaining moves aren't calculated.

## Board Representation

To represent the board is used a square-centric approach, where the board is an array with 64 integer values, where each integer represent a colored piece or an empty square.

## Evaluation

The evaluation function is purely material-based, which use the standard weights:

 - Pawn: 1
 - Bishop: 3
 - Knight: 3
 - Rook: 5
 - Queen: 9

# References

 - NORVIG, P.; RUSSELL, S. Inteligência Artificial. Elsevier, 3a ed., 2013.
 - [Board representation - Chess Programming ](https://www.chessprogramming.org/Board_Representation)
 - [Move generation - Chess Programming ](https://www.chessprogramming.org/Move_Generation)
 - [Python Generators](https://www.geeksforgeeks.org/generators-in-python/)

