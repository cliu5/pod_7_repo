print("Challenge 2.1:")
jamal_murray_3pts_made = 46
# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
FV_3made = 43
# TODO: Create variable here for number of 3 pt shots made by James Harden
JH_3made = 37

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
# TODO: Create print statement here for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred VanVleet made {FV_3made} 3 point shots")
# TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, James Harden made {JH_3made} 3 point shots")

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
JM_3attempt = 93
# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
FV_3attempt = 110
# TODO: Create variable here for number of 3 pt shot attempts by James Harden
JH_3attempt = 109
print()

print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and {JM_3attempt} 3 point shot attempts.")

print(f"In the 2020 NBA playoffs, Fred VanVeleet made {FV_3made} 3 point shots and {FV_3attempt} 3 point shot attempts.")

print(f"In the 2020 NBA playoffs, James Harden made {JH_3made} 3 point shots and {JH_3attempt} 3 point shot attempts.")
print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
JM_3point_percentage = jamal_murray_3pts_made/JM_3attempt
FV_3point_percentage = FV_3made/FV_3attempt
JH_3point_percentage = JH_3made/JH_3attempt
# TODO: Calculate and print the 3 point percentage for Jamal Murray
print(f"Jamal Murray's 3 point percentage in the 2020 NBA playoffs was {JM_3point_percentage}")
# TODO: Calculate and print the 3 point percentage for Fred VanVleet
print(f"Fred VanVleet's 3 point percentage in the 2020 NBA playoffs was {JM_3point_percentage}")
# TODO: Calculate and print the 3 point percentage for James Harden
print(f"James Harden's 3 point percentage in the 2020 NBA playoffs was {JM_3point_percentage}")
print()

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line

print('The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\
\nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \
\nThose three have made good developments with the Pelicans, especially Brandon Ingram.\
\nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \
\nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \
\nThe Lakers ended the season atop the Western Conference with a record of 49-14. \
\nThey were narrowly behind the Bucks for the best record in the league. \
\nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \
\nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.')

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case

text = 'The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\
\nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \
\nThose three have made good developments with the Pelicans, especially Brandon Ingram.\
\nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \
\nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \
\nThe Lakers ended the season atop the Western Conference with a record of 49-14. \
\nThey were narrowly behind the Bucks for the best record in the league. \
\nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \
\nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.'

print(text.upper())

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
lakers_are_the_best = False
# TODO: print out the variable in an f-string to convey your opinion on the lakers
print(f"The Lakers being the best team is {lakers_are_the_best}. The Seattle Supersonics are the best!")

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
print(int(lakers_are_the_best))
# TODO: Convert your `lakers_are best` variable to a float, and print it out
print(float(lakers_are_the_best))

print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
print(str(JM_3point_percentage))
print(str(FV_3point_percentage))
print(str(JH_3point_percentage))

# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
print(int(JH_3point_percentage))
print(int(FV_3point_percentage))
print(int(JH_3point_percentage))