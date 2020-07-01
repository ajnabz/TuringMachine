#assign character variables
A, B, L, R, D, H, S, o = 'A', 'B', 'L', 'R', '♦', '♥', '∧', '1'

#import timer to time how long the program takes
import time
#set start time for whole program
start = time.time()

#create the array for the users input to be stored in
arr = []
#set value of i - this will increment as the user adds more symbols to the tape
i = 0
#set value of loop so that the while loops will continue until value changed/'break' called
loop = 1
#inform user of what to enter
print("Enter 1 or ♦ (multiply). To finish tape, press enter key")

while loop == 1:
    #increment i every iteration of the while loop
    i += 1
    #get the users input
    userInput = input("Enter symbol %d: " %i)
    #if the user doesnt enter a value (presses enter key) then break out of the while loop and being the Turing machine
    if userInput == '':
        break
    #if the user inputs 0 then return error message and ask user to input again
    #this is not necessary as the Turing machine will terminate as soon as it reads in a 0
    if userInput == '0':
        print("Cannot multiply by 0")
        #if user inputs a second correct value then append the symbol to the array
        if userInput == '♦' or userInput == '1' or userInput == '∧':
            arr.append(userInput)
            print(arr)
        #if the user inputs a second incorrect value, do not accept it and try again
        else:
            print("Input not accepted")
            i -= 1
    #only allow user to input ♦, 1 or ∧ as a symbol
    if userInput == '♦' or userInput == '1' or userInput == '∧':
        #add symbol to array and print the tape
        arr.append(userInput)
        print(arr)
    else:
        #if the user doesnt enter allowed symbols, print error message
        print("Invalid input. Please enter: 1, ♦ or ∧ ")
        userInput = input("Enter symbol %d: " %i)
        if userInput == '♦' or userInput == '1' or userInput == '∧':
            arr.append(userInput)
            print(arr)
        else:
            print("Input not accepted")
            i -= 1

#if the user does not add any symbols to the array, return an error message
if len(arr) == 0:
    print("Error! No tape inputted")

#insert a space at location 0 which will act as location -1
arr.insert(0, S)
#add 5 extra ∧ symbols
arr.extend(S * 5)
#create a counter to keep track of how many tapes are being printed
counter = 0
#create a counter to sum all of the 1s after the ♥ symbol - answer of the multiplication
countOnes = 0
print()
#print the tape before beginnning the multiplication
print ('| ' + ' | '.join(arr))

#start at state q0
state = 0
#start pointer at 1 as ∧ symbol is set at 0
j = 1

#set start time after user input to ensure it times the multiplication only
startMult = time.time()

#while loop will run until loop value changed
while loop == 1:

    #state 0
    #at state q0 and the machine reads in a 1
    if state == 0 and arr[j] == '1':
        #keep the state at q0
        state = 0
        #keep the value in the array location, 1
        arr[j] = o
        print()
        #print the state location
        print("State q", state)
        #print the pointer location
        print("Pointer at", j)
        #plus or minus 1 depending on whether the tape is moving right or left
        j = j + 1
        #print the tape and add one to the tape counter
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 0 and arr[j] == '♦':
        state = 0
        arr[j] = D
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j + 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 0 and arr[j] == '0':
        state = 9
        arr[j] = '0'
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 0 and arr[j] == '∧':
        state = 1
        arr[j] = H
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    #state 1
    if state == 1 and arr[j] == '♦':
        state = 1
        arr[j] = D
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 1 and arr[j] == '1':
        state = 1
        arr[j] = o
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 1 and arr[j] == '∧':
        state = 2
        arr[j] = S
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j + 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    #state 2
    if state == 2 and arr[j] == '1':
        state = 3
        arr[j] = A
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j + 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 2 and arr[j] == '♦':
        state = 8
        arr[j] = D
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    #state 3
    if state == 3 and arr[j] == '♦':
        state = 4
        arr[j] = D
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j + 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 3 and arr[j] == '1':
        state = 3
        arr[j] = o
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j + 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    #state 4
    if state == 4 and arr[j] == '1':
        state = 5
        arr[j] = B
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j + 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 4 and arr[j] == '♥':
        state = 7
        arr[j] = H
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    #state 5
    if state == 5 and arr[j] == '♥':
        state = 5
        arr[j] = H
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j + 1
        print ('| ' + ' | '.join(arr))
        counter += 1
        
    if state == 5 and arr[j] == '1':
        state = 5
        arr[j] = o
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j + 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 5 and arr[j] == '∧':
        state = 6
        #add an extra space to the end of the tape for every 1 added
        #ensures no 'out of range' error message when adding multiple 1s
        arr.insert(j, S)
        arr[j] = o
        #add one to counter to get the answer to the multiplication
        countOnes += 1
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    #state 6
    if state == 6 and arr[j] == '1':
        state = 6
        arr[j] = o
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 6 and arr[j] == '♥':
        state = 6
        arr[j] = H
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 6 and arr[j] == 'B':
        state = 4
        arr[j] = B
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j + 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    #state 7
    if state == 7 and arr[j] == 'B':
        state = 7
        arr[j] = o
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 7 and arr[j] == '1':
        state = 7
        arr[j] = o
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 7 and arr[j] == '♦':
        state = 7
        arr[j] = D
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 7 and arr[j] == 'A':
        state = 2
        arr[j] = A
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j + 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    #state 8
    if state == 8 and arr[j] == 'A':
        state = 8
        arr[j] = o
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 8 and arr[j] == '∧':
        state = 10
        arr[j] = S
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j + 1
        print ('| ' + ' | '.join(arr))
        counter += 1
        
    #state 9
    if state == 9 and arr[j] == '∧':
        state = 10
        arr[j] = S
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j + 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 9 and arr[j] == '1':
        state = 9
        arr[j] = o
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    if state == 9 and arr[j] == '♦':
        state = 9
        arr[j] = D
        print()
        print("State q", state)
        print("Pointer at", j)
        j = j - 1
        print ('| ' + ' | '.join(arr))
        counter += 1

    #state f / state 10
    if state == 10:
        #break out of while loop once in final state
        loop = 2
        print()
        print("State q", state)
        print("Pointer at", j)
        print("Tape complete")
        print()
        print("Final Tape:")
        print ('| ' + ' | '.join(arr))
        counter += 1


            

print()
#print the number of tapes
print("Number of tapes = ", counter)
#print the answer of the multiplication
print("Answer = ", countOnes)
#print the time for the program to run in seconds
print("Time taken for program to run = %s seconds" % (time.time() - start))
#print the time for the multiplication to run in seconds
print("Time taken for multiplication to run = %s seconds" % (time.time() - startMult))
