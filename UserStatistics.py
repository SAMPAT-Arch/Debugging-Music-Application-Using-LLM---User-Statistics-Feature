class UserStatistics:
    def __init__(self):
        # Initialize the data structures for storing song data, genres, and artists
        self.songs = []       # List of all songs played
        self.genres = {}      # Dictionary to store genre frequencies
        self.artists = {}     # Dictionary to store artist frequencies

    def add_song(self, song, genre, artist):
        """
        Adds a song to the statistics.
        Updates the song, genre, and artist data.
        
        :param song: The song's name
        :param genre: The genre of the song
        :param artist: The artist of the song
        """
        self.songs.append(song)
        self.genres[genre] = self.genres.get(genre, 0) + 1
        self.artists[artist] = self.artists.get(artist, 0) + 1

    def most_listened_songs(self):
        """
        Returns a sorted list of songs, ordered by how many times they've been played.
        """
        song_counts = {}
        for song in self.songs:
            song_counts[song] = song_counts.get(song, 0) + 1
        return sorted(song_counts.items(), key=lambda x: x[1], reverse=True)

    def favorite_genres(self):
        """
        Returns the genres, sorted by the number of times they've been played.
        """
        return sorted(self.genres.items(), key=lambda x: x[1], reverse=True)

    def favorite_artists(self):
        """
        Returns the artists, sorted by the number of times their songs have been played.
        """
        return sorted(self.artists.items(), key=lambda x: x[1], reverse=True)

    def display_statistics(self, top_n=5):
        """
        Displays the user's most-listened songs, favorite genres, and favorite artists.
        
        :param top_n: The number of top entries to display (default is 5)
        """
        print("Top Most Listened Songs:")
        for song, count in self.most_listened_songs()[:top_n]:
            print(f"- {song}: {count} listens")

        print("\nTop Favorite Genres:")
        for genre, count in self.favorite_genres()[:top_n]:
            print(f"- {genre}: {count} listens")

        print("\nTop Favorite Artists:")
        for artist, count in self.favorite_artists()[:top_n]:
            print(f"- {artist}: {count} listens")

# Example usage of the UserStatistics class:

if __name__ == "__main__":
    # Create an instance of UserStatistics
    user_stats = UserStatistics()

    # Add some songs
    user_stats.add_song("Song A", "Pop", "Artist 1")
    user_stats.add_song("Song B", "Rock", "Artist 2")
    user_stats.add_song("Song C", "Pop", "Artist 1")
    user_stats.add_song("Song D", "Jazz", "Artist 3")
    user_stats.add_song("Song E", "Pop", "Artist 1")
    user_stats.add_song("Song F", "Rock", "Artist 2")

    # Display the statistics for the user
    user_stats.display_statistics(top_n=3)
