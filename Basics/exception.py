while(1):
    num = input('Input the number!\n')
    try:
        print(4, num)  
    except NameError:
        print('You are supposed to enter a number.')
    except ZeroDivisionError:
        print("Can't divide by zero.")
    except:
        print('Exception occured')
    finally:
        print('Done with the loop')    
