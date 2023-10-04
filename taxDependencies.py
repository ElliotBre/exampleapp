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
    match percentage:
        case 0.2:
            taxAmount = (taxAmount - 11850) * percentage
        case 0.4:
            taxAmount = (34500 * 0.2) + ((taxAmount - (34500 + 11850)) * 0.4)
        case 0.45:
            taxAmount = taxAmount - ((345000 * 0.2) + (150000 * 0.4) + ((taxAmount - (11850 + 34500 + 150000)) * 0.45))
            
    return taxAmount
