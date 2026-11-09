while True:                                    #never stop by itself, only break
    answer = input("ener a positive number: ") #ask every round
    if answer.isdigit() and int(answer) > 0: #both mush be true: all digits AND above 0
        print(f"you entered a posistive number: {answer}")
        break  #valid: stop the loop
    else:
        print("that is not a positive number, pleaase try again")#invalid: loop asks again