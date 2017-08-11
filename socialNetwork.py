class User():
    def __init__(self, n):
        self.name = n
        self.friend = []

    def __str__(self):
        friends = ""
        if len(self.friend) > 0:
            for user in range(len(self.friend) - 1):
                friends += self.friend[user].name + ", "
            friends += self.friend[len(self.friend) - 1].name
        info = "Name: " + self.name + "\tFriend(s): " + friends
        return info

    def addFriend(self, userName):
        self.friend.append(userName)

    def getName(self):
        return self.name

    def getFriends(self):
        friends = ""
        for user in range(len(self.friend) - 1):
            friends += user.name + ", "
        friends += self.friend[len(self.friend) - 1].name
        return friends

    def write(self):
        friends = ""
        if len(self.friend) > 0:
            for user in range(len(self.friend) - 1):
                friends += self.friend[user].name + ", "
            friends += self.friend[len(self.friend) - 1].name
        info = "User: " + self.name + "\tFriend(s): " + friends
        return info

class Network():
    def __init__(self):
        self.userList = []

    def __str__(self):
        string = ""
        for users in self.userList:
            string += users.write() + "\n"
        return string


    def getUser(self, userName):
        for person in self.userList:
            if person.name == userName:
                return person
        return None

    def addUser(self, userName):
        for person in self.userList:
            if userName.name == person.name:
                return False
        self.userList.append(userName)
        return True

    def addFriendship(self, person1, person2):
        found = 0
        for person in self.userList:
            if person.name == person1:
                person_1 = person
                found += 1
            if person.name == person2:
                person_2 = person
                found += 1
        if found == 2:
            if not person_1 in person_2.friend:
                person_2.addFriend(person_1)
            if not person_2 in person_1.friend:
                person_1.addFriend(person_2)

    def connections(self, person1, person2):
        notExplored = {}
        notExplored = set(notExplored)
        person_1 = self.getUser(person1)
        for users in self.userList:
            notExplored.add(users.name)
        dist = {}
        for users2 in self.userList:
            if users2 == person_1:
                dist[users2.name] = 0
            else:
                dist[users2.name] = 1000
        prev = {}
        for users3 in self.userList:
            prev[users3.name] = None

        shortestDist = person1
        checker = True
        while len(notExplored) > 0:
            for item in dist:
                if item in notExplored and checker == False:
                    shortestDist = item
                    checker = True
                if dist[item] < dist[shortestDist] and item in notExplored:
                    shortestDist = item
            shortest = self.getUser(shortestDist)
            notExplored.discard(shortestDist)
            for person in shortest.friend:
                if (dist[shortest.name] + 1) < dist[person.name]:
                    dist[person.name] = dist[shortest.name] + 1
                    prev[person.name] = shortest.name
            checker = False
        conInfo = person1 + " is " + str(dist[person2]) + " connection(s) away from " + person2
        conInfo2 = ""
        start = person2
        conInfo2 += person1
        for i in range(dist[person2]):
            conInfo2 += " -> " + start
            start = prev[start]
        return conInfo + "\n" + conInfo2

def main():
    n = Network()
    while True:
        print("Press 'u' to add a user\nPress 'f' to add a friendship\nPress 'v' to view a user\nPress 'c' to view the connection between two users\nPress 'n' to view the network")
        ans = input("Choice: ")

        if ans == 'u':
            user = input("Enter a user name: ")
            newUser = User(user)
            n.addUser(newUser)

        if ans == 'f':
            user1 = input("Enter the name of the first person: ")
            user2 = input("Enter the name of the second person: ")
            n.addFriendship(user1, user2)

        if ans == 'v':
            user = input("Enter the user you'd like to view: ")
            a = n.getUser(user)
            print("")
            print(a)
            print("")

        if ans == 'c':
            user1 = input("Enter the name of the first person: ")
            user2 = input("Enter the name of the second person: ")
            print("")
            print(n.connections(user1, user2))
            print("")

        if ans == 'n':
            print("")
            print(n)

        if ans == 'q':
            break

main()
