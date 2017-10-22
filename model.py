


## global constant , with value of 1 and -1 easy to switch around
EMPTY = 0
BLACK = 1
WHITE = -1


##exception

class GameOverError(Exception):
    pass
class InvalidMoveError(Exception):
    pass




#### Class part with methods make a move if it is valid and flip accessble discs
#### get the number of certain color disc and so on  
class game_board:
    
    def __init__(self,row,col,first_turn,start_disc,win_rule):
        self.board = self._start_board(row,col,start_disc)
        self.num_of_row = len(self.board)    
        self.num_of_col = len(self.board[1])
        self.turn = first_turn
        self.rule = win_rule
        

    def count_disc(self,color:'BLACK/WHITE')->int:
        '''count the disc with specified color'''
        self.count = 0
        for row in self.board:
            self.count+=row.count(color)
        return self.count  
    def board_row(self)->int:
        '''return the dimension of the game board'''
        return self.num_of_row  
    def board_column(self)->int:
        '''as the same as board_row method'''
        return self.num_of_col  


    def turn_swift(self)->None:
        '''swift a turn'''
        self.turn = -self.turn
    def current_turn(self)->int:
        '''show current turn '''
        return self.turn

    def move_and_flip(self,row,col)->None:
        '''drop a disc and flip all plausible discs'''
        if self.check_game_over():
            raise GameOverError
        if (row,col) in self._get_valid_list(self.turn):
        
            self._flip(row,col,0,1,self.turn)
            self._flip(row,col,0,-1,self.turn)
            self._flip(row,col,1,1,self.turn)
            self._flip(row,col,1,-1,self.turn)
            self._flip(row,col,-1,0,self.turn)
            self._flip(row,col,1,0,self.turn)
            self._flip(row,col,-1,1,self.turn)
            self._flip(row,col,-1,-1,self.turn)
            self.board[row-1][col-1] = self.turn
        else:
            raise InvalidMoveError
    
    def check_game_over(self)->bool:
        '''return if a game is over'''
        return self._get_valid_list(WHITE)==[] \
           and self._get_valid_list(BLACK)==[]

    
    def no_move_swift(self)->None:
        '''if there is not valid move for another players in
        next turn, no turn swift is made, otherwise, turn changes into
        another player
        '''
        if self._get_valid_list(-self.turn)==[]:
            self.turn = self.turn
        else:
            self.turn_swift()
        

    def winner(self)->int:
        '''print the winner for the game'''
        
        if self.check_game_over():
            if self.rule == '>':
                if self.count_disc(BLACK)>self.count_disc(WHITE):
                    
                    return BLACK
                elif self.count_disc(BLACK)<self.count_disc(WHITE):
                    
                    return WHITE
                elif self.count_disc(BLACK)==self.count_disc(WHITE):
                    
                    return
            elif self.rule == '<':
                if self.count_disc(BLACK)>self.count_disc(WHITE):
                    
                    return WHITE
                elif self.count_disc(BLACK)<self.count_disc(WHITE):
                    
                    return BLACK
                elif self.count_disc(BLACK)==self.count_disc(WHITE):
                    
                    return


## private functions, including create initial board, which will be an              
## attribute when creating the class; check if a disc call be flip
## check if a move is valid; create a valid move list and check if a 
## place is on board

    def _create_empty_board(self,num_of_rows:int,num_of_cols:int)->None:
        '''
        create a board with all empty cells
        '''
        self.board = []
        for row in range(num_of_rows):
            self.board.append([])
            for column in range(num_of_cols):
                self.board[row].append(0)
        


    def _start_board(self,num_of_rows:int, num_of_cols:int,start_disc:'BLACK or WHITE')->'board':
        '''
        create a initial board, with specified color disc in top left and bottom
        right
        '''

        self._create_empty_board(num_of_rows,num_of_cols)
    

        top_left_center = bottom_right_center = start_disc
        top_right_center = bottom_left_center = -start_disc
        self.board[int(num_of_rows/2-1)][int(num_of_cols/2-1)] = top_left_center 
        self.board[int(num_of_rows/2)][int(num_of_cols/2)] = bottom_right_center
        self.board[int(num_of_rows/2-1)][int(num_of_cols/2)] = top_right_center
        self.board[int(num_of_rows/2)][int(num_of_cols/2-1)] = bottom_left_center
    
        return self.board





    def _flip(self,row,col,rowdelta,coldelta,turn)->None:
        '''
        check if discs in one giving direction can be flipped
        '''
        if self._valid_check(row,col,rowdelta,coldelta,turn):
            next_row =row+rowdelta
            next_col = col+coldelta
        
            while self._check_on_board(next_row,next_col)== True:
                if self.board[next_row-1][next_col-1] !=turn:
                    self.board[next_row-1][next_col-1] = turn
                    next_row+=rowdelta
                    next_col+=coldelta
                
                else:
                    break
        else:
            pass


    def _get_valid_list(self,turn)->list:
        '''
        get a valid move list by scan the board and check each cell
        '''
        valid_list = []
        for row in range(len(self.board)):
            for col in range(len(self.board[1])):
                if self._check_valid_move(row+1,col+1,turn):
                    valid_list.append((row+1,col+1))
        return valid_list


    def _check_valid_move(self,row,col,turn)->bool:
        '''
        check a certain cell in all 8 directions to see
        if it could be a valid move
        '''
        if self._valid_check(row,col,0,1,turn) \
            or self._valid_check(row,col,0,-1,turn) \
            or self._valid_check(row,col,1,0,turn) \
            or self._valid_check(row,col,-1,0,turn) \
            or self._valid_check(row,col,1,-1,turn) \
            or self._valid_check(row,col,1,1,turn) \
            or self._valid_check(row,col,-1,-1,turn) \
            or self._valid_check(row,col,0-1,1,turn):
            return True
        return False
    
            



    def _valid_check(self,row:int,col:int,rowdelta:int,coldelta:int,turn)->bool:
        '''check a cell in one direction to see if it is movable in that direction
        '''
        if not self._check_on_board(row,col):
            raise InvalidMoveError
        drow_position = self.board[row-1][col-1]
        cell_count = 0
        if drow_position != 0:
            return False
        while True:
            row+=rowdelta
            col+=coldelta
            cell_count+=1
            if self._check_on_board(row,col) and self.board[row-1][col-1]==-turn:
                pass
            if self._check_on_board(row,col) and self.board[row-1][col-1]==0:
                return False
            if self._check_on_board(row,col) and self.board[row-1][col-1]== turn:
            
                if cell_count == 1:
                    return False
                return True
            if not self._check_on_board(row,col):
                break

    def _check_on_board(self,row,col)->bool:
        '''check if the specifie position is on board'''
        return 0<row<=len(self.board) and 0<col<=len(self.board[1])







