class Counter(object):
    def __init__(self, curr_value = 10, min_val = 5, max_val = 15):
        self.curr_value = curr_value
        self.min_val = min_val
        self.max_val = max_val

    def decrease(self):
        if (self.curr_value - 1) < self.min_val:
            print('Minimum value reached')
        else:
            self.curr_value -= 1
            print(self.curr_value)

    def increase(self):
        if (self.curr_value + 1) > self.max_val:
            print('Maximum value reached')
        else:
            self.curr_value += 1
            print(self.curr_value)

    def get_current_value(self):
        print(self.curr_value)

counter1 = Counter(max_val=11)

counter1.get_current_value()
counter1.increase()
counter1.increase()
counter1.get_current_value()
