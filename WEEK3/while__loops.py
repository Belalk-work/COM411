#task 3
print("how many bars should be charged?")
number_bars_to_charge=int(input())
charged_bar=0
print()
while charged_bar<number_bars_to_charge:
    charged_bar=charged_bar+1
    print(f"charging:{" ▌" *charged_bar}")




