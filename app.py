import user
import login
import time

def main():
    print("heloo")
    
    users = user.User("alaa", 12456)
    
    print(users)
    
    mt5 = login.LoguinMt5("aa",12,4,time.localtime,False)
    
    print(mt5.server)
    mt5.logar()
    
    
    
    
if __name__ == "__main__":
    main()