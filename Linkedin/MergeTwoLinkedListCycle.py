'''
题目：求两个linked list 是否 merge。要求考虑有环 和 没环的情况。面试官是两个国人，气氛非常友好，写得也比较顺。
'''
def mergeTwoLinkedList(head1, head2):
    # first judge if two linked list has cycles or not
    flag1 = False
    flag2 = False
    fast = slow = head1
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            flag1 = True
            break
    fast = slow = head2
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            flag2 = True
            break
    # the most simple case, both of them are not cycled
    if not flag1 and not flag2:
        length1 = 0
        length2 = 0
        temp1 = head1
        while temp1:
            length1 += 1
            temp1 = temp1.next
        temp2 = head2
        while temp2:
            length2 += 1
            temp2 = temp2.next
        diff = 0
        if length1 > length2:
            diff = length1 - length2
            temp1 = head1
            while diff:
                temp1 = temp1.next
                diff -= 1
            temp2 = head2
            while temp2.val != temp1.val:
                temp1 = temp1.next
                temp2 = temp2.next
            return temp1
        else:
            diff = length2 - length1
            temp1 = head1
            tem2 = head2
            while diff:
                temp2 = temp2.next
                diff -= 1
            while temp1.val != temp2.val:
                temp1 = temp1.next
                temp2 = temp2.next
            return temp1
    # this is for the case that both of the linked lists have cycles
    elif (flag1 and not flag2) or (not flag1 and flga2):
        return False
    else:
        cycle1 = head1
        fast = slow = head1
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        while cycle1.val != slow.val:
            cycle1 = cycle1.next
            slow = slow.next
        cycle2 = head2
        fast = slow = head2
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        while cycle2.val != slow.val:
            cycle2 = cycle2.next
            slow = slow.next
        temp2 = head2
        while temp2.val != cycle2.val:
            if temp2.val == cycle1.val:
                return True
            temp2 = temp2.next
        temp2 = temp2.next
        while temp2.val != cycle2.val:
            if temp2.val == cycle1.val:
                return True
            temp2 = temp2.next
        return False
