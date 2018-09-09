# Normalize all data in dataset
def NormalizeData(lrarray_5, lrarray_10, outdata, trainlables, windowsize):
    input_slopes = []
    input_intercept = []
    labels = []
    for i in range (6, len(trainlables)):
        index = outdata[i][0]

        if trainlables[i] == True:
            labels.append(1)
            slopesdiff, interceptdiff = CollectState(index ,lrarray_5, lrarray_10, windowsize)
            input_slopes.append(slopesdiff)
            input_intercept.append(interceptdiff)

        elif trainlables[i] == False:
            labels.append(0)
            slopesdiff, interceptdiff = CollectState(index ,lrarray_5, lrarray_10, windowsize)
            input_slopes.append(slopesdiff)
            input_intercept.append(interceptdiff)
    return input_slopes, input_intercept, labels


def CollectState(index ,lrarray_5, lrarray_10, windowsize):
    slopesdiff = []
    interceptdiff = []
    for i in range (0, windowsize):
        slop_10 = float (lrarray_10[index - windowsize + i + 1][0])
        slop_5 = float(lrarray_5[index - windowsize + i + 1][0])
        slopdeep = (slop_10 - slop_5) * 1000/slop_5
        slopesdiff.append(slopdeep)
        intercept10 =float( lrarray_10[index - windowsize + i + 1][1])
        intercept5 = float(lrarray_5[index - windowsize + i + 1][1])
        intercept =  (intercept10 - intercept5) * 1000/ intercept5
        interceptdiff.append(intercept)
    return slopesdiff, interceptdiff