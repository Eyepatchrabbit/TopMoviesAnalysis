# Investigate top 250 movies on IMDB
This is just a personal project to get myself into programming after hours. Personally thought it would be fun to analyse the data contained on the IMDB website containing the top 250 movies

## The questions I came up with:

1. With x==years and y==rating ->is there an increase in the quality of films over time? (V)
1. Does the runtime affect the rating?=> do longer movies have higher scores? (more exposition vs to long) (V)
1. Is there a cutoff in time => is there a length at which scores go down (V)
1. Which genres are the most in the top 250 of cases  (V)
1. Which genre has highest average score => drama action or crime (V)
1. Is there a change in movie genre over time ->to be seen how best to find this out (maybe for each decade?)
1. Does a director come up multiple times => if so who are most prominent? (V)
1. which languages are most spoken in the movies in top 250 =>would expect english to make 75% (V)
1. From which "country" do most of the cases come from? => would think most from USA?? (V)
1. Average Rating for the different countries? (V)
1. Is there a difference in number of reviews for each country
1. Which actor played in most of the movies in the list? ()
1. When did movies come out => in what month? (considering can be different dependent on country, see what would like to get out of it)

## data to collect
1. ranking
1. name
1. releaseYear
1. rating
1. genres
1. durationminutes
1. directors
1. countries
1. languages
1. actor
1. reviews

## From what I see in the data:  

### With x==years and y==rating ->is there an increase in the quality of films over time?
It indeed seems that the bulk of the movies in the 250 list are from after the 1990's. 
(?see review of movies globally ->are old movies more reviewed then older once?)

The most presented year is 1995 with 8 movies. This is followed by 2004 that has 7 movies. The years 1957, 2003, 2009 and 2019 have shared place on 3th with 6 movies.  
Movies of 1995:  
1. Se7en
1. The Usual Suspects
1. Braveheart
1. Toy Story
1. Heat
1. Casino
1. Before Sunrise
1. La haine

Movies of 2004:  
1. Eternal Sunshine of the Spotless Mind
1. Der Untergang
1. Hauru no ugoku shiro
1. Million Dollar Baby
1. Hotel Rwanda
1. The Incredibles
1. Before Sunset

If average out the ratings for each year we see that 1972 has highest value with 9.2. This year has just 1 movie: "The Godfather".  
=>todo; see what is highest movie in year (maybe this can show something new)


### Is it possible that the ranking is related to the number of reviews
It seems that the bulk  of the reviews are movies after 1970. Also  there seems a trend that the higher in rank, the more reviews there are.  
Most Reviewed movie: The Shawshank Redemption (rank 1), 2560535 reviews
Least reviewed movie:  Dersu Uzala (rank 228), 27639 reviews
 


### Does the runtime affect the rating?=> do longer movies have higher scores? (more exposition vs to long)
There is only a verry small correlation between runtime and a higher ranking. 
Seems that most of the movies do have a runtime around the 2h mark (average=129 minutes)

Longest movie in top250: Gone with the Wind (rank 157), 238 minutes  
Shortest movie in top250: Sherlock Jr. (rank 193), 45 minutes  

So seems there is no "cutoff-time"


### Examine genres
It seems that the most occurring genre is Drama with 182 movies (72.8%).  
The far following second place is Adventure (60 cases which is 24% of all)

Overview:
1. Drama: 182    72.8%
1. Adventure: 60    24.0%
1. Thriller: 54    21.6%
1. Crime: 51    20.4%
1. Action: 49    19.6%
1. Comedy: 48    19.2%
1. Mystery: 36    14.4%
1. War: 33    13.2%
1. Fantasy: 31    12.4%
1. Romance: 30    12.0%
1. Biography: 29    11.6%
1. Family: 28    11.2%
1. Sci-Fi: 27    10.8%
1. Animation: 23     9.2%
1. History: 13     5.2%
1. Western: 8     3.2%
1. Sport: 8     3.2%
1. Musical: 7     2.8%
1. Music: 6     2.4%
1. Horror: 5     2.0%
1. Film-Noir: 4     1.6%


### director
The top 1 spot of most appearing director is shared by following 5 persons with each 7 movies:
1. Steven Spielberg 
    * Schindler's List
    * Saving Private Ryan
    * Raiders of the Lost Ark
    * Indiana Jones and the Last Crusade
    * Jurassic Park
    * Catch Me If You Can
    * Jaws
1. Stanley Kubrick 
    * The Shining
    * Paths of Glory
    * Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb
    * 2001: A Space Odyssey
    * A Clockwork Orange
    * Full Metal Jacket
    * Barry Lyndon
1. Martin Scorsese 
    * Goodfellas
    * The Departed
    * Taxi Driver
    * The Wolf of Wall Street
    * Casino
    * Shutter Island
    * Raging Bull
1. Christopher Nolan 
    * The Dark Knight
    * Inception
    * Interstellar
    * The Prestige
    * Memento
    * The Dark Knight Rises
    * Batman Begins
1  Akira Kurosawa
    * Shichinin no samurai
    * Tengoku to jigoku
    * Ikiru
    * Ran
    * Yôjinbô
    * Rashômon
    * Dersu Uzala

### Languages
It seems that English is the most spoken language in the movielist with 214 movies (85.6%). French is far below the second with 18.8% and German on 3th with 14.8%. 

1. English: 214, 85.6%
1. French:  47, 18.8%
1. German:  37, 14.8%
1. Spanish:  28, 11.2%
1. Japanese:  24,  9.6%
1. Italian:  23,  9.2%
1. Latin:  16,  6.4%
1. Russian:  14,  5.6%
1. Arabic:   9,  3.6%


### country
Seems that the most prominent country is "United States", followed by the "United Kingdom"

1.	United States 187 (74.8%) - avg: 8.27 max: 9.2 min: 8.0
2.	United Kingdom 46 (18.4%) - avg: 8.22 max: 9.0 min: 8.0
3.	France 20 (8.0%) - avg: 8.25 max: 8.6 min: 8.0
4.	Japan 15 (6.0%) - avg: 8.27 max: 8.6 min: 8.0
5.	Germany 13 (5.2%) - avg: 8.34 max: 8.8 min: 8.1
6.	Italy 11 (4.4%) - avg: 8.31 max: 8.8 min: 8.0
7.	Spain 7 (2.8%) - avg: 8.24 max: 8.8 min: 8.1
8.	India 6 (2.4%) - avg: 8.17 max: 8.3 min: 8.0
9.	Canada 6 (2.4%) - avg: 8.22 max: 8.6 min: 8.0
10.	Australia 6 (2.4%) - avg: 8.22 max: 8.7 min: 8.1

### Actors
It seems that the most prominent actor is "Robert De Niro" with 9 movies. He is followed on shared second place with 7 movies by: "Morgan Freeman", "John Ratzenberger" and "Harrison Ford"

Showing actors who played in more then 4 movies on the Top250 list: 
1.	Robert De Niro 9 (3.6%)
2.	Morgan Freeman 7 (2.8%)
3.	John Ratzenberger 7 (2.8%)
4.	Harrison Ford 7 (2.8%)
5.	Tom Hanks 6 (2.4%)
6.	Michael Caine 6 (2.4%)
7.	Leonardo DiCaprio 6 (2.4%)
8.	Christian Bale 6 (2.4%)
9.	Takashi Shimura 5 (2.0%)
10.	Robert Duvall 5 (2.0%)
11.	Mark Ruffalo 5 (2.0%)
12.	Clint Eastwood 5 (2.0%)
13.	Charles Chaplin 5 (2.0%)
14.	Brad Pitt 5 (2.0%)
15.	Alec Guinness 5 (2.0%)

Process finished with exit code 0


Movies with "Robert De Niro":
1. The Godfather: Part II
1. Goodfellas
1. Joker
1. Once Upon a Time in America
1. Taxi Driver
1. Heat
1. Casino
1. Raging Bull
1. The Deer Hunter

extra: John Ratzenberger seems to be usualy playing minor characters in movies and series:
1. WALL·E
1. Toy Story
1. Toy Story 3
1. Up
1. Inside Out
1. Monsters, Inc.
1. Ratatouille


### Box Office
It seems that there isn't a big correlation between the rank and ROI/initial Budget. A stronger positive link exists between ROI and budget with releaseYear


Finding movies in top250 with lowest budget
	1) Blade Runner	           [174] budget= 1.0	 return= 41722423.0
	2) Ladri di biciclette	 [120] budget= 133000.0	 return= 303655.0
	3) Bacheha-Ye aseman	 [178] budget= 180000.0	 return= 753933.0
	4) Rashômon	 [149] budget= 250000.0	 return= -203192.0
	5) Monty Python and the Holy Grail	 [142] budget= 303039.0	 return= 1637867.0
	6) Jodaeiye Nader az Simin	 [118] budget= 500000.0	 return= 22426076.0
	7) Per qualche dollaro in più	 [125] budget= 600000.0	 return= 14400000.0
	8) La battaglia di Algeri	 [234] budget= 800000.0	 return= 162002.0
	9) Psycho	 [32] budget= 806947.0	 return= 31234984.0
	10) Citizen Kane	 [93] budget= 839727.0	 return= 805406.0
Finding movies in top250 with Highest budget
	1) Avengers: Endgame	 [79] budget= 356000000.0	 return= 2441501328.0
	2) Avengers: Infinity War	 [63] budget= 321000000.0	 return= 1727359754.0
	3) The Dark Knight Rises	 [68] budget= 250000000.0	 return= 831153097.0
	4) Spider-Man: No Way Home	 [67] budget= 200000000.0	 return= 1685588139.0
	5) Toy Story 3	 [83] budget= 200000000.0	 return= 866970811.0
	6) The Dark Knight	 [3] budget= 185000000.0	 return= 821102277.0
	7) WALL·E	 [57] budget= 180000000.0	 return= 341311890.0
	8) Inside Out	 [159] budget= 175000000.0	 return= 683848019.0
	9) Coco	 [76] budget= 175000000.0	 return= 632817888.0
	10) Up	 [110] budget= 175000000.0	 return= 560099102.0
Finding movies in top250 with lowest ROI
	1) Once Upon a Time in America	 [81] budget= 30000000.0	 return= -24526663.0
	2) Ran	 [139] budget= 11500000.0	 return= -7335717.0
	3) Das Boot	 [78] budget= 17971584.0	 return= -6483908.0
	4) Hotaru no haka	 [48] budget= 3700000.0	 return= -3183038.0
	5) North by Northwest	 [97] budget= 3101000.0	 return= -2958681.0
	6) La haine	 [244] budget= 2849000.0	 return= -2436086.0
	7) Metropolis	 [119] budget= 3369672.0	 return= -2019961.0
	8) Mr. Smith Goes to Washington	 [190] budget= 1900000.0	 return= -1755262.0
	9) Warrior	 [168] budget= 25000000.0	 return= -1691385.0
	10) Salinui chueok	 [196] budget= 2800000.0	 return= -1633283.0
Finding movies in top250 with Highest ROI
	1) Avengers: Endgame	 [79] budget= 356000000.0	 return= 2441501328.0
	2) Avengers: Infinity War	 [63] budget= 321000000.0	 return= 1727359754.0
	3) Spider-Man: No Way Home	 [67] budget= 200000000.0	 return= 1685588139.0
	4) Harry Potter and the Deathly Hallows: Part 2	 [179] budget= 125000000.0	 return= 1217359942.0
	5) The Lord of the Rings: The Return of the King	 [7] budget= 94000000.0	 return= 1052436214.0
	6) Jurassic Park	 [150] budget= 63000000.0	 return= 1036428303.0
	7) Joker	 [70] budget= 55000000.0	 return= 1019445730.0
	8) The Lion King	 [36] budget= 45000000.0	 return= 1018611805.0
	9) Toy Story 3	 [83] budget= 200000000.0	 return= 866970811.0
	10) The Lord of the Rings: The Two Towers	 [14] budget= 94000000.0	 return= 853896241.0