from operator import mul

def count_k(n, k):
    """return the number of ways to go up stairs of n steps by x , which is up to and include k, steps exactly.
    
    >>> count_k(3, 3)
    4
    >>> count_k(4, 4)
    8
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        total = 0
        for i in range(1, k + 1):
            total += count_k(n - i, k)
        return total

def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.

    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))

def check_hole_number(n):
    """
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """
    if n < 10:
        return True 
    return (n // 10 % 10 < n % 10 and n // 10 % 10 < n // 100 % 10) and check_hole_number(n // 100) 


def check_mountain_number(n):
    """
    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """
    def helper(n, increasing):
        if n < 10:
            return True
        if increasing and n % 10 < n // 10 % 10:
            return helper(n // 10, True)
        return n % 10 > n // 10 % 10 and helper(n // 10, False)
    return helper(n, True)

# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        max_b_height = max([height(b) for b in branches(t)])
        return 1 + max_b_height

def square_tree(t):
    """Return a tree with the square of every element in t
    """
    if is_leaf(t):
        return tree(label(t)**2)
    else:
        bs = [square_tree(b) for b in branches(t)]
        return tree(label(t)**2, bs)

def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if is_leaf(tree) and label(tree) != x:
        return None
    elif label(tree) == x:
        return [x]
    else:
        b_path = []
        for b in branches(tree):
            b_path = find_path(b, x)
            if b_path is not None:
                break
        if b_path == None:
            return None
        else:
            return [label(tree)] + b_path

def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    count = 0
    for e in lst:
        if x == e:
            count += 1
    lst += [el] * count
    return 

def group_by(s, fn):
    dic = {}
    for e in s:
        if fn(e) in dic:
            dic[fn(e)].append(e)
        else:
            dic[fn(e)] = [e]
    return dic


def partition_options(total, biggest):
    """
    Implement the following function partition_options which outputs all the ways to partition a number
    total using numbers no larger than biggest.
    >>> partition_options(2, 2)
    [[2], [1, 1]]
    >>> partition_options(3, 3)
    [[3], [2, 1], [1, 1, 1]]
    >>> partition_options(4, 3)
    [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
    """
    if total < 0:
        return None
    elif total == 0:
        return [[]]
    elif biggest == 1:
        temp = partition_options(total - 1, biggest)
        if temp == None:
            return None
        for part in temp:
            part.insert(0, 1)
        return temp 
    else:
        with_biggest = partition_options(total - biggest, biggest)
        without_biggest = partition_options(total, biggest - 1)
        part1, part2 = [], []
        if with_biggest != None:
            for part in with_biggest:
                part.insert(0, biggest)
        if with_biggest == None and without_biggest == None:
            return None
        elif with_biggest == None and without_biggest != None:
            return without_biggest
        elif with_biggest != None and without_biggest != None:
            return with_biggest + without_biggest

def min_elements(T, lst):
    """
    >>> min_elements(10, [4, 2, 1]) # 4 + 4 + 2
    3
    >>> min_elements(12, [9, 4, 1]) # 4 + 4 + 4
    3
    >>> min_elements(0, [1, 2, 3])
    0
    """
    if T < 0:
        return None
    if T == 0:
        return 0
    else:
        end_lst = []
        end = 0
        for e in lst:
            end = min_elements(T - e, lst)
            if end != None:
                end_lst += [1 + end]
        return min(end_lst)

def f(x):
    """
    >>> t = f(3)
    >>> x, y = t()
    >>> x
    2
    >>> y
    3
    """
    b = [x]
    def g():
        b[0] = b[0] - 1
        return b[0], x
    return g

def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def use_function(f):
        nonlocal n
        n = f(n)
        return n
    return use_function

def nonlocalist():
    """
    >>> prepend, get = nonlocalist()
    >>> prepend(2)
    >>> prepend(3)
    >>> prepend(4)
    >>> get(0)
    4
    >>> get(1)
    3
    >>> get(2)
    2
    >>> prepend(8)
    >>> get(2)
    3
    """
    get = lambda x: "Index out of range!"
    def prepend(value):
        nonlocal get
        f = get
        def get(i):
            if i == 0:
                return value
            return f(i - 1)
    return prepend, lambda x: get(x)


square = lambda x: x * x
double = lambda x: 2 * x
def memory(x, f):
    """Return a higher-order function that prints its
    memories.
    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    """
    def g(h):
        print(f(x))
        return memory(x, h)
    return g

def announce_losses(who, last_score=0):
    """
    >>> f = announce_losses(0)
    >>> f1 = f(10, 0)
    >>> f2 = f1(1, 10) # Player 0 loses points due to swine swap
    Oh no! Player 0 just lost 9 point(s).
    >>> f3 = f2(7, 10)
    >>> f4 = f3(7, 11) # Should not announce when player 0's score does not change
    >>> f5 = f4(11, 12)
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    def say(score0, score1):
        if who == 0:
            score = score0 - last_score
        elif who == 1:
            score = score1 - last_score
        if score < 0:
            print(f"Oh no! Player {who} just lost {-score} point(s).")
        return announce_losses(who, last_score + score)
    return say

def fox_says(start, middle, end, num):
    """
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """
    def repeat(k):
        return (middle + '-')* (k - 1) + middle
    return start + '-' + repeat(num) + '-' + end

def primary_stress(t):
    """
    >>> word = tree("", [ tree("w", [tree("s", [tree("min")]), tree("w", [tree("ne")])]), tree("s", [tree("s", [tree("so")]), tree("w", [tree("ta")])])])
    >>> primary_stress(word)
    'so'
    >>> phrase = tree("", [tree("s", [tree("s", [tree("law")]), tree("w", [tree("degree")])]),tree("w", [tree("requirement")])])
    >>> primary_stress(phrase)
    'law'
    """
    def helper(t, num_s):
        if is_leaf(t):
            return [label(t), num_s]
        if label(t) == "s":
            num_s = num_s + 1
        return max([helper(b, num_s) for b in branches(t)],
            key = lambda term: term[1])
    return helper(t, 0)[0]

def subset_sum(seq, k):
    """
    >>> subset_sum([2, 4, 7, 3], 5) # 2 + 3 = 5
    True
    >>> subset_sum([1, 9, 5, 7, 3], 2)
    False
    >>> subset_sum([1, 1, 5, -1], 3)
    False
    """
    if k in seq:
        return True
    elif k < 0:
        return False
    else:
        min_e = min(seq)
        seq.remove(min_e)
        return subset_sum(seq, k - min_e) 

def generate_subsets():
    """
    >>> subsets = generate_subsets()
    >>> for _ in range(3):
    ...     print(next(subsets))
    ...
    [[]]
    [[], [1]]
    [[], [1], [2], [1, 2]]
    """
    def subsets(n):
        if n == 0:
            return [[]]
        else:
            return subsets(n - 1) + [s + [n] for s in subsets(n - 1)]

    n = 0
    while True:
        lst = subsets(n) 
        yield lst
        n += 1

def sum_paths_gen(t):
    """
    >>> t1 = tree(5)
    >>> next(sum_paths_gen(t1))
    5
    >>> t2 = tree(1, [tree(2, [tree(3), tree(4)]), tree(9)])
    >>> sorted(sum_paths_gen(t2))
    [6, 7, 10]
    """
    if is_leaf(t):
        yield label(t)
    for b in branches(t):
        for sum_path in sum_paths_gen(b):
            yield label(t) + sum_path

class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.mgs = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        self.server.send()

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append(email)


class Pet():

    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

class Dog(Pet):

    def talk(self):
        print(self.name + ' says woof!')
    
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives
        is_alive = True

    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + ' says meow!') 

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        if self.lives == 0:
            print(self.name + ' has no more lives to lose!')
            is_alive = False
        else:
            self.lives -= 1

class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    #def __init__(self, name, owner, lives=9):
    # Is this method necessary? Why or why not?
        # NO.talk twice just
    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        Cat.talk(self)
        Cat.talk(self)

def sum_nums(lnk):
    """Write a function that takes in a a linked list and returns the sum of all its elements.
    You may assume all elements in lnk are integers.

    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk is Link.empty:
        return 0
    else:
        return lnk.first + sum_nums(lnk.rest)

def multiply_lnks(lst_of_lnks):
    """
    Write a function that takes in a Python list of linked lists and multiplies them
    element-wise. It should return a new linked list.
    If not all of the Link objects are of equal length, return a linked list whose length is
    that of the shortest linked list given. You may assume the Link objects are shallow
    linked lists, and that lst of lnks contains at least one linked list.
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return lnk

    end = 1
    for lnk in lst_of_lnks:
        end *= lnk.first
    return Link(end, multiply_lnks([lnk.rest for lnk in lst_of_lnks])) 


def filter_link(link, f):
    """
    Implement filter link, which takes in a linked list link and a function f and
    returns a generator which yields the values of link for which f returns True.
    Try to implement this both using a while loop and without using any form of
    iteration.
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest

def filter_no_iter(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> list(filter_no_iter(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    if link is Link.empty:
        return []
    elif f(link.first):
        return [link.first] + filter_no_iter(link.rest, f)
    else:
        return filter_no_iter(link.rest, f)

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'




def make_even(t):
    """Define a function make even which takes in a tree t whose values are integers, and
    mutates the tree such that all the odd integers are increased by 1 and all the even
    integers remain the same
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.is_leaf():
        if t.label % 2 == 1:
            t.label += 1

    else:
        if t.label % 2 == 1:
            t.label += 1
        for b in t.branches:
            make_even(b)

def square_tree(t):
    """Mutates a Tree t by squaring all its elements."""
    if t.is_leaf():
        t.label = t.label ** 2
    else:
        t.label = t.label ** 2
        for b in t.branches():
            square_tree(b)

def find_path(t, entry):
    """Define the procedure find path that, given a Tree t and an entry, returns a list
    containing the nodes along the path required to get from the root of t to entry. If
    entry is not present in t, return False.
    Assume that the elements in t are unique. Find the path to an element.
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1)])
    >>> find_path(tree_ex, 5)
    [2, 7, 6, 5]
    """
    if t.is_leaf():
        if t.label == entry:
            return [t.label]
        else:
            return False
    else:
        for b in t.branches:
            path = find_path(b, entry)
            if path:
                return [t.label] + path
        return False

def average(t):
    """
    Returns the average value of all the nodes in t.
    >>> t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
    >>> average(t0)
    1.5
    >>> t1 = Tree(8, [t0, Tree(4)])
    >>> average(t1)
    3.0
    """
    def sum_helper(t):
        total, count = t.label, 1
        for b in t.branches:
            tmp_total, tmp_count = sum_helper(b)
            total += tmp_total 
            count += tmp_count
        return total, count
    total, count = sum_helper(t)
    return total / count

def combine_tree(t1, t2, combiner):
    """
    Write a function that combines the values of two trees t1 and t2 together with the
    combiner function. Assume that t1 and t2 have identical structure. This function
    should return a new tree.
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    if t1.is_leaf():
        return Tree(combiner(t1.label, t2.label))
    else:
        new_bs = []
        for b1, b2 in zip(t1.branches, t2.branches):
            new_bs.append(combine_tree(b1, b2, combiner))
        return Tree(combiner(t1.label, t2.label), new_bs)


def alt_tree_map(t, map_fn):
    """
    Implement the alt tree map function that, given a function and a Tree, applies the
    function to all of the data at every other level of the tree, starting at the root.
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    def helper(t, map_fn, index):
        if t.is_leaf():
            if index % 2 == 0:
                t.label = map_fn(t.label)
            return t
        else:
            if index % 2 == 0:
                t.label = map_fn(t.label)
            new_bs = [helper(b, map_fn, index + 1) for b in t.branches]
            return Tree(t.label, new_bs)
    return helper(t, map_fn, 0)
    

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
    
def make_lambda(params, body):
    """
    >>> f = make_lambda("x, y", "x + y")
    >>> f(1, 2)
    3
    >>> g = make_lambda("a, b, c", "c if a > b else -c")
    >>> g(1, 2, 3)
    -3
    >>> make_lambda("f, x, y", "f(x, y)")(f, 1, 2)
    3
    """
    return eval("lambda " + params + ": " + body)

def make_lambda_use_fstring(params, body):
    """
    >>> f = make_lambda_use_fstring("x, y", "x + y")
    >>> f(1, 2)
    3
    >>> g = make_lambda_use_fstring("a, b, c", "c if a > b else -c")
    >>> g(1, 2, 3)
    -3
    >>> make_lambda_use_fstring("f, x, y", "f(x, y)")(f, 1, 2)
    3
    """
    return eval(f'lambda {params}: {body}')