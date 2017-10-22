## gameboard 

import tkinter
import model

import math
DEFAULT_FONT = ('Helvetica', 14)
class GraphicGameBoard:
    def __init__(self,game_row,game_col,first_move,start_disc,win_rule):
        self.game = model.game_board(game_row,game_col,first_move,start_disc, win_rule)
        self.col_interval = 1/self.game.board_column()
        self.row_interval = 1/self.game.board_row()
        self.disc_radius = _find_small(self.col_interval,self.row_interval)/2

        
        ## canvas

        self._root_window = tkinter.Toplevel()

        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 500, height = 500,
            background = '#00ffff')

        
        self._canvas.grid(
            row = 2, column = 0, columnspan =3, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        ## label: next_turn, number of black disc, number of white disc
        #turn
        self.turn_text  = tkinter.StringVar()
        self.turn_text.set('TURN: {}'.format(_turn_into_string(self.game.current_turn())))

        turn_label = tkinter.Label(
            master = self._root_window, textvariable = self.turn_text,
            font = ('Helvetica', 16))
        turn_label.grid(row = 0, column= 1, padx = 10, pady =10,
                        sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        #num of white disc
        self.white_number_text = tkinter.StringVar()
        self.white_number_text.set('WHITE: 2')
        white_count_label = tkinter.Label(
            master = self._root_window, textvariable = self.white_number_text,
            font =DEFAULT_FONT)
        white_count_label.grid(row=1,column = 0,padx = 10, pady =10,
                               sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        #num of black disc
        self.black_number_text = tkinter.StringVar()
        self.black_number_text.set('BLACK: 2')
        black_count_label = tkinter.Label(
            master = self._root_window, textvariable = self.black_number_text,
            font =DEFAULT_FONT)
        black_count_label.grid(row=1,column = 2,padx = 10, pady =10,
                               sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


        #window configure
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 2)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)
        self._root_window.columnconfigure(2, weight = 1)

    def start(self) -> None:
        self._root_window.grab_set()
        self._root_window.wait_window()


    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._draw_board()
    def _on_canvas_clicked(self,event:tkinter.Event) ->None:
        if not self.game.check_game_over():
            width = self._canvas.winfo_width()
            height = self._canvas.winfo_height()
            frac_click_center = (event.x/width,event.y/height)


            disc_row= 0
            disc_col= 0
            for row in range(self.game.board_row()):
                for col in range(self.game.board_column()):
                
                    if abs(frac_click_center[0]-self._get_center_list()[row][col][0])<self.col_interval/2 and \
                       abs(frac_click_center[-1]- self._get_center_list()[row][col][-1])<self.row_interval/2:



                        disc_row =row+1
                        disc_col =col+1
            try:
                self.game.move_and_flip(disc_row,disc_col)                
                self.game.no_move_swift()
                self.white_number_text.set('WHITE: {}'.format(self.game.count_disc(-1)))
                self.black_number_text.set('BLACK: {}'.format(self.game.count_disc(1)))

                if not self.game.check_game_over():
                    self.turn_text.set('TURN: {}'.format(_turn_into_string(self.game.current_turn())))

                else:
                    self.turn_text.set('Winner:{}'.format(_turn_into_string(self.game.winner())))
            except:
                pass
                
            finally:
                self._draw_board()
    




           
    def _draw_board(self):
        #delete old board and draw a current game board
        self._canvas.delete(tkinter.ALL)
        
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()



        for i in range(1,self.game.board_column()):
            
            self._canvas.create_line(width*self.col_interval*i,0,
                                     width*self.col_interval*i,height,
                                     )

        for i in range(1,self.game.board_row()):
            self._canvas.create_line(0,height*self.row_interval*i,
                                     width,height*self.row_interval*i
                                     )





            
        for row in range(self.game.board_row()):
            for col in range(self.game.board_column()):
                pixel_center_x =self._get_center_list()[row][col][0]*width
                pixel_center_y =self._get_center_list()[row][col][-1]*height        
                if self.game.board[row][col]==1:
                    self._canvas.create_oval(pixel_center_x-self.disc_radius*width+2,
                                         pixel_center_y-self.disc_radius*height+2,
                                         pixel_center_x+self.disc_radius*width-2,
                                         pixel_center_y+self.disc_radius*height-2,
                                         fill = 'black')
                elif self.game.board[row][col]==-1:
                    self._canvas.create_oval(pixel_center_x-self.disc_radius*width+2,
                                         pixel_center_y-self.disc_radius*height+2,
                                         pixel_center_x+self.disc_radius*width-2,
                                         pixel_center_y+self.disc_radius*height-2,
                                         fill = 'white')
                elif self.game.board[row][col]==0:
                    pass
                
    def _get_center_list(self):
        #get a list of tuple (x-coodinate,y-coodinate)
        center_list = []
        for row in range(self.game.board_row()):
            center_list.append([])
            for col in range(self.game.board_column()):
                center_list[row].append((0,0)) 

        for row in range(self.game.board_row()):
            for col in range(self.game.board_column()):
                
                center_list[row][col]=((1+2*col)*self.col_interval/2,(1+2*row)*self.row_interval/2)
        return center_list

def _find_small(n1:int,n2:int):
    '''find the smaller one in given two ints''' 
    if n1> n2:
        return n2
    return n1


def _turn_into_string(turn):
    ''' turn the 1 and -1 to black and white, according to the game logic'''
    if turn == -1:
        return 'white'
    if turn == 1:
        return 'black'
    return 'None'




###only for test
if __name__ == '__main__':
    GraphicGameBoard(6,4,model.WHITE,model.BLACK,'>')#.start()
    
