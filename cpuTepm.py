    from time import sleep

    from gpiozero import CPUTemperature
    cpu = CPUTemperature()

    while True:
      temp = cpu.temperature
      print(temp)
      sleep(1)
