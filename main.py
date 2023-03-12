# python3

def parallel_processing(n, m, data):
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    thread_number = [0] * n
    output = []

    for i in range(m):
        next_thread = 0
        for j in range(1,n):
            if thread_number[j] < thread_number[next_thread]:
                next_thread = j
        
        start = thread_number[next_thread]
        finish = start + data[i]

        thread_number[next_thread] = finish
        output.append((next_thread, start))

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    #n = 0
    #m = 0
    n, m = map(int, input().split())
    if not(1 <= n <= 10**5):
        raise ValueError("n range is between 1 and 10^5")
    if not(1 <= m <= 10**5):
        raise ValueError("m range is between 1 and 10^5")
    data = list(map(int, input().split()))
    for i in range(m):
        if not(0 <= data[i] <= 10**9):
            raise ValueError("Elements between 0 and 10^9")

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i in range(m):
        print(result[i][0], result[i][1])

if __name__ == "__main__":
    main()
