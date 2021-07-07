
import sys

#x = "Full normalization mode set [Time: 6/25/2021 5:41:33 PM, Resources: [Energy: 24.9111111111112], [Silver: 263430.073149072], [Token: 3.22583333333334], [Gem: 42], [Arena3X3ShopCurrency:       1278], [Arena3x3Token: 5], [Orb_MagicLow: 20], [Orb_MagicMid: 9], [Orb_MagicHigh: 4], [Orb_ForceMid: 97], [Orb_SpiritLow: 692], [Orb_SpiritMid: 111], [Orb_SpiritHigh: 28], [Orb_VoidLow: 45], [Orb_VoidMid: 80], [Orb_VoidHigh: 14], [Orb_ArcaneLow: 50], [Orb_ArcaneMid: 5], [Orb_ArcaneHigh: 26], [Medal_Bronze: 1], [Medal_Silver: 1], [Medal_Gold: 745], [AllianceBossKey:       1.04421296296297], [FractionWarKey_BannerLords: 6], [FractionWarKey_OgrynTribes: 10], [Forge_Magisteel: 3001], [Forge_Corehammer: 3], [Forge_SoulstoneRare: 367], [Forge_SoulstoneEpic:       434], [Forge_SoulstoneLeg: 20], [Forge_BloodstoneRare: 261], [Forge_BloodstoneEpic: 224], [Forge_BloodstoneLeg: 2], [Forge_NetherSpiderEggsRare: 200], [Forge_NetherSpiderEggsEpic: 19]      , [Forge_ScarabClawsRare: 7], [Forge_ScarabClawsEpic: 4], [Forge_MagmaDragonCoresRare: 406], [Forge_MagmaDragonCoresEpic: 129], [Forge_FrostSpiderSpinesRare: 7], [Forge_DragonBoneRare:       577], [Forge_DragonBoneEpic: 214], [Forge_GriffinFeatherRare: 211], [Forge_GriffinFeatherEpic: 1], [DoomTowerGoldKey: 10], [DoomTowerSilverKey: 10]]"

def main(x):
    # print(x)
    input =  x[67:-1]
    string =  input.split(',')
    myvars = {}
    for each in string:
        name, var = each.partition(":")[::2]
        try:
            myvars[name.strip()] = float(var[:-1])
        except:
            pass
        myvars[name[2:]] = var[:-1]

    energy = myvars['Energy'][:5]
    print('Energy: ' + energy)
    print('Silver: ' + myvars['Silver'])
    print('Gems: ' + myvars['Gem'])

def printAll(myvars):
    print(myvars['Energy'])
    print(myvars['Silver'])
    print(myvars['Token'])
    print(myvars['Gem'])
    print(myvars['Arena3X3ShopCurrency'])
    print(myvars['Arena3x3Token'])
    print(myvars['Orb_MagicLow'])
    print(myvars['Orb_MagicMid'])
    print(myvars['Orb_MagicHigh'])
    print(myvars['Orb_ForceMid'])
    print(myvars['Orb_SpiritLow'])
    print(myvars['Orb_SpiritMid'])
    print(myvars['Orb_SpiritHigh'])
    print(myvars['Orb_VoidLow'])
    print(myvars['Orb_VoidMid'])
    print(myvars['Orb_VoidHigh'])
    print(myvars['Orb_ArcaneLow'])
    print(myvars['Orb_ArcaneMid'])
    print(myvars['Orb_ArcaneHigh'])
    print(myvars['Medal_Bronze'])
    print(myvars['Medal_Silver'])
    print(myvars['Medal_Gold'])
    print(myvars['AllianceBossKey'])
    print(myvars['FractionWarKey_BannerLords'])
    print(myvars['FractionWarKey_OgrynTribes'])
    print(myvars['Forge_Magisteel'])
    print(myvars['Forge_Corehammer'])
    print(myvars['Forge_SoulstoneRare'])
    print(myvars['Forge_SoulstoneEpic'])
    print(myvars['Forge_SoulstoneLeg'])
    print(myvars['Forge_BloodstoneRare'])
    print(myvars['Forge_BloodstoneEpic'])
    print(myvars['Forge_BloodstoneLeg'])
    print(myvars['Forge_NetherSpiderEggsRare'])
    print(myvars['Forge_NetherSpiderEggsEpic'])
    print(myvars['Forge_ScarabClawsRare'])
    print(myvars['Forge_ScarabClawsEpic'])
    print(myvars['Forge_MagmaDragonCoresRare'])
    print(myvars['Forge_MagmaDragonCoresEpic'])
    print(myvars['Forge_FrostSpiderSpinesRare'])
    print(myvars['Forge_DragonBoneRare'])
    print(myvars['Forge_DragonBoneEpic'])
    print(myvars['Forge_GriffinFeatherRare'])
    print(myvars['Forge_GriffinFeatherEpic'])
    print(myvars['DoomTowerGoldKey'])
    print(myvars['DoomTowerSilverKey'])


try: main(sys.argv[1])
except: pass