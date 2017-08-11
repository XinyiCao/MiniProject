import media
import fresh_tomatoes

dunkirk = media.Movie("Dunkirk",
                      "A movie which portrays the Dunkirk evacuation of the Second World War.",
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                      "https://www.youtube.com/watch?v=T7O7BtBnsG4")
print(dunkirk.storyline)

wolf_warrior = media.Movie("Wolf Warrior II",
                           "A story of a loose cannon Chinese soldier named Leng Feng who takes on special missions around the world.",
                           "https://upload.wikimedia.org/wikipedia/en/b/b5/Wolf_Warriors_2_poster.jpeg",
                           "https://www.youtube.com/watch?v=xmJFp1-AvV4")
print(wolf_warrior.storyline)

spider_man = media.Movie("Spider-Man: Homecoming",
                         "Peter Parker tries to balance high school life with being Spider-Man, while facing the Vulture.",
                         "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                         "https://www.youtube.com/watch?v=U0D3AOldjMU")
# spider_man.show_trailer()
print(spider_man.storyline)

wonder_woman = media.Movie("Wonder Woman: Rise of the Warrior",
                           "A story of Princess Diana, who grows up on the Amazon island of Themyscira.",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")
print(wonder_woman.storyline)

minion = media.Movie("Despicable Me 3",
                     "Gru teams up with his long lost twin brother Dru in order to defeat a new enemy named Balthazar Bratt, a 1980s child actor who grows up to become a villain.",
                     "https://upload.wikimedia.org/wikipedia/en/9/91/Despicable_Me_3_%282017%29_Teaser_Poster.jpg",
                     "https://www.youtube.com/watch?v=6DBi41reeF0")
print(minion.storyline)

flower = media.Movie("Time-Lapse photography: A Garden Come to Life",
                     "A blooming garden of dancing flowers in this incredible four-minute short film.",
                     "https://www.colorblends.com/img/media/prime/product/1010_Amazon_CGC2218q.jpg",
                     "htt"
                     "ps://www.youtube.com/watch?v=m6Uw2DJ9Md8")
print(flower.storyline)

movies = [dunkirk, wolf_warrior, spider_man, wonder_woman, minion, flower]

# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)