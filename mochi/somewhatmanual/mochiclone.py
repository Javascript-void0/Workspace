from selenium import webdriver

links = ['https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/uC0GMkAV/New-SAT-Unit-01', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/mCdDqETa/New-SAT-Unit-02', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/SQGGLbwJ/New-SAT-Unit-03', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/MkZ5WWUR/New-SAT-Unit-04', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/oKAy8MGC/New-SAT-Unit-05', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/puVF5Cdn/New-SAT-Unit-06', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/ifBB2HZS/New-SAT-Unit-07', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/xE0graE4/New-SAT-Unit-08', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/OwXEuJwe/New-SAT-Unit-09', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/OM474ony/New-SAT-Unit-10', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/fAvhzzMe/New-SAT-Unit-11', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/di8IDs3V/New-SAT-Unit-12', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/eXUdX8ON/New-SAT-Unit-13', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/5z1bv1dN/New-SAT-Unit-14', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/N96yfMMt/New-SAT-Unit-15', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/HtOuky5b/New-SAT-Unit-16', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/673xEcXE/New-SAT-Unit-17', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/UrnE3kdH/New-SAT-Unit-18', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/HdaReAM9/New-SAT-Unit-19', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/105yWOCT/New-SAT-Unit-20', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/96lr2R08/New-SAT-Unit-21', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/CMd1HEwa/New-SAT-Unit-22', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/saFI2GbP/New-SAT-Unit-23', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/pT8C2nfa/New-SAT-Unit-24', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/s36ZodmO/New-SAT-Unit-25', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/M1qHxVFI/New-SAT-Unit-26', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/S8Bce1Ma/New-SAT-Unit-27', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/zoLoe2TS/New-SAT-Unit-28', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/2fLGZ3iF/New-SAT-Unit-29', 'https://app.mochi.cards/decks/702d8087-e247-41d0-bb47-d8d7531c46f6/tXi3Knfr/New-SAT-Unit-30']

for i in range(len(links)):
    driver = webdriver.Chrome()
    driver.get(links[i])

# venv no work