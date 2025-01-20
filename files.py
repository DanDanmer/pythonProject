# def are_files_equal(file1, file2):
#     with open(file1, 'r') as file1_object:
#         file1_content = file1_object.read()
#
#     with open(file2, 'r') as file2_object:
#         file2_content = file2_object.read()
#
#
#     return file1_content == file2_content
#
# result = are_files_equal(r"C:\Users\Daniel\Desktop\Archive - jobs, studying, work related\Python\vacation.txt", r'C:\Users\Daniel\Desktop\Archive - jobs, studying, work related\Python\file_test.txt')
# print(result)
from lists import longest


# def main():
#
#     file_path = input("Enter file path: ")
#     task = input("Enter task (rev, sort, last): ")
#
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#
#     if task == 'sort':
#
#         words = []
#         for line in lines:
#             words.extend(line.split())
#
#         unique_sorted_words = sorted(set(words))
#         print(unique_sorted_words)
#     elif task == 'rev':
#         for line in lines:
#             print(line.strip()[::-1])
#
#     elif task == "last":
#         n = int(input("Enter a number: "))
#         for line in lines[-n:]:
#             print(line.strip())
#
# if __name__ == "__main__":
#     main()

# COMMA = ", "
# dates = []
#
# try:
#     with open("harryPotterBooks.txt", "r") as books_input_file:
#         for row in books_input_file:
#             parts = row.strip().split(COMMA)
#             if len(parts) > 1:
#                 dates.append(parts[1])
#             else:
#                 print(f"Skipping row: {row.strip()} (Invalid format")
#
#     with open("harryPotterBooks.txt", "r") as dates_file:
#         dates_file.write("\n".join(dates))
#
#     print("Dates have been successfully written to harryPotterDates.txt.")
#
# except FileNotFoundError:
#     print("Error: The file harryPotterBooks.txt does not exist.")
#
# except Exception as e:
#     print(f"An error occurred: {e}")

# def copy_file_content(source, destination):
#     """
#     Copies the content of the source file to the destination file
#     :param source: Path to the source file
#     :param destination: Path to the destination file.
#     """
#
#     try:
#
#         with open(source, 'r') as src_file:
#             content = src_file.read()
#
#         with open(destination, 'w') as dest_file:
#             dest_file.write(content)
#
#         print(f"Content successfully copied from {source} to {destination}.")
#     except FileNotFoundError:
#         print(f"Error: The file {source} does not exist.")
#     except Exception as e:
#         print(f"An error occured : {e}")

# def who_is_missing(file_name):
#
#     with open(file_name, 'r') as file:
#         numbers = list(map(int, file.read().strip().split(',')))
#
#     n = max(numbers)
#     full_range = set(range(1, n + 1))
#     missing_number = list(full_range - set(numbers))[0]
#
#     with open('found.txt', 'w') as found_file:
#         found_file.write(str(missing_number))
#
#     return missing_number
#
# print(who_is_missing("findMe.txt"))

# def my_mp3_playlist(file_path):
#
#     with open(file_path, 'r') as file:
#         songs = file.readlines()
#
#     longest_song = ""
#     max_duration = 0
#     song_count = 0
#     artist_count = {}
#
#     for song in songs:
#         song = song.strip()
#         song_info = song.split(':')
#
#         song_name = song_info[0]
#         artist_name = song_info[1]
#         song_duration = song_info[2]
#
#         minutes, seconds = map(int, song_duration.split(':'))
#         total_seconds = minutes * 60 + seconds
#
#         if total_seconds > max_duration:
#             max_duration = total_seconds
#             longest_song = song_name
#
#
#         song_count += 1
#
#         if artist_name not in artist_count:
#             artist_count[artist_name] = 1
#         else:
#             artist_count[artist_name] += 1
#
#     most_frequent_artist = max(artist_count, key=artist_count.get)
#
#     return (longest_song, song_count, most_frequent_artist)


def my_mp4_playlist(file_path, new_song):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    while len(lines) < 3:
        lines.append("\n")

    parts = lines[2].strip().split(";")
    if len(parts) >= 3:
        parts[0] = new_song
        lines[2] = ";".join(parts) + ";\n"
    else:
        lines[2] = f"{new_song};Unknown;0:00;\n"

    with open(file_path, 'w') as file:
        file.writelines(lines)

    with open(file_path, 'r') as file:
        print(file.read())

