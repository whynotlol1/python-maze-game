# python-maze-game
### Requires python 3.10 or older to run

## Descryption
This is a simple maze game made with python. You are playing as a red character in a black and white maze. Your task is to find the exit.

## Changelog
### #0.0.2 beta
- Game "released". Still has many bugs [UNPLAYABLE!]
### #0.0.3 beta
- Game is still unplayable :3
- Minor code maintenance
- Removed everything related to player's view radius / field of view [FOV]. It will be added back later
- !NERD WARNING! Changed `__global_data__.GAME["BOUNDS"]` from list[int] to int type, now you cannot set different height and width for the game
### ~~#0.0.4 beta (code will be updated a bit later than the changelog)~~ REVERTED
~~- Made the player rendering position more accurate to the actual position~~
~~- Found an issue where the game traps you in the entrance area. Sadly this cannot be fixed and you have to restart the program if you come across this issue~~
~~- Added a collision handler (not the perfect one). Now the game is finally playable~~
~~- Player speed is now tied up to the unit size. That's a temporary measure made for the collision handler to work~~

## Credits:
- [@xsafter](https://github.com/xsafter) - Creating the [map generator algorithm](https://github.com/xsafter/map-generator) used in this game
- [@artkegor](https://github.com/artkegor) - game beta-versions testing
