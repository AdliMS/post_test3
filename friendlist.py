import os

# kelas FriendList merepresentasikan list in game.
class FriendList:

    # kelas FriendNode merepresentasikan node pada linked list. 
    class FriendNode:

        # constructor untuk kelas FriendNode
        def __init__(self, name, id_char, level, total_achievement):
            self.name = name
            self.id_char = id_char
            self.level = level
            self.total_achievement = total_achievement
            self.next = None

    # constructor untuk kelas FriendList
    def __init__(self):
        self.head = None
        
    # fungsi untuk menambahkan teman baru
    def add_friend(self, name, id_char, level, total_achievement):
        new_friend = self.FriendNode(name, id_char, level, total_achievement)
        if self.head == None:
            self.head = new_friend
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_friend

    # fungsi untuk menghapus teman dari daftar
    def remove_friend(self, name):
        if self.head == None:
            return
        
        if self.head.name == name:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next != None:
            if current.next.name == name:
                current.next = current.next.next
                return
            current = current.next

    # fungsi untuk melihat output list pertemanan in game.
    def print_friends(self):
        result = []
        current = self.head

        if self.head == None:
            return 'Friend list is empty. Go get a friend!'
        
        while current != None:
            result.append(current.name)
            current = current.next
        return ', '.join(result)
    
    # fungsi untuk melihat output seorang teman beserta atributnya.
    def print_detail(self, name):
        if self.head == None:
            return 'Friend list is empty. Go get a friend!'

        current = self.head
        while current != None:
            if current.name == name:
                friend = f"Name: {current.name}\nID: {current.id_char}\nLevel: {current.level}\nTotal Achievement: {current.total_achievement}"
                return friend
            current = current.next
    
myFriends = FriendList()

os.system('cls')
null = False
while not (null):
    
    os.system('cls')
    print(f'IN GAME FRIEND LIST \n \
        1. Show friend list \n \
        2. Show detailed info about a friend \n \
        3. Add friend \n \
        4. Unfriend ')
    try:
        usr_input = int(input('Select your need : '))

        if usr_input == 1:
            os.system('cls')
            print(myFriends.print_friends())

            null = input('More? (y/n) : ')
            if null == 'y':
                null = False
            else:
                print('Byeee~')
                null = True

        elif usr_input == 2:

            os.system('cls')
            name = input('Type the name : ')
            print(myFriends.print_detail(name))

            null = input('More? (y/n) : ')
            if null == 'y':
                null = False
            else:
                print('Byeee~')
                null = True

        elif usr_input == 3:

            os.system('cls')
            name = input('Name : ')
            id_char = int(input('ID : '))
            level = int(input('Level : '))
            avt = int(input('Total achievement : '))

            myFriends.add_friend(name, id_char, level, avt)

            null = input('More? (y/n) : ')
            if null == 'y':
                null = False
            else:
                print('Byeee~')
                null = True

        elif usr_input == 4:
            
            os.system('cls')
            unfriend = input('Input the name you want to unfriend : ')
            myFriends.remove_friend(unfriend)

            null = input('More? (y/n) : ')
            if null == 'y':
                null = False
            else:
                print('Byeee~')
                null = True

    except TypeError:
        print('Wrong input!')
        null = True

