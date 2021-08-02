how_old="How old are you?\n"
response_to_how_old=""
decade=0

response_to_how_old=int(input(how_old))
years=response_to_how_old%10
decade=response_to_how_old//10
print("You are "+ str(decade) +" decades and "+ str(years) +" year(s) old.")