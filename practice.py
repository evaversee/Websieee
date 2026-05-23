A = float(input("Enter Your First Digit :"))

Arithmetic = input("Select (+ - * /) : ")

B = float(input("Enter Your Second Digit :"))

if Arithmetic == "+":
    print("Result :", A + B)

elif Arithmetic == "-":
    print("Result :", A - B)

elif Arithmetic == "*":
    print("Result : ", A * B)

elif Arithmetic == "/":
    if B != 0:
        print("Result", A / B)
    else:
        print(" Cannot Divisible by 0")