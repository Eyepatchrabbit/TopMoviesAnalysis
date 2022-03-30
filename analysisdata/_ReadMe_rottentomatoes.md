# Investigate top movies on RottenTomatoes

Is the same as on imdb, but now a different site to see if there might be a difference in data

Entrypoint; https://www.rottentomatoes.com/top/bestofrt/

EXTRA: can use "https://www.rottentomatoes.com/top/bestofrt/?year=2021" to see possible evolution of movies?  
=>select top 10 movies for each year and then see what the evolution is of
* average/max score   
* number of reviews
* genres


#Questions to answer
1. With x==years and y==rating ->is there an increase in the quality of films over time? ( )
1. Does the runtime affect the rating?=> do longer movies have higher scores? (more exposition vs to long) ( )
1. Is there a cutoff in time => is there a length at which scores go down ( )
1. Which genres are the most in the top 250 of cases  ( )
1. Which genre has highest average score => drama action or crime ( )
1. Is there a change in movie genre over time ->to be seen how best to find this out (maybe for each decade?)
1. Does a director come up multiple times => if so who are most prominent? ( )
1. which languages are most spoken in the movies in top 250 =>would expect english to make 75% ( )
1. From which "country" do most of the cases come from? => would think most from USA??
1. Average Rating for the different countries? 
1. Which actor played in most of the movies in the list?

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

