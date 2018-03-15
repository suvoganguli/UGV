import numpy as np
from utils import *

def getIdx(x, roadSegmentLengths):
    sumLengths = 0
    idx = 0
    for k in range(len(roadSegmentLengths)):
        if sumLengths >= x:
            break
        else:
            sumLengths = sumLengths + roadSegmentLengths[k]
            idx = idx + 1

    return idx


def obstacleInfo(lanes, obstaclePresent, EObsStart, NObsStart, EObsEnd, NObsEnd, ThetaObs, idx_OffsetSafeZone):


    #roadSegmentLengths = lanes.roadSegmentLengths
    #laneWidth = lanes.laneWidth

    lane1Lines = lanes.lane1Lines
    lane2Lines = lanes.lane2Lines
    acrossLines = lanes.acrossLines

    idx_StartObstacle, laneNoStart = lanes.insideRoadSegment(EObsStart, NObsStart, lane1Lines, lane2Lines, acrossLines)
    #print(idx_StartObstacle)

    idx_EndObstacle, laneNoEnd = lanes.insideRoadSegment(EObsEnd, NObsEnd, lane1Lines, lane2Lines, acrossLines)
    #print(idx_EndObstacle)

    if laneNoStart != laneNoEnd:
        print("Obtstacle in both lanes")

    idx_StartSafeZone = idx_StartObstacle - idx_OffsetSafeZone

    if laneNoStart == 1:
        EObsStartSafeZone, NObsStartSafeZone = intersect(lane1Lines, acrossLines, idx_StartSafeZone)
    else:
        EObsStartSafeZone, NObsStartSafeZone = intersect(lane2Lines, acrossLines, idx_StartSafeZone)

    p1 = [EObsStartSafeZone, NObsStartSafeZone]
    p2 = [EObsStart, NObsStart]
    lengthSafeZone = distance(p1,p2)
    widthSafeZone = lanes.laneWidth

    p1 = [EObsStart, NObsStart]
    p2 = [EObsEnd, NObsEnd]
    lengthObstacle = distance(p1,p2)
    widthObstacle = lanes.laneWidth


    class obstacle():
        def __init__(self):
            self.obstaclePresent = obstaclePresent
            self.EObsStart = EObsStart
            self.EObsEnd = EObsEnd
            self.NObsStart = NObsStart
            self.NObsEnd = NObsEnd
            self.EObsStartSafeZone = EObsStartSafeZone
            self.NObsStartSafeZone = NObsStartSafeZone
            self.EObsEndSafeZone = EObsStart
            self.NObsEndSafeZone = NObsStart
            self.idx_StartObstacle = idx_StartObstacle
            self.idx_EndObstacle = idx_EndObstacle
            self.idx_StartSafeZone = idx_StartSafeZone
            self.idx_EndSafeZone = idx_StartObstacle
            self.lengthSafeZone = lengthSafeZone
            self.widthSafeZone = widthSafeZone
            self.thetaSafeZone = ThetaObs
            self.lengthObstacle = lengthObstacle
            self.widthObstacle = widthObstacle
            self.thetaObstacle = ThetaObs
            #self.xlimval = xlimval
            #self.ylimval = ylimval
            pass

    return obstacle