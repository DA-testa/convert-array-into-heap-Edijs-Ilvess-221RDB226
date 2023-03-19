# python3

def build_heap(data):
    swaps = []
    n=len(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(n):
        current=i
        while current>0:
            par=(current-1)//2
            if data[current]>data[par]:
                break
            swap=data[current]
            data[current]=data[par]
            data[par]=swap
            swaps.append((par,current))
            current=par
    return swaps
def sort_heap(data):
    swaps=build_heap(data)
    n=len(data)
    for i in range(n-1,0,-1):
        current=0
        swap=data[0]
        data[0]=data[i]
        data[i]=swap
        swaps.append((0,i))
    while True:
        first_con=2*current+1
        second_con=2*current+2
        if first_con<i and data[first_con]<data[mini]:
            mini=first_con
        if second_con<i and data[second_con]<data[mini]:
            mini=second_con
        if current!=mini:
            swap=data[current]
            data[current]=data[mini]
            data[mini]=swap
            swaps.append((current,mini))
            current=mini
        else:
            break
    return swaps

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F
    input_IF=input()
    if input_IF[0]=="I":
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    elif input_IF[0]=="F":
        tests=input()
        with open("tests/"+tests) as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        print("I/F error")

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
        
if __name__ == "__main__":
    main()
