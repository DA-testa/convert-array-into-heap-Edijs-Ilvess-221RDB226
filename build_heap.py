# python3

def build_heap(data):
    swaps = []
    n=len(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(n//2,-1,-1):
        current=i
        first_con=2*current+1
        second_con=2*current+2
        while first_con<n:
            tiny=current
            if data[first_con]<data[tiny]:
                tiny=first_con
            if second_con<n and data[second_con]<data[tiny]:
                tiny=second_con
            if tiny!=current:
                swap=data[tiny]
                data[tiny]=data[current]
                data[current]=swap
                swaps.append((current, tiny))
                current=tiny
                first_con=2*current+1
                second_con=2*current+2
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
        data = list(map(int, input().strip().split()))
    elif input_IF[0]=="F":
        tests=input()
        with open("test/"+tests) as f:
            n = int(f.readline())
            data = list(map(int, f.readline().strip().split()))
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
