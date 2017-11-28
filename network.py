import operator

class Node:
    """helper class
    a node to help with defining each member of the node

    ====Public Attributes ====
    :type name: str
        Name of Member
    :type sponsor: str
        Name of that member's sponsor
    :type mentor: str
        Name of that member's sponsor
    :type children: list
        list containing the name of each member's children
    :type assets: int
        Number of assets that member has
    """

    def __init__(self, name, sponsor, assets, next_=None):
        """
        Create a new Node self

        :type self: Node
        :type line: str
            Line of text
        :rtype: None
        """
        self.name = name
        self.sponsor = sponsor
        self.assets = assets
        self.children = []
        self.mentor = None
        self.next_ = None

    def __str__(self):
        """
        Return a user-friendly representation of this LinkedListNode.

        :rtype: None

        >>> n = Node("Liam", "Emma", 20, Node("Emma", "Liam", 20))
        >>> print(n)
        Liam: 20, sponsor: Emma, mentor: None, children: []
        <BLANKLINE>
        """
        # start with a string s to represent current node.
        s = ""
        #s = "{}: {}, sponsor: {}, mentor: {}, children: {}".format(self.name, self.assets, self.sponsor, self.mentor, self.children)
        # create a reference to "walk" along the list
        # for each subsequent node in the list, build s
        while self is not None:
            s += "{}: {}, sponsor: {}, mentor: {}, children: {}".format(self.name, self.assets, self.sponsor, self.mentor, self.children)
            s += "\n"
            self = self.next_

        return s

class List:
    """
    a chain of Nodes

    === Public Attributes ==
    :type front: Node
         first node of this List
    :type back: Node
         last node of this List
    """

    def __init__(self):
        """
        Create an empty linked list.
        """
        self.front, self.back = None, None

    def append(self, line):
        """
        Insert a new Node with value after self.back.

        :type self: List
        :type line: str
            Line of text
        :rtype: None

        >>> l = List()
        >>> l.append("Liam#20")
        >>> l.append("Emma#Liam#32")
        >>> l.append("Mason#Emma#14")
        >>> print(l)
        Liam: 20, sponsor: None, mentor: None, children: ['Emma']
        Emma: 32, sponsor: Liam, mentor: Liam, children: ['Mason']
        Mason: 14, sponsor: Emma, mentor: Emma, children: []
        <BLANKLINE>
        """

        data = line.split('#')
        if self.front is None:
            new_node = Node(data[0], None, data[1])
        else:
            new_node = Node(data[0], data[1], data[2])

        if self.front is None:
            # append to an empty LinkedList
            self.front = new_node
            self.back = new_node
        else:
            current = self.front
            while (current.name != data[1]):
                current = current.next_
            if len(current.children) == 0:
                new_node.mentor = current.name
            else:
                new_node.mentor = current.children[-1]
            current.children.append(new_node.name)
            new_node.sponsor = current.name
            self.back.next_ = new_node
            self.back = new_node

    def __str__(self):
        """
        Return a human-friendly string representation of
        LinkedList self.

        :rtype: str

        >>> l = List()
        >>> l.append("Liam#20")
        >>> l.append("Emma#Liam#32")
        >>> l.append("Mason#Emma#14")
        >>> print(l)
        Liam: 20, sponsor: None, mentor: None, children: ['Emma']
        Emma: 32, sponsor: Liam, mentor: Liam, children: ['Mason']
        Mason: 14, sponsor: Emma, mentor: Emma, children: []
        <BLANKLINE>
        """
        # deal with the case where this list is empty
        if self.front is None:
            assert self.back is None and self.size is 0, "ooooops!"
            return "well something isn't working"
        else:
            # use front.__str__() if this list isn't empty
            return str(self.front)




class Network(object):
    """A pyramid network.

    This class represents a pyramid network. The network topology can be loaded
    from a file, and it can find the best arrest scenario to maximize the seized
    asset.
    
    === Attributes ===

    :type name: str
        Name of Member
    :type sponsor: str
        Name of that member's sponsor
    :type mentor: str
        Name of that member's sponsor
    :type children: list
        list containing the name of each member's children
    :type assets: int
        Number of assets that member has
    """

    def load_log(self, log_file_name):
        """Load the network topology from the log log_file_name.

        :type self: Network
        :type log_file_name: str
            Name of the scenario file
        :rtype: None

        """
        self.thelist = []
        self.tree = {}
        self.somelist = List()
        log_file = open(log_file_name)


        for current_line in log_file:
            self.somelist.append(current_line.strip())

        node = self.somelist.front
        #while node != None:
         #   self.tree[node.name] = 0
          #  node = node.next_

        log_file.close()


    def sponsor(self, member_name):
        """Return the sponsor name of member with name member_name.

        :type self: Network
        :type member_name: str
            Name of the member
        :rtype: str

        >>> network = Network()
        >>> network.load_log("topology1.txt")
        >>> member_name = "Sophia"
        >>> print(member_name + "'s sponsor is " + network.sponsor(member_name))
        Sophia's sponsor is Emma
        """

        current = self.somelist.front
        while (current.name != member_name and current is not None):
            current = current.next_
        if current.sponsor != None:
            return current.sponsor
        else:
            return "None"


    def mentor(self, member_name):
        """Return the mentor name of member with name member_name.

        :type self: Network
        :type member_name: str
            Name of the member
        :rtype: str

        >>> network = Network()
        >>> network.load_log("topology1.txt")
        >>> member_name = "Ethan"
        >>> print(member_name + "'s mentor is " + network.mentor(member_name))
        Ethan's mentor is William
        """

        current = self.somelist.front
        while (current.name != member_name and current is not None):
            current = current.next_
        if current.mentor != None:
            return current.mentor
        else:
            return "None"


    def assets(self, member_name):
        """Return the assets of member with name member_name.

        :type self: Network
        :type member_name: str
            Name of the member
        :rtype: str

        >>> network = Network()
        >>> network.load_log("topology1.txt")
        >>> member_name = "Sophia"
        >>> print(member_name + "'s asset is " + str(network.assets(member_name)))
        Sophia's asset is 5
        """

        current = self.somelist.front
        while (current.name != member_name and current is not None):
            current = current.next_
        return current.assets


    def children(self, member_name):
        """Return the name of all children of member with name member_name.

        :type self: Network
        :type member_name: str
            Name of the member
        :rtype: list

        >>> network = Network()
        >>> network.load_log("topology1.txt")
        >>> member_name = "Sophia"
        >>> print(member_name + "'s children are " + str(network.children(member_name)))
        Sophia's children are []
        """

        current = self.somelist.front
        while (current.name != member_name and current is not None):
            current = current.next_
        return current.children


    def best_arrest_order(self, maximum_arrest):
        """Search for list of member names in the best arrest scenario that
        maximizes the seized assets. Consider all members as target zero,
        and the order in the list represents the order that members are
        arrested.

        :type self: Network
        :type maximum_arrest: int
            Maximum number of arrests
        :rtype: list

        >>> network = Network()
        >>> network.load_log("topology1.txt")
        >>> network.best_arrest_assets(4)
        162
        >>> network.best_arrest_order(4)
        ['Jacob', 'William', 'James', 'Alexander']
        """
        sums = self.best_arrest_assets(maximum_arrest)
        first = max(self.tree.items(), key=operator.itemgetter(1))[0]
        self.thelist.append(first)
        front = self.somelist.front
        while front.name != first:
            front = front.next_
        self.helper_arrests(front, maximum_arrest-1)
        return (self.thelist)


    def best_arrest_assets(self, maximum_arrest):
        """Search for the amount of seized assets in the best arrest scenario
        that maximizes the seized assets. Consider all members as target zero.

        :type self: Network
        :type maximum_arrest: int
            Maximum number of arrests
        :rtype: int


        >>> network = Network()
        >>> network.load_log("topology1.txt")
        >>> network.best_arrest_assets(4)
        162

        """
        node = self.somelist.front
        sums = self.helper_assets(node, maximum_arrest) - int(node.assets)
        return (sums)


    def helper_assets(self, node, number):
        """Helper function for getting best arrest list based on assets

        :type node: Node
            Node to traverse
        :type number:  max number of recursions
        :rtype: int
        """
        count, maxi = number+1, 0
        listing = {}
        if count != 0:
            first = node
            if len(node.children) == 0:
                return int(node.assets)
            else:
                child_sums = []
                for x in first.children:
                    while first.name != x:
                        first = first.next_
                    child_sums.append(self.helper_assets(first, number-1) + int(node.assets))
                    self.tree[x] = (self.helper_assets(first, number-1))
            return (max(child_sums))
        else:
            return 0

    def helper_arrests(self, node, number):
        """Helper function for getting best arrest list based on assets

        :type node: Node
            Node to traverse
        :type number:  max number of recursions
        :rtype: list
        """
        count = number
        if count != 0 and len(node.children) != 0:
            self.tree = {}
            self.helper_assets(node, number-1)
            first = max(self.tree.items(), key=operator.itemgetter(1))[0]
            self.thelist.append(first)
            front = self.somelist.front
            while front.name != first:
                front = front.next_
            self.helper_arrests(front, number-1)

        return None





if __name__ == "__main__":
    # A sample example of how to use a network object
    network = Network()
    network.load_log("topology1.txt")
    member_name = "William"
    print(member_name + "'s sponsor is " + network.sponsor(member_name))
    print(member_name + "'s mentor is " + network.mentor(member_name))
    print(member_name + "'s asset is " + str(network.assets(member_name)))
    print(member_name + "'s childrens are " + str(network.children(member_name)))
    maximum_arrest = 4
    print("The best arrest scenario with the maximum of " + str(maximum_arrest)\
          + " arrests will seize " + str(network.best_arrest_assets(maximum_arrest)))
    print("The best arrest scenario with the maximum of " + str(maximum_arrest)\
          + " arrests is: " + str(network.best_arrest_order(maximum_arrest)))
