#import packages
import sys
import pandas as pd
import numpy as np

# Formula for Absolute trick and Square Trick
def trick(cho,w1,w2):
    #p = input("Input the point: (sepate the x and y with commas): ")
    point = input("\nInput the point: (sepate the x and y with commas): ")
    point = point.split(",")
    print("\nPoint: ")
    print(point)
    learning_rate = float(input("\nInput Learning Rate: "))
    if cho ==1:
        p = float(point[0])
        w_1 = w1 + p*learning_rate
        w_2 = w2+learning_rate
        print("\nAbsolute Trick Formula: ")
        print("\ny = "+str(w_1)+"x + ("+str(w_2)+")")
    elif cho ==2:
        p = float(point[0])
        q = float(point[1])
        qi = w1*p+w2
        w_1 = w1+p*(q-qi)*learning_rate
        w_2 = w2+(q-qi)*learning_rate
        print("\nAbsolute Square Formula: ")
        print("\ny = "+str(w_1)+"x + ("+str(w_2)+")")

# Formula for Mean Absolute Error and Mean Square Error
def mean_error(cho,w1,w2):
    num_points = int(input("\nHow many points are you going to analyse: "))
    l_points = []
    for i in range(num_points):
        point = input("\nInput the point: (sepate the x and y with commas): ")
        point = point.split(",")
        for i in range(len(point)):
            point[i] = float(point[i])
        l_points.append(point)
    # DataFrame for all times
    points = pd.DataFrame(l_points, columns = ["x","y"])
    #points = pd.to_numeric(points, errors='coerce')
    if cho ==3:
        line_points = line_point(points,w1,w2)
        y_yi = abs(points["y"]-line_points["yi"])
        sum_y_yi = y_yi.sum()
        mean_abs_error = sum_y_yi/num_points
        print("\nMean Absolute Error: "+str(mean_abs_error))
    elif cho ==4:
        line_points = line_point(points,w1,w2)
        y_yi = (points["y"]-line_points["yi"])**2
        sum_y_yi = y_yi.sum()
        mean_abs_error = sum_y_yi/num_points
        print("\nMean Square Error: "+str(mean_abs_error))

def line_point(l_p,w_1,w_2):
    yi_value = []
    for i in range(len(l_p)):
        yi = w_1*l_p["x"][i]+w_2
        yi_value.append(yi)
    l_p["yi"]= yi_value
    l_p.drop(['y'], axis=1)
    return l_p


# main script
def main():
    w1_i = float(input("\nInsert W1: "))
    w2_i = float(input("Insert W2: "))
    print("\nthe line formula is:")
    print("y = "+str(w1_i)+"x + "+str(w2_i))
    print("\n Choose formulas")
    print("1: Absolute Trick")
    print("2: Square Trick")
    print("3: Mean Absolute Error")
    print("4: Mean Square Error")
    choice = int(input("choice: "))
    if choice == 1 or choice == 2:
        print(trick(choice,w1_i,w2_i))
    elif choice == 3 or choice == 4:
        print(mean_error(choice,w1_i,w2_i))

# calling main script
if __name__ == "__main__":
    main()
