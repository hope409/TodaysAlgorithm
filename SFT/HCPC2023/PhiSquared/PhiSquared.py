def find_last_one(cur_micro):
    stack = []
    top = -1
    i = 0

    while len(cur_micro) > 1:
        # If we have completed a full pass over the current microorganisms
        if i == len(cur_micro):
            cur_micro = stack
            top = -1
            i = 0
            stack = []
            continue

        cur_idx, cur_size = cur_micro[i]  # Current microorganism
        i += 1  # Move to the next index

        # Size of the new microorganism after absorption
        new_size = cur_size

        # If it's the first microorganism
        if i == 1:
            next_idx, next_size = cur_micro[i]
            # If the current size is greater than or equal to the next size
            if cur_size >= next_size:
                new_size += next_size
                i += 1  # Move to the next next microorganism
            stack.append((cur_idx, new_size))
            top += 1
            continue

        # Compare with the previous microorganism
        prev_idx, prev_size = stack[top]
        if cur_size >= prev_size:
            new_size += prev_size
            stack.pop()
            top -= 1

        # If it's the last microorganism, push to stack directly
        if i == len(cur_micro):
            stack.append((cur_idx, new_size))
            continue

        # Compare with the next microorganism
        next_idx, next_size = cur_micro[i]
        if cur_size >= next_size:
            new_size += next_size
            i += 1  # Move to the next next microorganism

        stack.append((cur_idx, new_size))
        top += 1

    # Output the information of the remaining microorganism
    last_index, last_size = cur_micro[0]
    print(last_size)
    print(last_index)

n = int(input())
micros = [(idx + 1, size) for idx, size in enumerate(list(map(int, input().split())))]
find_last_one(micros)