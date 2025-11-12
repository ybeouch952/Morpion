class Player:
    def __init__(self,symbol,index,size):
        self.symbol = symbol
        self.index = index
        self.size = size
        self.lins = [0]*size
        self.cols = [0]*size
        self.diag = 0
        self.diag2 = 0
    
    def update_counters(self,line,col):
        self.lins[line] += 1
        self.cols[col] += 1
        if line == col :
            self.diag += 1
        if line + col == self.size - 1 :
            self.diag2 +=1 
    
    def has_won(self,line,col) :
        if self.lins == self.size :
            return True
        if self.cols == self.size :
            return True
        if line == col and self.diag == self.size:
            return True
        if line+col == self.size - 1 and self.diag2 == self.size:
            return True
        return False
    