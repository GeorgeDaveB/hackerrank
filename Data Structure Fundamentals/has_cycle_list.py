    ## TRY USING A SET NOW FOR O(1) INSTEAD OF O(N) TO O(N^2)
def has_cycle(head):
    if not head:
        return 0
    if not head.next:
        return 0
    nav = head
    nav_list = []
    while nav:
        if nav in nav_list: 
            return 1
        else:
            nav_list.append(nav)
            nav = nav.next
    return 0