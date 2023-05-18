
def reverseStringWordWise(string):
    
    #Your code goes here
    output = string.split()

    output_str = ""

    for i in range(len(output) - 1, -1, -1):
        output_str = output_str + output[i] + " "

        # if i == 0:
        #     output_str = output_str + output[i]

    return output_str


string = input()
ans = reverseStringWordWise(string)
print(ans)
        
