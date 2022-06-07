class Device:
    def __init__(self, device, brand, measure_limit, year):
        self.device = device
        self.brand = brand
        self.measure_limit = measure_limit
        self.year = year

    def __gt__(self, other):
        if self.brand > other.brand:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.brand < other.brand:
            return True
        else:
            return False

    def __str__(self):
        return f"Device: {self.device} \n" \
               f"Brand: {self.brand} \n" \
               f"Measurement limit: {self.measure_limit} \n" \
               f"Year: {self.year}\n===================="


class BinaryTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self, side):
        print(side, "", self.data,)
        if self.left:
            self.left.print_tree("Left branch\n")
        if self.right:
            self.right.print_tree("Right branch\n")

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def get_node_over_measure(self, measure_limit):
        if self.left:
            self.left.get_node_over_measure(measure_limit)
        if self.data.measure_limit >= measure_limit:
            print(self.data)
        if self.right:
            self.right.get_node_over_measure(measure_limit)

    def min_value(self):
        current = self
        pre_current = None
        while current and current.left:
            pre_current = current
            current = current.left

        return current, pre_current

    def delete_by_year(self, year):
        if self.left:
            self.left = self.left.delete_by_year(year)
        if self.right:
            self.right = self.right.delete_by_year(year)
        if self.data.year == year:

            if not self.left and not self.right:  # no child
                return None
            elif not self.left:  # only right child
                return self.right
            elif not self.right:  # only left child
                return self.left

            # has 2 child
            temp, recurrent = self.right.minValue()
            if recurrent:
                if temp.right:
                    recurrent.left = temp.right
                else:
                    recurrent.left = None
            else:
                self.right = temp.right
            self.data = temp.data

        return self


dev1 = Device('Voltmeter1', 5, 12, 2001)
dev2 = Device('Voltmeter2', 2, 2, 2002)
dev3 = Device('Voltmeter3', 1, 32, 2003)

root = BinaryTreeNode(dev1)
root.insert(dev2)
root.insert(dev3)

root.insert(Device('Voltmeter_new1', 9, 8, 2002))
root.insert(Device('Voltmeter_new2', 7, 8, 2001))
root.insert(Device('Voltmeter_new3', 8, 8, 2004))
root.insert(Device('Voltmeter_new4', 10, 8, 2002))
root.print_tree('Main node:')


root.delete_by_year(2002)
root.print_tree(f'Delete by year:\n')


print("Over measure")
root.get_node_over_measure(9)
