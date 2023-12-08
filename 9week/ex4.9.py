class Family:
    def __init__(self, data):
        self.item = data
        self.son = None
        self.dad = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        if self.head == None:
            return 0
        else:
            member = self.head
            size = 1
            while member.son is not None:
                member = member.son
                size += 1
            return size

    def add(self, data, index=None):
        if self.head is None:
            new_member = Family(data)
            self.head = new_member
        else:
            if index == None:
                member = self.head
                while member.son is not None:
                    member = member.son
                new_member = Family(data)
                member.son = new_member
                new_member.dad = member
            elif index >= len(self):
                print('The index exceeds the length of the list')
            else:
                last_member = self.head
                member_index = 0
                while member_index <= index:
                    if member_index == index:
                        member = last_member
                        break
                    member_index += 1
                    last_member = last_member.son
                new_member = Family(data)
                new_member.son = member
                new_member.dad = member.dad
                if member.dad is not None:
                    member.dad.son = new_member
                member.dad = new_member

    def kick(self, index=None):
        if self.head is None:
            print("List is empty")
        else:
            if index == None:
                member = self.head
                while member.son is not None:
                    member = member.son
                if member.dad is not None:
                    member.dad.son = None
                else:
                    self.head = None
            elif index >= len(self):
                print('The index exceeds the length of the list')
            else:
                last_member = self.head
                member_index = 0
                while member_index <= index:
                    if member_index == index:
                        member = last_member
                        break
                    member_index += 1
                    last_member = last_member.son
                if member.dad is not None and member.son is not None:
                    member.dad.son = member.son
                    member.son.dad = member.dad
                elif member.dad is not None:
                    member.dad.son = None
                elif member.son is not None:
                    member.son.dad = None
                else:
                    self.head = None

    def value(self, index=None):
        if self.head is None:
            print("List is empty")
            return ''
        elif index == None:
            return self.head.item
        elif index >= len(self):
            print('The index exceeds the length of the list')
        else:
            last_member = self.head
            member_index = 0
            while member_index <= index:
                if member_index == index:
                    break
                member_index += 1
                last_member = last_member.son
            return last_member.item

    def print(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            ans = []
            member = self.head
            while member is not None:
                ans.append(member.item)
                member = member.son
            print(*ans)


DLL = DoublyLinkedList()
print('Enter list items')
data = list(input().split())
for elem in data:
    DLL.add(elem)
print(f'Number of elements in the list: {len(DLL)}')
print('Enter the value of the element and the index where to insert it as: value, index')
add_elem = list(map(int, input().split()))
DLL.add(add_elem[0], add_elem[1])
DLL.print()
print('Enter the index of the element you want to delete as: index')
index = int(input())
print(f'The value of the element with the index {index}: {DLL.value(index)}')
DLL.kick(index)
DLL.print()
