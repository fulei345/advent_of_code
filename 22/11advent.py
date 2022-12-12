def main(filename, first_part, iterations):
    monkeys = []
    with open(filename) as f:
        for line in f:
            monkeyline = line[0:len(line)-1]
            monkeyline = monkeyline.split(" ")
            if len(monkeyline) > 1:
                if monkeyline[0] == "Monkey":
                    pass
                elif monkeyline[2] == "Starting":
                    items = []
                    for i in range(4, len(monkeyline)):
                        temp = monkeyline[i].split(",")[0]
                        items.append(int(temp))
                elif monkeyline[2] == "Operation:":
                    operation = monkeyline[-2]
                    if monkeyline[-1].isnumeric():
                        num = int(monkeyline[-1])
                    else:
                        num = monkeyline[-1]
                    pass
                elif monkeyline[2] == "Test:":
                    module = int(monkeyline[-1])

                elif monkeyline[4] == "If" and monkeyline[5] == "true:":
                    true = int(monkeyline[-1])

                elif monkeyline[4] == "If" and monkeyline[5] == "false:":
                    false = int(monkeyline[-1])

            else:
                temp = Monkey(items, module, true, false, operation, num)
                monkeys.append(temp)

        temp = Monkey(items, module, true, false, operation, num)
        monkeys.append(temp)
        
        product = 1
        for monkey in monkeys:
            product *= monkey.module
        
        for monkey in monkeys:
            monkey.monkeys = monkeys
            monkey.product = product

        for i in range(iterations):
            for monkey in monkeys:
                monkey.inspect(first_part)

        insp_list = []
        for monkey in monkeys:
            print(monkey.items)
            insp_list.append(monkey.inspected)

        insp_list.sort()
        print(insp_list)
        print(insp_list[-1]*insp_list[-2])
        print("-------------------------------------------")
        
class Monkey:
    def __init__(self, items: list, module: int, true: int, false: int, operation: str, operation_num: any):
        self.items = items
        self.monkeys = []
        self.operation = operation
        self.operation_num = operation_num
        self.module = module
        self.true = true
        self.false = false
        self.inspected = 0
        self.product = 0

    def inspect(self, first_part):
        if len(self.items) == 0:
            return False
        for item in self.items:
            if self.operation_num == "old":
                if self.operation == "*":
                    temp = item * item
                else:
                    temp = item + item
            else:
                if self.operation == "*":
                    temp = item * self.operation_num
                else:
                    temp = item + self.operation_num

            if first_part:
                temp = temp // 3
            else:
                temp = temp % self.product
            if  temp % self.module == 0:
                self.monkeys[self.true].items.append(temp) 
            else:
                self.monkeys[self.false].items.append(temp)
            self.inspected += 1
        self.items = []
        return True


if __name__ == "__main__":
    main("input/test11.txt",True, 20)
    main("input/input11.txt",True, 20)
    main("input/test11.txt",False, 10000)
    main("input/input11.txt",False, 10000)
