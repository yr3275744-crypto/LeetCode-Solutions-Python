#https://leetcode.com/problems/valid-parentheses/description/

class Solution:
  """Check whether the parentheses were used correctly. 
  I used the LIFO principle to make sure that the order of the parentheses was correct, 
  and that the last parentheses opened were indeed the first ones closed."""
    def isValid(self, s: str) -> bool:
        brackets_value = {"{":1, "(":1, "[":1, "}":-1, ")":-1, "]":-1}
        opposite_pairs = {"{":"}", "(":")", "[":"]"}
        brackets_order = []
        for brackete in s:
            if brackets_value[brackete] > 0:
                brackets_order.append(brackete)
            else:
                if len(brackets_order) == 0:
                    return False
                last_brackete = brackets_order.pop()
                if brackete != opposite_pairs[last_brackete]:
                    return False
        if len(brackets_order) != 0:
            return False
        return True
