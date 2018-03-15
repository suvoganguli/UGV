from roadLaneData import *

mph2fps = 4.4/3

# ----------------------------------------------------------
# USER INPUTS
# ----------------------------------------------------------

# Test Case

case = 'roadStraightNorth'
#case = 'roadStraightEast'
#case = 'roadStraightNorthEast'
#case = 'UGVDemo1'
#case = 'UGVDemo1Debug'


# Experiment Number
# (see case in Main.py)
# roadStraightNorth: exptno = 1
# roadStraightEast: exptno = 11
# roadStraightNorthEast: exptno = 21
# UGVDemo: exptno = 31
# UGDemoDebug: exptno = 32
exptno = 1

# Number of states
# nstates = 6:
#   x0 = E, x1 = N, x2 = V, x3 = chi, x5 = Vdot, x6 = chidot
#   u0 = Vddot, u1 = chiddot
# nstates = 4:
#   x0 = E, x1 = N, x2 = V, x3 = chi
#   u0 = Vdot, u1 = chidot
nstates = 4

# Obstacle Present
# (True or False)
obstaclePresent = True

# ----------------------------------------------------------

if exptno == 1:     # 30 mph, STRAIGHT ROAD NORTH

    if nstates == 6:
        # NMPC Data
        N = 6
        T = 0.4

        # Ipopt settings
        nlpMaxIter = 100
        mpciterations = 20

        # Kinematic Constraints

        E0 = 0 # ft (East, lat)
        N0 = 0 # ft (North, long)
        Chi0 = 0*np.pi/180 # rad (w.r.t. North)
        V0 = 30*mph2fps
        x0 = [E0, N0, V0, Chi0, 0, 0]  # E, N, V, Chi, Vdot, Chidot
        lb_VddotVal = -2 # fps3
        ub_VddotVal = 2 # fps3
        lb_ChiddotVal = -30*np.pi/180 # rad/s2
        ub_ChiddotVal = 30*np.pi/180 # rad/s2
        lataccel_maxVal = 0.5*32.2 # fps2
        useLatAccelCons = 1
        lb_V = -2.0*V0
        ub_V = 2.0*V0

        # Tracking Tuning and Data
        W_P = 1.0      #1.0
        W_V = 1.0
        W_Vddot = 10.0   # 20.0
        W_Chiddot = 1.0 #0.1

        # Road and Obstacle Data
        EObsStart = 0 # ft
        NObsStart = 150 # ft
        EObsEnd = EObsStart # ft
        NObsEnd = NObsStart+20 # ft
        ThetaObs = Chi0 # rad
        idx_OffsetSafeZone = 2

        V_cmd = V0  # fps

        # Terminal constraint
        delta_yRoad = 0.5 # ft
        delta_yRoadRelaxed = 5 # ft, in safe zone
        delta_V = 1*mph2fps # fps

    elif nstates == 4:

        # NMPC Data
        N = 6  # 12
        T = 0.5  # 0.2

        # Ipopt settings
        nlpMaxIter = 100
        mpciterations = 18

        # Kinematic Constraints
        E0 = 0  # ft (North, long)
        N0 = 0  # ft (East, lat)
        Chi0 = 0 * np.pi / 180  # rad
        V0 = 30 * mph2fps
        x0 = [E0, N0, V0, Chi0]  # E, N, V, Chi, Vdot, Chidot

        lb_VdotVal = -2 * 100  # fps3
        ub_VdotVal = 2 * 100  # fps3
        lb_ChidotVal = -20 * np.pi / 180  # rad/s2
        ub_ChidotVal = 20 * np.pi / 180  # rad/s2
        lataccel_maxVal = 0.5 * 32.2  # fps2
        useLatAccelCons = 0
        lb_V = -2.0 * V0
        ub_V = 2.0 * V0

        # Tracking Tuning and Data
        W_P = 1.0
        W_V = 1.0
        W_Vdot = 10.0
        W_Chidot = 1.0

        # Road and Obstacle Data
        EObsStart = 0  # ft
        NObsStart = 180  # ft
        EObsEnd = EObsStart  # ft
        NObsEnd = NObsStart + 20  # ft
        ThetaObs = Chi0  # rad
        idx_OffsetSafeZone = 2

        V_cmd = V0  # fps

        # Terminal constraint
        delta_yRoad = 0.5  # ft
        delta_yRoadRelaxed = 5  # ft, in safe zone
        delta_V = 1 * mph2fps  # fps



elif exptno == 11:      # 30 mph, STRAIGHT ROAD EAST

    if nstates == 6:

        # NMPC Data
        N = 6 #12
        T = 0.4

        # Ipopt settings
        nlpMaxIter = 100
        mpciterations = 15

        # Kinematic Constraints
        E0 = 0 # ft (East, lat)
        N0 = 0 # ft (North, long)
        Chi0 = 90*np.pi/180 # rad (w.r.t. North)
        V0 = 30*mph2fps
        x0 = [E0, N0, V0, Chi0, 0, 0]  # E, N, V, Chi, Vdot, Chidot
        lb_VddotVal = -2 # fps3
        ub_VddotVal = 2 # fps3
        lb_ChiddotVal = -30*np.pi/180 # rad/s2
        ub_ChiddotVal = 30*np.pi/180 # rad/s2
        lataccel_maxVal = 0.5*32.2 # fps2
        useLatAccelCons = 1
        lb_V = -2.0*V0
        ub_V = 2.0*V0

        # Tracking Tuning and Data
        W_P = 1.0
        W_V = 1.0
        W_Vddot = 10.0
        W_Chiddot = 1.0

        # Road and Obstacle Data
        EObsStart = 150 # ft, E
        NObsStart = 0 # ft, N
        EObsEnd = EObsStart + 20 # ft
        NObsEnd = NObsStart
        ThetaObs =  Chi0
        idx_OffsetSafeZone = 2

        V_cmd = V0  # fps

        # Terminal constraint
        delta_yRoad = 0.5 # ft
        delta_yRoadRelaxed = 5 # ft, in safe zone
        delta_V = 1*mph2fps # fps

    elif nstates == 4:

        # NMPC Data
        N = 6  # 12
        T = 0.4  # 0.2

        # Ipopt settings
        nlpMaxIter = 100
        mpciterations = 15

        # Kinematic Constraints
        E0 = 0  # ft (North, long)
        N0 = 250 + 80 + 20 * 0  # ft (East, lat)
        Chi0 = 0 * np.pi / 180  # rad
        V0 = 10 * mph2fps
        x0 = [E0, N0, V0, Chi0]  # E, N, V, Chi, Vdot, Chidot

        lb_VdotVal = -2 * 100  # fps3
        ub_VdotVal = 2 * 100  # fps3
        lb_ChidotVal = -20 * np.pi / 180  # rad/s2
        ub_ChidotVal = 20 * np.pi / 180  # rad/s2
        lataccel_maxVal = 0.5 * 32.2  # fps2
        useLatAccelCons = 0
        lb_V = -2.0 * V0
        ub_V = 2.0 * V0

        # Tracking Tuning and Data
        W_P = 1.0
        W_V = 1.0
        W_Vdot = 10.0
        W_Chidot = 1.0

        # Road and Obstacle Data
        EObsStart = 0  # ft
        NObsStart = 180  # ft
        EObsEnd = EObsStart  # ft
        NObsEnd = NObsStart + 20  # ft
        ThetaObs = Chi0  # rad
        idx_OffsetSafeZone = 2

        V_cmd = V0  # fps

        # Terminal constraint
        delta_yRoad = 0.5 * 5  # ft
        delta_yRoadRelaxed = 5  # ft, in safe zone
        delta_V = 1 * mph2fps  # fps


elif exptno == 21:      # 30 mph, STRAIGHT ROAD 45deg

    if nstates == 6:
        # NMPC Data
        N = 12 #12
        T = 0.2

        # Ipopt settings
        nlpMaxIter = 50
        mpciterations = 20

        # Kinematic Constraints
        E0 = 0 # ft (East, lat)
        N0 = 0 # ft (North, long)
        Chi0 = 45*np.pi/180 # rad (w.r.t. North)
        V0 = 30*mph2fps
        x0 = [E0, N0, V0, Chi0, 0, 0]  # E, N, V, Chi, Vdot, Chidot
        lb_VddotVal = -2 # fps3
        ub_VddotVal = 2 # fps3
        lb_ChiddotVal = -30*np.pi/180 # rad/s2
        ub_ChiddotVal = 30*np.pi/180 # rad/s2
        lataccel_maxVal = 0.5*32.2 # fps2
        useLatAccelCons = 1
        lb_V = -2.0*V0
        ub_V = 2.0*V0

        # Tracking Tuning and Data
        W_P = 1.0
        W_V = 1.0
        W_Vddot = 10.0
        W_Chiddot = 1.0

        # Road and Obstacle Data
        EObsStart = 150/np.sqrt(2) # ft, E
        NObsStart = 150/np.sqrt(2) # ft, N
        EObsEnd = EObsStart + 20/np.sqrt(2) # ft
        NObsEnd = NObsStart + 20/np.sqrt(2)
        ThetaObs =  Chi0
        idx_OffsetSafeZone = 2

        V_cmd = V0  # fps

        # Terminal constraint
        delta_yRoad = 0.5 # ft
        delta_yRoadRelaxed = 5 # ft, in safe zone
        delta_V = 1*mph2fps # fps

    elif nstates == 4:

        # NMPC Data
        N = 6  # 12
        T = 0.4  # 0.2

        # Ipopt settings
        nlpMaxIter = 100
        mpciterations = 15

        # Kinematic Constraints
        E0 = 0  # ft (North, long)
        N0 = 250 + 80 + 20 * 0  # ft (East, lat)
        Chi0 = 0 * np.pi / 180  # rad
        V0 = 10 * mph2fps
        x0 = [E0, N0, V0, Chi0]  # E, N, V, Chi, Vdot, Chidot

        lb_VdotVal = -2 * 100  # fps3
        ub_VdotVal = 2 * 100  # fps3
        lb_ChidotVal = -20 * np.pi / 180  # rad/s2
        ub_ChidotVal = 20 * np.pi / 180  # rad/s2
        lataccel_maxVal = 0.5 * 32.2  # fps2
        useLatAccelCons = 0
        lb_V = -2.0 * V0
        ub_V = 2.0 * V0

        # Tracking Tuning and Data
        W_P = 1.0
        W_V = 1.0
        W_Vdot = 10.0
        W_Chidot = 1.0

        # Road and Obstacle Data
        EObsStart = 0  # ft
        NObsStart = 180  # ft
        EObsEnd = EObsStart  # ft
        NObsEnd = NObsStart + 20  # ft
        ThetaObs = Chi0  # rad
        idx_OffsetSafeZone = 2

        V_cmd = V0  # fps

        # Terminal constraint
        delta_yRoad = 0.5 * 5  # ft
        delta_yRoadRelaxed = 5  # ft, in safe zone
        delta_V = 1 * mph2fps  # fps


elif exptno == 31:               # UGV DEMO

    if nstates == 6:
        # NMPC Data
        N = 6  # 12
        T = 0.4  # 0.2

        # Ipopt settings
        nlpMaxIter = 100
        mpciterations = 30

        # Kinematic Constraints
        E0 = 0  # ft (North, long)
        #N0 = 330  # ft (East, lat)
        N0 = 240 # ft
        Chi0 = 0*np.pi/180  # rad
        V0 = 10*mph2fps
        x0 = [E0, N0, V0, Chi0, 0, 0]  # E, N, V, Chi, Vdot, Chidot

        lb_VddotVal = -2*100  # fps3
        ub_VddotVal = 2*100  # fps3
        lb_ChiddotVal = -30*np.pi/180*2 # rad/s2
        ub_ChiddotVal = 30*np.pi/180*2  # rad/s2
        lataccel_maxVal = 0.5*32.2  # fps2
        useLatAccelCons = 0
        lb_V = 0.9* V0
        ub_V = 1.1 * V0

        # Tracking Tuning and Data
        W_P = 1.0
        W_V = 1.0
        W_Vddot = 20.0
        W_Chiddot = 1.0

        # Road and Obstacle Data
        EObsStart = 0  # ft
        NObsStart = 300  # ft
        EObsEnd = EObsStart  # ft
        NObsEnd = NObsStart + 20  # ft
        ThetaObs = Chi0  # rad
        idx_OffsetSafeZone = 2

        V_cmd = V0  # fps

        # Terminal constraint
        delta_yRoad = 0.5  # ft
        delta_yRoadRelaxed = 5  # ft, in safe zone
        delta_V = 1 * mph2fps  # fps

    elif nstates == 4:

        # NMPC Data
        N = 6  # 12
        T = 0.4  # 0.2

        # Ipopt settings
        nlpMaxIter = 100
        mpciterations = 15

        # Kinematic Constraints
        E0 = 0  # ft (North, long)
        N0 = 250 + 80 + 20 * 0  # ft (East, lat)
        Chi0 = 0 * np.pi / 180  # rad
        V0 = 10 * mph2fps
        x0 = [E0, N0, V0, Chi0]  # E, N, V, Chi, Vdot, Chidot

        lb_VdotVal = -2 * 100  # fps3
        ub_VdotVal = 2 * 100  # fps3
        lb_ChidotVal = -20 * np.pi / 180  # rad/s2
        ub_ChidotVal = 20 * np.pi / 180  # rad/s2
        lataccel_maxVal = 0.5 * 32.2  # fps2
        useLatAccelCons = 0
        lb_V = -2.0 * V0
        ub_V = 2.0 * V0

        # Tracking Tuning and Data
        W_P = 1.0
        W_V = 1.0
        W_Vdot = 10.0
        W_Chidot = 1.0

        # Road and Obstacle Data
        EObsStart = 0  # ft
        NObsStart = 180  # ft
        EObsEnd = EObsStart  # ft
        NObsEnd = NObsStart + 20  # ft
        ThetaObs = Chi0  # rad
        idx_OffsetSafeZone = 2

        V_cmd = V0  # fps

        # Terminal constraint
        delta_yRoad = 0.5 * 5  # ft
        delta_yRoadRelaxed = 5  # ft, in safe zone
        delta_V = 1 * mph2fps  # fps

elif exptno == 32:               # UGV DEMO Debug
    
    if nstates == 6:
        # NMPC Data
        N = 6  #12
        T = 0.4 #0.2
    
        # Ipopt settings
        nlpMaxIter = 100
        mpciterations = 14
    
        # Kinematic Constraints
        E0 = 0 # ft (North, long)
        N0 = 250+80 # ft (East, lat)
        Chi0 = 0*np.pi/180 # rad
        V0 = 10*mph2fps
        x0 = [E0, N0, V0, Chi0, 0, 0]  # E, N, V, Chi, Vdot, Chidot
    
        lb_VddotVal = -2*100 # fps3
        ub_VddotVal = 2*100 # fps3
        lb_ChiddotVal = -30*np.pi/180 # rad/s2
        ub_ChiddotVal = 30*np.pi/180 # rad/s2
        lataccel_maxVal = 0.5*32.2 # fps2
        useLatAccelCons = 0
        lb_V = -2.0*V0
        ub_V = 2.0*V0
    
        # Tracking Tuning and Data
        W_P = 1.0
        W_V = 1.0
        W_Vddot = 10.0
        W_Chiddot = 1.0
    
        # Road and Obstacle Data
        EObsStart = 0 # ft
        NObsStart = 180 # ft
        EObsEnd = EObsStart # ft
        NObsEnd = NObsStart+20 # ft
        ThetaObs = Chi0 # rad
        idx_OffsetSafeZone = 2
    
        V_cmd = V0  # fps
    
        # Terminal constraint
        delta_yRoad = 0.5 # ft
        delta_yRoadRelaxed = 5 # ft, in safe zone
        delta_V = 1*mph2fps # fps
    
    elif nstates == 4:

        # NMPC Data
        N = 6  # 12
        T = 0.4  # 0.2

        # Ipopt settings
        nlpMaxIter = 100
        mpciterations = 15

        # Kinematic Constraints
        E0 = 0  # ft (North, long)
        N0 = 250 + 80 + 20*0  # ft (East, lat)
        Chi0 = 0 * np.pi / 180  # rad
        V0 = 10 * mph2fps
        x0 = [E0, N0, V0, Chi0]  # E, N, V, Chi, Vdot, Chidot

        lb_VdotVal = -2 * 100  # fps3
        ub_VdotVal = 2 * 100  # fps3
        lb_ChidotVal = -20 * np.pi / 180  # rad/s2
        ub_ChidotVal = 20 * np.pi / 180  # rad/s2
        lataccel_maxVal = 0.5 * 32.2  # fps2
        useLatAccelCons = 0
        lb_V = -2.0 * V0
        ub_V = 2.0 * V0

        # Tracking Tuning and Data
        W_P = 1.0
        W_V = 1.0
        W_Vdot = 10.0
        W_Chidot = 1.0

        # Road and Obstacle Data
        EObsStart = 0  # ft
        NObsStart = 180  # ft
        EObsEnd = EObsStart  # ft
        NObsEnd = NObsStart + 20  # ft
        ThetaObs = Chi0  # rad
        idx_OffsetSafeZone = 2

        V_cmd = V0  # fps

        # Terminal constraint
        delta_yRoad = 0.5*5  # ft
        delta_yRoadRelaxed = 5  # ft, in safe zone
        delta_V = 1 * mph2fps  # fps

else:

    print("Error in exptno")

# ------------------------------------------------------------

if nstates == 6:
    # problem size
    nx = 6
    nu = 2
    ncons = 2*N + 4 #running + lataccel + V0 + terminal constraint-y + terminal constraint-V
    t0 = 0
    u0 = np.zeros([N,nu])
    #mpciterations = int(18*N/(6))

    # nlpData
    nlpPrintLevel = 0

    # State and Control indices
    idx_E = 0
    idx_N = 1
    idx_V = 2
    idx_Chi = 3
    idx_Vdot = 4
    idx_Chidot = 5

elif nstates == 4:
    # problem size
    nx = 4
    nu = 2
    ncons = 2 * N + 2  # running + lataccel + terminal constraint-y
    t0 = 0
    u0 = np.zeros([N, nu])
    # mpciterations = int(18*N/(6))

    # nlpData
    nlpPrintLevel = 0

    # State and Control indices
    idx_E = 0
    idx_N = 1
    idx_V = 2
    idx_Chi = 3

    idx_Vdot = 0
    idx_Chidot = 1

else:

    print("Error in nstates")