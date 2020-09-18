f = open("complete","r")
dict = {}

for lines in f:
    data= lines.strip("\n").split(",")
    state = data[1]
    confirmed = data[4]
    death = data[5]
    recovered = data[6]

    if (state not in dict):
        dict[state] = {"confirmed": confirmed, "recovered": recovered, "death": death}
    else:
        dict[state] = {"confirmed": confirmed, "recovered": recovered, "death": death}

def Fetchdata(**kwargs):
    if(kwargs["state"] not in dict):
        print("No result found")
    else:
        for k,v in dict.items():
            if(k==kwargs["state"]):
                print("Total confirmed cases : ",v["confirmed"])
                if("param" in kwargs):
                    temp=kwargs["param"]
                    if(temp=="recovered"):
                        print("Recoverd :",v["recovered"])
                    elif(temp=="death"):
                        print("Death :",v["death"])
                else:
                    print("no data")

Fetchdata(state="Kerala",param="recovered")


