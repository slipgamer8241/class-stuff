class LinkedListNode:
    def __init__(self, number):
        self.number = number
        self.next = None


def delete_zero_sum_pairs(head):
    """
    Delete pairs of consecutive nodes in a linked list that sum to zero.
    This function modifies the linked list in place and returns the modified head.
    """
    while True:
        found_zero_sum = False
        prev = None
        curr = head

        while curr and curr.next:
            if curr.number + curr.next.number == 0:
                if prev is None:
                    head = curr.next.next
                else:
                    prev.next = curr.next.next
                found_zero_sum = True
                break
            prev = curr
            curr = curr.next

        if not found_zero_sum:
            break

    return head
