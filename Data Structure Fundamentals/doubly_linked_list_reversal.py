# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#


def reverse(llist):
    while llist:
        savepoint = llist.next  #   if node is 1, we save 2         # if node is 2, we save 3        # if node is 3, we save none
        if not savepoint:
            llist.next = llist.prev
            llist.prev = None
            return llist
        llist.next = llist.prev #  node's next from 2 becomes none     # node's next from 3 becomes 2   # node's next from none becomes 2
        llist.prev = savepoint  # node's prev from none becomes 2      # node's prev from 1 becomes 3   # node's prev from 2 becomes o none
        llist = llist.prev      # we now move to 2                  # we now move to 3               # node now moves to none
    return llist

