print("Challenge 2.1:")
jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37
print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020  NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jamal_murray_3pts_attmp = 93 
fred_vanvleet_3pts_attmp = 110
james_harden_3pts_attmp = 109

print("Challenge 2.4: Build on your print statement")
print(f"In the 2020 NBA playoffs, Jamal Murray attempted {jamal_murray_3pts_attmp} 3 point shots")
print(f"In the 2020  NBA playoffs, Fred VanVleet attempted {fred_vanvleet_3pts_attmp} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden attempted {james_harden_3pts_attmp} 3 point shots")

print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
jamal_murray_3pts_pct = round(46/93,3)*100
fred_vanvleet_3pts_pct = round(43/110,3)*100
james_harden_3pts_pct = round(james_harden_3pts_made/james_harden_3pts_attmp,3)*100 
print(f"In the 2020 NBA playoffs, Jamal Murray's 3 pt pct was {jamal_murray_3pts_pct}%")
print(f"In the 2020  NBA playoffs, Fred VanVleet's 3pt pct was {fred_vanvleet_3pts_pct}%")
print(f"In the 2020 NBA playoffs, James Harden's 3pt pct was {james_harden_3pts_pct}%")

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
lakers_string = "The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\n\
They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\n\
Those three have made good developments with the Pelicans, especially Brandon Ingram.\n\
But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\n\
Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\n\
The Lakers ended the season atop the Western Conference with a record of 49-14.\n\
They were narrowly behind the Bucks for the best record in the league.\n\
Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\n\
Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season."
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
print(lakers_string)# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
lakers_are_best = True
print(f"It is {lakers_are_best} that the Lakers are the best basketball team in the NBA")


print('Challenge 3.4: Type Conversion')
print(int(lakers_are_best))
print(float(lakers_are_best))

# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
# TODO: Convert your `lakers_are best` variable to a float, and print it out

print('Challenge 3.5: Type Conversion Part 2')
print(str(jamal_murray_3pts_pct))
print(str(fred_vanvleet_3pts_pct))
print(str(james_harden_3pts_pct))

print(int(jamal_murray_3pts_pct))
print(int(fred_vanvleet_3pts_pct)
print(int(james_harden_3pts_pct))


# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
