class UserStatistics:
    def __init__(self):
        self.songs = []
        self.genres = {}
        self.artists = {}

    def add_song(self, song, genre, artist):
        self.songs.append(song)
        self.genres[genre] = self.genres.get(genre, 0) + 1
        self.artists[artist] = self.artists.get(artist, 0) + 1

    def most_listened_songs(self):
        song_counts = {}
        for song in self.songs:
            song_counts[song] = song_counts.get(song, 0) + 1
        return sorted(song_counts.items(), key=lambda x: x[1], reverse=True)

    def favorite_genres(self):
        return sorted(self.genres.items(), key=lambda x: x[1], reverse=True)

    def favorite_artists(self):
        return sorted(self.artists.items(), key=lambda x: x[1], reverse=True)

    def display_statistics(self, top_n=5):
        print("Top Most Listened Songs:")
        for song, count in self.most_listened_songs()[:top_n]:
            print(f"- {song}: {count} listens")

        print("\nTop Favorite Genres:")
        for genre, count in self.favorite_genres()[:top_n]:
            print(f"- {genre}: {count} listens")

        print("\nTop Favorite Artists:")
        for artist, count in self.favorite_artists()[:top_n]:
            print(f"- {artist}: {count} listens")
