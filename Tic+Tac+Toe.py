# modules
def print_board(l):
    print('\n')
    print('%s|%s|%s'%(l['7'],l['8'],l['9']))
    print('-----')
    print('%s|%s|%s'%(l['4'],l['5'],l['6']))
    print('-----')
    print('%s|%s|%s'%(l['1'],l['2'],l['3']))
    print('\n')

def player_move(p, board, player_positions):
    while True:
        move = input('Move of %s, please use the numeric keypad: '%p)
        if move in list(board.keys()):
            if board[move]==' ':
                board[move] = p
                player_positions[p].append(int(move))
                break
            else:
                print('Wrong position!\n')
        else:
            print('Wrong position!\n')

def check_win(p, win_cases, player_positions, win):
    if set(player_positions[p]) in win_cases:
        win[0] = 1
        print('Play %s won!\n'%p)
            
# main function            
def tic_tac_toe():
    play_or_not = 'Y'
    win_cases = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{7,5,3},{1,5,9}]
    while play_or_not == 'Y':
        # initialization
        board = {'7':' ','8':' ','9':' ','4':' ','5':' ','6':' ','1':' ','2':' ','3':' '}
        player_positions = {'x':[],'o':[]}
        print_board(board)
        win = [0]
        blank = [' ']
        
        while win[0] == 0 and blank[0] in list(board.values()):
            
            # play x's input
            player_move('x', board, player_positions)
            print_board(board)
            
            # check if someone wins
            check_win('x', win_cases, player_positions, win)
            if win[0] == 1:
                break
                
            # check if no one wins
            if blank[0] not in list(board.values()):
                print('Draw!\n')
                break
        
            # play x's input
            player_move('o', board, player_positions)
            print_board(board)
                  
            # check if someone wins
            check_win('o', win_cases, player_positions, win)
            if win[0] == 1:
                break
            
            # check if no one wins
            if blank[0] not in list(board.values()):
                print('Draw!\n')
                break
        
        # check if continue play
        play_or_not = input('Play again?(Y/N): ').upper()

        
# call the main function to play
tic_tac_toe()


