__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode

    # ascending
    def insertionSortList_TLE(self, head):
        """
        Known issue: Time Limit Excedded
        """
        comparator = lambda x, y: cmp(x.val, y.val)
        # open set & closed set
        # iterate through all the nodes
        dummy_head = ListNode(0)
        dummy_head.next = head


        closed_tail = dummy_head.next
        while(closed_tail and closed_tail.next):
            open_head = closed_tail.next
            # open_head_next = closed_tail.next.next

            # find position
            ptr_before = dummy_head
            ptr = dummy_head.next # error using ptr = head

            # WHILE BEFORE IF THUS INCREASING TIME COMPLEXITY
            while(ptr_before):
                if comparator(ptr, open_head)>0:
                    ptr_before.next = open_head
                    closed_tail.next = open_head.next
                    open_head.next = ptr

                    # closed_tail.next = open_head_next
                    break

                if ptr==open_head:
                    closed_tail = closed_tail.next
                    break

                ptr_before = ptr_before.next
                ptr = ptr.next


        return dummy_head.next


    def insertionSortList(self, head):
        """
        Know issue: Time Limit Excedded
        """
        comparator = lambda x, y: cmp(x.val, y.val)
        # open set & closed set
        # iterate through all the nodes
        dummy_head = ListNode(0)
        dummy_head.next = head

        closed_tail = head
        while (closed_tail and closed_tail.next):
            open_head = closed_tail.next
            open_head_next = closed_tail.next.next
            if not comparator(closed_tail, open_head)<=0: # only compare the closed set tail and open set head

                pre = dummy_head
                while comparator(pre.next, open_head)<0: # find position 
                    pre = pre.next

                # swap nodes
                open_head.next = pre.next
                pre.next = open_head
                closed_tail.next = open_head_next



            else:
                closed_tail = closed_tail.next


        return dummy_head.next

if __name__=="__main__":
    import random
    lst = [ListNode(i) for i in random.sample(xrange(-1000, 1000), 1000)]
    # lst = [ListNode(1), ListNode(3), ListNode(2)]
    # lst = [ListNode(i) for i in range(10, -1, -1)]
    for i in range(len(lst)):
        try:
            lst[i].next = lst[i+1]
        except IndexError: # last
            lst[i].next = None



    head = Solution().insertionSortList(lst[0])
    current = head
    for i in range(len(lst)):
        print current.val
        current = current.next



