def tim(ds,pt):
    find =ds.count(pt)
    return find

ds = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8]
n= int(input("tim cai gi "))
print(f"cai can tim {n}, va có {tim(ds,n)}")
