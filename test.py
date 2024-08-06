def test_2(ll: list):
    c = 0
    for ind, val in enumerate(ll):
        if val == 0:
            c += 1
        else:
            ll[ind-c] = ll[ind]

    return ll

ll = [0, 1, 0, 3]

print(test_2(ll))
