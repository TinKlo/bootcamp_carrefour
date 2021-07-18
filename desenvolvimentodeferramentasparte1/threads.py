from threading import Thread
import time
def car(speed, pilot):
    track = 0
    while track <= 100:
        track += speed
        print('Pilot: {} Km: {} \n'.format(pilot, track))
        time.sleep(0.5)



t_car1 = Thread(target=car, args=[1, 'Bruno'])
t_car2 = Thread(target=car, args=[5, 'Pyhon'])

t_car1.start()
t_car2.start()