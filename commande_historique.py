class CommandeNode:
  def __init__(self , data):
    self.data = data
    self.next_node = None

class chained_list :
  def __init__(self):
    self.first_node = None
    self.length = 0

  def append(self, data):

    self.length += 1
    current_node = self.first_node
    if current_node == None:
      self.first_node = CommandeNode(data)
      return

    while current_node.next_node != None:
      current_node = current_node.next_node

    current_node.next_node = CommandeNode(data)

  def get(self,id):
    if id > self.length or id < 0:
      return
    i = 0
    current_node = self.first_node
    while i < id :
      current_node = current_node.next_node
      i += 1
    return current_node.data

  def search(self,value):
    current_node = self.first_node

    while current_node != None:
      if current_node.data == value:
        return True
      current_node = current_node.next_node

    return False



  def insert(self,data,id):
    if self.length < id or id < 0:
      return

    i = 1
    current_node = self.first_node
    while i < id:
      current_node = current_node.next_node
      i += 1

    New_node = CommandeNode(data)
    New_node.next_node = current_node.next_node
    current_node.next_node = New_node
    self.length += 1
    
  def derniere(self):
    return self.get(self.length-1)


  def tout_afficher(self):
    all_commands = []
    current_node = self.first_node
    while current_node:
        all_commands.append(current_node.data)
        current_node = current_node.next_node
    return all_commands
  
  # vider une liste chainée
  def vider(self):
    self.first_node = None
    self.length = 0
    return self.first_node