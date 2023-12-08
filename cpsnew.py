from threading import Timer

class CPS():
    
    def __init__(self):
        self.choose = 5    
        self.num = 0
        self.cps = 0
        self.status = False
        self.cpstrack = Timer(5, self.pcps)

    def pcps(self):
        self.status = True
        self.cps = self.num/5
        self.cps = str(self.cps)

    def runcps(self):
        self.cpstrack.start()
        self.num += 1
    
    def numadd(self):
        self.num += 1