import copy

def F(a):
    x = copy.deepcopy(a)
    # Face Rotation
    a[3][6] = x[5][6]
    a[3][7] = x[4][6]
    a[3][8] = x[3][6]
    a[4][6] = x[5][7]
    a[4][8] = x[3][7]
    a[5][6] = x[5][8]
    a[5][7] = x[4][8]
    a[5][8] = x[3][8]
    #Side Rotation
    a[2][6] = x[5][5]
    a[2][7] = x[4][5]
    a[2][8] = x[3][5]
    a[3][9] = x[2][6]
    a[4][9] = x[2][7]
    a[5][9] = x[2][8]
    a[6][6] = x[5][9]
    a[6][7] = x[4][9]
    a[6][8] = x[3][9]
    a[5][5] = x[6][8]
    a[4][5] = x[6][7]
    a[3][5] = x[6][6]

def Fi(a):
    x = copy.deepcopy(a)
    # Face Rotation
    a[3][6] = x[3][8]
    a[3][7] = x[4][8]
    a[3][8] = x[5][8]
    a[4][6] = x[3][7]
    a[4][8] = x[5][7]
    a[5][6] = x[3][6]
    a[5][7] = x[4][6]
    a[5][8] = x[5][6]
    # Side Rotation
    a[5][5] = x[2][6]
    a[4][5] = x[2][7]
    a[3][5] = x[2][8]
    a[2][6] = x[3][9]
    a[2][7] = x[4][9]
    a[2][8] = x[5][9]
    a[5][9] = x[6][6]
    a[4][9] = x[6][7]
    a[3][9] = x[6][8]
    a[6][8] = x[5][5]
    a[6][7] = x[4][5]
    a[6][6] = x[3][5]

def R(a):
    x = copy.deepcopy(a)
    # Side Rotation
    a[3][0] = x[2][8]
    a[4][0] = x[1][8]
    a[5][0] = x[0][8]
    a[8][8] = x[3][0]
    a[7][8] = x[4][0]
    a[6][8] = x[5][0]
    a[3][8] = x[6][8]
    a[4][8] = x[7][8]
    a[5][8] = x[8][8]
    a[0][8] = x[3][8]
    a[1][8] = x[4][8]
    a[2][8] = x[5][8]
    # Face Rotation
    a[3][11] = x[3][9]
    a[4][11] = x[3][10]
    a[5][11] = x[3][11]
    a[3][10] = x[4][9]
    a[5][10] = x[4][11]
    a[3][9] = x[5][9]
    a[4][9] = x[5][10]
    a[5][9] = x[5][11]

def Ri(a):
    x = copy.deepcopy(a)
    # Face Rotation
    a[3][9] = x[3][11]
    a[3][10] = x[4][11]
    a[3][11] = x[5][11]
    a[4][9] = x[3][10]
    a[4][11] = x[5][10]
    a[5][9] = x[3][9]
    a[5][10] = x[4][9]
    a[5][11] = x[5][9]
    # Side Rotation
    a[2][8] = x[3][0]
    a[1][8] = x[4][0]
    a[0][8] = x[5][0]
    a[3][0] = x[8][8]
    a[4][0] = x[7][8]
    a[5][0] = x[6][8]
    a[6][8] = x[3][8]
    a[7][8] = x[4][8]
    a[8][8] = x[5][8]
    a[3][8] = x[0][8]
    a[4][8] = x[1][8]
    a[5][8] = x[2][8]

def L(a):
    x = copy.deepcopy(a)
    # Face Rotation
    a[3][3] = x[5][3]
    a[3][4] = x[4][3]
    a[3][5] = x[3][3]
    a[4][3] = x[5][4]
    a[4][5] = x[3][4]
    a[5][3] = x[5][5]
    a[5][4] = x[4][5]
    a[5][5] = x[3][5]
    # Side Rotation
    a[0][6] = x[5][2]
    a[1][6] = x[4][2]
    a[2][6] = x[3][2]
    a[3][6] = x[0][6]
    a[4][6] = x[1][6]
    a[5][6] = x[2][6]
    a[8][6] = x[5][6]
    a[7][6] = x[4][6]
    a[6][6] = x[3][6]
    a[3][2] = x[8][6]
    a[4][2] = x[7][6]
    a[5][2] = x[6][6]

def Li(a):
    x = copy.deepcopy(a)
    # Face Rotation
    a[5][3] = x[3][3]
    a[4][3] = x[3][4]
    a[3][3] = x[3][5]
    a[5][4] = x[4][3]
    a[3][4] = x[4][5]
    a[5][5] = x[5][3]
    a[4][5] = x[5][4]
    a[3][5] = x[5][5]
    # Side Rotation
    a[5][2] = x[0][6]
    a[4][2] = x[1][6]
    a[3][2] = x[2][6]
    a[0][6] = x[3][6]
    a[1][6] = x[4][6]
    a[2][6] = x[5][6]
    a[5][6] = x[8][6]
    a[4][6] = x[7][6]
    a[3][6] = x[6][6]
    a[8][6] = x[3][2]
    a[7][6] = x[4][2]
    a[6][6] = x[5][2]

def U(a):
    x = copy.deepcopy(a)
    # Face Rotation
    a[0][6] = x[2][6]
    a[0][7] = x[1][6]
    a[0][8] = x[0][6]
    a[1][6] = x[2][7]
    a[1][8] = x[0][7]
    a[2][6] = x[2][8]
    a[2][7] = x[1][8]
    a[2][8] = x[0][8]
    # Side Rotation
    a[3][2] = x[3][5]
    a[3][1] = x[3][4]
    a[3][0] = x[3][3]
    a[3][11] = x[3][2]
    a[3][10] = x[3][1]
    a[3][9] = x[3][0]
    a[3][6] = x[3][9]
    a[3][7] = x[3][10]
    a[3][8] = x[3][11]
    a[3][3] = x[3][6]
    a[3][4] = x[3][7]
    a[3][5] = x[3][8]

def Ui(a):
    x = copy.deepcopy(a)
    # Face Rotation
    a[2][6] = x[0][6]
    a[1][6] = x[0][7]
    a[0][6] = x[0][8]
    a[2][7] = x[1][6]
    a[0][7] = x[1][8]
    a[2][8] = x[2][6]
    a[1][8] = x[2][7]
    a[0][8] = x[2][8]
    # Side Rotation
    a[3][5] = x[3][2]
    a[3][4] = x[3][1]
    a[3][3] = x[3][0]
    a[3][2] = x[3][11]
    a[3][1] = x[3][10]
    a[3][0] = x[3][9]
    a[3][9] = x[3][6]
    a[3][10] = x[3][7]
    a[3][11] = x[3][8]
    a[3][6] = x[3][3]
    a[3][7] = x[3][4]
    a[3][8] = x[3][5]

def D(a):
    x = copy.deepcopy(a)
    # Face Rotation
    a[6][6] = x[8][6]
    a[6][7] = x[7][6]
    a[6][8] = x[6][6]
    a[7][6] = x[8][7]
    a[7][8] = x[6][7]
    a[8][6] = x[8][8]
    a[8][7] = x[7][8]
    a[8][8] = x[6][8]
    # Side Rotation
    a[5][6] = x[5][3]
    a[5][7] = x[5][4]
    a[5][8] = x[5][5]
    a[5][9] = x[5][6]
    a[5][10] = x[5][7]
    a[5][11] = x[5][8]
    a[5][0] = x[5][9]
    a[5][1] = x[5][10]
    a[5][2] = x[5][11]
    a[5][3] = x[5][0]
    a[5][4] = x[5][1]
    a[5][5] = x[5][2]

def Di(a):
    x = copy.deepcopy(a)
    # Face Rotation
    a[8][6] = x[6][6]
    a[7][6] = x[6][7]
    a[6][6] = x[6][8]
    a[8][7] = x[7][6]
    a[6][7] = x[7][8]
    a[8][8] = x[8][6]
    a[7][8] = x[8][7]
    a[6][8] = x[8][8]
    # Side Rotation
    a[5][3] = x[5][6]
    a[5][4] = x[5][7]
    a[5][5] = x[5][8]
    a[5][6] = x[5][9]
    a[5][7] = x[5][10]
    a[5][8] = x[5][11]
    a[5][9] = x[5][0]
    a[5][10] = x[5][1]
    a[5][11] = x[5][2]
    a[5][0] = x[5][3]
    a[5][1] = x[5][4]
    a[5][2] = x[5][5]

def B(a):
    x = copy.deepcopy(a)
    # Face Rotation
    a[3][0] = x[5][0]
    a[3][1] = x[4][0]
    a[3][2] = x[3][0]
    a[4][0] = x[5][1]
    a[4][2] = x[3][1]
    a[5][0] = x[5][2]
    a[5][1] = x[4][2]
    a[5][2] = x[3][2]
    # Side Rotation
    a[0][8] = x[5][11]
    a[0][7] = x[4][11]
    a[0][6] = x[3][11]
    a[3][3] = x[0][8]
    a[4][3] = x[0][7]
    a[5][3] = x[0][6]
    a[8][8] = x[5][3]
    a[8][7] = x[4][3]
    a[8][6] = x[3][3]
    a[3][11] = x[8][8]
    a[4][11] = x[8][7]
    a[5][11] = x[8][6]

def Bi(a):
    x = copy.deepcopy(a)
    #Face Rotation
    a[5][0] = x[3][0]
    a[4][0] = x[3][1]
    a[3][0] = x[3][2]
    a[5][1] = x[4][0]
    a[3][1] = x[4][2]
    a[5][2] = x[5][0]
    a[4][2] = x[5][1]
    a[3][2] = x[5][2]
    # Side Rotation
    a[5][11] = x[0][8]
    a[4][11] = x[0][7]
    a[3][11] = x[0][6]
    a[0][8] = x[3][3]
    a[0][7] = x[4][3]
    a[0][6] = x[5][3]
    a[5][3] = x[8][8]
    a[4][3] = x[8][7]
    a[3][3] = x[8][6]
    a[8][8] = x[3][11]
    a[8][7] = x[4][11]
    a[8][6] = x[5][11]

def HR(a): #Middle row horizontally to the right
    x = copy.deepcopy(a)
    a[4][0] = x[4][9]
    a[4][1] = x[4][10]
    a[4][2] = x[4][11]
    a[4][3] = x[4][0]
    a[4][4] = x[4][1]
    a[4][5] = x[4][2]
    a[4][6] = x[4][3]
    a[4][7] = x[4][4]
    a[4][8] = x[4][5]
    a[4][9] = x[4][6]
    a[4][10] = x[4][7]
    a[4][11] = x[4][8]

def HL(a): #Middle row horizontally to the left
    x = copy.deepcopy(a)
    a[4][9] = x[4][0]
    a[4][10] = x[4][1]
    a[4][11] = x[4][2]
    a[4][0] = x[4][3]
    a[4][1] = x[4][4]
    a[4][2] = x[4][5]
    a[4][3] = x[4][6]
    a[4][4] = x[4][7]
    a[4][5] = x[4][8]
    a[4][6] = x[4][9]
    a[4][7] = x[4][10]
    a[4][8] = x[4][11]

def VU(a): #Middle row vertically up
    x = copy.deepcopy(a)
    a[0][7] = x[3][7]
    a[1][7] = x[4][7]
    a[2][7] = x[5][7]
    a[3][7] = x[6][7]
    a[4][7] = x[7][7]
    a[5][7] = x[8][7]
    a[6][7] = x[5][1]
    a[7][7] = x[4][1]
    a[8][7] = x[3][1]
    a[5][1] = x[0][7]
    a[4][1] = x[1][7]
    a[3][1] = x[2][7]

def VD(a): #Middle row vertically down
    x = copy.deepcopy(a)
    a[3][7] = x[0][7]
    a[4][7] = x[1][7]
    a[5][7] = x[2][7]
    a[6][7] = x[3][7]
    a[7][7] = x[4][7]
    a[8][7] = x[5][7]
    a[5][1] = x[6][7]
    a[4][1] = x[7][7]
    a[3][1] = x[8][7]
    a[0][7] = x[5][1]
    a[1][7] = x[4][1]
    a[2][7] = x[3][1]
