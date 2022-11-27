def simple_interest(principle,time_period,interest_rate):
    print("principle value is",principle)
    print("Time Period is",time_period)
    print("Interest is",interest_rate)
    
    final_result=principle*time_period*interest_rate/100
    print("Result is ",final_result)
    return final_result

simple_interest(8,10,12)