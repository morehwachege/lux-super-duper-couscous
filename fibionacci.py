input_num = int(input("Please enter the number of terms: "))

def fibionacci_checker(input_num):
    num1, num2 = 0, 1
    count = 0
    checker_list = []

    if(input_num <= 0):
        print("Invalid input, please enter an integer number bigger than 0")
        print(f"Cannot generate the fibionacci sequence for number {input_num} : ")
    
    elif(input_num == 1):
        print(f"The number {input_num} is not in the Fibionacci sequence")
        print(num1)
    
    else:
        # print(f"Generating Fibonacci Sequence upto {input_num} : ")
        while count < input_num:
            # print(num1)
            checker_list.append(num1)
            num_th = num1 + num2
            # swapping the values for num1 and num2
            num1 = num2
            num2 = num_th
            count += 1
    if not input_num in checker_list:
        print(f"The number {input_num} is not in the Fibionacci sequence")
        if checker_list != []:
            print(checker_list)
    else:
        pass
fibionacci_checker(input_num)