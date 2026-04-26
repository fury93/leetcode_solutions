# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        backbone = cur = PolyNode()
        while poly1 and poly2:
            coeff = power = 0
            if poly1.power > poly2.power:
                coeff = poly1.coefficient
                power = poly1.power
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                coeff = poly2.coefficient
                power = poly2.power
                poly2 = poly2.next
            else:
                coeff = poly1.coefficient + poly2.coefficient
                power = poly1.power
                poly1 = poly1.next
                poly2 = poly2.next
            
            if coeff !=0:
                cur.next = PolyNode(coeff, power)
                cur = cur.next

        cur.next = poly1 if poly1 else poly2

        return backbone.next
        

class Solution2:
    def addPoly(self, poly1: "PolyNode", poly2: "PolyNode") -> "PolyNode":
        sum_ = PolyNode()
        current = sum_
        table = {}

        # Calculate terms for sum
        self._process_nodes(table, poly1)
        self._process_nodes(table, poly2)

        # Iterate over sorted keys and build sum
        for key in sorted(table.keys(), reverse=True):
            current.next = PolyNode(table[key], key)
            current = current.next

        return sum_.next

    def _process_nodes(self, table, node):
        while node:
            if node.power in table:
                new_coefficient = node.coefficient + table[node.power]
                if new_coefficient == 0:
                    table.pop(node.power)
                else:
                    table[node.power] = new_coefficient
            else:
                table[node.power] = node.coefficient
            node = node.next