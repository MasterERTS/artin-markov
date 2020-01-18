# Markov Decision Processes 

<p align="center">
<img src="https://raw.githubusercontent.com/master-coro/artin-markov/master/res/mdp.png">
</p>
The number in each tile represents the immediate reward obtained when moving to it. The black tiles are walls.

The tiles with rewards +1 and −1 are terminal nodes : when the robot reaches them it can never move again. Hence, the utility for these tiles(from iteration 1 on) is just the immediate reward. 
 
We assume that each time the robot tries to move in one direction, there is a 10% chance that it goes left (relatively to the direction chosen) instead of straight ahead and 10% chance it goes right (still relative). If this makes it go into a wall, it just stays put (does not move).

Run :
```python src/main.py```

That will give you the final utilities and the number of iterations it took to compute them. You can tweak the parameters and the map in lib/world.py and use your own map.

