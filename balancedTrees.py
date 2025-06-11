# By Alana Wesly, 06/10/2025. ICS 311 Assignment 2, Balanced Trees.
# Olelo Noeau excepts found at https://oleloworkshop.weebly.com/uploads/2/4/0/7/24075835/%CA%BB%C5%8Clelo_no%CA%BBeau.pdf
# No olelo hawaii explanations were found for the sayings, so they are left out.

# node and binary search tree structure
class Node:
    # olelo explanation could be easily added (if usable, if olelo explanations are found)
    def __init__(self, saying, translation, explanation):
        self.saying = saying
        self.translation = translation
        self.explanation = explanation
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, saying, translation, explanation):
        new_node = Node(saying, translation, explanation)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)
    
    def member(self, saying):
        return self._member_recursive(self.root, saying)
    
    def first(self):
        if self.root is None:
            return None
        return self._first_recursive(self.root)
    
    def last(self):
        if self.root is None:
            return None
        return self._last_recursive(self.root)
    
    def predecessor(self, saying):
        if self.root is None:
            return None
        return self._predecessor_recursive(self.root, saying)

    def successor(self, saying):
        if self.root is None:
            return None
        return self._successor_recursive(self.root, saying)
    
    def meHua(self, word):
        return self._meHua_recursive(self.root, word)
    
    def withWord(self, word):
        return self._withWord_recursive(self.root, word)

    # helper functions for the binary search tree
    def _insert_recursive(self, current, new_node):
        if new_node.saying < current.saying:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def _member_recursive(self, current, saying):
        if current is None:
            return False
        if current.saying == saying:
            return True
        elif saying < current.saying:
            return self._member_recursive(current.left, saying)
        else:
            return self._member_recursive(current.right, saying)
        
    def _first_recursive(self, current):    
        if current.left is None:
            return current.saying, current.translation, current.explanation
        else:
            return self._first_recursive(current.left)
        
    def _last_recursive(self, current):
        if current.right is None:
            return current.saying, current.translation, current.explanation
        else:
            return self._last_recursive(current.right)

    def _predecessor_recursive(self, current, saying):
        if current is None:
            return None
        if current.saying == saying:
            if current.left is not None:
                return self._last_recursive(current.left)
            else:
                return None
        elif saying < current.saying:
            return self._predecessor_recursive(current.left, saying)
        else:
            pred = self._predecessor_recursive(current.right, saying)
            return pred if pred else current.saying, current.translation, current.explanation
        
    def _successor_recursive(self, current, saying):
        if current is None:
            return None
        if current.saying == saying:
            if current.right is not None:
                return self._first_recursive(current.right)
            else:
                return None
        elif saying < current.saying:
            succ = self._successor_recursive(current.left, saying)
            return succ if succ else current.saying, current.translation, current.explanation
        else:
            return self._successor_recursive(current.right, saying)
        
    def _meHua_recursive(self, current, word):
        if current is None:
            return []
        results = []
        word_lower = word.lower()
        if (word_lower in current.saying.lower() or 
            word_lower in current.translation.lower() or 
            word_lower in current.explanation.lower()):
            results.append((current.saying, current.translation, current.explanation))
        results.extend(self._meHua_recursive(current.left, word))
        results.extend(self._meHua_recursive(current.right, word))
        return results

    def _withWord_recursive(self, current, word):
        if current is None:
            return []
        results = []
        word_lower = word.lower()
        if (word_lower in current.saying.lower() or 
            word_lower in current.translation.lower() or 
            word_lower in current.explanation.lower()):
            results.append((current.saying, current.translation, current.explanation))
        results.extend(self._withWord_recursive(current.left, word))
        results.extend(self._withWord_recursive(current.right, word))
        return results

# instance of binary search tree to add the phrases to
olelo_noeau_tree = binarySearchTree()

# list of phrases and their translations
olelo_noeau_tree.insert(
    "E kaupē aku nō i ka hoe a kō mai.",
    "Put forward the paddle and draw it back.",
    "Go on with the task that is started and finish it.")
olelo_noeau_tree.insert(
    "Hoʻokahi nō lā o ka malihini.",
    "A stranger only for a day.",
    "After the first day as a guest, one must help with the work.")
olelo_noeau_tree.insert(
    "Aloha kekahi i kekahi.",
    "Love one another.",
    "")
olelo_noeau_tree.insert(
    "He aliʻi ka ʻāina, he kauā ke kanaka.",
    "The land is a chief; man is its servant.",
    "Land has no need for man, but man needs the land and works it for a livelihood. We have to take care of the land.")
olelo_noeau_tree.insert(
    "ʻO ke kahua ma mua, ma hope ke kūkulu.",
    "The site first, and then the building.",
    "Learn all you can, then practice.")
olelo_noeau_tree.insert(
    "I ka ʻōlelo nō ke ola, i ka ʻōlelo nō ka make.",
    "Life is in speech; death is in speech.",
    "Words can heal; words can destroy. Be careful with what you say. It can lead to good and bad consequences.")

# testing the binary search tree functionality. with added spaces for readability
print("\n")

# expected result - First saying: ('Aloha kekahi i kekahi.', 'Love one another.', '')
print("First saying:", olelo_noeau_tree.first()) 
print("\n")

# expected result - Last saying: ('ʻO ke kahua ma mua, ma hope ke kūkulu.', 'The site first, and then the building.', 'Learn all you can, then practice.')
print("Last saying:", olelo_noeau_tree.last())
print("\n")

# expected result - Member 'E kaupē aku nō i ka hoe a kō mai.': True
print("Member 'Aloha kekahi i kekahi.':", olelo_noeau_tree.member("Aloha kekahi i kekahi."))
print("\n")

# expected result - Predecessor of 'He aliʻi ka ʻāina, he kauā ke kanaka.': ('E kaupē aku nō i ka hoe a kō mai.', 'Put forward the paddle and draw it back.', 'Go on with the task that is started and finish it.')
print("Predecessor of 'He aliʻi ka ʻāina, he kauā ke kanaka.':", olelo_noeau_tree.predecessor("He aliʻi ka ʻāina, he kauā ke kanaka."))
print("\n")

# expected result - Successor of 'E kaupē aku nō i ka hoe a kō mai.': ('He aliʻi ka ʻāina, he kauā ke kanaka.', 'The land is a chief; man is its servant.', 'Land has no need for man, but man needs the land and works it for a livelihood. We have to take care of the land.')
print("Successor of 'E kaupē aku nō i ka hoe a kō mai.':", olelo_noeau_tree.successor("E kaupē aku nō i ka hoe a kō mai."))
print("\n")

# expected result - Me Hua 'aloha': [('Aloha kekahi i kekahi.', 'Love one another.', '')]
print("Me Hua 'aloha':", olelo_noeau_tree.meHua('aloha'))
print("\n")

# expected result - With Word 'ka': [('E kaupē aku nō i ka hoe a kō mai.', 'Put forward the paddle and draw it back.', 'Go on with the task that is started and finish it.'), ('Aloha kekahi i kekahi.', 'Love one another.', ''), ('Hoʻokahi nō lā o ka malihini.', 'A stranger only for a day.', 'After the first day as a guest, one must help with the wkahi i kekahi.', 'Love one another.', ''), ('Hoʻokahi nō lā o ka malihini.', 'A stranger only for a day.', 'After the first day as a guest, one must help with the work.'), ('He aliʻi ka ʻāina, he kauā ke kanaka.', 'The land is a chief; man is its servant.', 'Land has no need for man, but man needs the land and works it for a livelihood. We have to take care of the land.'), ('ʻO ke kahua ma mua, ma hope ke kūkulu.', 'The site first, and then the building.', 'Learn all you can, then practice.'), ('I ka ʻōlelo nō ke ola, i ka ʻōlelo nō ka make.', 'Life is in speech; death is in speech.', 'Words can heal; words can destroy. Be careful with what you say. It can lead to good and bad consequences.')]
print("With Word 'ka':", olelo_noeau_tree.withWord('ka'))
print("\n")
