class Node :
  def __init__(self,data):
    self.data = data
    self.right = None
    self.left = None

  def add_node(self,new_data,old_data, yes_no):
    if old_data == self.data:
      new_node = Node(new_data)
      if yes_no == "1":
        self.right = new_node
      if yes_no == "2":
        self.left = new_node
    else:
      if self.right != None:
        self.right.add_node(new_data,old_data, yes_no) 
      if self.left != None:
        self.left.add_node(new_data,old_data, yes_no)



class BinaryTree:
  def __init__(self):
    self.first_node = None
    self.current_node = self.first_node

  def add_dataTree(self, new_data,old_data, yes_no):
    if self.first_node == None:
      self.first_node = Node(new_data)
    else:
      self.first_node.add_node(new_data,old_data, yes_no)

  def get_questionTree(self):
    if self.current_node == None:
      self.current_node = self.first_node
    return self.current_node.data

  def send_answerTree(self, answer):

    if answer == "1":
      self.current_node = self.current_node.right

    elif answer == "2" :
      self.current_node = self.current_node.left

    elif answer == "reset":
      self.current_node = self.first_node
      return "C'est fini"

    if self.current_node == None:
      self.current_node = self.first_node 
      return "C'est fini"

    return self.current_node.data
  
  
Discussion = BinaryTree()
Discussion.add_dataTree("Aimez-vous les plats épicés ?(1:Oui / 2:Non)", "", "")

Discussion.add_dataTree("Préférez-vous la cuisine asiatique?(1:Oui / 2:Non)", "Aimez-vous les plats épicés ?(1:Oui / 2:Non)", "1")
Discussion.add_dataTree("Préférez-vous la cuisine italienne?(1:Oui / 2:Non)", "Aimez-vous les plats épicés ?(1:Oui / 2:Non)", "2")

Discussion.add_dataTree("Aimez-vous le poisson?(1:Oui / 2:Non)", "Préférez-vous la cuisine asiatique?(1:Oui / 2:Non)", "1")
Discussion.add_dataTree("Préférez-vous les pâtes?(1:Oui / 2:Non)", "Préférez-vous la cuisine asiatique?(1:Oui / 2:Non)", "2")

Discussion.add_dataTree("Essayez la cuisine japonaise!🍣", "Aimez-vous le poisson?(1:Oui / 2:Non)", "1")
Discussion.add_dataTree("Essayez la cuisine chinoise!🥡", "Aimez-vous le poisson?(1:Oui / 2:Non)", "2")

Discussion.add_dataTree("Essayez la pizza italienne!🍕", "Préférez-vous les pâtes?(1:Oui / 2:Non)", "1")
Discussion.add_dataTree("Essayez les lasagnes!🍝", "Préférez-vous les pâtes?(1:Oui / 2:Non)", "2")

Discussion.add_dataTree("C'est fini!", "Essayez la cuisine japonaise!🍣", "")
Discussion.add_dataTree("C'est fini!", "Essayez la cuisine chinoise!🥡", "")
Discussion.add_dataTree("C'est fini!", "Essayez la pizza italienne!🍕", "")
Discussion.add_dataTree("C'est fini!", "Essayez les lasagnes!🍝", "")