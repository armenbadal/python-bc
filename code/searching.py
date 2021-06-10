def linearSearch(elist, sv):
    for inx, value in enumerate(elist):
       if value == sv:
           return inx

    return -1


# որոնել դատարկ ցուցակում
ix = linearSearch([], 7)
print(ix)  # ակնկալվում է ix == -1

# որոնել ցուցակից բացակայող տարրը
ix = linearSearch([2, 4, 6, 8], 5)
print(ix)  # նորից ակնկալվում է ix == -1

# որոնել ցուցակում առկա տարրը
ix = linearSearch([1, 3, 5, 7, 9], 5)
print(ix)  # նորից ակնկալվում է ix == 2

