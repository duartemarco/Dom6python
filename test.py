import math

baseFat = int(input("Spell base fatigue:"))
spellLvl = int(input("Spell level:"))
casterLvl = int(input("Caster level:"))
slaveNbr = int(input("Amount of slaves:")) # ask user if communion. if yes, ask for amount of slaves
slaveLvl = int(input("Slave level:")) # only if amount of slaves is more than 0
casterEnc = int(input("Caster encumberance:"))
magScale = int(input("Province magic scale:"))

comBoost = 0 if slaveNbr == 0 else math.floor(math.log2(slaveNbr))
casterTotal = comBoost + casterLvl if slaveNbr > 0 else casterLvl

slaveMult = 0
if slaveLvl < casterLvl / 2:
    slaveMult = 4
elif slaveLvl < casterLvl:
    slaveMult = 2
elif slaveLvl == casterLvl:
    slaveMult = 1
elif slaveLvl > casterLvl:
    slaveMult = 0.5

casterFat = (baseFat * (1 - (magScale * 0.1)) * (1 / (casterTotal + 1 - spellLvl)) + casterEnc) / (slaveNbr + 1)
slaveFat = 0 if slaveNbr <= 0 else casterFat * slaveMult

print(f"Caster Fatigue: {casterFat}")
print(f"Slave Fatigue: {slaveFat}")