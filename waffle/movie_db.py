import pickle

# CONST STRING
ADD_GENRE = "add_genre "
ADD_MOVIE = "add_movie "
REMOVE_GENRE = "remove_genre "
REMOVE_MOVIE = "remove_movie "
PRINT_GENRE = "print_genre "
PRINT_ALL = "print_all"
SAVE = "save"
LOAD = "load"
EXIT = "exit"
LINE = "----------"


class Genre:
    count_genre = 0
    genre_list = []

    def __init__(self, _name):
        self.name = _name
        self.movie_list = []
        Genre.genre_list.append(self)

    def __del__(self):
        print(self.name + "장르가 삭제되었습니다.")

    def add_movie(self, _movie):
        self.movie_list.append(_movie)

    @classmethod
    def remove_genre(cls, _genre):
        for genre in cls.genre_list:
            if genre.name == _genre:
                cls.genre_list.remove(genre)
                del genre
                return
        print(_genre + "는 존재하지 않는 장르 입니다.")

    @classmethod
    def remove_movie(cls, _genre, _movie):
        for genre in cls.genre_list:
            if genre.name == _genre:
                for movie in genre.movie_list:
                    if movie == _movie:
                        genre.movie_list.remove(_movie)
                        print(_genre + " 장르의 " + _movie + " 가 삭제되었습니다.")
                        return
                print(_genre + "에 " + _movie + "가 존재하지 않습니다.")
        print(_genre + "는 존재하지 않는 장르 입니다.")

    @classmethod
    def print_genre(cls, _genre):
        for genre in cls.genre_list:
            if genre.name == _genre:
                print(LINE)
                print("장르: " + _genre)
                if len(genre.movie_list) == 0:
                    print("--empty")
                for i in range(len(genre.movie_list)):
                    print(str(i + 1) + ". " + genre.movie_list[i])
                print(LINE)
                return
        print(_genre + "가 존재하지 않습니다.")

    @classmethod
    def print_all(cls):
        for genre in cls.genre_list:
            print(LINE)
            print("장르:" + genre.name)
            for i in range(len(genre.movie_list)):
                print(str(i + 1) + ". " + genre.movie_list[i])
            print(LINE)


if __name__ == '__main__':
    while True:
        # INPUT COMMAND
        command = input()
        # ADD GENRE
        if ADD_GENRE in command:
            genre_name = command[len(ADD_GENRE):]
            Genre(genre_name)
            print(genre_name + "장르가 생성되었습니다.")
        # ADD MOVIE
        elif ADD_MOVIE in command:
            genre_name, movie_name = command[len(ADD_MOVIE):].split()
            for i in range(len(Genre.genre_list)):
                if genre_name == Genre.genre_list[i].name:
                    Genre.genre_list[i].add_movie(movie_name)
                    Genre.print_genre(genre_name)
                elif i == len(Genre.genre_list) - 1:
                    print(genre_name + "장르가 없습니다.")
        # REMOVE GENRE
        elif REMOVE_GENRE in command:
            genre_name = command[len(REMOVE_GENRE):]
            Genre.remove_genre(genre_name)
        # REMOVE_MOVIE
        elif REMOVE_MOVIE in command:
            genre_name, movie_name = command[len(REMOVE_MOVIE):].split()
            Genre.remove_movie(genre_name, movie_name)
        # PRINT GENRE
        elif PRINT_GENRE in command:
            genre_name = command[len(PRINT_GENRE):]
            Genre.print_genre(genre_name)
        # PRINT ALL
        elif PRINT_ALL in command:
            Genre.print_all()
        # SAVE
        elif SAVE in command:
            print("현재 정보를 저장합니다.")
            with open("db.txt", 'wb') as file:
                pickle.dump(Genre.genre_list, file)
        # LOAD
        elif LOAD in command:
            print("이전 정보를 불러옵니다.")
            with open("db.txt", 'rb') as file:
                Genre.genre_list = pickle.load(file)
            Genre.print_all()
        # EXIT
        elif EXIT in command:
            break
