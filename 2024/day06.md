# Day 6: Guard Gallivant
Our input is a 2d map of obstacles # and a guard with direction ^
This is very common puzzle and should probably make a generalized parser
He goes forward until he hits an obstacle and then we turns 90 degrees to the right

## Part 1
In part 1 we need to find all the coordinates he is on before going outside
I am thinking enum for direction and struct for movement

## Part 2
In part 2 we need to multiply the numbers on the left side with how many of them are on the right
This can be done with a hashmap.
The most effecient is probably looping over each N + M and with space equal to M
