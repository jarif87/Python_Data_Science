# =============================================================================
# Let us discuss the formula for compound interest. The formula to calculate compound interest annually is given by: 
# 
# A = P(1 + R/100) t 
# 
# Compound Interest = A – P 
# 
# Where, 
# A is amount 
# P is the principal amount 
# R is the rate and 
# T is the time span
# =============================================================================

def compound_interest(principle,time_period,interest_rate):
    print("Principle is",principle)
    print("Time period is",time_period)
    print("interest rate is ",interest_rate)
    result=principle*(pow((1+interest_rate/100),time_period))
    final_result=result-principle
    print("Compound Interest is",final_result)

compound_interest(10,20,30)









































