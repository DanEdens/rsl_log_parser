import sys
import subprocess
import os
import time

# _mqttPub = os.environ.get('RAID_LOG_PUB', False)
_mqttPub = True

# If broker configured on server, pub results: raid/status/{key} {value}
if _mqttPub == True:
    print('Mqtt Pub Enabled.')
    import paho.mqtt.client as paho
    import socket
    client = paho.Client('RSL_parser_' + str(socket.gethostname()), clean_session=True)
    client.connect(os.environ.get("AWSIP"), int(os.environ.get("AWSPORT")))




def post(key, value):
    if os.environ.get('RAID_LOG_PUB', False):
        try:
            print(key + ': %12s' % value)
            client.publish(f'status/raid/{key}', value, retain=True)
        except: pass
    else:
        print(key + ': %12s' % value)    


def main(x):
    """Parses contents of piped log data"""

    # Remove msg header, which is already in dictionary format
    input =  x[67:-1]

    # Split dictionary
    string =  input.split(',')

    myvars = {}
    for each in string:
        name, var = each.partition(":")[::2]
        try:
            myvars[name.strip()] = float(var[:-1])
        except:
            pass
        myvars[name[2:]] = var[:-1]

    # Set current time
    timer = time.strftime("%H:%M.%S")

    # Compare to previous, print values that have changed
    if os.path.exists("file.txt"):
        file = open("last.txt", "r")
        file_lines = file.read()
        bakvars = file_lines.split("\n")
        diff1=set(bakvars) - set(myvars)
        list_diff = list(diff1)
    else:
        list_diff = myvars
    with open("last.txt", "w") as file:
        file_lines = "\n".join(myvars)
        file.write(file_lines)
    
    # Remove decimal place
    energy = list_diff['Energy'].split('.')[0]
    silver = list_diff['Silver'].split('.')[0]
    # DreadhornPlatesRare = myvars['Forge_DreadhornPlatesRare'].split('.')[0]
    DreadhornPlatesEpic = list_diff['Forge_DreadhornPlatesEpic'].split('.')[0]
    DreadhornPlatesLeg = list_diff['Forge_DreadhornPlatesLeg'].split('.')[0]

    if os.environ.get('RAID_LOG_PUB', False):
        try:
            client.publish('status/raid/energy', energy, retain=True)
            client.publish('status/raid/silver', silver, retain=True)
            client.publish('status/raid/gems', list_diff['Gem'], retain=True)
            client.publish('status/raid/time', timer, retain=True)
            # client.publish('status/raid/DreadhornPlatesRare', DreadhornPlatesRare, retain=True)
            client.publish('status/raid/DreadhornPlatesEpic', DreadhornPlatesEpic, retain=True)
            client.publish('status/raid/DreadhornPlatesLeg', DreadhornPlatesLeg, retain=True)
        except: pass

    print('------------------------------')
    print('Energy: %12s' % energy)
    print('Silver: %12s' % silver)
    print('Gems: %14s' % myvars['Gem'])
    print('Time: %14s' % timer)


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
