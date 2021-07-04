import sys
from random import seed
from time import time

from Article import *

seed(48)

# left node is starting and right is ending
def solve(left, right):
    # get links here because the for loop won't work without them
    left.forwardlinks()
    right.backlinks()

    # check if lists match up
    for item in left.links:
        # if there's a match, it links the two ends of the linked list
        # if match is found, the program won't get views, which saves time (neat!)
        if item in right.links:
            new = Article(item)
            left(new)
            new(right)
            return

    left.get_views_dict()
    right.get_views_dict()

    left.child = Article(left.best_link())
    right.parent = Article(right.best_link())

    left(left.child) # callable that links parent(child)
    right.parent(right) # right is the child in this case because we're using backlinks
    
    print(f"\n{left.child.title} <---> {right.parent.title}", flush = True)
    
    solve(left.child, right.parent)


# prints list of articles with the game's solution (you gotta solve first solving)
def printer(start_article):
    print("\n")
    current = start_article

    print(current.title)
    total_articles = 1

    # keeps printing as long as there's children
    while current.child is not None:
        current = current.child
        print(current.title)
        total_articles += 1

    return total_articles        

if __name__ == "__main__":
    name1 = "Avengers (comics)" # starting article
    name2 = "The Room" # finish article

    if len(sys.argv) > 1:
        cmd1 = str(sys.argv[1])
        cmd2 = str(sys.argv[2])
    else:
        cmd1 = input('starting link: ')
        cmd2 = input('ending link: ')
    
    if cmd1 != "":
        name1 = cmd1
    if cmd2 != "":
        name2 = cmd2
    
    start = Article(name1)
    end = Article(name2)

    print("Searching")

    ti = time()
    solve(start, end)
    tf = time()

    tot = printer(start)
    print(f"time = {tf-ti}")
    print(f"{(tf-ti)/tot} per article")
