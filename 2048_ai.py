#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import *
from tkinter import messagebox
import random
import copy as cp

class Board:
    bg_color={

        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#edc850',
        '16': '#edc53f',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#f2b179',
        '1024': '#f59563',
        '2048': '#edc22e',
    }
    color={
         '2': '#776e65',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#776e65',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }

    def __init__(self):
        self.n=4
#         self.window=Tk()
#         self.window.title('ProjectGurukul 2048 Game')
#         self.gameArea=Frame(self.window,bg= 'azure3')
#         self.board=[]
        self.gridCell=[[0]*4 for i in range(4)]
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0

    def reverse(self):
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                self.gridCell[ind][i],self.gridCell[ind][j]=self.gridCell[ind][j],self.gridCell[ind][i]
                i+=1
                j-=1

    def transpose(self):
        self.gridCell=[list(t)for t in zip(*self.gridCell)]

    def compressGrid(self):
        self.compress=False
        temp=[[0] *4 for i in range(4)]
        for i in range(4):
            cnt=0
            for j in range(4):
                if self.gridCell[i][j]!=0:
                    temp[i][cnt]=self.gridCell[i][j]
                    if cnt!=j:
                        self.compress=True
                    cnt+= 1
        self.gridCell=temp

    def mergeGrid(self):
        self.merge=False
        for i in range(4):
            for j in range(4 - 1):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True

    def random_cell(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]=2
    
    def can_merge(self):
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j+1]:
                    return True
        
        for i in range(3):
            for j in range(4):
                if self.gridCell[i+1][j] == self.gridCell[i][j]:
                    return True
        return False

    def paintGrid(self):
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j]==0:
                    self.board[i][j].config(text='',bg='azure4')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]),
                    bg=self.bg_color.get(str(self.gridCell[i][j])),
                    fg=self.color.get(str(self.gridCell[i][j])))
        

class Game:
    def __init__(self,gamepanel):
        self.gamepanel=gamepanel
        self.end=False
        self.won=False

    def start(self):
        self.gamepanel.random_cell()
        return self.gamepanel.gridCell
#         self.gamepanel.paintGrid()
#         self.gamepanel.window.bind('<Key>', self.algo())

#         self.gamepanel.window.bind('<Key>', self.link_keys)
#         self.gamepanel.window.mainloop()
    
    def link_keys(self, move):
        if self.end or self.won:
            return

        self.gamepanel.compress = False
        self.gamepanel.merge = False
        self.gamepanel.moved = False

#         presed_key=event.keysym

        if move=='Up':
#             print('up')
            self.gamepanel.transpose()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.transpose()

        elif move=='Down':
#             print('down')
            self.gamepanel.transpose()
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
            self.gamepanel.transpose()

        elif move=='Left':
#             print('left')
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()

        elif move=='Right':
#             print('right')
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
        else:
            pass

        return self.gamepanel.gridCell, self.gamepanel.score
#         self.gamepanel.paintGrid()

    def is_gameover(self):
        flag=0
        for i in range(4):
            for j in range(4):
                if(self.gamepanel.gridCell[i][j]==2048):
                    flag=1
                    break
                    
        zero = 0
        for i in range(4):
            for j in range(4):
                if(self.gamepanel.gridCell[i][j]==0):
                    zero = 1
                    break
                    
        if not (flag or self.gamepanel.can_merge() or zero):
            self.end=True
#             messagebox.showinfo('2048','Game Over!!!')
            print("Over")
            return True
        print('return false')
        return False
        
    def get_space_count(self):
        count = 0
        for i in range(4):
            for j in range(4):
                if self.gamepanel.gridCell[i][j] == 0:
            
                    count += 1
        return count
    
    def copy_data(self, panel):
        copy = cp.deepcopy(panel.gamepanel.gridCell)
        self.gamepanel.gridCell = copy
        

    
    def get_monotonicity_value(self):
        mono = [0,0,0,0]
        
        for r in range(4):
            cur = 0
            nextone = cur + 1
            while nextone < 4:
                while nextone < 4 and self.gamepanel.gridCell[r][nextone] > 0:
                    nextone += 1
                    
                if nextone >= 4: nextone-=1
                    
                cur_value, next_value = self.gamepanel.gridCell[r][cur], self.gamepanel.gridCell[r][nextone]
                if cur_value > next_value:
                    mono[0] += next_value - cur_value
                elif next_value > cur_value:
                    mono[1] += cur_value - next_value
                cur = nextone
                nextone += 1
        for c in range(4):
            cur = 0
            nextone = cur + 1
            while nextone < 4:
                while nextone < 4 and self.gamepanel.gridCell[nextone][c] > 0:
                    nextone += 1
                    
                if nextone >= 4: nextone-=1
                    
                cur_value, next_value = self.gamepanel.gridCell[cur][c], self.gamepanel.gridCell[nextone][c]
                if cur_value > next_value:
                    mono[2] += next_value - cur_value
                elif next_value > cur_value:
                    mono[3] += cur_value - next_value
                cur = nextone
                nextone += 1
        return max(mono[0], mono[1]) + max(mono[2], mono[3])

def print_map(gamepanel):
#     print('in print map func')
    print('score: ', gamepanel.score)
    for i in range(4):
        print('[ ', end='')
        for j in range(4):
            print(gamepanel.gridCell[i][j],end=' ')
        print(']')
        

gamepanel =Board()
game2048 = Game( gamepanel)
game2048.start()
print(game2048.gamepanel.gridCell)

DEPTH_LIMIT = 1
LOW_PROBABILITY = 0.000001

def Expect_Mini_Max(score, grid):
    num_of_moves = 0
    dic = ['Up','Down','Left','Right']
#     convert = {0: 'Up',1:'Down', 2:'Left',3:'Right'}
    # while not game2048.is_gameover():
    game_panel = Board()
    game_moni = Game( game_panel)
    game_moni.start()
    game_moni.gamepanel.gridCell = grid
    best_move = find_best_move(game_moni)
    game2048.gamepanel.gridCell = grid
    # print("best move: ", best_move)
    if best_move in dic:
        num_of_moves += 1
        game2048.link_keys(best_move)
        # print_map(game2048.gamepanel)
    return score+game2048.gamepanel.score, game2048.gamepanel.gridCell
    # return game2048.gamepanel.gridCell

        
        
    # if game2048.is_gameover():
    #     print("final number of moves: ", num_of_moves)
#         mb = messagebox.askyesno(title="gameover", message="遊戲結束!\n是否退出遊戲!")
#         if mb:
#             exit()
#         else:
#             game.start()
#             Expect_Mini_Max()
                
def find_best_move(gamepanel):
    best = 0
    bestmove = -1
    movement = ['Up','Down','Left','Right']
    count = 0
    for move in movement:
        score = score_toplevel_move(gamepanel, move)
        count += 1
        if score > best:
            best = score
            bestmove = move
        if count == 4:
            break
#     print('out')
    if bestmove == -1:
#         print('no bestmove')
        for move in movement:
            game_panel_new = Board()
            game_moni_new = Game( game_panel_new)
            game_moni_new.start()
            game_moni_new.copy_data(gamepanel)
            if Move_success(game_moni_new, move):
                bestmove = move
                break
    return bestmove

def score_toplevel_move(gamepanel, move):
    game_panel_new = Board()
    game_moni_new = Game( game_panel_new)
    game_moni_new.start()
    game_moni_new.copy_data(gamepanel)
    game_moni_new.link_keys(move)
    
    if gamepanel.gamepanel.gridCell == game_moni_new.gamepanel.gridCell:
        return 0

    depth = 1
    prob = 1
#     print('loop')
    return score_tile_choose_node(depth, game_moni_new, prob)

def score_tile_choose_node(depth, gamepanel, prob):
    if depth > DEPTH_LIMIT or prob < LOW_PROBABILITY:
#         print('depth: ', depth)
        return expected_value_map(gamepanel)
    
    empty_positions = []
    for r in range(4):
        for c in range(4):
            if gamepanel.gamepanel.gridCell[r][c] == 0:
                empty_positions.append((r,c))
    res = 0
    if len(empty_positions) != 0:
#         print_map(gamepanel.gamepanel)
        prob /= len(empty_positions)
    
    for pos in empty_positions:
        r,c = pos
        game_panel_new = Board()
        game_moni_new = Game( game_panel_new)
        game_moni_new.start()
        game_moni_new.copy_data(gamepanel)
        game_moni_new.gamepanel.gridCell[r][c] = 1
        res += score_after_move(depth, game_moni_new, prob*0.9)
        game_moni_new.gamepanel.gridCell[r][c] = 2
        res += score_after_move(depth, game_moni_new, prob*0.1)
    return res

def score_after_move(depth, gamepanel, prob):
    depth += 1
    best = 0
    movement = ['Up','Down','Left','Right']

    for move in movement:
        
        game_panel_new = Board()
        game_moni_new = Game( game_panel_new)
        game_moni_new.start()
        game_moni_new.copy_data(gamepanel)
        game_moni_new.link_keys(move)
        
        if(game_moni_new.gamepanel.gridCell != gamepanel.gamepanel.gridCell):
#             print('here')
            best = max(best, score_tile_choose_node(depth, game_moni_new, prob))
            
    return best

def expected_value_map(gamepanel):
    empty = gamepanel.get_space_count()
    mono = gamepanel.get_monotonicity_value()
    return  mono + 10 * empty

def Move_success(new_game, move):
    if move == 'Up':
        new_game.link_keys('Up')
        return new_game.gamepanel.moved
    if move == 'Down':
        new_game.link_keys('Down')
        return new_game.gamepanel.moved
    if move == 'Left':
        new_game.link_keys('Left')
        return new_game.gamepanel.moved
    if move == 'Right':
        new_game.link_keys('Right')
        return new_game.gamepanel.moved
    
print_map(game2048.gamepanel)
# Expect_Mini_Max(grid)      

def revive(score, grid):
    row = -1
    col = -1
    # row, col = -1, -1
    max = 0
    
    game_panel_tt = Board()
    game_moni_tt = Game( game_panel_tt)
    game_moni_tt.start()
    game_moni_tt.gamepanel.gridCell = grid
    # return score, game_moni_tt.gamepanel.gridCell


    for r in range(4):
        for c in range(4):
            if game_moni_tt.gamepanel.gridCell[r][c] > max:
                max = game_moni_tt.gamepanel.gridCell[r][c]
                row = r
                col = c
                # row, col = r, c
    
    if row == 0 or row == 3:
        if col == 1:
            if game_moni_tt.gamepanel.gridCell[row][col-1] != 0:
                game_moni_tt.gamepanel.gridCell[row][col-1] = 0
                # game_moni_tt.link_keys('Left')
                return score, game_moni_tt.gamepanel.gridCell
        if col == 2:
            if game_moni_tt.gamepanel.gridCell[row][col+1] != 0:
                game_moni_tt.gamepanel.gridCell[row][col+1] = 0
                # game_moni_tt.link_keys('Right')
                return score, game_moni_tt.gamepanel.gridCell
    if row == 1 or row == 2:
        if row == 1:
            if game_moni_tt.gamepanel.gridCell[row-1][col] != 0:
                game_moni_tt.gamepanel.gridCell[row-1][col] = 0
                # game_moni_tt.link_keys('Up')
                return score, game_moni_tt.gamepanel.gridCell
        if row == 2:
            if game_moni_tt.gamepanel.gridCell[row+1][col] != 0:
                game_moni_tt.gamepanel.gridCell[row+1][col] = 0
                # game_moni_tt.link_keys('Down')
                return score, game_moni_tt.gamepanel.gridCell
    if (row == 0 or row == 3) and (col == 0 or col == 3):
        if row == 0:
            game_moni_tt.gamepanel.gridCell[row+1][col] = 0
        if row == 3:
            game_moni_tt.gamepanel.gridCell[row-1][col] = 0
    return score, game_moni_tt.gamepanel.gridCell

def find_target(grid, target):
    for r in range(4):
        for c in range(4):
            if grid[r][c] == target:
                return True
    return False






