import numpy as np

def Encoder(data):
    data = np.append(data, [0, 0, 0, 0]) #Shift Register 설정 및 초기화
    dataSize = np.shape(data)[0] #(64,)
    shiftReg = [0, 0, 0, 0] # k=4
    encoded_bit = np.zeros((2, dataSize)) # R=1/2 1비트 들어오면 2비트 출력 2행

    for i in range(dataSize):
        shiftReg[3] = shiftReg[2]
        shiftReg[2] = shiftReg[1]
        shiftReg[1] = shiftReg[0]
        shiftReg[0] = data[i]
        encoded_bit[0, i] = np.logical_xor(np.logical_xor(shiftReg[0], shiftReg[1]), np.logical_xor(shiftReg[2], shiftReg[3]))
        encoded_bit[1, i] = np.logical_xor(np.logical_xor(shiftReg[2], shiftReg[3]),shiftReg[0])

    return encoded_bit

def ViterbiDecoder(encoded_bit):

    ref_out = np.zeros((2,16))
    ref_out[0, :] = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1]
    ref_out[1, :] = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]

    dataSize = np.shape(encoded_bit)[1] #2 by 원래데이터길이+3[0,0,0]
    cumDist = [0, 100, 100, 100, 100, 100, 100, 100] #초기값 설정
    prevState=[]
    for i in range(dataSize):
        tmpData = np.tile(encoded_bit[:, i].reshape(2,1), (1,16))
        dist = np.sum(np.abs(tmpData - ref_out), axis=0)
        tmpDist = np.tile(cumDist, (1, 2)) + dist
        tmpPrevState=[]
        for a in range(4):
            if tmpDist[0, 2 * a + 0] <= tmpDist[0, 2 * a + 1]:
                cumDist[a] = tmpDist[0, 2 * a + 0]
                tmpPrevState.append((a % 2) * 2 + 0)
            else:
                cumDist[a] = tmpDist[0, 2 * a +1]
                tmpPrevState.append((a % 2) * 2 + 1)
            prevState.append(tmpPrevState)
            state_index = np.argmin(cumDist)
            decoded_bit=[]
    for b in range(dataSize - 1, -1, -1):
        decoded_bit.append(int(state_index / 2))
        state_index = prevState[b][state_index]
    data_size = np.shape(decoded_bit)[0]
    decoded_bit = np.flip(decoded_bit)[0:data_size - 4]
    return decoded_bit
    


