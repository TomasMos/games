# Tic-tac-toe

## The algorithm employed is minimax with alpha-beta pruning (similar to Monte Carlo), to recursively iterate throuh all possible outcomes of each move. On the frontend, pygame is used to create the graphics and GUI. The backend enables a human to make moves and calculates the optimum move for an AI to play. 


### Gamplay

#### This is the home page, where a human can choose to play as X or O, if one chooses O they play second, X goes first.

![Home Page](https://raw.githubusercontent.com/TomasMos/tictactoe/main/Home.PNG)

#### I chose to play as X and the AI chose the top left corner cell as O.

![Play as X](https://raw.githubusercontent.com/TomasMos/tictactoe/main/X_1.PNG)

#### After I played a series of suboptimal moves, the AI has won.

![Make suboptimal moves, the AI will win](https://raw.githubusercontent.com/TomasMos/tictactoe/main/X_win.PNG)

#### This is the AI playing as X.

![Play as O](https://raw.githubusercontent.com/TomasMos/tictactoe/main/O_1.PNG)

#### The AI has cornered me with a catch-22, where I cannot prevent losing as there are two winning moves for the AI.

![The AI has cornered me with a catch-22](https://raw.githubusercontent.com/TomasMos/tictactoe/main/O_2.PNG)

#### The AI wins again.

![The AI has won](https://raw.githubusercontent.com/TomasMos/tictactoe/main/O_win.PNG)
