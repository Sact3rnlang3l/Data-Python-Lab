

CupcakeInvoices = open("CupcakeInvoices.csv")
product = 1
totals = []
ChocoTotal = []
VanTotal = []
StrawTotal = []
# for cake_of_cup_proportions in CupcakeInvoices:
#     # print(cake_of_cup_proportions)
#     i = cake_of_cup_proportions.rstrip("\n").split(',')
    
#     price = float(i[4])
#     amount = float(i[3])
#     print("This cake of cup proportions is", i[2], "Flavored")
#     print("Your total for this order is $", price*amount)
#     totals = totals + [price]

# # print(sum(totals))

for j in CupcakeInvoices:
    j = j.rstrip("\n").split(',')
    price = float(j[4])
    amount = float(j[3])
    total = price*amount

    if j[2] == "Chocolate":
        ChocoTotal = ChocoTotal + [total]
    elif j[2] == "Vanilla":
        VanTotal = VanTotal + [total]
    elif j[2] == "Strawberry":
        StrawTotal = StrawTotal + [total]

print("Chocoloate made", sum(ChocoTotal))
print("Vanilla made", sum(VanTotal))
print("Strawberry made", sum(StrawTotal))

CupcakeInvoices.close()

