class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining elements
    current.next = l1 if l1 else l2
    
    # Convert to list for output
    result = []
    node = dummy.next
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    n1 = int(input().strip())
    list1 = [int(input().strip()) for _ in range(n1)]
    
    n2 = int(input().strip())
    list2 = [int(input().strip()) for _ in range(n2)]
    
    # Build linked lists
    def build_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    l1 = build_linked_list(list1)
    l2 = build_linked_list(list2)
    
    # Merge and print
    merged = merge_sorted_lists(l1, l2)
    for val in merged:
        print(val)