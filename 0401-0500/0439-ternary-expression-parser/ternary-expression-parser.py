# Approach 1: Find Rightmost Atomic Expression
class Solution:
    def parseTernary(self, expression: str) -> str:

        # Checks if the string s is a valid atomic expression
        def isValidAtomic(s):
            return s[0] in 'TF' and s[1] == '?' and s[2] in 'TF0123456789'\
                and s[3] == ':' and s[4] in 'TF0123456789'

        # Returns the value of the atomic expression
        def solveAtomic(s):
            return s[2] if s[0] == 'T' else s[4]

        # Reduce expression until we are left with a single character
        while len(expression) != 1:
            j = len(expression) - 1
            while not isValidAtomic(expression[j-4:j+1]):
                j -= 1
            expression = expression[:j-4] + \
                solveAtomic(expression[j-4:j+1]) + expression[j+1:]

        # Return the final character
        return expression


# Approach 2: Reverse Polish Notation
class Solution2:
    def parseTernary(self, expression: str) -> str:

        # Reduce expression until we are left with a single character
        while len(expression) != 1:
            questionMarkIndex = len(expression) - 1
            while expression[questionMarkIndex] != '?':
                questionMarkIndex -= 1

            # Find the value of the expression.
            if expression[questionMarkIndex - 1] == 'T':
                value = expression[questionMarkIndex + 1]
            else:
                value = expression[questionMarkIndex + 3]

            # Replace the expression with the value
            expression = expression[:questionMarkIndex - 1] + value\
                + expression[questionMarkIndex + 4:]

        # Return the final character
        return expression


# Approach 3: Reverse Polish Notation using Stack
class Solution3:
    def parseTernary(self, expression: str) -> str:
        
        # Initialize a stack
        stack = []
        i = len(expression) - 1

        # Traverse the expression from right to left
        while i >= 0:

            # Current character
            char = expression[i]
            
            # Push every T, F, and digit on the stack
            if char in 'TF0123456789':
                stack.append(char)
            
            # As soon as we encounter ?, 
            # replace top two elements of the stack with one
            elif char == '?':
                onTrue = stack.pop()
                onFalse = stack.pop()
                stack.append(onTrue if expression[i - 1] == 'T' else onFalse)
                
                # Decrement i by 1 as we have already used
                # Previous Boolean character
                i -= 1
            
            # Go to the previous character
            i -= 1
        
        # Return the final character
        return stack[0]

class Solution32:
    def parseTernary(self, expression: str) -> str:
        
        # Initialize a stack
        stack = []
        
        # Traverse the expression from right to left
        for char in expression[::-1]:
            
            # If stack top is ?, then replace next four characters
            # with E1 or E2 depending on the value of B
            if stack and stack[-1] == '?':
                stack.pop()
                onTrue = stack.pop()
                stack.pop()
                onFalse = stack.pop()
                stack.append(onTrue if char == 'T' else onFalse)
            
            # Otherwise, push this character
            else:
                stack.append(char)
        
        # Return the final character
        return stack[0]

# Approach 4: Binary Tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution4:
    def parseTernary(self, expression: str) -> str:
        
        # Global Index to Construct Binary Tree
        self.index = 0
        root = self.constructTree(expression)
        
        # Parse the binary tree till we reach the leaf node
        while root.left and root.right:
            if root.val == 'T':
                root = root.left
            else:
                root = root.right
        
        return root.val

    def constructTree(self, expression):
        
        # Storing current character of expression
        root = TreeNode(expression[self.index])

        # If the last character of expression, return
        if self.index == len(expression) - 1:
            return root
        
        # Check the next character
        self.index += 1
        if expression[self.index] == '?':
            self.index += 1
            root.left = self.constructTree(expression)
            self.index += 1
            root.right = self.constructTree(expression)
            
        return root


# Approach 5: Recursion
class Solution5:
    def parseTernary(self, expression: str) -> str:

        # To analyze the expression between two indices
        def solve(i, j):

            # If expression is a single character, return it
            if i == j:
                return expression[i]

            # Find the index of ?
            questionMarkIndex = i
            while expression[questionMarkIndex] != '?':
                questionMarkIndex += 1

            # Find one index after corresponding :
            aheadColonIndex = questionMarkIndex + 1
            count = 1
            while count != 0:
                if expression[aheadColonIndex] == '?':
                    count += 1
                elif expression[aheadColonIndex] == ':':
                    count -= 1
                aheadColonIndex += 1

            # Check the value of B and recursively solve
            if expression[i] == 'T':
                return solve(questionMarkIndex + 1, aheadColonIndex - 2)
            else:
                return solve(aheadColonIndex, j)

        # Solve for the entire expression
        return solve(0, len(expression) - 1)

# Approach 6: Constant Space Solution
class Solution6:
    def parseTernary(self, expression: str) -> str:
        
        # Pointer for Traversal. It will maintain Loop Invariant.
        i = 0
        
        # Loop invariant: We will always be at the first character of 
        # expression which we should FOCUS on.
        while True:
            
            # If this first character is not boolean, it means no nesting
            # is there. Thus, we can simply return this character.
            if expression[i] not in 'TF':
                answer = expression[i]
                break
            
            # If this is last character, then we can simply return this
            if i == len(expression) - 1:
                answer = expression[i]
                break
            
            # If succeeding character is :, it means we have processed
            # the FOCUS part. Ignore the ahead part and return this character.
            if expression[i + 1] == ':':
                answer = expression[i]
                break

            # Now it means this character is boolean followed by ?.
            # If this boolean is T, then process after ? sub-expression.
            if expression[i] == 'T':
                i = i + 2
            
            # If this boolean is F, then make i point to the character
            # after ": of this ?". To have corresponding :, we 
            # can maintain count
            else:
                count = 1
                i = i + 2
                while count != 0:
                    if expression[i] == ':':
                        count -= 1
                    elif expression[i] == '?':
                        count += 1
                    i += 1
        
        # Return Answer Character
        return answer

class Solution62:
    def parseTernary(self, expression: str) -> str:

        i = 0
        while True:

            if expression[i] not in 'TF' or i == len(expression) - 1\
            or expression[i + 1] == ':':
                return expression[i]
            if expression[i] == 'T':
                i = i + 2
            else:
                count = 1
                i = i + 2
                while count != 0:
                    if expression[i] == ':':
                        count -= 1
                    elif expression[i] == '?':
                        count += 1
                    i += 1

