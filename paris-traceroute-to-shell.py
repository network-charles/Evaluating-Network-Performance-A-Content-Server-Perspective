# Subprocess makes it possible to run other languages inside a Python script.
import subprocess

# A mini python program is defined, so that it runs only when you call it.
def pinger():
    # The batch script file is called from the folder it was saved in my PC.
    subprocess.call([r'sh', '/mnt/c/Users/Admin/Documents/Project/./shellCopy.sh'])

try:
    number_of_runs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

    string_per_run = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", "thirty", "thirty-one", "thirty-two", "thirty-three", "thirty-four", "thirty-five", "thirty-six", "thirty-seven", "thirty-eight", "thirty-nine", "forty", "forty-one", "forty-two", "forty-three", "forty-four", "forty-five", "forty-six", "forty-seven", "forty-eight", "forty-nine", "fifty"]

    for run in number_of_runs:
        pinger()
        print(f'{string_per_run[run]} Paris traceroute has been completed')

except IndexError:
    pass
