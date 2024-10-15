import eyed3

def read_audio_file_metadata(file_path):
    audio_file = eyed3.load(file_path)
    print("Title:", audio_file.tag.title)
    print("Artist:", audio_file.tag.artist)
    print("Album:", audio_file.tag.album)
    print("Genre:", audio_file.tag.genre)

# Example usage:
read_audio_file_metadata('song.mp3')