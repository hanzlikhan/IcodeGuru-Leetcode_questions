class MinStack:
    def __init__(self):
        self.originalstack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.originalstack.append(val)
        if len(self.minstack) == 0 or self.minstack[-1] >= val:
            self.minstack.append(val)

    def pop(self) -> None:
        if len(self.originalstack) <= 0:
            return

        topele = self.originalstack.pop()
        if topele == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        if len(self.originalstack) == 0:
            return None
        return self.originalstack[-1]

    def getMin(self) -> int:
        if len(self.minstack) == 0:
            return None
        return self.minstack[-1]

# Example usage:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    # Instantiate MinStack object
    obj = MinStack()

    # Push elements
    obj.push(3)
    obj.push(5)
    obj.push(2)
    obj.push(8)

    # Pop an element
    obj.pop()

    # Get top element
    print("Top element:", obj.top())  # Output: 2

    # Get minimum element
    print("Minimum element:", obj.getMin())  # Output: 2
