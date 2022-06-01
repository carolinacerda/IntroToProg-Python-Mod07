# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with error handling, pickling
#              and storing data in a binary file
#              to create a program that recommends
#              music based on mood and allows new moods
#              and music to be added or removed
# ChangeLog (Who,When,What):
# CCerda, 05.31.2022, Created starting script
# CCerda, 06.01.2022, Modified code to complete assignment 07
# ---------------------------------------------------------------------------- #

import pickle

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
dict_row = {}  # A row of data separated into elements of a dictionary {Mood, Song, Artist}
lstSuggest = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing -------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def save_data_to_file(file_name, list_of_data):
        """ Saves data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_data: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        try:
            file = open(file_name, "wb")
            pickle.dump(list_of_data, file)
            file.close()
        except Exception as e:
            print("There was an error! Check file permissions.")
        return list_of_data

    @staticmethod
    def read_data_from_file(file_name, list_of_data):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_data: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "rb")
        while True:
            try:
                dict_row = pickle.load(file)
                for line in dict_row:
                    mood, song, artist = line["Mood"], line["Song"], line["Artist"]
                    row = {"Mood": mood.strip(), "Song": song.strip(), "Artist": artist.strip()}
                    list_of_data.append(row)
            except EOFError:
                break
            except Exception as e:
                print("There was a general error!")
                print(e, e.__doc__, type(e), sep="\n")
                break
        file.close()
        return list_of_data

    @staticmethod
    def recommend_data_from_list(mood, list_of_data):
        """ Retrieves data from a list of dictionary rows

        :param mood: (string) with name of mood:
        :param list_of_data: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        for row in list_of_data:
            if str(mood).lower() == str(row["Mood"]).lower():
                print("Since your mood today is ", "'", mood, "'", ", the song recommended for you is ", "'", str(row["Song"]).title(), "'", " by ", str(row["Artist"]).title(), sep="", end=".\n")
                print("\nHope you like it! ღゝ◡╹)ノ♥︎")
                break
            else:
                pass
        else:
            print("Sorry, there is no recommendation for the mood, ", "'", mood, "'", "! Please try again or select "
                                                                                      "'Option 3' to add a new "
                                                                                      "song recommendation for "
                                                                                      "this mood.", sep="")
        print()  # Add an extra line for looks
        return list_of_data

    @staticmethod
    def add_data_to_list(mood, song, artist, list_of_data):
        """ Adds data to a list of dictionary rows

        :param mood: (string) with name of mood:
        :param song: (string) with name of song:
        :param artist: (string) with name of artist:
        :param list_of_data: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        new_row = {"Mood": str(mood).strip(), "Song": str(song).strip(), "Artist": str(artist).strip()}
        list_of_data.append(new_row)
        return list_of_data

    @staticmethod
    def remove_data_from_list(mood, list_of_data):
        """ Removes data from a list of dictionary rows

                :param mood: (string) with name of mood:
                :param list_of_data: (list) you want filled with file data:
                :return: (list) of dictionary rows
                """
        try:
            for row in list_of_data:
                if mood.lower() == row["Mood"].lower():
                    list_of_data.remove(row)
                    print("  Song suggestion for the mood, ", "'", mood.title(), "'", ", was successfully removed!\n",
                          sep="")
                    break
                else:
                    pass
            else:
                print("  Sorry, the song suggestion for mood, ", "'", mood.title(), "'", ", could not be found. "
                                                                                         "Please try again.\n", sep="")
        except:
            print("An error has occurred!")
        return list_of_data


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print("""
                Welcome to the Mood Library!
This is a music library that recommends a song to you based on your mood.
   Below is a menu of options from which you can choose from. Enjoy!
            """)
        print('''
        Menu of Options
        1) View Current Music Library
        2) Get a Song Suggestion Based on Your Mood
        3) Add a Song for a Mood
        4) Remove a Mood and its Song
        5) Save Changes to Library        
        6) Exit Program''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Please choose an option [1 to 6]: ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_moods_in_list(list_of_data):
        """ Shows the current song suggestions for moods in the list of dictionaries rows

        :param list_of_data: (list) of rows you want to display
        :return: nothing
        """
        try:
            if int(len(list_of_data)) > 0:
                print("------------- YOUR MUSIC LIBRARY ---------------")
                print("MOOD  | SONG SUGGESTION")
                for row in list_of_data:
                    print(row["Mood"] + " | " + row["Song"] + " by " + row["Artist"])
                print("------------------------------------------------")
                print()  # Add an extra line for looks
        finally:
            if int(len(list_of_data)) == 0:
                print("  No current music in mood library! Please choose 'Option 3' to add songs to the library!\n")

    @staticmethod
    def input_mood_to_recommend(list_of_data):
        """ Input a mood and receive a song suggestion from in the list of dictionary rows

        :param list_of_data: (list) of rows you want to display
        :return: (string) with mood
        """
        if int(len(list_of_data)) > 0:
            print("Here is the list of available moods to choose from: \n")
            print("  --- MOODS ---")
            for row in list_of_data:
                print("    ", row["Mood"])
            print("  -------------\n")
            mood = str(input("  What is your mood today?: ")).title().strip()
            print()  # Add an extra line for looks
            return mood
        elif int(len(list_of_data)) == 0:
            pass

    @staticmethod
    def input_new_mood_song_and_artist():
        """  Gets mood, song, and artist values to be added to the list

        :return: (string, string, string) with mood, song, and artist
        """
        print("Enter a new mood and a song and its artist to match the mood.")
        print()  # Add an extra line for looks
        mood = str(input("  Enter the mood: ")).strip()
        song = str(input("  Enter a song: ")).strip()
        artist = str(input("  Enter the artist: ")).strip()
        print()  # extra line for looks
        return mood.title(), song.title(), artist.title()

    @staticmethod
    def input_mood_to_remove():
        """  Gets the mood name to be removed from the list

        :return: (string) with mood
        """
        mood = str(input("Which mood suggestion would you like to remove?: ")).strip()
        print()  # Add an extra line for looks
        return mood


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name=strFileName, list_of_data=lstSuggest)  # read file data

# Step 2 - Display a menu of choices to the user
IO.output_menu_tasks()  # Shows menu
while True:
    print()  # Add an extra line for looks
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 3 - Process user's menu choice
    if choice_str.strip() == '1':  # Show current data in the list/table
        IO.output_current_moods_in_list(list_of_data=lstSuggest)

    elif choice_str.strip() == '2':  # Get a song recommendation based on your mood
        mood = IO.input_mood_to_recommend(list_of_data=lstSuggest)
        lstSuggest = Processor.recommend_data_from_list(mood=mood, list_of_data=lstSuggest)

    elif choice_str.strip() == '3':  # Add a new Mood and Song Suggestion
        mood, song, artist = IO.input_new_mood_song_and_artist()
        lstSuggest = Processor.add_data_to_list(mood=mood, song=song, artist=artist, list_of_data=lstSuggest)
        continue  # to show the menu

    elif choice_str == '4':  # Remove an existing Mood and Song Suggestion
        mood = IO.input_mood_to_remove()
        lstSuggest = Processor.remove_data_from_list(mood=mood, list_of_data=lstSuggest)
        continue  # to show the menu

    elif choice_str == '5':  # Save Data to File
        lstSuggest = Processor.save_data_to_file(file_name=strFileName, list_of_data=lstSuggest)
        print("  Changes Saved to Music Library!\n")
        continue  # to show the menu

    elif choice_str == '6':  # Exit Program
        print("  Exiting Program. Goodbye!")
        break  # by exiting loop

    else:
        print("  Input not recognized! Please try again.\n")
        continue
