    
class Time:
    def __init__(self,seconds):
        self.s = seconds
        self.min = 0
        self.secmin = 0
        self.hrs = 0
        self.minhrs = 0
        self.sechrs = 0
              
    def convert_to_minuites(self):
        self.min = int(self.s/60)
        self.secmin = self.s%60
        return ("if seconds is {}, then minuites:seconds is {}:{}".format(self.s,self.min,self.secmin))
    def convert_to_hours(self):
        self.hrs = int((self.s)/3600)
        self.minhrs = int((self.s/60)-60)
        self.sechrs = (self.s%60)
        return ("if seconds is {}, then hours:minuites:seconds is {}:{}:{}".format(self.s,self.hrs,self.minhrs,self.sechrs))

seconds = int(input("Enter the value of seconds you want to convert: "))
specify = input("Do you want to convert the seconds into (minutes) or (hours): ")

if seconds>=0:
    if specify.lower() == 'minuites':
        if seconds >= 3600:
            print("\n\nPlease use the hours conversion because {} can be easily converted into hours".format(seconds))
        elif seconds < 3600:
            call = print("\n\n",Time(seconds).convert_to_minuites())
            
    elif specify.lower() == 'hours':
        if seconds >= 3600:
            call = print("\n\n",Time(seconds).convert_to_hours())
        elif seconds < 3600:
            print("\n\nPlease use the minuites conversion, \nbecause {} converted to hours is zero(0).\n{} can be easily converted into minuites".format(seconds,seconds))
    else:
        print("\n\nPlease enter a correct quantity to convert to (either minuites or hours)")
elif seconds<0:
    if specify == 'minuites' or specify == 'hours':
        print("\n\nDo not use negative numbers for seconds")
    else:
        print("\n\nDo not use negative numbers for seconds.\nAlso check the quantity you want convert to (either minuites or hours)")


      
        
        
        
        
