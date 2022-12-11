
def main(filename, first_part):
    monkeys = []
    all_index =0
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
                #     two_old = True
                #     if monkeyline[-1].isnumeric():
                #         two_old = False
                #         num = int(monkeyline[-1])
                #     if monkeyline[-2] == "+":
                #         if two_old:
                #             operation = lambda old : old + old
                #         else:
                #             operation = lambda old : old + num
                #             print("+",num, all_index)
                #     elif monkeyline[-2] == "*":
                #         if two_old:
                #             operation = lambda old : old * old
                #         else:
                #             operation = lambda old : old * num
                #             print("*", num, all_index)
                    pass
                elif monkeyline[2] == "Test:":
                    module = int(monkeyline[-1])

                elif monkeyline[4] == "If" and monkeyline[5] == "true:":
                    true = int(monkeyline[-1])

                elif monkeyline[4] == "If" and monkeyline[5] == "false:":
                    false = int(monkeyline[-1])

            else:
                temp = Monkey(all_index, items, module, true, false)
                monkeys.append(temp)
                all_index += 1

        product = 1
        for monkey in monkeys:
            product *= monkey.module
        
        for monkey in monkeys:
            monkey.monkeys = monkeys
            monkey.product = product

        if len(monkeys) == 4:
            monkeys[0].operation = lambda old : old * 19
            monkeys[1].operation = lambda old : old + 6
            monkeys[2].operation = lambda old : old * old
            monkeys[3].operation = lambda old : old + 3
        else:
            monkeys[0].operation = lambda old : old * 3
            monkeys[1].operation = lambda old : old + 2
            monkeys[2].operation = lambda old : old + 1
            monkeys[3].operation = lambda old : old + 5
            monkeys[4].operation = lambda old : old + 4
            monkeys[5].operation = lambda old : old + 8
            monkeys[6].operation = lambda old : old * 7
            monkeys[7].operation = lambda old : old * old

        if first_part:

            for i in range(20):
                for monkey in monkeys:
                    monkey.inspect(first_part)
        else:
            for i in range(10000):
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
    def __init__(self, index: int, items: list, module: int, true: int, false: int ):
        self.index = index
        self.items = items
        self.monkeys = []
        self.operation = None
        self.module = module
        self.true = true
        self.false = false
        self.inspected = 0
        self.product = 0

    def inspect(self, first_part):
        if len(self.items) == 0:
            return False
        for item in self.items:
            temp = self.operation(item)
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
    main("input/test11.txt",True)
    main("input/input11.txt",True)
    main("input/test11.txt",False)
    main("input/input11.txt",False)
