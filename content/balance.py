from gen import move_answer
# (unit, checkpoint index, new position of the correct option)
for n, qi, t in [(20, 1, 0), (18, 1, 0), (9, 0, 0), (16, 0, 0), (14, 0, 0)]:
    move_answer(n, qi, t)
