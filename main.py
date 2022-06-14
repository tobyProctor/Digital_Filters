# Importing Required Libraries
import numpy as np
import matplotlib.pyplot as plt
import sys
import pygame

COLOUR_BACKGROUND = (12, 22, 79)
SCREEN_RES_X = 1400
SCREEN_RES_Y = 900
COLOUR_SUN = (255, 255, 0)
RANGE = 35
FIR_COEF = [1, 1, 1, 1 , 1]
TIME_SIZE = 4096

def apply_fir_filter(signal):
    y = [0, 0, 0, 0, 0]
    filter_signal = []

    for x in range(len(signal)-4):
        y[0] = signal[x]   * FIR_COEF[0]
        y[1] = signal[x+1] * FIR_COEF[1]
        y[2] = signal[x+2] * FIR_COEF[2]
        y[3] = signal[x+3] * FIR_COEF[3]
        y[4] = signal[x+4] * FIR_COEF[4]
        filter_signal.append(np.sum(y))

    return filter_signal

def qpsk_modulation(data, time):
    x = 0
    y = 0
    time = np.arange(TIME_SIZE)*np.pi/2048
    output_signal = [0] * int((TIME_SIZE*len(data)*0.5))

    for i in range(len(data)):
        if(x >= len(data)):
            break

        data_width = y*TIME_SIZE

        if "{}{}".format(data[x], data[x+1]) == "00":
            output_signal[data_width:data_width+TIME_SIZE] = np.sin(time-0)
        elif "{}{}".format(data[x], data[x+1]) == "01":
            output_signal[data_width:data_width+TIME_SIZE] = np.sin(time-np.pi/2)
        elif "{}{}".format(data[x], data[x+1]) == "10":
            output_signal[data_width:data_width+TIME_SIZE] = np.sin(time-np.pi)
        elif "{}{}".format(data[x], data[x+1]) == "11":
            output_signal[data_width:data_width+TIME_SIZE] = np.sin(time-np.pi*1.5)
        else:
            print("Error - Invalid data")

        x+=2
        y+=1
        
    return output_signal

def main():
    data = "0011001100100111000110"
    signal_length = TIME_SIZE * int(len(data)*0.5)
    time = np.arange(signal_length)*np.pi/2048

    transmitted_signal = qpsk_modulation(data, time)
    fft = abs(np.fft.fft(transmitted_signal))

    transmitted_signal_noise = transmitted_signal + np.sin(200*time)*0.3 + np.sin(100*time)*0.3 + np.sin(130*time)*0.4
    fft_noise = abs(np.fft.fft(transmitted_signal_noise))

    filter_signal = apply_fir_filter(transmitted_signal_noise)
    filter_fft = abs(np.fft.fft(filter_signal))

    fig = plt.figure(figsize=(10, 9))
    axes = fig.subplots(nrows=4, ncols=2)

    axes[0][0].title.set_text('Input signal')
    axes[0][0].plot(transmitted_signal)

    axes[0][1].title.set_text('Input signal PD')
    axes[0][1].plot(fft)

    axes[1][0].title.set_text('Input signal with noise')
    axes[1][0].plot(transmitted_signal_noise)

    axes[1][1].title.set_text('Input signal with noise PD')
    axes[1][1].plot(fft_noise)

    axes[2][0].title.set_text('FIR filtered input signal')
    axes[2][0].plot(filter_signal)

    axes[2][1].title.set_text('FIR filtered input PD')
    axes[2][1].plot(filter_fft)

    plt.show()

if __name__ == "__main__":
     main()