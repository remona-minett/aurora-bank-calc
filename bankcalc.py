from os import system

# Menu logic
system('cls')
print(f"Aurora Bank Calculator")
loop = True
while loop: # Species
    species = int(input("Select Species:\n1> Human\n2> Skrell\n3> Unathi\n4> Tajara\n5> Diona\n6> IPC\n7> Vaurca\n")) # ta vaurca = 8
    if 0 < species < 8:
        loop = False
    else:
        print(f"{species} is out of range, try again.") 
    if species == 7: # vaurca have different pay based on subspecies
        loop = True
        while loop:
            speciesvaurca = int(input(f"\nSpecies Subtype Selection:\n1> Non-Ta Vaurca\n2> Ta Vaurca\n"))
            if speciesvaurca == 1:
                loop = False
                species = 7
            elif speciesvaurca == 2:
                loop = False
                species = 8
    if species == 1:
        speciestext = "human"
    elif species == 2:
        speciestext = "skrell"
    elif species == 3:
        speciestext = "unathi"
    elif species == 4:
        speciestext = "tajara"
    elif species == 5:
        speciestext = "diona"
    elif species == 6:
        speciestext = "ipc"
    elif species == 7:
        speciestext = "vaurca"
    elif species == 8:
        speciestext = "ta vaurca"

system('cls')
loop = True
while loop: # Job
    job = int(input("Select Job Department:\n1> Command\n2> Civilian\n3> Engineering\n4> Medical\n5> Science\n6> Security\n7> Silicon\n8> Outsider\n\nThis is the department you work in - the specific job comes afterwards.\n"))
    if 0 < job < 9:
        while loop: # sub jobs
            if job == 1:
                jobposition = int(input("\n1> Captain\n2> Research Director\n3> Exec Officer\n4> Ops Manager\n5> C. Engineer\n6> C. Medical Officer\n7> Head of Security\n8> HRA\n9> Bridge Crew\n"))
                if 0 < jobposition < 10:
                    loop = False
            elif job == 2:
                jobposition = int(input("\n1> Bartender\n2> Chef\n3> Gardener\n4> Janitor\n5> Reporter\n6> Librarian\n7> Chaplain\n8> Hangar Technician\n9> Shaft Miner\n10> Machinist\n11> Assistant\n12> Off Duty\n13> Passenger\n"))
                if 0 < jobposition < 14:
                    loop = False
            elif job == 3:
                jobposition = int(input("\n1> Engineer\n2> Atmos Technician\n3> Apprentice\n"))
                if 0 < jobposition < 4:
                    loop = False
            elif job == 4:
                jobposition = int(input("\n1> Physician\n2> Surgeon\n3> Pharmacist\n4> Psychiatrist\n5> Psychologist\n6> First Responder\n7> Intern\n"))
                if 0 < jobposition < 8:
                    loop = False
            elif job == 5:
                jobposition = int(input("\n1> Scientist\n2> Archaeologist\n3> Biologist\n4> Botanist\n5> Lab Assistant\n"))
                if 0 < jobposition < 6:
                    loop = False
            elif job == 6:
                jobposition = int(input("\n1> Warden\n2> Investigator\n3> Officer\n4> Cadet\n"))
                if 0 < jobposition < 5:
                    loop = False
            elif job == 7:
                jobposition = int(input("\n1> AI\n2> Cyborg\n"))
                if 0 < jobposition < 3:
                    loop = False
            elif job == 8:
                jobposition = int(input("\n1> Corp. Liaison\n2> Consular Officer\n"))
                if 0 < jobposition < 3:
                    loop = False
    else:
        print(f"{job} is out of range, try again.")

system('cls')
loop = True
while loop: # Wealth
    wealth = int(input("Select Wealth:\n1> Wealthy\n2> Well-Off\n3> Average\n4> Underpaid\n5> Poor\n6> Impoverished\n\nThis is a measure of how much more or less you make than the average pay for the job. \"Average\" is the default.\n"))
    if 0 < wealth < 7:
        loop = False
        if wealth == 1:
            wealthtext = "a wealthy"
        elif wealth == 2:
            wealthtext = "a well-off"
        elif wealth == 3:
            wealthtext = "an average"
        elif wealth == 4:
            wealthtext = "a underpaid"
        elif wealth == 5:
            wealthtext = "a poor"
        elif wealth == 6:
            wealthtext = "an impoverished"
    else:
        print(f"{wealth} is out of range, try again.")

# Number logic - it's made this way to be easy to edit in the future.

if species == 1: # human
    speciespay = 12
elif species == 2: # skrell
    speciespay = 12
elif species == 3: # unathi
    speciespay = 7
elif species == 4: # cat
    speciespay = 7
elif species == 5: # diona
    speciespay = 3
elif species == 6: # ipc
    speciespay = 3
elif species == 7: # non ta vaurca
    speciespay = 2
elif species == 8: # ta vaurca
    speciespay = 3

if wealth == 1: # wealthy
    wealthpay = 1.3
elif wealth == 2: # well off
    wealthpay = 1.15
elif wealth == 3: # average
    wealthpay = 1
elif wealth == 4: # underpaid
    wealthpay = 0.75
elif wealth == 5: # poor
    wealthpay = 0.5
elif wealth == 6: # destitute/impoverished
    wealthpay = 0.25

if job == 1:
    if jobposition == 1: # captain
        jobtext = "captain"
        jobposition = 1
        pay = 20
    elif jobposition == 2: # rd
        jobtext = "research director"
        jobposition = 2
        pay = 15
    elif jobposition == 3: # exec officer
        jobtext = "executive officer"
        jobposition = 3
        pay = 10
    elif jobposition == 4: # ops manager
        jobtext = "operations manager"
        jobposition = 4
        pay = 10
    elif jobposition == 5: # ce
        jobtext = "chief engineer"
        jobposition = 5
        pay = 10
    elif jobposition == 6: # cmo
        jobtext = "chief medical officer"
        jobposition = 6
        pay = 10
    elif jobposition == 7: # hos
        jobtext = "head of security"
        jobposition = 7
        pay = 10
    elif jobposition == 8: # hra
        jobtext = "human resource assistant"
        jobposition = 8
        pay = 10
    elif jobposition == 9: # bridge crew
        jobtext = "bridge crew"
        jobposition = 9
        pay = 5
elif job == 2:
    if jobposition == 1: # bartender
        jobtext = "bartender"
        jobposition = 10
        pay = 2
    elif jobposition == 2: # chef
        jobtext = "chef"
        jobposition = 11
        pay = 2
    elif jobposition == 3: # gardener
        jobtext = "gardener"
        jobposition = 12
        pay = 2
    elif jobposition == 4: # janitor
        jobtext = "janitor"
        jobposition = 13
        pay = 2
    elif jobposition == 5: # reporter
        jobtext = "reporter"
        jobposition = 14
        pay = 2
    elif jobposition == 6: # librarian
        jobtext = "librarian"
        jobposition = 15
        pay = 2
    elif jobposition == 7: # chaplain
        jobtext = "chaplain"
        jobposition = 16
        pay = 2
    elif jobposition == 8: # hangar tech
        jobtext = "hangar tech"
        jobposition = 17
        pay = 2
    elif jobposition == 9: # shaft miner
        jobtext = "shaft miner"
        jobposition = 18
        pay = 5
    elif jobposition == 10: # machinist
        jobtext = "machinist"
        jobposition = 19
        pay = 5
    elif jobposition == 11: # assistant
        jobtext = "grayshirt"
        jobposition = 20
        pay = 1
    elif jobposition == 12: # off duty
        jobtext = "off duty crewmate"
        jobposition = 21
        pay = 1
    elif jobposition == 13: # passenger
        jobtext = "passenger"
        jobposition = 22
        pay = 1
elif job == 3:
    if jobposition == 1: # engineer
        jobtext = "engineer"
        jobposition = 23
        pay = 5
    elif jobposition == 2: # atmos technician
        jobtext = "atmos technician"
        jobposition = 24
        pay = 5
    elif jobposition == 3: # apprentice
        jobtext = "engineering apprentice"
        jobposition = 25
        pay = 2
elif job == 4:
    if jobposition == 1: # physician
        jobtext = "physician"
        jobposition = 26
        pay = 7
    elif jobposition == 2: # surgeon
        jobtext = "surgeon"
        jobposition = 27
        pay = 7
    elif jobposition == 3: # pharmacist
        jobtext = "pharmacist"
        jobposition = 28
        pay = 5
    elif jobposition == 4: # psychiatrist
        jobtext = "psychiatrist"
        jobposition = 29
        pay = 5
    elif jobposition == 5: # psychologist
        jobtext = "psychologist"
        jobposition = 30
        pay = 4
    elif jobposition == 6: # first responder
        jobtext = "first responder"
        jobposition = 31
        pay = 4
    elif jobposition == 7: # intern
        jobtext = "medical intern"
        jobposition = 32
        pay = 2
elif job == 5:
    if jobposition == 1: # scientist
        jobtext = "scientist"
        jobposition = 33
        pay = 7
    elif jobposition == 2: # archaeologist
        jobtext = "archaeologist"
        jobposition = 34
        pay = 7
    elif jobposition == 3: # biologist
        jobtext = "biologist"
        jobposition = 35
        pay = 7
    elif jobposition == 4: # botanist
        jobtext = "xenobotanist"
        jobposition = 36
        pay = 7
    elif jobposition == 5: # lab ass
        jobtext = "lab ass"
        jobposition = 37
        pay = 2
elif job == 6:
    if jobposition == 1: # warden
        jobtext = "warden"
        jobposition = 38
        pay = 5
    elif jobposition == 2: # investigator
        jobtext = "detective"
        jobposition = 39
        pay = 5
    elif jobposition == 3: # officer
        jobtext = "officer"
        jobposition = 40
        pay = 4
    elif jobposition == 4: # cadet
        jobtext = "cadet"
        jobposition = 41
        pay = 2
elif job == 7:
    if jobposition == 1: # ai
        jobtext = "ai"
        jobposition = 42
        pay = 0
    elif jobposition == 2: # cyborg
        jobtext = "cyborg"
        jobposition = 43
        pay = 0
elif job == 8:
    if jobposition == 1: # corp liaison
        jobtext = "corporate liaison"
        jobposition = 44
        pay = 15
    elif jobposition == 2: # consular
        jobtext = "consular officer"
        jobposition = 45
        pay = 15

# calculation logic
minpay = ((((5+5)*wealthpay)*pay)*speciespay)
maxpay = ((((50+50)*wealthpay)*pay)*speciespay)
avgpay = ((((27.5+27.5)*wealthpay)*pay)*speciespay)
# write final result
system('cls')
print(f"As {wealthtext} {jobtext} {speciestext}, your pay can be the following:\n") # wealthtext includes a[n]
print(f"Maximum: {maxpay}cr\nAverage: {avgpay}cr\nMinimum: {minpay}cr\n\n")
input("v1.2-py built 07/26/2023 - Press the enter key to exit.")

# TODO - jobposition is depreciated and can be removed in later versions.

# 1.2 - added outsider jobs. fixed a code escape with vaurca selection.
# 1.1 - fixed issue with pay being totally wrong lol. Oops.