class Node:
  def __init__(self, value) -> None:
    self.value = value
    self.left  = None
    self.right = None

class BST:
  def __init__(self) -> None:
    self.root = None

  def insert(self,value) -> bool:
    new_node = Node(value)
    if self.root is None: 
      self.root = new_node
      return True
    
    temp = self.root
    while True:
      if new_node.value == temp.value: 
        return False
      if new_node.value < temp.value:
        if temp.left is None:
          temp.left = new_node
          return True
        temp = temp.left
      else:
        if temp.right is None:
          temp.right = new_node
          return True
        temp = temp.right

  def BSF(self) -> list:
    temp = self.root
    queue = []
    result = []
    queue.append(temp)

    while len(queue) > 0:
      temp = queue.pop(0)
      if temp is None:
        result.append(None)
      else:
        result.append(temp.value)
        if temp.left is not None:
          queue.append(temp.left)
        if temp.right is not None:
          queue.append(temp.right)
    return result
  
  def complete_BSF(self) -> list :
    temp = self.root
    queue = []
    result = []
    queue.append(temp)

    while len(queue) > 0:
      temp = queue.pop(0)
      if temp is None:
        result.append(None)
      else:
        result.append(temp.value)
        if temp.left is not None:
          queue.append(temp.left)
        else:
          if temp.right is not None or temp.left is not None:
            queue.append(None)
        if temp.right is not None:
          queue.append(temp.right)
        else:
          if temp.right is not None or temp.left is not None:
            queue.append(None)
    return result

  def height(self, *args) -> int:
    if len(args) == 0:
      temp= self.complete_BSF()
    else:
      temp = args[0]
    size = 0
    while len(temp) > 0 and size < 50:
      temp = temp[(2**size):]
      size += 1
    return size
  
  def display(self) -> None:
    temp = self.complete_BSF()
    size = self.height(temp)
    space_size = (2 ** (size +1 ))
    for i in range(size*2 - 1):
      if i %2 ==0:
        i = i // 2
        for _ in range(2**i):
          if len(temp) > 0:
            x = temp.pop(0)
            if x is not None:
              print(str(x).center(space_size," "), end="")
            else:
              print(".".center(space_size," "), end="")
          else: break
        print()
        space_size = space_size // 2
      else:
        x = space_size//2 -1
        i = (i+1) // 2
        k = 0
        for _ in range(2**i):
          if k == 0:
            if temp[_] is not None:
              print(" "*x,"/","▔"*x,sep="", end=" ")
            else :
              print(" "*(2*x), end="  ")
            k = 1
          else: 
            if temp[_] is not None:
              print("▔"*x,"\\"," "*x,sep="", end=" ")
            else :
              print(" "*(2*x), end="  ")
            k = 0
        print()

  def dfs_pre_order(self) -> list:
      results = []
      def traverse(current_node):
          results.append(current_node.value)
          if current_node.left is not None:
              traverse(current_node.left)
          if current_node.right is not None:
              traverse(current_node.right)
      traverse(self.root)
      return results
  
  def dfs_post_order(self) -> list:
      results = []
      def traverse(current_node):
          if current_node.left is not None:
              traverse(current_node.left)
          if current_node.right is not None:
              traverse(current_node.right)
          results.append(current_node.value)
      traverse(self.root)
      return results

  def dfs_in_order(self) -> list:
      results = []
      def traverse(current_node):
          if current_node.left is not None:
              traverse(current_node.left)
          results.append(current_node.value) 
          if current_node.right is not None:
              traverse(current_node.right)          
      traverse(self.root)
      return results
  
tree = BST()

# Example 1
# tree.insert(47)
# tree.insert(21)
# tree.insert(76)
# tree.insert(18)
# tree.insert(27)
# tree.insert(52)
# tree.insert(82)

# Example 2
tree.insert(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(17)
tree.insert(19)
tree.insert(27)
tree.insert(28)
tree.insert(26)
tree.insert(52)
tree.insert(51)
tree.insert(53)
tree.insert(82)
tree.insert(81)
tree.insert(83)

print(tree.BSF())
print("height" ,tree.height())
tree.display()
print("DFS Preorder", tree.dfs_pre_order())
print("DFS Preorder", tree.dfs_post_order())
print("DFS Inorder", tree.dfs_in_order())


"""
    EXPECTED OUTPUT 1:
    ----------------
    [47, 21, 76, 18, 27, 52, 82]
    height 3
          47       
      /▔▔ ▔▔\    
      21       76   
    /▔ ▔\   /▔ ▔\  
    18   27  52    82 
    DFS Preorder [47, 21, 18, 27, 76, 52, 82]
    DFS Preorder [18, 27, 21, 52, 82, 76, 47]
    DFS Inorder [18, 21, 27, 47, 52, 76, 82]
    -----------------
    EXPECTED OUTPUT 2:
    ----------------
    [47, 21, 76, 18, 27, 52, 82, 17, 19, 26, 28, 51, 53, 81, 83]
    height 4
                   47
           /▔▔▔▔ ▔▔▔▔\
          21                76
      /▔▔ ▔▔\        /▔▔  ▔▔\
      18        27      52         82
    /▔ ▔\   /▔ ▔\   /▔ ▔\   /▔ ▔\
    17  19   26    28  51    53 81    83
    DFS Preorder [47, 21, 18, 17, 19, 27, 26, 28, 76, 52, 51, 53, 82, 81, 83]
    DFS Preorder [17, 19, 18, 26, 28, 27, 21, 51, 53, 52, 81, 83, 82, 76, 47]
    DFS Inorder [17, 18, 19, 21, 26, 27, 28, 47, 51, 52, 53, 76, 81, 82, 83]
    -----------------
"""