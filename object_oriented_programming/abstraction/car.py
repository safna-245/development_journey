from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):

        pass

    @abstractmethod
    def accelerate(self):

        pass

    @abstractmethod
    def stop(self):

        pass

class Baleno(Car):

    def start(self):

        print("Baleno start method..")

    def accelerate(self):

        print("Baleno car accelerate...")

    def stop(self):

        print("Baleno car stop...")

baleno_instance = Baleno()

baleno_instance.start()

baleno_instance.accelerate()

baleno_instance.stop()