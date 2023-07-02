# David Wu
# Week 1 Project Main

from social_network_classes import SocialNetwork, Person
import social_network_ui

ai_social_network = SocialNetwork()

if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")

    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            user_id = input("\nEnter your ID to manage your account: ")
            user = next((person for person in ai_social_network.list_of_people if person.id == user_id), None)

            if user:
                while True:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

                    if inner_menu_choice == "1":
                        new_id = input("\nEnter new ID: ")
                        new_year = int(input("Enter new age: "))
                        user.id = new_id
                        user.year = new_year
                        print("Account updated succesfuly")

                    elif inner_menu_choice == "2":
                        friend_id = input("\nEnter friend's ID: ")
                        user.add_friend(ai_social_network, friend_id)

                    elif inner_menu_choice == "3":
                        friend_id = input("\nEnter friend's ID: ")
                        message = input("Enter your message: ")
                        user.send_message(ai_social_network, friend_id, message)


                    elif inner_menu_choice == "4":
                        for message in user.messages:
                            print(f"From {message['from']}: {message['message']}")
                    
                    elif inner_menu_choice == "5":
                        user.view_friend_list()

                    elif inner_menu_choice == "6":
                        friend_id = input("\nEnter friend's ID to block: ")
                        user.block_friend(friend_id)

                    elif inner_menu_choice == "7":
                        break

                    else:
                        print("Invalid option. Try Again!")

            else:
                print("\nUser not found.")

        elif choice == "3":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Your input is invalid. Try Again!")

        choice = social_network_ui.mainMenu()
