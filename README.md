## Code Challenge: Jumping on the Clouds
A player can jump on any cloud having a number that is equal to the number of the current cloud plus `1` or `2`. Player gets an array of clouds numbered `0` if they are safe or `1` if they must be avoided. Determine the minimum number of jumps it will take to jump from starting position to the last cloud, avoiding the unsafe clouds. It is always possible to win.

**Notes:** 
For example, `c = [0,1,0,0,0,1,0]` indexed from `0...6`. The number on each cloud is its index in the list so she must avoid the clouds at indexes `1` and `5`. Player could follow the following 2 paths: `0 --> 2 --> 4 --> 6` or `0 --> 2 --> 3 --> 4 --> 6`. The first path takes `3` jumps while the second takes `4`. 

Return the minimum number of jumps required, as an integer

#### Example 1:
```
Input: 7, [0, 0, 1, 0, 0, 1, 0]
Output: 4
```

**Explanation:** 
Player must avoid c[2] and c[5], can win the game with a minimum of `4` jumps.


Source: HackerRank
