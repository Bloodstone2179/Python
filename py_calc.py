from cmath import sqrt
abc = input("Please enter the side you want to find (A, B, C): ")

if abc == "A" or abc == "a":
    xsqaured = float()
    side_b = float(input("Side B: "))
    side_c = float(input("Side C:"))

    xsqaured = (side_b*side_b) - (side_c*side_c)
    ans = sqrt(xsqaured)
    print("X^2 = " + str(xsqaured))
    print("X = " + str(ans))