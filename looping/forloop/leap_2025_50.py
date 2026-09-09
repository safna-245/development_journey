for year in range(2025,2051):

    if(year %100 == 0 and year %400 == 0) or (year %100 != 0 and year %4 == 0)  :
        
        print(year)

    