from nmpc import *
import printPlots
from problemData import *
from roadLaneData import *
from obstacleData import *
import time

# -------------------------------------------------------------------
# Main.py lets the user run different test cases for Model
# Predictive Control (MPC) based trajectory generation
#
# The user needs to select 3 items:
# 1. Test Case Type: Road shape and orientation
# 2. Experiment Number: Sets various design parameters for MPC
# 3. Number of States: Sets the vehicles states and control states
#
# Edit problemData.py to run different experiments
#
# Version 9.0
# 01/15/2018
# -------------------------------------------------------------------

# Road and Lane data
lanesClass = roadLanes(case)
lanes = lanesClass()

# Obstacle data (static)
obstacleClass = obstacleInfo(lanes, obstaclePresent, EObsStart, NObsStart, EObsEnd, NObsEnd, ThetaObs, idx_OffsetSafeZone)
obstacle = obstacleClass()

# Storage data
t = np.zeros([mpciterations, 1])
x = np.zeros([mpciterations, nx])
u = np.zeros([mpciterations, nu])

# Iteration data
tmeasure = t0
xmeasure = x0
u_new = np.zeros([1,nu])
mpciter = 0

# print to File
writeToFile = True
if writeToFile == True:
    fileName = 'logFile.txt'
    fHandle = open(fileName, 'w')
else:
    fHandle = -1
    fileName = ''

tElapsed = np.zeros(mpciterations)

# Main loop
while mpciter < mpciterations:

    #if mpciter % 25 == 0:
    #    print(" k = %d" % mpciter)

    #  get new initial value
    t0, x0 = measureInitialValue(tmeasure, xmeasure)

    # solve optimal control problem
    tStart = time.time()
    u_new, info = solveOptimalControlProblem(N, t0, x0, u0, T, ncons, nu, lanes, obstacle)
    tElapsed[mpciter] = (time.time() - tStart)

    # solution information
    printPlots.nmpcPrint(mpciter, info, N, x0, writeToFile, fHandle, tElapsed[mpciter], \
                         lanes, obstacle, u_new)

    # mpc  future path plot
    printPlots.nmpcPlotSol(u_new, lanes, mpciter, mpciterations, x0, obstacle, case, info)

    # store closed loop data
    t[mpciter] = tmeasure
    for k in range(nx):
        x[mpciter, k] = xmeasure[k]
    for j in range(nu):
        u[mpciter, j] = u_new[0,j]

    # apply control
    tmeasure, xmeasure = applyControl(T, t0, x0, u_new)

    # prepare restart
    u0 = shiftHorizon(N, u_new)

    mpciter = mpciter + 1

# close log file
if writeToFile == True:
    fHandle.close()

# create plots
print('done!')
figno = printPlots.nmpcPlot(t, x, u, lanes, obstacle, tElapsed, case)

# Save Data
answer =  raw_input('Save Figures and Data [y/n]:  ')
if answer == 'y':
    dirname = raw_input('Enter Folder Name: ')
    printPlots.savePlots(dirname, figno)



