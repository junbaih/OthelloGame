import tkinter
import gameboard
DEFAULT_FONT = ('Helvetica', 14)


class GameMenu:
    def __init__(self):
        self.menu_window = tkinter.Toplevel()

        indication_label = tkinter.Label(
            master = self.menu_window, text = 'Please choose following  game rules',
            font = DEFAULT_FONT)

        indication_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W +tkinter.N + tkinter.E+tkinter.S)

        row_choose_label = tkinter.Label(
            master = self.menu_window, text = 'Choose the number of rows',
            font = DEFAULT_FONT,background = 'cyan')

        row_choose_label.grid(
            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)
        self.row_option =tkinter.StringVar()
        self.row_option.set('4')
        
        row_option_menu = tkinter.OptionMenu(self.menu_window,self.row_option,'4','6','8','10','12','14','16')
        row_option_menu.grid(row = 1, column = 2, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        

        col_choose_label = tkinter.Label(master = self.menu_window, text = 'Choose the number of columns',
                                         font = DEFAULT_FONT,background = 'cyan')

        col_choose_label.grid(
            row = 2, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)
        self.col_option =tkinter.StringVar()
        self.col_option.set('4')
        
        col_option_menu = tkinter.OptionMenu(self.menu_window,self.col_option,'4','6','8','10','12','14','16')
        col_option_menu.grid(row = 2, column = 2, padx = 10, pady = 10,
            sticky = tkinter.W)


        first_move_disc_label = tkinter.Label(master = self.menu_window,text = 'Which player moves first',
                                              font = DEFAULT_FONT,background = 'cyan')

        first_move_disc_label.grid(row=3, column = 0, columnspan = 2, padx = 10, pady = 10,
                                   sticky = tkinter.W)
        self.first_player_option = tkinter.StringVar()
        self.first_player_option.set('white')
        
        first_player_menu = tkinter.OptionMenu(self.menu_window,self.first_player_option,'white','black')
        first_player_menu.grid(row =3 ,column =2 ,padx=10,pady=10,
                               sticky = tkinter.W)


        top_left_disc_label = tkinter.Label(master= self.menu_window, text = 'which disc on top left and bottom right',
                                            font = DEFAULT_FONT,background = 'cyan')
        top_left_disc_label.grid(row =4 ,column=0, columnspan=2 , padx =10, pady=10,
                                 sticky = tkinter.W)
        self.top_left_option = tkinter.StringVar()
        self.top_left_option.set('white')

        top_left_menu = tkinter.OptionMenu(self.menu_window,self.top_left_option,'white','black')
        top_left_menu.grid(row =4, column=2,padx =10, pady =10, sticky =tkinter.W)
        

        win_rule_label = tkinter.Label(master =self.menu_window, text = 'choose a winner rule',
                                       font=DEFAULT_FONT,background = 'cyan')
        win_rule_label.grid(row =5, column=0, columnspan =2,padx =10, pady=10,
                            sticky= tkinter.W)
        self.win_rule_option  =tkinter.StringVar()
        self.win_rule_option.set('>')
        win_rule_menu = tkinter.OptionMenu(self.menu_window,self.win_rule_option,'>','<')
        win_rule_menu.grid(row =5, column=2,padx =10, pady =10, sticky =tkinter.W)



        button_frame = tkinter.Frame(master = self.menu_window)
        button_frame.grid(
            row = 6, column= 0, columnspan=3,padx =10,pady =10,
            sticky = tkinter.E + tkinter.S )

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)
        cancel_button = tkinter.Button(
            master = button_frame,text = 'Cancel',font =DEFAULT_FONT,
            command = self._on_cancel_button)

        ok_button.grid(row = 0,column= 0, padx =10, pady=10,sticky = tkinter.W)
        cancel_button.grid(row =0 ,column = 1, padx =10 ,pady=10,sticky =tkinter.E)

        

        self.menu_window.rowconfigure(0 ,weight =1)
        self.menu_window.rowconfigure(1 ,weight =1)
        self.menu_window.rowconfigure(2 ,weight =1)
        self.menu_window.rowconfigure(3 ,weight =1)
        self.menu_window.rowconfigure(4 ,weight =1)
        self.menu_window.rowconfigure(5 ,weight =1)
        self.menu_window.rowconfigure(6 ,weight =1)
        self.menu_window.columnconfigure(0 ,weight =1)
        self.menu_window.columnconfigure(1 ,weight =1)
        self.menu_window.columnconfigure(2 ,weight =1)



        
        self._ok_click = False

        self.game_row_choice = '4'
        self.game_col_choice = '4'
        self.game_firstpl_choice ='white'
        self.top_left_position_choice = 'white'
        self.game_win_choice  = '>'

    def show(self):
        
        self.menu_window.grab_set()
        
        self.menu_window.wait_window()
        
    def _on_ok_button(self):
        self._ok_click = True
        self.game_row_choice = self.row_option.get()
        self.game_col_choice = self.col_option.get()
        self.game_firstpl_choice =self.first_player_option.get()
        self.top_left_position_choice = self.top_left_option.get()
        self.game_win_choice  = self.win_rule_option.get()
        row_choice = int(self.game_row_choice)
        col_choice = int(self.game_col_choice)
        firstpl_choice =_string_to_int(self.game_firstpl_choice)
        top_left_position_choice = _string_to_int(self.top_left_position_choice)
        win_choice  =self.game_win_choice
        self.menu_window.destroy()
        game = gameboard.GraphicGameBoard(row_choice,col_choice,firstpl_choice,top_left_position_choice,win_choice).start()        
    def _on_cancel_button(self):
        self.menu_window.destroy()


class OthelloGame:
    def __init__(self):
        self.root_window = tkinter.Tk()

        self.greeting_canvas = tkinter.Canvas(
            master = self.root_window,  width =600, height = 600,
            background = '#00ffff')
        self.greeting_canvas.create_text(
            300,350,text = 'Click  to play the game,\n the rule for the game is: FULL',
            font =DEFAULT_FONT)
        self.greeting_canvas.create_text(300,200,text ='Othello',font =
                                         ('Helvetica',24,'bold'))
        self.greeting_canvas.create_text(470,550,text =' created by Junbai Hou, 61471604',font =
                                         ('Helvetica',12))

        self.greeting_canvas.bind('<Button-1>',self._show_menu)


    def _show_menu(self,event: tkinter.Event):
        
        menu = GameMenu()
        menu.show()

        
        
            
            

    def start(self):
        self.greeting_canvas.pack()
        self.root_window.mainloop()


def _string_to_int(s:str)->int:
    if s == 'white':
        return -1
    return 1


if __name__ == '__main__':
    OthelloGame().start()
