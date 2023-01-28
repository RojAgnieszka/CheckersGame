from pionki import Pawns

class Board:
    def __init__(self):
        self.board = self.make_board()
        self.x_left = self.o_left = 12
        self.player = 'o'
        self.x_player_points = self.o_player_points = 0
        self.double = 0
        self.current_pawn = Pawns.o
        
    def make_board(self):
        board = [[' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
             ['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '],
             [' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
             [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
             ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' ']]
        return board
    
    def print_board(self, my_board):
        list_numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
        list_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        print('   ', ' '.join(list_numbers))
        for i in range(8):
            print(list_letters[i], '|', '|'.join(my_board[i]), '|')
            
    def choose_place(self, komunikat):
        choose = input(komunikat)
        list_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        if len(choose) != 2:
            print('podaj litere i liczbe')
            return 0
        if choose[0].upper() in list_letters:
            row = list_letters.index(choose[0].upper())
        else:
            print('Wybrano nieprawidlowy rzad')
            return 0
        try:
            if int(choose[1]) > 0 and int(choose[1]) < 9:
                col = int(choose[1])-1
            else:
                print('Wybrano nieprawidlowa kolumne')
                return 0
        except ValueError:
            print("Kolumna musi byc liczba")
            return 0
        return (row, col)
    
    def is_there_pawn(self, place):
        if self.board[place[0]][place[1]] in ['X', 'M']:
            return 'X'
        elif self.board[place[0]][place[1]] in ['o', '●']:
            return 'o'
        else:
            return False
        
    def get_place(self, place):
        return self.board[place[0]][place[1]]
        
    def set_currentPawn(self, place_old):
        if self.get_place(place_old) == 'X':
            self.current_pawn = Pawns.X
        elif self.get_place(place_old) == 'M':
            self.current_pawn = Pawns.M
        elif self.get_place(place_old) == 'o':
            self.current_pawn = Pawns.o
        else:
            self.current_pawn = Pawns.O 
            
    def move_down(self, place_old, place_new):
        if (place_new[1]+1)==place_old[1] or (place_new[1]-1) == place_old[1]:
            self.put_pawn(place_old, place_new)
            return (1, 1)
        return (0, 1)
            
    def move_up(self, place_old, place_new):
        if (place_new[1]+1)==place_old[1] or (place_new[1]-1) == place_old[1]:
            self.put_pawn(place_old, place_new)
            return (1, 1)
        return (0, 1)
            
    def attack_down(self, place_old, place_new):
        if(place_new[1]+2) == place_old[1]:
            good_attack = self.attack_down_lef(place_old, place_new)
        elif(place_new[1]-2) == place_old[1]:
            good_attack = self.attack_down_right(place_old, place_new)
        else:
            good_attack = 0 
        if good_attack:
            if_double = self.double_move(place_new)
        else:
            if_double = 1
        return (good_attack, if_double)
    
    def attack_up(self, place_old, place_new):
        if(place_new[1]+2) == place_old[1]:
            good_attack = self.attack_up_lef(place_old, place_new)
        elif(place_new[1]-2) == place_old[1]:
            good_attack = self.attack_up_right(place_old, place_new)     
        else:
            good_attack = 0
        if good_attack:
            if_double = self.double_move(place_new)
        else:
            if_double = 1
        return (good_attack, if_double)
    
    def attack_up_lef(self, place_old, place_new):
        place = self.board[place_old[0]-1][place_old[1]-1]
        if (place in ['X', 'M'] and self.player == 'o') or (place in ['o', '●'] and self.player == 'X'):
            self.board[place_old[0]-1][place_old[1]-1] = ' '
        else:
            return 0
        self.put_pawn(place_old, place_new)
        self.attack_comment()
        return 1
        
    def attack_up_right(self, place_old, place_new):
        place = self.board[place_old[0]-1][place_old[1]+1]
        if (place in ['X', 'M'] and self.player == 'o') or (place in ['o', '●'] and self.player == 'X'):
            self.board[place_old[0]-1][place_old[1]+1] = ' '
        else:
            return 0
        self.put_pawn(place_old, place_new)
        self.attack_comment()
        return 1
    
    def attack_down_lef(self, place_old, place_new):
        place = self.board[place_old[0]+1][place_old[1]-1]
        if (place in ['X', 'M'] and self.player == 'o') or (place in ['o', '●'] and self.player == 'X'):
            self.board[place_old[0]+1][place_old[1]-1] = ' '
        else:
            return 0
        self.put_pawn(place_old, place_new)
        self.attack_comment()
        return 1  
    
    def attack_down_right(self, place_old, place_new):
        place = self.board[place_old[0]+1][place_old[1]+1]
        if (place in ['X', 'M'] and self.player == 'o') or (place in ['o', '●'] and self.player == 'X'):
            self.board[place_old[0]+1][place_old[1]+1] = ' '
        else:
            return 0
        self.put_pawn(place_old, place_new)
        self.attack_comment()
        return 1
    
        
        
    def is_good_move2(self, place_new, place_old): 
        self.set_currentPawn(place_old)
        if (place_new[0] - 1) == place_old[0] and 'move_down' in self.current_pawn.value:
            return self.move_down(place_old, place_new)
        elif (place_new[0] + 1) == place_old[0] and 'move_up' in self.current_pawn.value:
            return self.move_up(place_old, place_new)
        elif (place_new[0]-2) == place_old[0] and 'attack_down' in self.current_pawn.value:
            return self.attack_down(place_old, place_new)
        elif (place_new[0]+2) == place_old[0] and 'attack_up' in self.current_pawn.value:
            return self.attack_up(place_old, place_new)
        else:
            return (0,1)
        
        
        
    # def is_good_move(self, place_new, place_old):
    #     if self.board[place_old[0]][place_old[1]] in ['M', 'o', '●']:
    #         if (place_new[0] + 1) == place_old[0]:
    #             if (place_new[1]+1)==place_old[1] or (place_new[1]-1) == place_old[1]:
    #                 self.put_pawn(place_old, place_new)
    #                 return (1, 1)
    #         elif (place_new[0]+2) == place_old[0]:
    #             return self.attack(place_old, place_new)
    #     elif self.board[place_old[0]][place_old[1]] in ['●', 'X', 'M']:
    #         if (place_new[0] - 1) == place_old[0]:
    #             if (place_new[1]+1)==place_old[1] or (place_new[1]-1) == place_old[1]:
    #                 self.put_pawn(place_old, place_new)
    #                 return (1, 1)
    #         elif (place_new[0]-2) == place_old[0]:
    #             return self.attack(place_old, place_new)
    #     return (0, 1)
    
    def put_pawn(self, place_old, place_new):
        self.board[place_new[0]][place_new[1]] = self.board[place_old[0]][place_old[1]]
        self.board[place_old[0]][place_old[1]] = ' '
        if self.player == 'o' and place_new[0] == 0:
            self.board[place_new[0]][place_new[1]] = '●'
        elif self.player == 'X' and place_new[0] == 7:
            self.board[place_new[0]][place_new[1]] = 'M'
        
        
    def attack_comment(self):
        if self.player == 'o':
            self.x_left -= 1
            self.o_player_points += 1
        elif self.player == 'X':
            self.o_left -= 1
            self.x_player_points += 1
        print('zbiles pion przeciwnika')
        
    # def attack_side(self, place_old, place_new): # chyba jest done. do poprawy - strony nie dzialaja w przypadku roznych graczy, brak wskazania czy przeciwnika szukac u gory czy na dole, na poczatku zrobic if ktory sprawdza ktory to gracz i potem tylko jedna wersje txt i tez w zaleznosci od strony.
    #     if self.player =='o':
    #         if (place_new[1]+2)==place_old[1] and self.board[place_old[0]-1][place_old[1]-1] in ['X', 'M']:
    #             self.board[place_old[0]-1][place_old[1]-1] = ' '
    #         elif (place_new[1]-2)==place_old[1] and self.board[place_old[0]-1][place_old[1]+1] in ['X', 'M']:
    #             self.board[place_old[0]-1][place_old[1]+1] = ' '
    #         else:
    #             return 0
    #     else:
    #         if (place_new[1]+2)==place_old[1] and self.board[place_old[0]+1][place_old[1]-1] in ['o', '●']:
    #             self.board[place_old[0]-1][place_old[1]-1] = ' '
    #         elif (place_new[1]-2)==place_old[1] and self.board[place_old[0]+1][place_old[1]+1] in ['o', '●']:
    #             self.board[place_old[0]-1][place_old[1]+1] = ' '
    #         else:
    #             return 0
    #     self.put_pawn(place_old, place_new)
    #     self.attack_comment()
    #     return 1
    
    # def attack(self, place_old, place_new):
    #     if self.player == 'o':
    #         if (place_new[0]+2) == place_old[0]:
    #             good_attack = self.attack_side(place_old, place_new) 
    #         elif (place_new[0]-2) == place_old[0] and self.board[place_old[0]][place_old[1]] == '●':
    #             good_attack = self.attack_side(place_old, place_new)
    #         else:
    #             return 0
    #     else:
    #         if (place_new[0]-2) == place_old[0]:
    #             good_attack = self.attack_side(place_old, place_new)
    #         elif (place_new[0]+2) == place_old[0] and self.board[place_old[0]][place_old[1]] == 'M':
    #             good_attack = self.attack_side(place_old, place_new)
    #         else:
    #             return 0
    #     if good_attack:
    #         if_double = self.double_move(place_new)
    #     else:
    #         if_double = 1
    #     return (good_attack, if_double)
    
    def double_done(self, place):
        self.print_board(self.board)
        self.double = place
        return 0
    
    def double_move(self, place):  # do wyczyszczenia
        if self.player == 'o':
            if place[0] - 2 >= 0:
                if place[1] - 2 >= 0:  
                    if self.board[place[0]-1][place[1]-1] in ['X', 'M'] and self.board[place[0]-2][place[1]-2] == " ":
                        return self.double_done(place)
                if place[1] + 2 <= 7:
                    if self.board[place[0]-1][place[1]+1] in ['X', 'M'] and self.board[place[0]-2][place[1]+2] == " ":
                        return self.double_done(place)
            if place[0] + 2 <= 7 and self.board[place[0]][place[1]] == '●':
                if place[1] - 2 >= 0:
                    if self.board[place[0]+1][place[1]-1] in ['X', 'M'] and self.board[place[0]+2][place[1]-2] == " ":
                        return self.double_done(place)
                if place[1] + 2 <=7:
                    if self.board[place[0]+1][place[1]+1] in ['X', 'M'] and self.board[place[0]+2][place[1]+2] == " ":
                        return self.double_done(place)
        else:
            if place[0] + 2 <= 7:
                if place[1] - 2 >= 0:
                    if self.board[place[0]+1][place[1]-1] in ['o', '●'] and self.board[place[0]+2][place[1]-2] == " ":
                        return self.double_done(place)
                if place[1] + 2 <=7:
                    if self.board[place[0]+1][place[1]+1] in ['o', '●'] and self.board[place[0]+2][place[1]+2] == " ":
                        return self.double_done(place)
            elif place[0] -2 >= 0 and self.board[place[0]][place[1]] == 'M':
                if place[1] - 2 >= 0:  
                    if self.board[place[0]-1][place[1]-1] in ['o', '●'] and self.board[place[0]-2][place[1]-2] == " ":
                        return self.double_done(place)
                if place[1] + 2 <= 7:
                    if self.board[place[0]-1][place[1]+1] in ['o', '●'] and self.board[place[0]-2][place[1]+2] == " ":
                        return self.double_done(place)
        self.double = 0
        return 1
    
    def change_player(self):
        if self.player == 'o':
            print('Masz punktow:', self.o_player_points)
            self.player = 'X'
        elif self.player == 'X':
            print('Masz punktow:', self.x_player_points)
            self.player ='o'
                
            
                    
        

        
    def make_move(self):
        if self.double:
            pawn_old = self.double
        else:
            pawn_old = self.choose_place("Jaki pionek wybierasz?")
        if pawn_old:                                                        # (row, col) or 0
            pawn_this = self.is_there_pawn(pawn_old)
            if pawn_this == self.player:                                    # player pawn or 0, we are using our pawn
                pawn_new = self.choose_place("Gdzie chcesz sie ruszyc?")
                if pawn_new:
                    if self.is_there_pawn(pawn_new) == False:
                        is_good = self.is_good_move2(pawn_new, pawn_old)     # spr czy mozna zrobic taki ruch
                        if is_good[0]:
                            return is_good[1]                               # 0 tylko jak ma powtarzac
                        else:
                            print('nieprawidlowy ruch')
                    else:
                        print("to miejsce jest zajete")
            else:
                print("Nie ma tam Twojego pionka!")
        return 0