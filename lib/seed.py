from env import session, fake
from random import randint, sample
from models import Movie, Genre, MovieGenre, Actor, Cast, Fave, User

genres_data = [
    {'name': 'Action'},
    {'name': 'Adventure'},
    {'name': 'Comedy'},
    {'name': 'Drama'},
    {'name': 'Fantasy'}
]

actors_data = [
    {'name': 'Tom Hanks'},
    {'name': 'Leonardo DiCaprio'},
    {'name': 'Scarlett Johansson'},
    {'name': 'Meryl Streep'},
    {'name': 'Denzel Washington'},
    {'name': 'Brad Pitt'},
    {'name': 'Jennifer Lawrence'},
    {'name': 'Johnny Depp'},
    {'name': 'Natalie Portman'},
    {'name': 'Robert Downey Jr.'},
    {'name': 'Chris Evans'},
    {'name': 'Emma Stone'},
    {'name': 'Christian Bale'},
    {'name': 'Anne Hathaway'},
    {'name': 'Matt Damon'},
    {'name': 'Charlize Theron'},
    {'name': 'Will Smith'},
    {'name': 'Angelina Jolie'},
    {'name': 'Ryan Gosling'},
    {'name': 'Jessica Chastain'}
]

movies_data = [
    {'title': 'The Shawshank Redemption', 'plot': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', },
    {'title': 'Inception', 'plot': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.', },
    {'title': 'Forrest Gump', 'plot': 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.', },
    {'title': 'The Godfather', 'plot': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.', },
    {'title': 'The Dark Knight', 'plot': 'When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham. The Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.', },
    {'title': 'Pulp Fiction', 'plot': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.', },
    {'title': 'The Lord of the Rings: The Fellowship of the Ring', 'plot': 'A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.', },
    {'title': 'The Matrix', 'plot': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.', },
    {'title': 'Avatar', 'plot': 'A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.', },
    {'title': 'Jurassic Park', 'plot': 'During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok.', },
]


def create_movies(movies):
    for movie in movies:
        new_movie = Movie(**movie)
        session.add(new_movie)
    session.commit()

def create_genres(genres):
    for genre in genres:
        new_genre = Genre(**genre)
        session.add(new_genre)
    session.commit()

def create_actors(actors):
    for actor in actors:
        new_actor = Actor(**actor)
        session.add(new_actor)
    session.commit()

def create_movie_genres():
    movies = session.query(Movie).all()
    genres = session.query(Genre).all()

    for movie in movies:
        random_num = randint(1, randint(1,3))
        
        genres_sample = sample(genres, random_num)
        for genre in genres_sample:
            movie_genre = MovieGenre(movie_id=movie.id, genre_id=genre.id)
            session.add(movie_genre)
        
    session.commit()

def create_casts():
    movies = session.query(Movie).all()
    actors = session.query(Actor).all()

    for actor in actors:
        random_num = randint(1, randint(1,5))
        
        movies_sample = sample(movies, random_num)

        for movie in movies_sample:
            cast = Cast(movie_id=movie.id, actor_id=actor.id, role=fake.name())
            session.add(cast)
        
    session.commit()

def delete_all():
    session.query(Movie).delete()
    session.query(Genre).delete()
    session.query(MovieGenre).delete()
    session.query(Actor).delete()
    session.query(Cast).delete()


if __name__ == "__main__":
    delete_all()

    create_movies(movies_data)
    create_genres(genres_data)
    create_actors(actors_data)
    create_movie_genres()
    create_casts()

    print("✅ Seeding complete...")
