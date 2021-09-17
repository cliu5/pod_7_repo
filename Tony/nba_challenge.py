print("Challenge 2.1:")
jm3 = 46
# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
fvv3 = 43
# TODO: Create variable here for number of 3 pt shots made by James Harden
jh3 = 37

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jm3} 3 point shots")
# TODO: Create print statement here for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fvv3} 3 point shots")
# TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, James Harden made {jh3} 3 point shots")
print()

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
jm3a = 93
# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
fvv3a = 110
# TODO: Create variable here for number of 3 pt shot attempts by James Harden
jh3a = 109
print()

print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
print(f"In the 2020 NBA playoffs, Jamal Murray made {jm3} 3 point shots and {jm3a} shot attempts")
# TODO: Create print statement here for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fvv3} 3 point shots and {fvv3a} shot attempts")
# TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, James Harden made {jh3} 3 point shotsand {jh3a} shot attempts")
print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3 point percentage for Jamal Murray
print(f"In the 2020 NBA playoffs, Jamal Murray had a 3 point success rate of {jm3 / jm3a}")
# TODO: Calculate and print the 3 point percentage for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred VanVleet had a 3 point success rate of {fvv3 / fvv3a}")
# TODO: Calculate and print the 3 point percentage for James Harden
print(f"In the 2020 NBA playoffs, James Harden had a \ 3 point success rate of {jh3 / jh3a}")
print()

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line

paragraph = "The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \n\
They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \n\
Those three have made good developments with the Pelicans, especially Brandon Ingram. \n\
But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \n\
Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \n\
The Lakers ended the season atop the Western Conference with a record of 49-14. \n\
They were narrowly behind the Bucks for the best record in the league. \n\
Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \n\
Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season."

print(paragraph)


print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, print out the paragraph with only 1 sentence per line, and all in upper case

print(paragraph.upper())

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
# TODO: print out the variable in an f-string to convey your opinion on the lakers

lakers_are_the_best = False
print(lakers_are_the_best)

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
print(int(lakers_are_the_best))

# TODO: Convert your `lakers_are best` variable to a float, and print it out
print(float(lakers_are_the_best))

print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
print(str(jm3 / jm3a))
print(str(fvv3 / fvv3a))
print(str(jh3 / jh3a))

# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
print(int(jm3 / jm3a))
print(int(fvv3 / fvv3a))
print(int(jh3 / jh3a))
