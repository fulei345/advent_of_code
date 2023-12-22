import time

                            

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()

        inits = liste[0].split(",")

        boxes = []
        for i in range(256):
            boxes.append([])

        total = 0
        for init in inits:
            if "-" in init:
                remove_init(boxes, init)
            elif "=" in init:
                add_init(boxes, init)       
        for i, box in enumerate(boxes):
            total += calc_focus(box, i)
    return total

def calc_value(init):
    current_value = 0
    for char in init:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value

def add_init(boxes, init):
    liste = init.split("=")
    box_id = calc_value(liste[0])
    label_focus = (liste[0], int(liste[1]))
    index_add = -1
    for i, box in enumerate(boxes[box_id]):
        if box[0] == liste[0]:
            index_add = i
            break
    if index_add > -1:
        boxes[box_id].pop(index_add)
        boxes[box_id].insert(index_add,label_focus)
    else:
        boxes[box_id].append(label_focus)

def remove_init(boxes, init):
    liste = init.split("-")
    box_id = calc_value(liste[0])
    index_remove = -1
    for i, box in enumerate(boxes[box_id]):
        if box[0] == liste[0]:
            index_remove = i
            break
    if index_remove > -1:
        boxes[box_id].pop(index_remove)

def calc_focus(box, index):
    focus = 0
    for i, init in enumerate(box):
        focus += (index + 1) * (i + 1) * init[1]
    return focus

if __name__ == "__main__":
    
    start = time.time()
    result = main("test15.txt")
    end = time.time()
    expected = 145
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    start = time.time()
    result = main("input15.txt")
    end = time.time()
    expected = 233537
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)
    