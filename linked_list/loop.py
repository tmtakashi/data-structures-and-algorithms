def loop(head):
    fast = head
    slow = head

    while fast != None and fast.next != None:
        if fast == slow:
            break
        fast = fast.next.next
        slow = fast.next

    if fast is None or fast.next is None:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast
