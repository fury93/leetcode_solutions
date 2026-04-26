class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = map(int, date.split('-'))
        return f'{year:b}-{month:b}-{day:b}'
        
        # return "-".join(f"{int(d):b}" for d in date.split("-"))
        
        # return  '-'.join([bin(int(num))[2:] for num in date.split('-')])