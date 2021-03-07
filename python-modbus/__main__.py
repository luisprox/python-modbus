# -*- coding: utf-8 -*-
u"""Main application.

Test python modbus libraries.

Created on Mar-2021
Author: Luís Prox

"data_format" option is according to python struct library
https://docs.python.org/3/library/struct.html

supported "function code" options
cst.READ_COILS = 1
cst.READ_DISCRETE_INPUTS = 2
cst.READ_HOLDING_REGISTERS = 3
cst.READ_INPUT_REGISTERS = 4
cst.WRITE_SINGLE_COIL = 5
cst.WRITE_SINGLE_REGISTER = 6
cst.READ_EXCEPTION_STATUS = 7
cst.DIAGNOSTIC = 8
cst.REPORT_SLAVE_ID = 17
cst.WRITE_MULTIPLE_COILS = 15
cst.WRITE_MULTIPLE_REGISTERS = 16
cst.READ_WRITE_MULTIPLE_REGISTERS = 23
cst.DEVICE_INFO = 43
"""
from __future__ import print_function

# Set project context
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


# Libraries
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp, hooks
import logging

from timeloop import Timeloop
from datetime import timedelta


# logger
logger = modbus_tk.utils.create_logger("console", level=logging.DEBUG)

# Timeloop for cyclic execution
tl = Timeloop()

# Modbus config
DEVICE_ADDRESS = '127.0.0.1'    # device IP address (modbusTCP)
PORT = 5020                     # device port (default=502)
ID = 16                         # device ID
TIMEOUT = 5.0                   # timeout in sec


# Example hooking a function to run after receiving data from modbus Master
def on_after_recv_master(data):
    master, bytes_data = data
    logger.info(bytes_data)


hooks.install_hook('modbus.Master.after_recv', on_after_recv_master)


# hooking a function to run everytime before a connection
def on_before_connect(args):
    # logging before connect received info as args
    master = args[0]
    logger.debug("on_before_connect {0} {1}".format(
        master._host, master._port))


# hooking the function for before connection
hooks.install_hook(
    "modbus_tcp.TcpMaster.before_connect", on_before_connect)


# Hooking a function to run everytime after receiving data
def on_after_recv(args):
    # Example logging after connect received info as args
    response = args[1]
    logger.debug(
        "on_after_recv {0} bytes received".format(len(response)))


# hooking the function for after receive
hooks.install_hook("modbus_tcp.TcpMaster.after_recv", on_after_recv)


# Connect to the modbus slave
master = modbus_tcp.TcpMaster(
    host=DEVICE_ADDRESS, port=PORT, timeout_in_sec=TIMEOUT)
master.set_timeout(TIMEOUT)     # example changing timeout value
master.set_verbose(True)        # verbose option
logger.info("connected")


# Read values every 3 seconds
@tl.job(interval=timedelta(seconds=3))
def read_analogs():
    logger.info('-------- reading modbus values --------')
    try:
        # read analogs as 16-bits integers
        read_result = master.execute(
            ID,                          # slave address (ID)
            cst.READ_HOLDING_REGISTERS,  # function code
            0,                           # start register address
            4)                           # register count (number of words)
        logger.info(read_result)
        # read analogs as 32-bits integers
        read_result = master.execute(
            ID,                          # slave address (ID)
            cst.READ_HOLDING_REGISTERS,  # function code
            4,                           # start register address
            4,                           # register count (number of words)
            data_format='ii')            # data format (optional) = 2 integers
        logger.info(read_result)
        # read analogs as 32-bits floats
        read_result = master.execute(
            ID,                          # slave address (ID)
            cst.READ_HOLDING_REGISTERS,  # function code
            8,                           # start register address
            4,                           # register count (number of words)
            data_format='ff')            # data format (optional) = 2 floats
        logger.info(read_result)
    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())


# Write values every 3 seconds
@tl.job(interval=timedelta(seconds=3))
def write_analogs():
    logger.info('-------- writing modbus values --------')
    try:
        # write analogs as 16-bits integers
        write_result = master.execute(
            ID,                            # slave address (ID)
            cst.WRITE_MULTIPLE_REGISTERS,  # function code
            0,                             # start register address
            output_value=[10, 20, 30, 40])  # output array
        logger.info(write_result)
        # write analogs as 32-bits integers
        write_result = master.execute(
            ID,                            # slave address (ID)
            cst.WRITE_MULTIPLE_REGISTERS,  # function code
            4,                             # start register address
            output_value=[55555, 66666],   # output array
            data_format='ii')              # data format (optional) = 2 integers
        logger.info(write_result)
        # write analogs as 32-bits floats
        write_result = master.execute(
            ID,                            # slave address (ID)
            cst.WRITE_MULTIPLE_REGISTERS,  # function code
            8,                             # start register address
            output_value=[77.11, 88.22],   # output array
            data_format='ff')              # data format (optional) = 2 floats
        logger.info(write_result)
    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())


if __name__ == "__main__":
    # start timeloop for cyclic execution
    tl.start(block=True)
