UNO Card Game (Group Project from Group 5)


ABOUT RULES:

DO NOT CLICK THE MOUSE ARBITRARILY, OR THERE WILL BE SOME MISTAKES. JUST FOLLOW THE RULES EXACTLY

1. When it is your turn, you should choose a card to discard and a card will join in your hand automatically

2. after 1., if there is a card that can be played, you must play it. If there is not, click your card area, and there will be a card joining your hand card and if it can be played, it played automatically as well.

3. after doing 1. & 2., when there are 2 cards left in your hand, and one of them can be played, you should click it to play and click UNO button before clicking ¡Ì button (which means to end turn). If not, you will get a panelty card

4. There is also a emoji button beside, but do not send emoji between 1. & 2. , you can click it before 1. or after 2.


ABOUT REFERENCE:

1. AI_action.py:
   1) from line 55 to 89, get thought from https://www.youtube.com/watch?v=7BXDcBfk-04, but composed by self
   2) reference to PY-UNO-master\AI_card_logic.py and simplify it but not that advanced, we composed that AI-players discard cards and get card and preferentially discard '+2','skip','reverse' and then '+4','wild' and finally numbercard
   
   
2. driver.py:
   1) get structures from https://www.youtube.com/watch?v=cVX7hR3bX7A&t=1652s£¬https://www.youtube.com/watch?v=-Y2YIEhU75M&t=2003s and chatGPT£¬ but details and functions are composed by group members
   2£©code MOUSECLICK struture rewrite from chatGPT and https://github.com/Rutvik-C/UNO.git
   3) code 241-281 refer from https://github.com/Rutvik-C/UNO.git
   
3.classes.py:
   Classes rewrite from https://github.com/Rutvik-C/UNO.git
   
ABOUT FUNCTIONS(except new rules):

1. We created an emoji button, and player can send emoji during playing, which means increase the interaction between player and computer

2. Our scoreboard has "play again" button that can quickly return the start screen

3. Our "UNO" voice is recorded by our group member

4. A new interface is added at the beginning. Each player draws a new card, and then decides the playing order by comparing the card numbers

ON FAILED AND SUCCESSFUL ATTEMPTS:

1. We initially wanted to include a conversation function, but later changed it to send emoticons

2. We tried to create a Card class, a Player class, a FuncCard class and a NumCard class, but due to various problems with the coupling process we decided to split these parts into player_function and deck, but still achieve the same functionality

3. For the leaderboard, we animated it and were able to land the uno icon consistently on the interface, but had problems with the actual display. The scoreboard UI is misaligned and the "Quit" button does not work
