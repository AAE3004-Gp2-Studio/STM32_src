import matplotlib.pyplot as plt

filePath = "C:\\Users\\qqj48\\Desktop\\y3s1\\AAE3004\\lab\\ws\\src\\simulation_python\\analysis_src\\serial_log.txt"
FREQ = 20

class DataStructure:
    
    def __init__(self, time, X_speed, Y_speed, Z_speed):
        
        self.time = time

        self.X_speed = X_speed
        self.Y_speed = Y_speed
        self.Z_speed = Z_speed


def inverse_bin(binval):
   
  newBin = ''
  for i in range(0, len(binval)):
    if(binval[i] == '0'):
        newBin = newBin + '1'
    elif(binval[i] == '1'):
        newBin = newBin + '0'

  return newBin

def XYZ_Target_Speed_transition(High, Low):

  binHigh = bin(int(High, 16))[2:].zfill(8)
  binLow = bin(int(Low, 16))[2:].zfill(8)
  isNegative = False

  if(binHigh[0] == '1'):
    isNegative = True

  if(isNegative):
    High = int(inverse_bin(binHigh), 2)
    Low = int(inverse_bin(binLow), 2) + 1
  else:
    High = int(High, 16)
    Low = int(Low, 16)
  # if(127 <= High < 255):
  #   High = 255 - High
  #   Low = 255 - Low
  #   print(High)
  # print(~255 + 1)
  # print("test^^^")
  
  print(bin(High) + ' + ' + bin(Low))
  transition=((High<<8) + Low)
  if(isNegative):
    return -(transition / 1000 + (transition % 1000) * 0.001)
  else:
    return transition / 1000 + (transition % 1000) * 0.001



def main():

  fp = open(filePath, 'r')

  rawData = fp.readline()

  dataLines = rawData.split(" 7D 7B ")

  data = []
  time = 0
  del_time = 1 / 20
  for i in range(1, len(dataLines) - 1):
      
    tempData = dataLines[i].split()
    
    X_speed = XYZ_Target_Speed_transition(tempData[1], tempData[2])
    Y_speed = XYZ_Target_Speed_transition(tempData[3], tempData[4])
    Z_speed = XYZ_Target_Speed_transition(tempData[5], tempData[6])
    time = time + del_time

    data.append(DataStructure(time, X_speed, Y_speed, Z_speed))

  x_axis = []
  y_axis = []
  for i in range(0, len(data)):
      
    x_axis.append(data[i].time)
    y_axis.append(data[i].X_speed)

  # scale_coef = 1.25
  plt.xlim((0, 10))
  # plt.ylim((min(y_axis) * scale_coef, max(y_axis) * scale_coef))
  plt.title("Real Response - Kp = 100  Ki = 700  Kd = 0", fontdict={'size'   : 16})
  plt.xlabel('Time', fontsize=14)
  plt.ylabel('Velocity_X', fontsize=14)

  plt.plot(x_axis, y_axis)

  plt.grid()
  plt.show()





if __name__ == "__main__":
  main()