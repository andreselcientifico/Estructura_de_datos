from random import randint
from node_based_queue import Queue
from time import sleep

class Track:
    def __init__(self, title = None):
        self.title = title
        self.length = randint(5,6)

class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        print(f"Count: {self.count}")


        while self.count > 0 and self.head is not None:
            current_track_node = self.dequeue()
            print(f"Now playing {current_track_node.title}")

            sleep(current_track_node.length)



if __name__ == '__main__':
    track1 = Track("Highway to hell")
    track2 = Track("Go")
    track3 = Track("Light years")
    track4 = Track("Heartbreaker")
    track5 = Track("Breath me")
    track6 = Track("How to dissappear completely")
    Media_player = MediaPlayerQueue()
    Media_player.add_track(track1)
    Media_player.add_track(track2)
    Media_player.add_track(track3)
    Media_player.add_track(track4)
    Media_player.add_track(track5)
    Media_player.add_track(track6)
    Media_player.play()