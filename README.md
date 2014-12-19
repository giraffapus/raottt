# Random Acts Of Tic Tac Toe

A modified version of Tic Tac Toe (Noughts and Crosses, Xs and Os) where each
player only gets 3 pieces. Once a player has placed all pieces on the board,
subsequent moves are made by moving a piece to an empty spot. Thus, the game
continues on and could -- in theory -- go on forever.

As an added twist, each piece can only remain in the same spot for 5 rounds.
Once the time is up the player is forces to move that piece. This ensure a
player does not occupy the center spot for the entire game, and adds another
dimension for the player to consider.

![Simple Console Game](../screenshots/raottt.png)

### To Install
```bash
$ git clone https://github.com/giraffapus/raottt.git
$ cd raottt
$ pip install -r requirements.txt
```

### To Play

Computer vs Computer (just sit back and relax ...)
```bash
$ ./play --show
```

Human vs Computer (if you want to join ...)
```bash
$ ./play --blue=Human --red=Computer --show
```
