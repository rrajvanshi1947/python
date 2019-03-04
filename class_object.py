import random
import time 

class Ssn:
    random.seed(time.time()

    ssn = random.randrange(1000000000,9999999999)

    def changeSsn(self): 
        self.ssn = random.randrange(1000000000,9999999999)
        print(self.ssn)

    def printSsn(self):
        print(self.ssn)

employee1SSN = Ssn()
employee1SSN.printSsn()
employee1SSN.changeSsn()
employee2SSN = Ssn()
employee2SSN.printSsn()
employee2SSN.changeSsn()    
