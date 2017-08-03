# -*- coding: utf-8 -*-

import subprocess
import threading
import time


class TCPDump:
    def __init__(self, tcpdump_call, interface, traffic_filter="", print_traffic=False):
        self.__tcpdump_call = tcpdump_call
        self.__interface = interface
        self.__traffic_filter = traffic_filter
        self.__print_traffic = print_traffic
        self.__p = None
        self.__thr = None
        self.__is_running = False
        self.__lock = threading.Lock()
        self.__last_packet_timestamp = time.time()
        self.__status_checker = None

    def init_tcpdump(self):
        self.__p = subprocess.Popen([self.__tcpdump_call, "-l", "-i", self.__interface, "-n", self.__traffic_filter],
                                    stdout=subprocess.PIPE)

    def get_status_checker(self, offline_threshold=60):
        if self.__status_checker is None:
            self.__status_checker = self.StatusChecker(self, offline_threshold)
        else:
            if self.__status_checker.offline_threshold != offline_threshold:
                self.__status_checker.offline_threshold = offline_threshold
        return self.__status_checker

    def get_last_packet_timestamp(self):
        self.__lock.acquire()
        timestamp = self.__last_packet_timestamp
        self.__lock.release()
        return timestamp

    def set_last_packet_timestamp(self, timestamp):
        self.__lock.acquire()
        self.__last_packet_timestamp = timestamp
        self.__lock.release()

    def isAlive(self):
        return self.__thr.isAlive()

    def read_traffic(self):
        while self.__p.poll() is None and self.__is_running:
            if self.__print_traffic:
                print(self.__p.stdout.readline().rstrip())
            else:
                self.__p.stdout.readline()
            timestamp = time.time()
            self.__last_packet_timestamp = timestamp

    def run(self):
        self.init_tcpdump()
        if self.__p is not None:
            self.__is_running = True
            self.__thr = threading.Thread(target=self.read_traffic, args=())
            self.__thr.start()
        else:
            print("Error occurred during tcpdump initialization!")

    def stop(self):
        self.__p.terminate()
        self.__is_running = False

    # def is_Online(self, offline_threshold=60):
    #     if time.time() - self.__tcpdump.get_last_packet_timestamp() > offline_threshold:
    #         return True

    class StatusChecker:
        def __init__(self, tcpdump_class, offline_threshold=60):
            self.__tcpdump = tcpdump_class
            self.offline_threshold = offline_threshold

        def is_Online(self):
            if time.time() - self.__tcpdump.get_last_packet_timestamp() < self.offline_threshold:
                return True
            else:
                return False
