# @Date    : 22:32 07/11/2020
# @Author  : ClassicalPi
# @FileName: 5177.py
# @Software: PyCharm

# Given a date string in the form Day Month Year, where:
#
# Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
# Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
# Year is in the range [1900, 2100].
# Convert the date string to the format YYYY-MM-DD, where:
#
# YYYY denotes the 4 digit year.
# MM denotes the 2 digit month.
# DD denotes the 2 digit day
#

class Solution:
    def reformatDate(self, date: str) -> str:
        raw_day,month,year=date.split(" ")
        day=""
        for each in raw_day:
            if each.isnumeric():
                day+=each
        if len(day)==1:
            day="0"+day
        dict_month={"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05",
                    "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        return f"{year}-{dict_month[month]}-{day}"

if __name__ == '__main__':
    S=Solution()
    print(S.reformatDate("20th Oct 2052"))
    print(S.reformatDate("6st Jun 1933"))
    print(S.reformatDate("26nd May 1960"))

