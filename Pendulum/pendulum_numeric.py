#! /usr/bin/python3

'''
Pendulum simulator using scientific python.

Based on example code from ODE tutorial.
'''

from argparse import ArgumentParser, Namespace
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def main(l: np.float64, theta: np.float64, theta_dot: np.float64 = np.float64(0.),
         g: np.float64 = np.float64(9.8067)) -> None:
    '''
    2D idealized pendulum simulation

    l = pendulum length in meters
    theta = initial angle in degrees from down
    theta_dot = initial angular speed in degrees per second; default is 0 degrees per second
    g = acceleration due to gravity in m/**s; default is Earth
    '''
    pass


def f(X, t) -> None:
    '''The derivative function'''
    return

# numerical solution at small angles (sin(theta) aprox equal theta)


def Euler(func, x0, t) -> np.ndarray:
    '''Euler integrator'''
    dt = t[1] - t[0]
    nt: int = len(t)
    x: np.ndarray = np.zeros([nt, len(x0)])
    x[0] = x0
    for i in range(nt-1):
        x[i+1] = x[i] + func(x[i], t[i]) * dt
    return x


def RK4(func, x0, t) -> np.ndarray:
    '''Runge and Kutta 4 integrator'''
    dt = t[1] - t[0]
    nt: int = len(t)
    x = np.zeros([nt, len(x0)])
    x[0] = x0
    for i in range(nt-1):
        k1 = func(x[i], t[i])
        k2 = func(x[i] + dt/2. * k1, t[i] + dt/2.)
        k3 = func(x[i] + dt/2. * k2, t[i] + dt/2.)
        k4 = func(x[i] + dt * k3, t[i] + dt)
        x[i+1] = x[i] + dt / 6. * (k1 + 2. * k2 + 2. * k3 + k4)
    return x

# ODEint is preloaded


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('length', metavar='l',
                        help='pendulum length from pivot to center of mass, in meters')
    parser.add_argument('angle', metavar='θ',
                        help='starting angle, in degrees from down')
    parser.add_argument('--angular_speed', metavar='\u03b8\u0307',
                        help='starting angular speed, in degrees per second')
    parser.add_argument('-g',
                        help='acceleration due to gravity, in meters per second per second')
    args: Namespace = parser.parse_args()
    # currently ignoring angular speed and acceleration due to gravity
    main(np.float64(args.length), np.float64(args.angle))
