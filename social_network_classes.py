import json

class SocialNetwork:
    def __init__(self):
        self.list_of_people = []

    def save_social_media(self):
        with open('social_network.json', 'w') as file:
            data = [person.__dict__ for person in self.list_of_people]
            json.dump(data, file)

    def reload_social_media(self):
        with open('social_network.json', 'r') as file:
            data = json.load(file)
            self.list_of_people = [Person(**person) for person in data]

    def create_account(self):
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        person = Person(name, age)
        self.list_of_people.append(person)
        print("Account created successfully!")


class Person:
    def __init__(self, id, year, friendlist = None, messages = None, blocklist = None):
        self.id = id
        self.year = year
        self.friendlist = friendlist if friendlist else []
        self.messages = messages if messages else []
        self.block_list = blocklist if blocklist else []

    def add_friend(self, ai_social_network, friend_id):
        # Check if friend_id exists in ai_social_network's list_of_people
        if any(person.id == friend_id for person in ai_social_network.list_of_people):
            if friend_id not in self.friendlist:
                self.friendlist.append(friend_id)
                print(f"{friend_id} added to your friend list.")
            else:
                print(f"{friend_id} is already in your friend list.")
        else:
            print("Friend not found.")

    def block_friend(self, friend_id):
        if friend_id in self.friendlist:
            self.friendlist.remove(friend_id)
            self.block_list.append(friend_id)
            print(f"{friend_id} has been blocked and removed from your friend list.")
        else:
            print(f"{friend_id} is not in your friend list.")
        
    def view_friend_list(self):
        if self.friendlist:
            print("Here is ALL of your friends:")
            for friend_id in self.friendlist:
                print(friend_id)
        else:
            print("You got no friends loner")

    def send_message(self, ai_social_network, friend_id, message):
        if friend_id in self.friendlist:
            for person in ai_social_network.list_of_people:
                if person.id == friend_id:
                    person.messages.append({'from': self.id, 'message': message})
                    print("Message sent successfully!")
                    return
        print("Message sending failed. Friend not found or not in your friend list.")