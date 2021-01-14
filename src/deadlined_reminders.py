from abc import ABCMeta, abstractmethod
from collections.abc import Iterable 
from abc import ABC
from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):

    @abstractmethod
    def is_due():
        pass

class DeadlinedReminder(ABC, Iterable):

    @abstractmethod
    def is_due():
        pass

class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text

    def is_due():
        return self.date <= datetime.now()

    def __iter__():
        iter([self.text, self.date.isoformat()])