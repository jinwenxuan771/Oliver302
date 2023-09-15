import sqlite3

# Function to create the SQLite database and table
def create_database_table():
    connection = sqlite3.connect("stephen_king_adaptations.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (
                      movieID TEXT PRIMARY KEY,
                      movieName TEXT,
                      movieYear INTEGER,
                      imdbRating REAL
                    )''')
    connection.commit()
    connection.close()

# Function to read data from the file and insert into the database
def insert_data_from_file():
    stephen_king_adaptations_list = []
    with open("stephen_king_adaptations.txt", "r") as file:
        for line in file:
            movieID, movieName, movieYear, imdbRating = line.strip().split(',')
            stephen_king_adaptations_list.append((movieID, movieName, int(movieYear), float(imdbRating)))

    connection = sqlite3.connect("stephen_king_adaptations.db")
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO stephen_king_adaptations_table VALUES (?, ?, ?, ?)", stephen_king_adaptations_list)
    connection.commit()
    connection.close()

# Function to search for movies based on user input
def search_movies():
    while True:
        print("\nOptions:")
        print("1. Search by movie name")
        print("2. Search by movie year")
        print("3. Search by movie rating")
        print("4. STOP")
        choice = input("Enter your choice: ")

        if choice == "1":
            movie_name = input("Enter movie name: ")
            search_movie_by_name(movie_name)
        elif choice == "2":
            year = int(input("Enter movie year: "))
            search_movie_by_year(year)
        elif choice == "3":
            rating = float(input("Enter minimum movie rating: "))
            search_movie_by_rating(rating)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Function to search for movies by name
def search_movie_by_name(name):
    connection = sqlite3.connect("stephen_king_adaptations.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName LIKE ?", ('%' + name + '%',))
    movies = cursor.fetchall()
    connection.close()

    if movies:
        for movie in movies:
            print("Movie Name:", movie[1])
            print("Movie Year:", movie[2])
            print("IMDb Rating:", movie[3])
    else:
        print("No such movie exists in our database.")

# Function to search for movies by year
def search_movie_by_year(year):
    connection = sqlite3.connect("stephen_king_adaptations.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?", (year,))
    movies = cursor.fetchall()
    connection.close()

    if movies:
        for movie in movies:
            print("Movie Name:", movie[1])
            print("Movie Year:", movie[2])
            print("IMDb Rating:", movie[3])
    else:
        print("No movies were found for that year in our database.")

# Function to search for movies by rating
def search_movie_by_rating(rating):
    connection = sqlite3.connect("stephen_king_adaptations.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (rating,))
    movies = cursor.fetchall()
    connection.close()

    if movies:
        for movie in movies:
            print("Movie Name:", movie[1])
            print("Movie Year:", movie[2])
            print("IMDb Rating:", movie[3])
    else:
        print("No movies at or above that rating were found in the database.")

# Main program
if __name__ == "__main__":
    create_database_table()
    insert_data_from_file()
    search_movies()
