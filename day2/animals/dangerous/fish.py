class Fish: 
    def __init__(self): 
        ''' Constructor for this class. ''' 
        # Create some member animals 
        self.members = ['evil Trout', 'evil Shark', 'evil Goldfish'] 
  
  
    def printMembers(self): 
        print ('Printing members of Fish class...') 
        for member in self.members: 
           print('\t%s ' % member)
