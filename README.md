# 🐼♟️ pandinha-engine

Pandinha-engine is a chess engine that use [MinMax Algorithm](https://en.wikipedia.org/wiki/Minimax) and [Alpha–beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) to search moves.

The engine follows the [UCI Protocol](http://wbec-ridderkerk.nl/html/UCIProtocol.html), so it works with any GUI that accepts custom engines especified with the UCI Protocol.

# Screenshots

![human vs IA](/assets/playing.gif)

# Especification

## Evaluation

The evaluation function is purely material-based, which use the standard weights:

 - Pawn: 1
 - Bishop: 3
 - Knight: 3
 - Rook: 5
 - Queen: 9

## GUI's

The recommended GUI is [jerry](https://github.com/asdfjkl/jerry) because the engines were tested using this GUI. However, soon all the UCI commands will be implemented to allow the engine to work with all UCI GUI's.

# References

 - NORVIG, P.; RUSSELL, S. Inteligência Artificial. Elsevier, 3a ed., 2013.
