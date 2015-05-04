class Date(object):

	day = 0
	month = 0
	year = 0

	def __init__(self, day=0, month=0, year=0):
		self.day = day
		self.month = month
		self.year = year

	@classmethod
	def fromString(cls, date_as_string):
		day, month, year = map(int, date_as_string.split('-'))
		return cls(day, month, year)

	@staticmethod
	def isDateValid(date_as_string):
		day, month, year = map(int, date_as_string.split('-'))
		return 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 3999

print Date.fromString('09-11-2014')
print Date.isDateValid('09-11-2014')
print Date.isDateValid('09-14-2014')
print Date.isDateValid('00-14-2014')

import abc

class Pizza(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def getOut(self):
		''' returns ingredient list '''

print dir(Pizza)
Pizza()