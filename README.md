# python-maze-game [MAY BE BUGGED & UNPLAYABLE]

## Descryption
This is a simple maze game made with python. You are playing as a red character in a black and white maze. Your task is to find the exit.

## Requirements
- Python: 3.10 or newer
- Packages (install with `pip3 install <package_name>`): [pygame](https://pypi.org/project/pygame/)

## Changelog
### #0.0.2 beta
- Game "released". Still has many bugs [UNPLAYABLE!]
### #0.0.3 beta
- Game is still unplayable :3
- Minor code maintenance
- Removed everything related to player's view radius / field of view [FOV]. It will be added back later
- *!NERD WARNING!* Changed `__global_data__.GAME["BOUNDS"]` from list[int] to int type, now you cannot set different height and width for the game
### #0.0.4 beta ~~(code will be updated a bit later than the changelog)~~ REVERTED
### #0.0.4 beta
- Made the player rendering position more accurate to the actual position
- Fixed the maze borders rendering bug (right and bottom borders would not render properly before)
- Found an issue where the game traps you in the entrance area or makes it unable to reach the exit. Sadly this cannot be fixed, and you have to restart the program if you come across this issue
- Added an exit generation algorithm...
- Added a collision handler (not the perfect one)...
- So the game is finally playable!
- Added a congratulation text when the maze is beaten
- Player speed is now tied up to the unit size. That's a temporary measure made for the collision handler to work
### #0.0.4.1 beta
- Minor code maintenance
- *!NERD WARNING!* `__global_data__.GAME["BOUNDS"]` will never be a list[int] again. FOV and/or view radius though are going to be added soon:tm:
- Added a proper congratulation for beating the maze
- Commented the `__global_data__` file as it's used as game configuration file. You can now change some variables here
### #0.0.4.2 beta
- Minor code maintenance
### #0.0.4.3 beta
- Minor code maintenance
### #0.0.5 beta
- Added main menu
- Added "Quit" and "Play" buttons to main menu
- Added cursor rendering for main menu
- **!IMPORTANT! Buttons are a bit bugged and will be reworked soon:tm:**
### #0.0.5.1 beta
- Added a "Try again" button to the congratulation screen (doesn't work properly yet, will be fixed in #0.0.5.1 beta)
- *!NERD WARNING!* Added an IS_RENDERED_ON parameter for buttons
- Made it so if you are trapped, you can just press [+] to get back to main menu
- Please, do not change anything in the files (including `__global_data__` and `__game_initialisation__`)
### #0.0.5.2 beta
- Reworked the buttons
- Made the code much more readable.
- Reworked the project structure
_ "Try again" button is now "Retry". It's still not working correctly though

## Features to be added:
- Player speed is now tied up to the unit size. That's a temporary measure made for the collision handler to work (message from #0.0.4 beta changelog)
- FOV and/or view radius though are going to be added soon:tm: (removed in #0.0.3 beta, message from #0.0.4.1 beta changelog)

## Credits:
- [@xsafter](https://github.com/xsafter) - Creating the [map generator algorithm](https://github.com/xsafter/map-generator) used in this game
- [@artkegor](https://github.com/artkegor) - game beta-versions testing
