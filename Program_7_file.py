import os


def get_min_mpg():
    while True:
        try:
            min_mpg = float(input("Enter the minimum mpg ==> "))
            if min_mpg<0:
                print("Fuel economy given must be greater than 0")
            elif min_mpg>100:
                print("Fuel economy must be less than 100")
            else:
                return min_mpg
        except:
            print("You must enter a number for the fuel economy")      #when a non-num is entered return ask user

def get_file():
    while True:
        user_file = input("Enter the name of the input vehicle file ==> ")
        try:
            with open(user_file,'r') as user_file:
                file_contents = user_file.read()
                user_file.close
                return [[data.strip() for data in line.strip().split('\t')] for line in read_file.readlines()]

        except:
            print("Could not open file", user_file)                   #bad file entry - ask again


def write_to_file(min_miles,save_data):
    while True:
        try:
            output_file = input("Enter the name of the file to output to ==>")
            with open(output_file,'w') as write_file:
                for data in save_data:
                    try:
                        if min_miles>=float(data[7]):
                            write_file.write('{0:<5}{1:<40}{2:<40}{3:>10}\n',(format(data[0],data[1],data[2],data[7])))
                    except:
                        print("Could not convert value invalid for vehicle",data[0],data[1],data[2])
        except:
            print("There is an IO Error",file_name)                 #issue with file name, ask again please.


def main():
    min_mileage= get_min_mpg()
    file_data= get_file()[1:]
    write_to_file(min_mileage,file_data)

main()
