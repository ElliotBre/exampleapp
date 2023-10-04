def getIncomeTax(taxAmount):
    percentage = 0
    if taxAmount <= 11850:
        taxAmount = 0
        return taxAmount
    else:
        if taxAmount <= 34500:
            percentage = 0.2
        else:
            if taxAmount <=150000:
                percentage = 0.4
            else:
                percentage = 0.45
    taxAmount *= percentage
    return taxAmount
