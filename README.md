# Random NPC Generator

This project is closed. In the near feature I will publish [NPC Generator](https://github.com/ajwalkiewicz/NPC-Generator) which is a newest version of Random NPC Generator
Random NPC Generator is my own project that I did in order to learn Python. I am aware that there is a lot of mistakes. Variables naming convention is a big mess and there is a lot of spaghetti code. Some parts of code are totally not necessary others could have been written in a better way.

<p align="center">
  <img alt="Random NPC Generator " src="https://github.com/ajwalkiewicz/random-npc-generator/blob/master/program.png">
</p>

# Description

This program generates a non-player character for the tabletop RPG game named Call of Cthulhu (7th ed.).  So far only basic characteristics are available such as: name, last name, gender, occupation and other main traits listed in CoC game.
It is still missing character skills, even though some solutions has been implemented for that, but the issue occurs to be much more complicated than it seemed to be.

# Features

<p align="center">
  <img alt="Random NPC Generator " src="https://github.com/ajwalkiewicz/random-npc-generator/blob/master/description.png">
</p>

Left panel:
1.	Choose gender. There are 3 options: man, female, random.
2.	Choose occupation. So far are only 2 options available: random and optimal.
Random: occupation is randomly chosen from whole list of occupations.
Optimal: occupation is randomly chosen from the group of occupations that give the higher amount of occupation points.
3.	Generate: generate character and display it in a middle panel.
4.	Clear: clear character’s statistics from middle panel.

Middle panel: displays the generated character information’s

Right panel:

5. Save: does not work.
6. Exit: exit the program.

# Extra information’s

•	Man and woman first names are randomly chosen from the list of 200 most popular names given to babies from 1920. Separated for man a woman.
•	Las names are chosen from the list of 1000 most popular last names from 1990. Unfortunately, I could not find any older data.
