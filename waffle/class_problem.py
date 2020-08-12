class Player:
    def __init__(self, name, code, position, winning_rate):
        self.name = name
        self.code = code
        self.position = position
        self.winning_rate = winning_rate


class Team:
    # TODO: Modify
    def __init__(self):
        self.teamwork = 0
        self.name = ""
        self.code = ""
        self.p1 = ""
        self.p2 = ""
        self.p3 = ""
        self.p4 = ""
        self.p5 = ""
        self.p6 = ""


player_list = []
t1 = Team()
t2 = Team()


def check_duplicate(p):  # DO NOT MODIFY!
    for player in player_list:
        if player.code == p.code:
            print("duplicate code exists! code should be unique!")
            return True
    return False


def print_p(p):  # DO NOT MODIFY!
    print(f"player code : {p.code}")
    print(f"player name : {p.name}")
    print(f"player position : {p.position}")
    print(f"player winning rate : {p.winning_rate}")


def print_t(t):  # DO NOT MODIFY!
    print(f"team code: {t.code}")
    print(f"team name : {t.name}")
    print(f"teamwork : {t.teamwork}")
    print(f"first team member : {t.p1.name} {t.p1.code}")
    print(f"second team member : {t.p2.name} {t.p2.code}")
    print(f"third team member : {t.p3.name} {t.p3.code}")
    print(f"fourth team member : {t.p4.name} {t.p4.code}")
    print(f"fifth team member : {t.p5.name} {t.p5.code}")
    print(f"sixth team member : {t.p6.name} {t.p6.code}")


def input_player():
    # / * write code below * /
    player = Player()
    # input code
    while True:
        code = int(input("input code : "))
        player.code = code
        if not check_duplicate(player):
            break
    # input name
    name = input("input name : ")
    player.name = name
    # input position
    position = input("input position : ")
    player.position = position
    # input winning rate
    win_rate = int(input("input winning rate : "))
    player.winning_rate = win_rate
    print("winning rate should be between 0 and 100")
    # plus player to player_list
    player_list.append(player)
    return player


def simulate(t1, t2):
    # / *write code below*/
    print(f"{t1.name} win!")
    print(f"{t2.name} win!")
    print("Unpredictable!")


def calc_teamwork(t):  # DO NOT MODIFY!
    t.teamwork += t.p1.winning_rate + t.p2.winning_rate + t.p3.winning_rate
    t.teamwork += t.p4.winning_rate + t.p5.winning_rate + t.p6.winning_rate


def print_line():  # DO NOT MODIFY!
    print("======================================================================")


# done
def search_position(position):
    # / *write code below*/
    for player in player_list:
        if player.position == position:
            print_p(player)
            return
    print("No position exists!")


# done
def search_player_name(name):
    # / *write code below*/
    for player in player_list:
        if player.name == name:
            print_p(player)
            return
    print("No player exists!")


# done
def search_player_code(code):
    # / *write code below*/
    for player in player_list:
        if player.code == code:
            print_p(player)
            return player
    print("No player exists!")


# done
def modify_player(code):
    # / * write code below * /
    for player in player_list:
        if player.code == code:
            player.name = input("input name : ")
            player.position = input("input position : ")
            player.winning_rate = int(input("input winning rate : "))
    print("No player exists!")


def print_player():  # / * write code here * /
    print(player_list)


def delete_player(code):
    # / * write code below * /
    print("No such player exists in player list")


def check_team_condition():  # DO NOT MODIFY!
    if len(player_list) > 5:
        return True
    else:
        return False


def build_team(t):
    # / * write code below * /

    t.code = int(input("Input team code : "))

    t.name = input("Input team name : ")
    print_player()
    t.p1 = search_player_code(int(input("Input first team member's code : ")))
    print_player()
    t.p2 = search_player_code(int(input("Input second team member's code : ")))
    print_player()
    t.p3 = search_player_code(int(input("Input third team member's code : ")))
    print_player()
    t.p4 = search_player_code(int(input("Input fourth team member's code : ")))
    print_player()
    t.p5 = search_player_code(int(input("Input fifth team member's code : ")))
    print_player()
    t.p6 = search_player_code(int(input("Input sixth team member's code : ")))


def build_best_team():
    # / * write code here * /

    pass


def print_logo():  # DO NOT MODIFY!
    print_line()
    print(",--.   ,--.        ,--.            ,--.   ,--.                        ")
    print("|   `.'   | ,--,--.`--',--,--,     |   `.'   | ,---. ,--,--, ,--.,--. ")
    print("|  |'.'|  |' ,-.  |,--.|      |    |  |'.'|  || .-. :|      ||  ||  | ")
    print("|  |   |  |` '-'  ||  ||  ||  |    |  |   |  |`   --.|  ||  |'  ''  ' ")
    print("`--'   `--' `--`--'`--'`--''--'    `--'   `--' `----'`--''--' `----'  ")
    print_line()


def show_help():  # DO NOT MODIFY!
    print("Command list")
    print("help - print commands")
    print("new player - Insert new player")
    print("search player - Search player from list")
    print("delete player - Remove player from player list")
    print("modify player - Modify player from player list")
    print("print player - Print all player")
    print("build team - Build a new team")
    print("build best team - Build a best team")
    print("print team - Print all team")
    print("simulate - Simulate teams")
    print("exit - To terminate program")
    print_line()


def check_command(command):  # DO NOT MODIFY!
    if command == "new player":
        p = input_player()
        player_list.append(p)
        print_line()
    elif command == "print player":
        if len(player_list) == 0:
            print("player list is empty")
            print_line()
        else:
            print_player()
    elif command == "search player":
        select = -1
        if len(player_list) == 0:
            print("player list is empty")
        else:
            while True:
                print("Select keyword to search")
                print("0 : Search with player code")
                print("1 : Search with player name")
                print("2 : Search with player position")
                print_line()
                select = int(input())
                if select == 0:
                    keyword = input("Input player code : ")
                    print_line()
                    search_player_code(keyword)
                    break
                if select == 1:
                    keyword = input("Input player name : ")
                    print_line()
                    search_player_name(keyword)
                    break
                if select == 2:
                    keyword = "Input position : "
                    print_line()
                    search_position(keyword)
                    break
                else:
                    print("Invalid keyword!")
                    print_line()
                    continue
    elif command == "delete player":
        if len(player_list) == 0:
            print("player list is empty")
            print_line()
        else:
            name = input("Input player code : ")
            delete_player(name)
            print_line()
    elif command == "build team":
        if check_team_condition():
            print("select team to build")
            print("0 : Team 1")
            print("1 : Team 2")
            cond = int(input())
            if cond == 0:
                build_team(t1)
            elif cond == 1:
                build_team(t2)
            print_line()
        else:
            print("Not enough players to a build team")
    elif command == "build best team":
        if check_team_condition():
            build_best_team()
        else:
            print("Not enough players to build a team")
        print_line()
    elif command == "simulate":
        if t1.name == "":
            print("Team 1 is empty!")
        elif t2.name == "":
            print("Team 2 is empty!")
        else:
            simulate(t1, t2)
        print_line()
    elif command == "print team":
        if t1.name == "":
            print("Team 1 is empty!")
        else:
            print_t(t1)
        print_line()
        if t2.name == "":
            print("Team 2 is empty!")
        else:
            print_t(t2)
        print_line()
    elif command == "modify player":
        if len(player_list) == 0:
            print("player list is empty")
            print_line()
        else:
            code = input("Input player code to modify : ")
            modify_player(code)
            print_line()
    elif command == "help":
        print_logo()
        show_help()

    elif command == "exit":
        return False
    else:
        print(command)
        print("Invalid command!")
    return True


command = "help"
while (check_command(command)):
    command = input()
