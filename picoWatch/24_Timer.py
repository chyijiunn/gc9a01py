from machine import Timer
tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:print('ok'))
