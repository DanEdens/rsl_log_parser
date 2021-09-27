
 # Raid Shadow Legends -- PC Client Log Parser
### Created by Dan Edens



##  Requirments:

  xargs, grep, tail are requried unix commands included with [Git Bash](https://git-scm.com/download/win) on Windows



##  Python librays:

   paho.mqtt


# Description

When a change occurs on your account, the following values are printed to a logfile, These can be retreived by tailing the file and greping for "normalization"

    tail -f %log% | grep --line-buffered normalization | xargs -I {} python main.py {}


     "Full normalization mode set [Time: 6/25/2021 5:41:33 PM,

     Resources:
     [Energy: 24.9111111111112],
     [Silver: 263430.073149072],
     [Token: 3.22583333333334],
     [Gem: 42],
     [Arena3X3ShopCurrency:       1278],
     [Arena3x3Token: 5],
     [Orb_MagicLow: 20],
     [Orb_MagicMid: 9],
     [Orb_MagicHigh: 4],
     [Orb_ForceMid: 97],
     [Orb_SpiritLow: 692],
     [Orb_SpiritMid: 111],
     [Orb_SpiritHigh: 28],
     [Orb_VoidLow: 45],
     [Orb_VoidMid: 80],
     [Orb_VoidHigh: 14],
     [Orb_ArcaneLow: 50],
     [Orb_ArcaneMid: 5],
     [Orb_ArcaneHigh: 26],
     [Medal_Bronze: 1],
     [Medal_Silver: 1],
     [Medal_Gold: 745],
     [AllianceBossKey:       1.04421296296297],
     [FractionWarKey_BannerLords: 6],
     [FractionWarKey_OgrynTribes: 10],
     [Forge_Magisteel: 3001],
     [Forge_Corehammer: 3],
     [Forge_SoulstoneRare: 367],
     [Forge_SoulstoneEpic:       434],
     [Forge_SoulstoneLeg: 20],
     [Forge_BloodstoneRare: 261],
     [Forge_BloodstoneEpic: 224],
     [Forge_BloodstoneLeg: 2],
     [Forge_NetherSpiderEggsRare: 200],
     [Forge_NetherSpiderEggsEpic: 19],
     [Forge_ScarabClawsRare: 7],
     [Forge_ScarabClawsEpic: 4],
     [Forge_MagmaDragonCoresRare: 406],
     [Forge_MagmaDragonCoresEpic: 129],
     [Forge_FrostSpiderSpinesRare: 7],
     [Forge_DragonBoneRare:       577],
     [Forge_DragonBoneEpic: 214],
     [Forge_GriffinFeatherRare: 211],
     [Forge_GriffinFeatherEpic: 1],
     [DoomTowerGoldKey: 10],
     [DoomTowerSilverKey: 10]]"
