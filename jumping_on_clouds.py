def jumpingOnClouds(c):

    count = 0
    idx = 0

    while idx < len(c) - 1:
        # jump up to 2 clouds ahead
        if c[idx] == 0:
            idx += 1
        # if the cloud we jumped onto is a cloud to avoid, still increment count as if we had to backtrack
        count += 1
        idx += 1

    print(count)
    return count


if __name__ == '__main__':

    jumpingOnClouds([0, 0, 0, 0, 1, 0])
    jumpingOnClouds([0, 0, 0, 1, 0, 1, 0])
    jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
