# 🐼♟️ pandinha-engine

## Screenshots

![human vs IA](/assets/playing.gif)

## Introduction

Pandinha-engine is a chess engine that use [MinMax Algorithm](https://en.wikipedia.org/wiki/Minimax) and [Alpha–beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) to search moves.

The engine follows the [UCI Protocol](http://wbec-ridderkerk.nl/html/UCIProtocol.html), so it works with any GUI that accepts custom engines especified with the UCI Protocol.

## Implementations

The following are some design/implementation decisions made:

### Processing Model

The search can be done sequential or can be parallel, in the parallel approach, is created a pool of processes.

### Move generation

To generate moves is created a function that return a python generator, where the moves are computed on demand, this is useful because when some nodes are cutted-off the remaining moves aren't calculated.

### Board Representation

To represent the board is used a square-centric approach, where the board is an array with 64 integer values, where each integer represent a colored piece or an empty square.

### Evaluation

The evaluation function is purely material-based, which use the standard weights:

 - Pawn: 1
 - Bishop: 3
 - Knight: 3
 - Rook: 5
 - Queen: 9

## Usage

To use the engine you need to install an GUI's that supports the UCI Protocol to communicate with the engine. 

After installing a GUI, access the `src/settings.py` file and change the values to your preference. Also, you need figure out how to add a custom engine in your GUI, by doing that add the engine main file path: `main.py`.

The recommended GUI is [jerry](https://github.com/asdfjkl/jerry) because the engines were tested using this GUI. However, soon all the UCI commands will be implemented to allow the engine to work with all UCI GUI's.

## TODO

The project was developed as a learning proposal, so some features to turn this software useful are needed to be implemented. The following list some of them:

 - Add support to castle movement.
 - Add support to *En Passant* movement.
 - Currently is supported pawn promotion to queen and knight. Is needed to add support to rook and bishop promotion.
 - The depth of the search is a fixed constant. however, the value must be set dynamically by communicating with the GUI interface, this is useful for supporting diferent time formats: classical, blitz, bullet and so on.
 - Implement all commands/responses used in the UCI protocol.

## References

 - NORVIG, P.; RUSSELL, S. Inteligência Artificial. Elsevier, 3a ed., 2013.
 - [Board representation - Chess Programming ](https://www.chessprogramming.org/Board_Representation)
 - [Move generation - Chess Programming ](https://www.chessprogramming.org/Move_Generation)
 - [Python Generators](https://www.geeksforgeeks.org/generators-in-python/)

## Contributing

As shown in [TODO](#TODO) section, there is a lot of work to complete, I am open to accepting pull requests implementing some of these features. 

## License

Released under the MIT License. See [LICENSE.md](/LICENSE) for details.
