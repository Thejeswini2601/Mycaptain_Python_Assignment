def most_frequent(a):
    d={}
    import operator
    for i in a :
        count=a.count(i)
        d.update({i:count})
    sort=sorted(d.items(),reverse=True,key=operator.itemgetter(1))
    for i in sort:
            print(i)

a=input("enter a string:")
(most_frequent(a))
