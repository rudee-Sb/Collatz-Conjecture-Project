import csv
import time

info = {}
iteration = 1
headers = ["x_value","y_value"]

num = int(input("Enter the number : "))

with open("data.csv", "w") as myfile :
    csv_writer = csv.DictWriter(myfile, fieldnames=headers)
    csv_writer.writeheader()
    info = {
            "x_value": iteration,
            "y_value": num
        }
    csv_writer.writerow(info)
    
    while num > 1 :
        if num % 2 == 0 :
            num = int(num / 2)

            info = {
                    "x_value": iteration,
                    "y_value": num
                }

            csv_writer.writerow(info)

        else:
            num = int((3 * num) + 1)

            info = {
                    "x_value": iteration,
                    "y_value": num
                }

            csv_writer.writerow(info)
        iteration+=1

    else:
        print(num)
        print('Done!')
        info.clear()