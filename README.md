# Snake

# Description
Simple classic Snake written in Python's pygame and PyQt5 in which you may either play or watch the game being played by bot.
Bot's algorithm generates Hamilton's cycle (a path that goes through each field exactly once and ends where it started) on the game board and checks if the snake can take a shortcut on its path (the condition is that the snake must be shorter than a number of skipped fields). Normal snake's rules apply. The bot's winning chance is 100%. The cycle is different every time.

# Main menu:
![obraz](https://github.com/mikolajWasik/snake/assets/96197911/7526ea2f-3c41-405b-8012-3d234cda4afc)

Scores are stored in a .txt file.

# Game screen:
![obraz](https://github.com/mikolajWasik/snake/assets/96197911/9a9c0811-9d78-4661-97d5-3a5595f3a8b5)

![obraz](https://github.com/mikolajWasik/snake/assets/96197911/62dcf542-32d0-49d7-a565-ef3fd2d25624)

# Bot's play:
Early stage:

![obraz](https://github.com/mikolajWasik/snake/assets/96197911/8c5a9a2f-3d04-4230-9f83-ffbd401e32c5)


Late stage:

![obraz](https://github.com/mikolajWasik/snake/assets/96197911/39a2f1d1-9a47-4eb2-a363-7e0d924d2603)

Bot almost stopped taking shortcuts because they were too dangerous. Max possible score is 2400 and then the snake occupies every board's tile.
