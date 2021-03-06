import math
import cmath
import csv
import panda
import matplotlib.pyplot as plt




def leapYearCheck(year):                          # function take the value and puts it in the variable "year"
    year=int(year)                                # year is formatted as integer datatype
    if year%4==0 and year%100!=0 or year%400==0:
        return True                               # funtions returns true or 1 if the year is a leap year

def oddEven(number):                              # function takes the value and stores it in the variable "number"
    number=int(number)                            # number is formatted as integer datatype
    if number%2==0:
        return True                               # funtion returns true or 1 if the number is an even number


def quadraticEquation(a, b, c):
    a=float(a)
    b=float(b)
    c=float(c)

    ans = []
    ans.append(b**2 - 4*a*c)
    
    if ans[0]>0:
        ans.append((-b + math.sqrt(ans[0])/(2*a)))
        ans.append((-b - math.sqrt(ans[0])/(2*a)))

    elif ans[0]==0:
        ans.append(-b/(2*a))

    elif ans[0]<0:

        ans.append((-b + cmath.sqrt(ans[0])/(2*a)))
        ans.append((-b - cmath.sqrt(ans[0])/(2*a)))
    return ans

def isPrime(n):
    n=int(n)
    if n<2:
        return False
    elif n>2:
        for i in range(2,math.ceil(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
    else:
        return True

def lineEquation(x1, y1, x2, y2):
    x1=int(x1)
    y1=int(y1)
    x2=int(x2)
    y2=int(y2)

    equation=[]
    equation.append((y2-y1)/(x2-x1))
    equation.append(y1-equation[0]*x1)
    return equation

def lineStdEquation(x1, y1, x2, y2):
    x1=int(x1)
    y1=int(y1)
    x2=int(x2)
    y2=int(y2)

    equation = []

    equation.append(y2-y1)
    equation.append(x1-x2)
    equation.append((x2-x1)*y1 - (y2-y1)*x1)

    return equation

def populationStdDeviation(datalist):
    mean=sum(datalist)/len(datalist)
    variance=0
    for data in datalist:
        variance=variance+(data-mean)**2
    return (variance/len(datalist))**0.5

def sampleStdDeviation(datalist):
    mean=sum(datalist)/len(datalist)
    variance=0                                   
    for data in datalist:
        variance=variance+(data-mean)**2
    return (variance/(len(datalist)-1))**0.5


def standardDeviation2D(x_values, y_values):
    x_mean=sum(x_values)/len(x_values)
    y_mean=sum(y_values)/len(y_values)
    variance_x=variance_y=0
    for x in x_values:
        
        variance_x =variance_x+(x-x_mean)**2

    for y in y_values:
        variance_y =variance_y+(y-y_mean)**2

    return ((variance_y + variance_x)/len(x_values))**0.5


def dataInput():
    dict={}
    while int(input("Add a city?\n0.No\n1.Yes\n"))!=0:
        key=input("city name\n")
        # dict[key+"_x"]=list(int(x) for x in input("Enter the X for "+key+" separated by space: ").split())
        # dict[key+"_y"]=list(int(y) for y in input("Enter the Y for " +key+" separated by space: ").split())
        dict[key]=list(int(x) for x in input("Enter the X for "+key+" separated by space: ").split()), list(int(y) for y in input("Enter the Y for " +key+" separated by space: ").split())
    return dict
    #the dictionary created and returned here is in the format {'cityname':[x cordinates],[y coordinates],
    #                                                           'cityname':[x cordinates],[y coordinates]}


def citySprawl():
    data=panda.cityDataSet()
    max=0
    cities=[]
    for city, value in data.items():    #this loops through the keys which each city, one by one and the value[0] and value[1] are x and y coordinate list respectively
        
        dispersion=standardDeviation2D(value[0], value[1]) #the value[0] and value[1] are x and y coordinate list respectively
        plt.scatter(value[0], value[1])
        cities.append(city)
        if dispersion>max: #as loop iterates this compares the dispersion and stores the city with higher dispersion
            max=dispersion
            ans=city
    
    print(ans+" Is the most spread out city based upon the dispersion of the coordinates of the houses.")
    plt.legend(cities)
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.show()
    
def sumAndSqSum(list_x, list_y):

    result={'sum_x':sum(list_x), 'sum_y':sum(list_y), 'sum_xy':sum(x*y for x, y in zip(list_x, list_y)), 'sum_x_sq':sum(x**2 for x in list_x), 'sum_y_sq':sum(y**2 for y in list_y)}
    return result

def guestInput():
    list=[]
    

    with open('guestlist.csv', 'a', newline='') as file:
        list.append(input("Enter guest name "))
        list.append(input("Enter age "))
        list.append(input("Enter Phone number "))
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(list)

    return 0

def csvListTranspose(filename):
    
    with open('%s.csv' % filename, newline='') as file:
        reader=csv.reader(file)
        guests=list(reader)

        names=list(map(list, zip(*guests)))
        

        return names

def strToInt(str_list): #function to conver list datatype from string to integers, pass list with strings, as argument and returns same list with integers
        int_list = list(int(x) for x in str_list)
        return int_list
