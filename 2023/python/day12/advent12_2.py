import sys
import functools
import time

@functools.lru_cache(maxsize=None)
def calc(record, groups):

    # Did we run out of groups? We might still be valid
    if not groups:

        # Make sure there aren't any more damaged springs, if so, we're valid
        if "#" not in record:
            # This will return true even if record is empty, which is valid
            return 1
        else:
            # More damaged springs that we can't fit
            return 0

    # There are more groups, but no more record
    if not record:
        # We can't fit, exit
        return 0

    # Look at the next element in each record and group
    next_character = record[0]
    next_group = groups[0]

    # Logic that treats the first character as pound
    def pound():

        # If the first is a pound, then the first n characters must be
        # able to be treated as a pound, where n is the first group number
        this_group = record[:next_group]
        this_group = this_group.replace("?", "#")

        # If the next group can't fit all the damaged springs, then abort
        if this_group != next_group * "#":
            return 0

        # If the rest of the record is just the last group, then we're
        # done and there's only one possibility
        if len(record) == next_group:
            # Make sure this is the last group
            if len(groups) == 1:
                # We are valid
                return 1
            else:
                # There's more groups, we can't make it work
                return 0

        # Make sure the character that follows this group can be a seperator
        if record[next_group] in "?.":
            # It can be seperator, so skip it and reduce to the next group
            return calc(record[next_group+1:], groups[1:])

        # Can't be handled, there are no possibilites
        return 0

    # Logic that treats the first character as a dot
    def dot():
        # We just skip over the dot looking for the next pound
        return calc(record[1:], groups)

    if next_character == '#':
        # Test pound logic
        out = pound()

    elif next_character == '.':
        # Test dot logic
        out = dot()

    elif next_character == '?':
        # This character could be either character, so we'll explore both
        # possibilities
        out = dot() + pound()

    else:
        raise RuntimeError

    print(record, groups, out)
    return out

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()

        total_combs = 0

        for y, line in enumerate(liste):
            springs, nums = line.split(" ")
            nums = list(map(int,nums.split(",")))

            springs = list(springs)

            temp = len(nums)
            nums.extend(nums)
            nums.extend(nums)
            nums.extend(nums[0:temp:])

            temp = []
            for i in range(5):
                for n in springs:
                    temp.append(n)
                if i != 4:
                    temp.append("?")

            springs = "".join(temp)

            total_combs += calc(springs, tuple(nums))

        return total_combs


if __name__ == "__main__":
    
    start = time.time()
    result = main("test12.txt")
    end = time.time()
    expected = 525152
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    start = time.time()
    result = main("input12.txt")
    end = time.time()
    #assert result == 6717, f"Expected 6717 but got {result}"
    print(result)
    print(end - start)
    