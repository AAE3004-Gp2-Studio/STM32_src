import matplotlib as plt

calculate_time_ms = 200

oscillator = 1 / (8 * 10**6)
sys_clock = oscillator * 12

Velocity_KP = 700
Velocity_KI = 700
Velocity_KD = 700

Bias = 0
Last_bia = 0
Pre_Last_bia = 0

Pwm = 0


def Incremental_PID(realval, target):

    Bias = target - realval
    Pwm = Pwm + Velocity_KP * (Bias - Last_bia) + Velocity_KI * Bias + Velocity_KD * (Bias - 2 * Last_bia + Pre_Last_bia)
    Prev_Last_bia = Last_bia
    Last_bia = Bias; 


def realval_simulation():
    realval = 0
    return realval



def main():

    target = 20

    calculate_num = int(calculate_time_ms / sys_clock)

    print(calculate_num)

    for i in range(0, calculate_num):
        realval = realval_simulation()
        Incremental_PID(realval, target)




if __name__ == "__main__":
    main()


