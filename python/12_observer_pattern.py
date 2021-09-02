"""
Observer Design Pattern:
------------------------
The observer pattern is a software design pattern in which an object, named the subject,
maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.


Realtime Analogy:
-----------------

Each YouTuber has many subscribers on their channel. Each subscriber wants to watch their subscribed channel's videos.
So till a subscriber has an interest in a specific YouTuber’s channel, they subscribe to it. 
When they lose interest, they unsubscribe the channel. Here, we can think of subscribers as an observer and the YouTuber as the subject.
So, if we start creating domains we should create a class that adds, deletes, or notifies all observers.

"""

from abc import ABC, abstractmethod
from typing import List

class IObserver(ABC):
    @abstractmethod
    def update(self, youtuber_name: str, video_name: str):
        pass

class ISubject:

    @abstractmethod
    def subscribe(self, observer: IObserver):
        pass
    @abstractmethod
    def un_subscribe(self, observer: IObserver):
        pass
    @abstractmethod
    def notify_observers(self, video_name: str):
        pass
    @abstractmethod
    def upload_video(self, video_name):
        pass

class Youtuber(ISubject):

    def __init__(self, youtuber_name: str) -> None:
        self.youtuber_name = youtuber_name
        self.subscribers: List[IObserver] = []
    
    def subscribe(self, observer: IObserver):
        self.subscribers.append(observer)

    def un_subscribe(self, observer: IObserver):
        self.subscribers.remove(observer)

    def upload_video(self, video_name):
        print(f"{self.youtuber_name} uploaded video named: {video_name}")
        self.notify_observers(video_name)
    
    def notify_observers(self, video_name: str):
        if self.subscribers:
            for subscriber in self.subscribers:
                subscriber.update(self.youtuber_name, video_name)

class Subscriber(IObserver):
    def __init__(self, subscriber_name) -> None:
        self.subscriber_name = subscriber_name
    
    def update(self, youtuber_name: str, video_name: str):
        print(f"Hey {self.subscriber_name}! {youtuber_name} has posted a new video named: {video_name}, check it out if you intrested.")

if __name__ == "__main__":
    tech_burner_youtuber: Youtuber = Youtuber("TechBurner Channel")
    t_series_youtuber: Youtuber = Youtuber("TSeries Channel")

    # Subscribers
    max: IObserver = Subscriber('Max')
    jack: IObserver = Subscriber('Jack')

    # subscribing to channels
    tech_burner_youtuber.subscribe(max)
    tech_burner_youtuber.subscribe(jack)

    t_series_youtuber.subscribe(max)
    t_series_youtuber.subscribe(jack)

    # Uploading viedos
    tech_burner_youtuber.upload_video("Design patterns")
    tech_burner_youtuber.upload_video("Basic Programming")

    t_series_youtuber.upload_video("New Bollywood movies")
    t_series_youtuber.upload_video("New Tollyhood movies")




