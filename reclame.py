from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."
print(aanbieding_1("aardbei", 4, 0.1))
def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag_btw = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag_btw} euro btw betaald dient te worden."
week_inkomsten = [220, 430, 125, 600, 350]
print(inkomsten_totaal(week_inkomsten, 0.09))
def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]
week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(laag_en_hoog(week_inkomsten))
def gemiddelde(inkomsten):
    totaal = sum(inkomsten)
    aantal = len(inkomsten)
    gemiddelde_bedrag = totaal / aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_bedrag} euro."
week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(week_inkomsten))
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
voorbeeld = [10, 5, 3, 2, 1, 2, 9]
print(meervoudig(voorbeeld))
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print(combinatie(voorbeeld))