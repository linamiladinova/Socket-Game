import os
import socket
import threading

HOST = "130.204.10.84"
PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

w, h = 60, 30

global free_row
free_row = 1

grid = [["#" for x in range(w)] for y in range(h)]

def render():
    os.system("clear")
    for y in range(h):
        for x in range(w):
            print(grid[y][x], end ="")
        print("")

for y in range(int(h-2)):
    for x in range(int(w-2)):
        grid[y+1][x+1] = " "

render()

def receive():
    global free_row
    while(1):
        answer = (s.recv(1024).decode("utf-8"))
        print(answer)
        if answer != " ":
            for i in range(len(answer)):
                grid[free_row][i+2] = answer[i]
            render()
            free_row += 1

x = threading.Thread(target = receive)

x.start()

while (free_row != 20):
    string = input(" > ")
    s.send(string.encode("utf-8"))

s.close()
