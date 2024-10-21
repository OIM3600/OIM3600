def draw(n):
    """
    #
    ##
    ###
    """
    for i in range(n):
        print("🧱" * (i + 1))


def draw_recur(n):
    print(f'{n=}')
    if n == 0:
        return
    draw_recur(n - 1)
    print("🧱" * n)


# draw(4)
draw_recur(4)
