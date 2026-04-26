class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()

        # Traverse through the expression
        for curr_char in expression:
            if curr_char == "," or curr_char == "(":
                curr_char  # Skip commas and open parentheses

            # Push operators and boolean values to the stack
            if curr_char in ["t", "f", "!", "&", "|"]:
                st.append(curr_char)

            # Handle closing parentheses and evaluate the subexpression
            elif curr_char == ")":
                has_true = False
                has_false = False

                # Process the values inside the parentheses
                while st[-1] not in ["!", "&", "|"]:
                    top_value = st.pop()
                    if top_value == "t":
                        has_true = True
                    elif top_value == "f":
                        has_false = True

                # Pop the operator and evaluate the subexpression
                op = st.pop()
                if op == "!":
                    st.append("t" if not has_true else "f")
                elif op == "&":
                    st.append("f" if has_false else "t")
                else:
                    st.append("t" if has_true else "f")

        # The final result is at the top of the stack
        return st[-1] == "t"