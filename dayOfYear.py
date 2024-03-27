class Solution:
    def dayOfYear(self, date: str) -> int:
        # Function to check if a given year is a leap year
        def isLeap(year):
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            elif year % 4 == 0:
                return True
            return False

        # List of days in each month for non-leap and leap years
        if isLeap(int(date[:4])):
            days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # If the month is January, return the day directly
        if date[5:7] == '01':
            return int(date[-2:])
        
        # Calculate the day of the year by summing up days in preceding months and adding the day
        return sum(days_in_month[0:int(date[5:7]) - 1]) + int(date[-2:])
    
obj = Solution()

print(obj.dayOfYear("2002-05-29"))