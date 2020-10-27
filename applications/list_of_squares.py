def list_of_squares(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d





if __name__ == '__main__':

    
    lis = list_of_squares(12)
    print(lis)
    print(list_of_squares(12))
    print(list_of_squares(9))
    