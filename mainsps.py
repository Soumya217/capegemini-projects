from SPS import game
from SPS import play
def show_menu():
    print("\n========Stone,Paper,Scissors Shoot!========")
    print("1.Play Game")
    print("2.Exit")

def main():
    while True:
        show_menu()

        choice=input("enter your choice:")

        if choice=='1':
            play()
        elif choice=='2':
            print("Thank You for visiting!")
        else:
            print("invalid choice!")
if __name__=="__main__":
    main()
