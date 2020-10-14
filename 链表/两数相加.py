class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def show(self):
        if not self.head:
            print('')
            return
        vals = []
        cur = self.head
        vals.append(cur.val)
        while cur.next:
            cur = cur.next
            vals.append(cur.val)
        print(vals)

    def create(self, vals):
        if not self.head:
            self.head = ListNode(vals.pop(0))
        cur = self.head
        while cur.next:
            cur = cur.next
        for v in vals:
            node = ListNode(v)
            cur.next = node
            cur = cur.next

    def addTwoNumbers(self, l1, l2):
        print(l1)
        cur1, cur2 = l1.head, l2.head
        num1 = num2 = ''
        while cur1:
            num1 += str(cur1.val)
            cur1 = cur1.next
        while cur2:
            num2 += str(cur2.val)
            cur2 = cur2.next
        sum = int(num1) + int(num2)
        nums = list(map(int, [i for i in str(sum)]))
        self.create(nums)
        return self

def handle_input(inp1, inp2):
    res1 = list(map(int, inp1.strip('[] ').split(',')))
    res2 = list(map(int, inp2.strip('[] ').split(',')))
    return res1, res2

inp1 = input()
inp2 = input()
s1, s2 = handle_input(inp1, inp2)

solution1 = Solution()
solution1.create(s1)
solution2 = Solution()
solution2.create(s2)

sum_solution = Solution.addTwoNumbers(Solution(), solution1, solution2)
sum_solution.show()
