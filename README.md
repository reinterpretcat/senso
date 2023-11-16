# SENSO

A very lightweight sensor monitoring system for Raspberry Pi clusters running Kubernetes. So far support is added only for BME280 Barometric sensor.

![image](https://github.com/reinterpretcat/senso/assets/1611077/432125fc-d96b-4fcc-8019-78632d228daf)

# Description

This project is based on [OMNI](https://github.com/mattogodoy/omni), so many things from its README would fit here as well.


# Install

0. Enable `I2C` interface on your device (using `raspi-config`)
1. Get `InfluxDB` installed (e.g. from  helm)
2. Set values for the corresponding environment variables in `senso-install.yaml`
3. Run 
        
        kubectl apply -f senso-install.yaml

4.  Check with

        kubectl get all -n senso-system


# Motivation

I built it to get time series data from BME280 Barometric sensor saved in InfluxDB. I need it mostly to see whether there is dependency between changes in air pressure and my headache.
