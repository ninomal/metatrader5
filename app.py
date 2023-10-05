import user
import login
def main():
    print("heloo")
    
    users = user.User("alaa", 12456)
    
    print(users)
    
    logar = login.LoguinMt5("aa",12,4,5)
    
    print(logar.server)
    logar.logar()
    
    
    
    
if __name__ == "__main__":
    main()