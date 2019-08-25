import threading

class ExampleThread(threading.Thread):
    def run(self):
        for _ in range(5):
            print(threading.currentThread().getName())

x = ExampleThread(name = 'First thread')
y = ExampleThread(name = 'Second thread')

x.start()
y.start()