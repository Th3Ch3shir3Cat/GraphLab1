import numpy as np;
import math;
import copy;

from tkinter import *;

class model:

    def __init__(self):
        self.edge = self.readFile();

    def readFile(self):
        array = [];
        with open("input.txt") as my_file:
            for line in my_file:
                array.append([float(x) for x in line.split()]);
        return array;

myModel = model();

PROECT = 0;

global matrix_moving;
global matrix_scaling;
global matrix_turn_x;
global matrix_turn_y;
global matrix_turn_z;

matrix_return = np.array([[1,0,0,0],
                          [0,1,0,0],
                          [0,0,1,0],
                          [-350,-150,0,1]]).transpose();

matrix_return2 = np.array([[1,0,0,0],
                           [0,1,0,0],
                           [0,0,1,0],
                           [350,150,0,1]]).transpose();

def sum(e,matr):
    temp = 0;
    for i in range(len(e)):
        temp += e[i] * matr[i];
    return temp;

def multiplication(matr):
    temp = [];
    for e in myModel.edge:
        qwer = [];
        for i in range(len(matr)):
            qwer.append(sum(e,matr[i]));
        temp.append(qwer);
    return temp;

def click_button_move(x,y,z):
    a = 0;
    b = 0;
    c = 0;
    if(len(x.get()) > 0):
        a = int(x.get());
    if(len(y.get()) > 0):
        b = int(y.get());
    if(len(z.get()) > 0):
        c = z.get();
    matrix_moving = np.array([[1,0,0,0],
                 [0,1,0,0],
                 [0,0,1,0],
                 [int(x.get()),int(y.get()),int(z.get()),1]]);
    matrix_moving = matrix_moving.transpose();
    myModel.edge = multiplication(matrix_moving);

def click_button_scale(x,y,z):
    a = 0;
    b = 0;
    c = 0;
    if(len(x.get()) > 0):
        a = float(x.get());
    if(len(y.get()) > 0):
        b = float(y.get());
    if(len(z.get()) > 0):
        c = float(z.get());
    matrix_scaling = np.array([[a,0,0,0],
                      [0,b,0,0],
                      [0,0,c,0],
                      [0,0,0,1]]);
    matrix_scaling = matrix_scaling.transpose();

    myModel.edge = multiplication(matrix_return);
    myModel.edge = multiplication(matrix_scaling);
    myModel.edge = multiplication(matrix_return2);

def click_button_turn(x,y,z):
    a = 0;
    b = 0;
    c = 0;
    if(int(x.get()) > 0):
        a = int(x.get());
    if(int(y.get()) > 0):
        b = int(y.get());
    if(int(z.get()) > 0):
        c = int(z.get());
    matrix_turn_x = np.array([[1,0,0,0],
                              [0,math.cos(math.radians(a)), math.sin(math.radians(a)),0],
                              [0, -math.sin(math.radians(a)), math.cos(math.radians(a)), 0],
                              [0,0,0,1]]).transpose();
    matrix_turn_y = np.array([[math.cos(math.radians(b)),0,-math.sin(math.radians(b)),0],
                              [0,1,0,0],
                              [math.sin(math.radians(b)),0,math.cos(math.radians(b)),0],
                              [0,0,0,1]]).transpose();
    matrix_turn_z = np.array([[math.cos(math.radians(c)),math.sin(math.radians(c)),0,0],
                              [-math.sin(math.radians(c)),math.cos(math.radians(c)),0,0],
                              [0,0,1,0],
                              [0,0,0,1]]).transpose();

    if(a > 0):
        myModel.edge = multiplication(matrix_return);
        myModel.edge = multiplication(matrix_turn_x);
        myModel.edge = multiplication(matrix_return2);
    if(b > 0):
        myModel.edge = multiplication(matrix_return);
        myModel.edge = multiplication(matrix_turn_y);
        myModel.edge = multiplication(matrix_return2);
    if(c > 0):
        myModel.edge = multiplication(matrix_return);
        myModel.edge = multiplication(matrix_turn_z);
        myModel.edge = multiplication(matrix_return2);

def proection():
    global PROECT;
    PROECT = PROECT + 1;
    if(PROECT == 2):
        PROECT = 0;

def update(c):
    c.delete("all");
    temp = [];
    matrix_kosougl = np.array([[1,0,0,0],
                               [0,1,0,0],
                               [-0.5*math.cos(math.radians(45)), -0.5*math.sin(math.radians(45)),0,0],
                               [0,0,0,1]]).transpose();

    matrix_proect = np.array([[1,0,0,0],
                              [0,1,0,0],
                              [0,0,1,-0.0005],
                              [0,0,0,1]]).transpose();

    if PROECT == 0:
        temp = multiplication(matrix_kosougl);
    else:
        temp = multiplication(matrix_proect);
        for i in range(len(temp)):
            temp[i][0] /= temp[i][3];
            temp[i][1] /= temp[i][3];
            temp[i][2] /= temp[i][3];

    for i in range(len(temp) - 2):
        c.create_line(temp[i][0], temp[i][1], temp[i + 1][0], temp[i + 1][1], fill = "white");
    c.create_line(temp[len(myModel.edge) - 2][0], temp[len(myModel.edge) - 2][1], temp[len(myModel.edge) - 1][0], temp[len(myModel.edge) - 1][1],fill = "white");

def main():
    root = Tk();
    root.title("Графика №1");
    root.geometry('900x600');

    canvas = Canvas(root, width = 700, height = 600, bg = 'grey');
    canvas.place(x = 0, y = 0);
    update(canvas);

    lbl_move_x = Label(root, text = "x").place(x = 750, y = 20);
    lbl_move_y = Label(root, text = "y").place(x = 750, y = 40);
    lbl_move_z = Label(root, text = "z").place(x = 750, y = 60);

    lbl_scale_x = Label(root, text = "x").place(x = 750, y = 140);
    lbl_scale_y = Label(root, text = "y").place(x = 750, y = 160);
    lbl_scale_z = Label(root, text = "z").place(x = 750, y = 180);

    lbl_turn_x = Label(root, text = "x").place(x = 750, y = 260);
    lbl_turn_y = Label(root, text = "y").place(x = 750, y = 280);
    lbl_turn_z = Label(root, text = "z").place(x = 750, y = 300);

    move_x = StringVar();
    move_y = StringVar();
    move_z = StringVar();

    scale_x = StringVar();
    scale_y = StringVar();
    scale_z = StringVar();

    turn_x = StringVar();
    turn_y = StringVar();
    turn_z = StringVar();

    txt_move_x = Entry(root, textvariable = move_x, width = 5).place(x = 780, y = 20);
    txt_move_y = Entry(root, textvariable = move_y ,width = 5).place(x = 780, y = 40);
    txt_move_z = Entry(root, textvariable = move_z ,width = 5).place(x = 780, y = 60);

    button_move = Button(root, text = "Переместить", command = lambda:[click_button_move(move_x,move_y,move_z), update(canvas)]).place(x = 750, y = 100);

    txt_scale_x = Entry(root, textvariable = scale_x, width = 5).place(x = 780, y = 140);
    txt_scale_y = Entry(root, textvariable = scale_y, width = 5).place(x = 780, y = 160);
    txt_scale_z = Entry(root, textvariable = scale_z, width = 5).place(x = 780, y = 180);

    button_scale = Button(root, text = "Масштабировать", command = lambda:[click_button_scale(scale_x,scale_y,scale_z), update(canvas)]).place(x = 750, y = 220);

    txt_turn_x = Entry(root, textvariable = turn_x, width = 5).place(x = 780, y = 260);
    txt_turn_y = Entry(root, textvariable = turn_y, width = 5).place(x = 780, y = 280);
    txt_turn_z = Entry(root, textvariable = turn_z, width = 5).place(x = 780, y = 300);

    button_turn = Button(root, text = "Повернуть", command = lambda:[click_button_turn(turn_x, turn_y, turn_z), update(canvas)]).place(x = 770, y = 340);
    button_proection = Button(root, text = "Проекция", command = lambda:[proection(),update(canvas)]).place(x = 770, y = 380);

    root.mainloop();

if __name__ == "__main__":
    main();
