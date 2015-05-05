from flask import Flask, render_template
from flask.ext.socketio import SocketIO, send, emit
import os
app = Flask(__name__)
socketio = SocketIO(app)

mission = False
admiralTaken = False
engineerTaken = False
navigationsTaken = False
tacticalTaken = False
operationsTaken = False
brokenSystemList = []
nearbyShipList = []
admiralName = ""
engineerName = ""
navigationsName = ""
tacticalName = ""
operationsName = ""
brokenSystemName = ""
remoteCode = ""
warpEnginePower = 100
impulseEnginePower = 100
thrusterPower = 100
mainComputerPower = 100
lifeSupportPower = 100
weaponsSystemPower = 100
tractorBeamPower = 100
cloakingDevicePower = 100
transporterPower = 100
powerLevel = "900"
weaponsHeat = 0
weaponsCoolant = 100
engineHeat = 0
engineCoolant = 100
wGoAhead = "Yes"
eGoAhead = "Yes"
mainReactorEject = "No"
dylithiumStatus = "normaldylithium"
selfDestruct = "No"
navigationsBlack = False
operationsBlack = False
tacticalBlack = False
engineeringBlack = False
allBlack = False
scanningForCourse = False
courseTo = ""
courseEntered = False
xFD = ""
yFD = ""
zFD = ""
courseSet = False
x = ""
y = ""
z = ""
warpSpeed = "0"
impulseSpeed = "0"
transWarp = ""
courseScanAnswered = False
targetLock = ""
phaser1 = []
torpedoLoaded = 0
torpedoAvailable = 0
shields = False
THX = ""
CRM = ""
cloaking = ""
tranzineGas = "deactivated"
bulkheadDoors = "opened"
securityTeam1 = ""
securityTeam2 = ""
securityTeam3 = ""
externalScan = ""
externalScanAnswer = ""
internalScan = ""
internalScanAnswer = ""
sensorsInfo = ""
frequency = "General Use"
hailing = False
hailingfd = False
calling = ""
mainSpeakers = False
longRangeFD = []
longRangeOPS = []
transporterTargets = []
currentDamageReport = ""
missionObjectives = ""
currentlyFixing = ""
mainComputerBroken = False
@socketio.on('message', namespace="/main")
def handle_message(message):
    global mission
    global admiralTaken
    global engineerTaken
    global tacticalTaken
    global navigationsTaken
    global operationsTaken
    global admiralName
    global engineerName
    global tacticalName
    global operationsName
    global navigationsName
    global brokenSystemList
    global nearbyShipList
    global remoteCode
    global warpEnginePower
    global impulseEnginePower
    global thrusterPower
    global mainComputerPower
    global lifeSupportPower
    global weaponsSystemPower
    global tractorBeamPower
    global cloakingDevicePower
    global transporterPower
    global powerLevel
    global weaponsHeat
    global weaponsCoolant
    global engineHeat
    global engineCoolant
    global wGoAhead
    global eGoAhead
    global mainReactorEject
    global dylithiumStatus
    global selfDestruct
    global navigationsBlack
    global operationsBlack
    global tacticalBlack
    global engineeringBlack
    global allBlack
    global scanningForCourse
    global courseTo
    global courseEntered
    global xFD
    global yFD
    global zFD
    global courseSet
    global x
    global y
    global z
    global courseScanAnswered
    global warpSpeed
    global transWarp
    global impulseSpeed
    global targetLock
    global phaser1
    global torpedoLoaded
    global torpedoAvailable
    global shields
    global THX
    global CRM
    global cloaking
    global tranzineGas
    global bulkheadDoors
    global securityTeam1
    global securityteam2
    global securityTeam3
    global externalScan
    global externalScanAnswer
    global internalScan
    global internalScanAnswer
    global sensorsInfo
    global frequency
    global hailing
    global hailingfd
    global calling
    global mainSpeakers
    global longRangeFD
    global longRangeOPS
    global transporterTargets
    global currentDamageReport
    global missionObjectives
    global currentlyFixing
    global mainComputerBroken
    if message == "maincomputeroffline":
        send(message, broadcast = True)
        mainComputerBroken = True
    if message == "maincomputeronline":
        send(message, broadcast = True)
        mainComputerBroken = False
    if message.startswith("currentlyfixing: "):
        send(message, broadcast = True)
        currentlyFixing = message[17:]
    if message == "reloadstations":
        send(message, broadcast = True)
    if message.startswith("transportedto: "):
        send(message, broadcast = True)
    if message == "cleartargets":
        send(message, broadcast = True)
    if message == "start mission":
        mission = True
        send("missionyes", broadcast=True)
        print mission
    if message.startswith("admiral name: "):
        admiralName = message[14:]
        admiralTaken = True
        send("admiraltaken: "+admiralName, broadcast=True)
        print admiralName
    if message.startswith("engineer name: "):
        engineerName = message[15:]
        engineerTaken = True
        send("engineertaken: "+engineerName, broadcast=True)
        print engineerName
    if message.startswith("navigations name: "):
        navigationsName = message[18:]
        navigationsTaken = True
        send("navigationstaken: "+ navigationsName, broadcast=True)
        print navigationsName
    if message.startswith("tactical name: "):
        tacticalName = message[15:]
        tacticalTaken = True
        send("tacticaltaken: " + tacticalName, broadcast=True)
    if message.startswith("operations name: "):
        operationsName = message[17:]
        operationsTaken = True
        send("operationstaken: " + operationsName, broadcast=True)
    if message.startswith("brokensystem: "):
        brokenSystemName = message[14:]
        brokenSystemList.append(brokenSystemName)
        send("predamage", broadcast=True)
        for system in brokenSystemList:
            send("brokensystem: " + system, broadcast=True)
    if message.startswith("fixsystem: "):
        fixSystemName = message[11:]
        brokenSystemList.remove(fixSystemName)
        if fixSystemName == currentlyFixing:
            currentDamageReport = ""
            send("damagereport: ", broadcast=True)
            currentlyFixing = ""
            send("currentlyfixing: ", broadcast=True)
        print fixSystemName
        send("predamage", broadcast=True)
        for system in brokenSystemList:
            send("brokensystem: " + system, broadcast=True)
    if message.startswith("addship: "):
        nearbyShipList.append(message[9:])
        send("preship", broadcast=True)
        for ship in nearbyShipList:
            send("nearbyship: " + ship, broadcast=True)
    if message.startswith("removeship: "):
        nearbyShipList.remove(message[12:])
        send("preship", broadcast=True)
        for ship in nearbyShipList:
            send("nearbyship: " + ship, broadcast=True)
    if message.startswith("longrangemessagefd: "):
        longRangeFD.append(message[20:])
        send("premessagefd", broadcast=True)
        for longmessage in longRangeFD:
            send("longrangemessagefd: " + longmessage, broadcast=True)
    if message.startswith("deletelongrangemessagefd: "):
        longRangeFD.remove(message[26:])
        send("premessagefd", broadcast=True)
        for longmessage in longRangeFD:
            send("longrangemessagefd: " + longmessage, broadcast=True)
    if message.startswith("longrangemessageops: "):
        longRangeOPS.append(message[21:])
        send("premessageops", broadcast=True)
        for longmessage in longRangeOPS:
            send("longrangemessageops: " + longmessage, broadcast=True)
    if message.startswith("deletelongrangemessageops: "):
        longRangeOPS.remove(message[27:])
        send("premessageops", broadcast=True)
        for longmessage in longRangeOPS:
            send("longrangemessageops: " + longmessage, broadcast=True)
    if message.startswith("transportertarget: "):
        transporterTargets.append(message[19:])
        send("pretransport", broadcast=True)
        for target in transporterTargets:
            send("transportertarget:  " + target, broadcast=True)
    if message.startswith("transportedtarget: "):
        transporterTargets.remove(message[19:])
        send("pretransport", broadcast=True)
        for target in transporterTargets:
            send("transportertarget: " + target, broadcast=True)
    if message.startswith("remoterepaircode: "):
        remoteCode = message
        send(message, broadcast=True)
    if message.startswith("increasepower: "):
        message = message[15:]
        if message == "Warp Engines":
            warpEnginePower = warpEnginePower + 25
            if warpEnginePower > 100:
                warpEnginePower = 100
            warpEnginePower = str(warpEnginePower)
            send("warpenginepower: " + warpEnginePower, broadcast=True)
            print warpEnginePower
            warpEnginePower = int(warpEnginePower)
        if message == "Impulse Engines":
            impulseEnginePower = impulseEnginePower + 25
            if impulseEnginePower > 100:
                impulseEnginePower = 100
            impulseEnginePower = str(impulseEnginePower)
            send("impulseenginepower: " + impulseEnginePower, broadcast=True)
            print impulseEnginePower
            impulseEnginePower = int(impulseEnginePower)
        if message == "Thrusters":
            thrusterPower = thrusterPower + 25
            if thrusterPower > 100:
                thrusterPower = 100
            thrusterPower = str(thrusterPower)
            send("thrusterpower: " + thrusterPower, broadcast=True)
            print thrusterPower
            thrusterPower = int(thrusterPower)
        if message == "Main Computer":
            mainComputerPower = mainComputerPower +25
            if mainComputerPower > 100:
                mainComputerPower = 100
            mainComputerPower = str(mainComputerPower)
            send("maincomputerpower: " + mainComputerPower, broadcast=True)
            print mainComputerPower
            mainComputerPower = int(mainComputerPower)
        if message == "Life Support":
            lifeSupportPower = lifeSupportPower + 25
            if lifeSupportPower > 100:
                lifeSupportPower = 100
            lifeSupportPower = str(lifeSupportPower)
            send("lifesupportpower: " + lifeSupportPower, broadcast=True)
            print lifeSupportPower
            lifeSupportPower = int(lifeSupportPower)
        if message == "Weapons":
            weaponsSystemPower = weaponsSystemPower + 25
            if weaponsSystemPower > 100:
                weaponsSystemPower = 100
            weaponsSystemPower = str(weaponsSystemPower)
            send("weaponssystempower: " + weaponsSystemPower, broadcast=True)
            print weaponsSystemPower
            weaponsSystemPower = int(weaponsSystemPower)
        if message == "Tractor Beam":
            tractorBeamPower = tractorBeamPower + 25
            if tractorBeamPower > 100:
                tractorBeamPower = 100
            tractorBeamPower = str(tractorBeamPower)
            send("tractorbeampower: " + tractorBeamPower, broadcast=True)
            print tractorBeamPower
            tractorBeamPower = int(tractorBeamPower)
        if message == "Cloaking Device":
            cloakingDevicePower = cloakingDevicePower + 25
            if cloakingDevicePower > 100:
                cloakingDevicePower = 100
            cloakingDevicePower = str(cloakingDevicePower)
            send("cloakingdevicepower: " + cloakingDevicePower, broadcast=True)
            print cloakingDevicePower
            cloakingDevicePower = int(cloakingDevicePower)
        if message == "Transporters":
            transporterPower = transporterPower + 25
            if transporterPower > 100:
                transporterPower = 100
            transporterPower = str(transporterPower)
            send("transporterpower: " + transporterPower, broadcast=True)
            print transporterPower
            transporterPower = int(transporterPower)
    if message.startswith("decreasepower: "):
        message = message[15:]
        if message == "Warp Engines":
            warpEnginePower = warpEnginePower - 25
            if warpEnginePower < 0:
                warpEnginePower = 0
            warpEnginePower = str(warpEnginePower)
            send("warpenginepower: " + warpEnginePower, broadcast=True)
            print warpEnginePower
            warpEnginePower = int(warpEnginePower)
        if message == "Impulse Engines":
            impulseEnginePower = impulseEnginePower - 25
            if impulseEnginePower < 0:
                impulseEnginePower = 0
            impulseEnginePower = str(impulseEnginePower)
            send("impulseenginepower: " + impulseEnginePower, broadcast=True)
            print impulseEnginePower
            impulseEnginePower = int(impulseEnginePower)
        if message == "Thrusters":
            thrusterPower = thrusterPower - 25
            if thrusterPower < 0:
                thrusterPower = 0
            thrusterPower = str(thrusterPower)
            send("thrusterpower: " + thrusterPower, broadcast=True)
            print thrusterPower
            thrusterPower = int(thrusterPower)
        if message == "Main Computer":
            mainComputerPower = mainComputerPower - 25
            if mainComputerPower < 0:
                mainComputerPower = 0
            mainComputerPower = str(mainComputerPower)
            send("maincomputerpower: " + mainComputerPower, broadcast=True)
            print mainComputerPower
            mainComputerPower = int(mainComputerPower)
        if message == "Life Support":
            lifeSupportPower = lifeSupportPower - 25
            if lifeSupportPower < 0:
                lifeSupportPower = 0
            lifeSupportPower = str(lifeSupportPower)
            send("lifesupportpower: " + lifeSupportPower, broadcast=True)
            print lifeSupportPower
            lifeSupportPower = int(lifeSupportPower)
        if message == "Weapons":
            weaponsSystemPower = weaponsSystemPower - 25
            if weaponsSystemPower < 0:
                weaponsSystemPower = 0
            weaponsSystemPower = str(weaponsSystemPower)
            send("weaponssystempower: " + weaponsSystemPower, broadcast=True)
            print weaponsSystemPower
            weaponsSystemPower = int(weaponsSystemPower)
        if message == "Tractor Beam":
            tractorBeamPower = tractorBeamPower - 25
            if tractorBeamPower < 0:
                tractorBeamPower = 0
            tractorBeamPower = str(tractorBeamPower)
            send("tractorbeampower: " + tractorBeamPower, broadcast=True)
            print tractorBeamPower
            tractorBeamPower = int(tractorBeamPower)
        if message == "Cloaking Device":
            cloakingDevicePower = cloakingDevicePower - 25
            if cloakingDevicePower < 0:
                cloakingDevicePower = 0
            cloakingDevicePower = str(cloakingDevicePower)
            send("cloakingdevicepower: " + cloakingDevicePower, broadcast=True)
            print cloakingDevicePower
            cloakingDevicePower = int(cloakingDevicePower)
        if message == "Transporters":
            transporterPower = transporterPower - 25
            if transporterPower < 0:
                transporterPower = 0
            transporterPower = str(transporterPower)
            send("transporterpower: " + transporterPower, broadcast=True)
            print transporterPower
            transporterPower = int(transporterPower)
    if message.startswith("coursescan: "):
        send(message, broadcast=True)
        scanningForCourse = True
        courseScanAnswered = False
        courseTo = message[12:]
    if message == "cancelcoursescan":
        send(message, broadcast=True)
        scanningForCourse = False
        courseTo = ""
    if message.startswith("decreasecoolant: "):
        message = message[17:]
        if message == "Weapons System":
            weaponsCoolant = weaponsCoolant - 10
            if weaponsCoolant < 0:
                weaponsCoolant = 0
                if weaponsHeat > 0:
                    wGoAhead = "Yes"
                if weaponsHeat < 0:
                    wGoAhead = "No"
            if wGoAhead == "Yes":
                weaponsHeat = weaponsHeat - 5
                if weaponsHeat < 0:
                    weaponsHeat = 0
            weaponsCoolant = str(weaponsCoolant)
            send("weaponscoolant: " + weaponsCoolant, broadcast=True)
            weaponsCoolant = int(weaponsCoolant)
            weaponsHeat = str(weaponsHeat)
            send("weaponsheat: " + weaponsHeat, broadcast= True)
            weaponsHeat = int(weaponsHeat)
        if message == "Engine System":
            engineCoolant = engineCoolant - 10
            if engineCoolant < 0:
                engineCoolant = 0
                if weaponsHeat > 0:
                    eGoAhead = "Yes"
                if weaponsHeat <0:
                    eGoAhead = "No"
            if eGoAhead == "Yes":
                engineHeat = engineHeat - 5
                if engineHeat < 0:
                    engineHeat = 0
            engineCoolant = str(engineCoolant)
            send("enginecoolant: " + engineCoolant, broadcast=True)
            engineCoolant = int(engineCoolant)
            engineHeat = str(engineHeat)
            send("engineheat: " + engineHeat, broadcast= True)
            engineHeat = int(engineHeat)
    if message.startswith("flightdirectorweaponscoolant: "):
        message = message[30:]
        weaponsCoolant = message
        weaponsCoolant= str(weaponsCoolant)
        send("weaponscoolant: " + weaponsCoolant, broadcast=True)
        weaponsCoolant = int(weaponsCoolant)
    if message.startswith("flightdirectorweaponsheat: "):
        message = message[27:]
        weaponsHeat = message
        weaponsHeat = str(weaponsHeat)
        send("weaponsheat: " + weaponsHeat, broadcast=True)
        weaponsHeat = int(weaponsHeat)
    if message.startswith("flightdirectorenginecoolant: "):
        message = message[29:]
        engineCoolant = message
        engineCoolant= str(engineCoolant)
        send("enginecoolant: " + engineCoolant, broadcast=True)
        engineCoolant = int(engineCoolant)
        print "done"
    if message.startswith("flighdirectorengineheat: "):
        message = message[25:]
        engineHeat = message
        engineHeat = str(engineHeat)
        send("engineheat: " + engineHeat, broadcast=True)
        engineHeat = int(engineHeat)
        print "doneengine"
    if message.startswith("powerlevel: "):
        message = message[12:]
        powerLevel = message
        send("powerlevel: " + powerLevel, broadcast=True)
        print "powerchange"
    if message.startswith("blackout: "):
        send(message, broadcast=True)
        message = message[10:]
        if message == "navigations":
            navigationsBlack = True
        if message == "operations":
            operationsBlack = True
        if message == "tactical":
            tacticalBlack = True
        if message == "engineering":
            engineeringBlack = True
        if message == "all":
            allBlack = True
            navigationsBlack = True
            operationsBlack = True
            tacticalBlack = True
            engineeringBlack = True
    if message.startswith("unblackout: "):
        send(message, broadcast=True)
        message = message[12:]
        if message == "navigations":
            navigationsBlack = False
        if message == "operations":
            operationsBlack = False
        if message == "tactical":
            tacticalBlack = False
        if message == "engineering":
            engineeringBlack = False
        if message == "all":
            allBlack = False
            navigationsBlack = False
            operationsBlack = False
            tacticalBlack = False
            engineeringBlack = False
    if message.startswith("xcoordinatefd: "):
        send(message, broadcast=True)
        xFD = message[15:]
    if message.startswith("ycoordinatefd: "):
        send(message, broadcast=True)
        yFD = message[15:]
    if message.startswith("zcoordinatefd: "):
        send(message, broadcast=True)
        zFD = message[15:]
    if message.startswith("speedchange: w"):
        send(message, broadcast=True)
        send("speedchange: -t", broadcast=True)
        send("speedchange: i0", broadcast=True)
        warpSpeed = message[14:]
        impulseSpeed = "0"
        transWarp = ""
    if message.startswith("speedchange: f"):
        send("speedchange: f", broadcast=True)
        send("speedchange: w0", broadcast=True)
        send("speedchange: -t", broadcast=True)
        send("speedchange: i0", broadcast=True)
        warpSpeed = "0"
        impulseSpeed = "0"
        transWarp = ""
    if message.startswith("speedchange: t"):
        send(message ,broadcast=True)
        send("speedchange: w0", broadcast=True)
        send("speedchange: i0", broadcast=True)
        transWarp = "activated"
        warpSpeed = "0"
        impulseSpeed= "0"
    if message.startswith("speedchange: tauthorized"):
        send(message, broadcast=True)
        transWarp = "authorized"
    if message.startswith("speedchange: -t"):
        send(message, broadcast = True)
        transWarp = ""
        warpSpeed = "0"
        impulseSpeed = "0"
    if message.startswith("speedchange: i"):
        send(message, broadcast = True)
        send("speedchange: w0", broadcast=True)
        send("speedchange: -t", broadcast=True)
        impulseSpeed = message[14:]
        warpSpeed = "0"
        transWarp = ""
    if message.startswith("thruster: "):
        send(message, broadcast = True)
    if message.startswith("phasercharged: "):
        send(message, broadcast = True)
        phaser1.append(message[15:])
    if message.startswith("phaserfired: "):
        send(message, broadcast = True)
        phaser1.remove(message[13:])
    if message == "precoursefd":
        send(message, broadcast=True)
        courseEntered = True
        courseScanAnswered = False
    if message.startswith("xcoordinate: "):
        send(message, broadcast=True)
        x = message[13:]
        print x
    if message.startswith("ycoordinate: "):
        send(message, broadcast=True)
        y = message[13:]
        print y
    if message.startswith("zcoordinate: "):
        send(message, broadcast=True)
        z = message[13:]
        print z
    if message.startswith("locktarget: "):
        send(message, broadcast = True)
        targetLock = message[12:]
    if message == "precourseset":
        send(message, broadcast=True)
        courseSet = True
    if message == "ejectmainreactor":
        send(message, broadcast=True)
        mainReactorEject = "Yes"
    if message == "cancelejectmainreactor":
        send(message, broadcast=True)
        mainReactorEject = "No"
    if message == "normaldylithium":
        send("normaldylithium", broadcast=True)
        dylithiumStatus = "normaldylithium"
    if message == "cautiondylithium":
        send("cautiondylithium", broadcast=True)
        dylithiumStatus = "cautiondylithium"
    if message == "criticaldylithium":
        send("criticaldylithium", broadcast=True)
        dylithiumStatus = "criticaldylithium"
    if message == "selfdestruct":
        send("selfdestruct", broadcast=True)
        selfDestruct = "Yes"
    if message == "cancelselfdestruct":
        send("cancelselfdestruct", broadcast=True)
        selfDestruct = "No"
    if message.startswith("torpedoavailablefd: "):
        torpedoAvailable = int(message[20:])
        send("torpedoavailableleft: " + str(torpedoAvailable), broadcast=True)
        print "torpedo fd"
    if message == "torpedoloaded":
        if torpedoAvailable == 1:
            onOne1 = "yes"
        else: 
            onOne1 = "no"
        torpedoAvailable = torpedoAvailable - 1
        if torpedoAvailable <= 0:
            torpedoAvailable = 0
            send("torpedoavailableleft: " + str(torpedoAvailable), broadcast=True)
            if onOne1 == "yes":
                torpedoLoaded = torpedoLoaded + 1
                send("torpedoavailableleft: " + str(torpedoAvailable), broadcast=True)
                send("torpedoloadedleft: " + str(torpedoLoaded), broadcast=True)
        if torpedoAvailable > 0:
            torpedoLoaded = torpedoLoaded + 1
            send("torpedoavailableleft: " + str(torpedoAvailable), broadcast=True)
            send("torpedoloadedleft: " + str(torpedoLoaded), broadcast=True)
    if message == "torpedoaway":
        if torpedoLoaded == 1:
            onOne = "yes"
        else:
            onOne = "no"
        torpedoLoaded = torpedoLoaded - 1
        if torpedoLoaded <= 0:
            torpedoLoaded = 0
            send("torpedoloadedleft: " + str(torpedoLoaded), broadcast=True)
            if onOne == "yes":
                send("torpedoaway", broadcast=True)
        if torpedoLoaded > 0:
            send("torpedoloadedleft: " + str(torpedoLoaded), broadcast=True)
            send("torpedoaway", broadcast=True)
    if message == "cleartargets":
        targetLock = ""
    if message == "shieldsactivated":
        send(message, broadcast=True)
        shields = True
    if message == "shieldsdeactivated":
        send(message, broadcast=True)
        shields = False
    if message == "activatethx":
        send(message, broadcast=True)
        THX = "authorizing"
    if message == "activatethxfd":
        send(message, broadcast=True)
        THX = "authorized"
    if message == "deactivatethx":
        send(message, broadcast=True)
        THX = ""
    if message == "activatecrm":
        send(message, broadcast=True)
        CRM = "authorizing"
    if message == "activatecrmfd":
        send(message, broadcast=True)
        CRM = "authorized"
    if message == "deactivatecrm":
        send(message, broadcast=True)
        CRM = ""
    if message == "activatecloaking":
        send(message, broadcast=True)
        cloaking = "authorizing"
    if message == "activatecloakingfd":
        send(message, broadcast=True)
        cloaking = "authorized"
    if message == "deactivatecloaking":
        send(message, broadcast=True)
        cloaking = ""
    if message.startswith("sendsecurityteam1: "):
        send(message, broadcast=True)
        securityTeam1 = message[19:]
    if message == "recallsecurityteam1":
        send(message, broadcast=True)
        securityTeam1 = ""
    if message.startswith("sendsecurityteam2: "):
        send(message, broadcast=True)
        securityTeam2 = message[19:]
    if message == "recallsecurityteam2":
        send(message, broadcast=True)
        securityTeam2 = ""
    if message.startswith("sendsecurityteam3: "):
        send(message, broadcast=True)
        securityTeam3 = message[19:]
    if message == "recallsecurityteam3":
        send(message, broadcast=True)
        securityTeam3 = ""
    if message == "closebulkheaddoors":
        send(message, broadcast=True)
        bulkheadDoors = "closed"
    if message == "openbulkheaddoors":
        send(message, broadcast=True)
        bulkheadDoors = "opened"
    if message == "activatetranzinegas":
        send(message, broadcast=True)
        tranzineGas = "activated"
    if message == "deactivatetranzinegas":
        send(message, broadcast=True)
        tranzineGas = "deactivated"
    if message.startswith("external scan: "):
        send(message, broadcast=True)
        externalScan = message[15:]
        externalScanAnswer = ""
    if message.startswith("external scan answer: "):
        send(message, broadcast=True)
        externalScanAnswer = message[22:]
        externalScan = ""
    if message == ("cancelexternalscan"):
        send(message, broadcast=True)
        externalScan = ""
    if message.startswith("internal scan: "):
        send(message, broadcast=True)
        internalScan = message[15:]
        internalScanAnswer = ""
    if message.startswith("internal scan answer: "):
        send(message, broadcast=True)
        internalScanAnswer = message[22:]
        internalScan = ""
    if message == ("cancelinternalscan"):
        send(message, broadcast=True)
        internalScan = ""
    if message.startswith("sensors info: "):
        send(message, broadcast=True)
        sensorsInfo = message[14:]
    if message.startswith("frequency: "):
        send(message, broadcast=True)
        frequency = message[11:]
    if message.startswith("hailing: "):
        send(message + frequency, broadcast=True)
        hailing = True
    if message == "hailingfd":
        send(message, broadcast=True)
        hailingfd = True
    if message.startswith("calling: "):
        send(message, broadcast=True)
        calling = message[9:]
    if message.startswith("connectmainspeakers"):
        send(message, broadcast=True)
        mainSpeakers = True
    if message.startswith("disconnectmainspeakers"):
        send(message, broadcast=True)
        mainSpeakers = False
    if message == "disconnectcommunications":
        send(message, broadcast=True)
        send("disconnectmainspeakers", broadcast=True)
        mainSpeakers = False
        hailing = False
        hailingfd = False
        calling = ""
    if message.startswith("damagereport: "):
        currentDamageReport = message[14:]
    if message.startswith("missionobjectives: "):
        send(message, broadcast=True)
        missionObjectives = message[19:]
@socketio.on('connect', namespace="/main")
def startSocket():
    global mission
    global admiralTaken
    global engineerTaken
    global navigationsTaken
    global tacticalTaken
    global operationsTaken
    global admiralName
    global navigationsName
    global engineerName
    global tacticalName
    global operationsName
    global brokenSystemList
    global nearbyShipList
    global warpEnginePower
    global impulseEnginePower
    global thrusterPower
    global mainComputerPower
    global lifeSupportPower
    global weaponsSystemPower
    global tractorBeamPower
    global cloakingDevicePower
    global transporterPower
    global powerLevel
    global weaponsHeat
    global weaponsCoolant
    global engineHeat
    global engineCoolant
    global mainReactorEject
    global dylithiumStatus
    global selfDestruct 
    global navigationsBlack
    global operationsBlack
    global tacticalBlack
    global engineeringBlack
    global allBlack
    global scanningForCourse
    global courseTo
    global courseEntered
    global xFD
    global yFD
    global zFD
    global courseSet
    global x
    global y
    global z
    global courseScanAnswered
    global warpSpeed
    global transWarp
    global impulseSpeed
    global targetLock
    global phaser1
    global torpedoLoaded
    global torpedoAvailable
    global shields
    global THX
    global CRM
    global cloaking
    global tranzineGas
    global bulkheadDoors
    global securityTeam1
    global securityTeam2
    global securityTeam3
    global externalScan
    global externalScanAnswer
    global internalScan
    global internalScanAnswer
    global sensorsInfo
    global frequency
    global hailing
    global hailingfd
    global calling
    global mainSpeakers
    global longRangeFD
    global longRangeOPS
    global transporterTargets
    global currentDamageReport
    global missionObjectives
    global currentlyFixing
    global mainComputerBroken
    if currentlyFixing != "":
        send("currentlyfixing: " + currentlyFixing)
    send("damagereport: " + currentDamageReport)
    send("missionobjectives: " + missionObjectives)
    send("predamage")
    send("preship")
    send("premessagefd")
    send("premessageops")
    send("pretransport")
    send("speedchange: i" + impulseSpeed)
    send("torpedoloadedleft: " + str(torpedoLoaded))
    send("torpedoavailableleft: " + str(torpedoAvailable))
    send("frequency: " + frequency)
    if mainComputerBroken == True:
        send("maincomputeroffline")
    if mainComputerBroken == False:
        send("maincomputeronline")
    if shields == True:
        send("shieldsactivated")
    else:
        send("shieldsdeactivated")
    if targetLock == "":
        print "1010101110101"
    else:
        send("locktarget: " + targetLock)
    warpSpeed = int(warpSpeed)
    if warpSpeed > 0:
        warpSpeed = str(warpSpeed)
        send("speedchange: w" + warpSpeed)
    if transWarp == "activated":
        send("speedchange: t")
    if transWarp == "authorized":
        send("speedchange: tauthorized")
    warpEnginePower = str(warpEnginePower)
    send("warpenginepower: "  + warpEnginePower)
    warpEnginePower = int(warpEnginePower)
    
    impulseEnginePower = str(impulseEnginePower)
    send("impulseenginepower: " + impulseEnginePower)
    impulseEnginePower = int(impulseEnginePower)
    
    thrusterPower = str(thrusterPower)
    send("thrusterpower: " + thrusterPower)
    thrusterPower = int(thrusterPower)
    
    mainComputerPower = str(mainComputerPower)
    send("maincomputerpower: " + mainComputerPower)
    mainComputerPower = int(mainComputerPower)
    
    lifeSupportPower = str(lifeSupportPower)
    send("lifesupportpower: " + lifeSupportPower)
    lifeSupportPower = int(lifeSupportPower)
    
    weaponsSystemPower = str(weaponsSystemPower)
    send("weaponssystempower: " + weaponsSystemPower)
    weaponsSystemPower = int(weaponsSystemPower)
    
    tractorBeamPower = str(tractorBeamPower)
    send("tractorbeampower: " + tractorBeamPower)
    tractorBeamPower = int(tractorBeamPower)
    
    cloakingDevicePower = str(cloakingDevicePower)
    send("cloakingdevicepower: " + cloakingDevicePower)
    cloakingDevicePower = int(cloakingDevicePower)
    
    transporterPower = str(transporterPower)
    send("transporterpower: " + transporterPower)
    transporterPower = int(transporterPower)
    
    send("powerlevel: " + powerLevel)
    send(remoteCode)
    
    weaponsHeat = str(weaponsHeat)
    send("weaponsheat: " + weaponsHeat)
    weaponsHeat = int(weaponsHeat)
    
    weaponsCoolant = str(weaponsCoolant)
    send("weaponscoolant: " + weaponsCoolant)
    weaponsCoolant = int(weaponsCoolant)
    
    engineHeat = str(engineHeat)
    send("engineheat: " + engineHeat)
    engineHeat = int(engineHeat)
    
    engineCoolant = str(engineCoolant)
    send("enginecoolant: " + engineCoolant)
    engineCoolant = int(engineCoolant)
    
    send(dylithiumStatus)
    
    if hailingfd == True:
        send("hailingfd")
    if hailing == True:
        send("hailing: " + frequency)
    if calling == "":
        print ":LKDJ:LKJ"
    else:
        send("calling: " + calling)
    if mainSpeakers == True:
        send("connectmainspeakers")
    else:
        send("disconnectmainspeakers")
    if securityTeam1 == "":
        send("recallsecurityteam1")
    else:
        send("sendsecurityteam1: " + securityTeam1)
    if securityTeam2 == "":
        send("recallsecurityteam2")
    else:
        send("sendsecurityteam2: " + securityTeam2)
    if securityTeam3 == "":
        send("recallsecurityteam3")
    else:
        send("sendsecurityteam3: " + securityTeam3)
    if tranzineGas == "deactivated":
        send("deactivatetranzinegas")
    else:
        send("activatetranzinegas")
    if bulkheadDoors == "opened":
        send("openbulkheaddoors")
    else:
        send("closebulkheaddoors")
    if externalScan == "":
        send("cancelexternalscan")
    else:
        send("external scan: " + externalScan)
    if externalScanAnswer == "":
        print "a;slkdfj"
    else:
        send("external scan answer: " + externalScanAnswer)
    if internalScan == "":
        send("cancelinternalscan")
    else:
        send("internal scan: " + internalScan)
    if internalScanAnswer == "":
        print "a;slkfjdas"
    else:
        send("internal scan answer: " + internalScanAnswer)
    if sensorsInfo == "":
        print ";laksjdfkl"
    else:
        send("sensors info: " + sensorsInfo)
    if THX == "authorizing":
        send("deactivatecrm")
        send("deactivatecloaking")
        send("activatethx")
    if THX == "authorized":
        send("deactivatecrm")
        send("deactivatecloaking")
        send("activatethxfd")
    if CRM == "authorizing":
        send("deactivatethx")
        send("deactivatecloaking")
        send("activatecrm")
    if CRM == "authorized":
        send("deactivatethx")
        send("deactivatecloaking")
        send("activatecrmfd")
    if cloaking == "authorizing":
        send("deactivatethx")
        send("deactivatecrm")
        send("activatecloaking")
    if cloaking == "authorized":
        send("deactivatethx")
        send("deactivatecrm")
        send("activatecloakingfd")
    if mission == True:
        send("connected")
        send("missionyes")
        print "hallelujia"
    if mission == False:
        send("connected")
        print mission
    if admiralTaken == True:
        send("admiraltaken: "+admiralName)
        print "asdfjkl;"
    if engineerTaken == True:
        send("engineertaken: "+engineerName)
        print "efvrgb"
    if navigationsTaken == True:
        send("navigationstaken: " + navigationsName)
        print"abcdefghijkl"
    if tacticalTaken == True:
        send("tacticaltaken: " + tacticalName)
    if operationsTaken == True:
        send("operationstaken: " + operationsName)
    for target in transporterTargets:
        send("transportertarget: " + target)
    for system in brokenSystemList:
        send("brokensystem: " + system)
    for ship in nearbyShipList:
        send("nearbyship: " + ship)
    for phaser in phaser1:
        send("phasercharged: " + phaser)
    for message in longRangeFD:
        send("longrangemessagefd: " + message)
    for message in longRangeOPS:
        send("longrangemessageops: " + message)
    if mainReactorEject == "Yes":
        send("ejectmainreactor")
    if selfDestruct == "Yes":
        send("selfdestruct")
    else: 
        send("cancelselfdestruct")
    if navigationsBlack == True:
        send("blackout: navigations")
    if operationsBlack == True:
        send("blackout: operations")
    if tacticalBlack == True:
        send("blackout: tactical")
    if engineeringBlack == True:
        send("blackout: engineering")
    if allBlack == True:
        send("blackout:all")
    if scanningForCourse == True:
        send("coursescan: " + courseTo)
    if scanningForCourse == False:
        send("cancelcoursescan")
    if courseScanAnswered == True:
        send("precoursefd")
        send("xcoordinatefd: " + xFD)
        send("ycoordinatefd: " + yFD)
        send("zcoordinatefd: " + zFD)
    if courseSet == True:
        send("precourseset")
        send("xcoordinate: " + x)
        send("ycoordinate: " + y)
        send("zcoordinate: " + z)
        
@app.route('/')
def load():
    return render_template("index.html")

@app.route('/index.html')
def loadbackup():
    return render_template("index.html")
  
@app.route('/sound_portal.html')
def loadsoundportal():
    return render_template("sound_portal.html")

@app.route('/flight-director.html')
def loadflightdirector():
    return render_template("flight-director.html")

@app.route('/flight-director-navigations.html')
def loadflightdirectornavigations():
    return render_template("flight-director-navigations.html")

@app.route('/flight-director-operations.html')
def loadflightdirectoroperations():
    return render_template("flight-director-operations.html")

@app.route('/flight-director-tactical.html')
def loadflightdirectortactical():
    return render_template("flight-director-tactical.html")

@app.route('/flight-director-engineering.html')
def loadflightdirectorengineering():
    return render_template("flight-director-engineering.html")

@app.route('/flight-director-admiral.html')
def loadflightdirectoradmiral():
    return render_template("flight-director-admiral.html")

@app.route('/flight-director-voice.html')
def loadflightdirectorvoice():
    return render_template("flight-director-voice.html")

@app.route('/flight-director-navigations-voice.html')
def loadflightdirectornavigationsvoice():
    return render_template("flight-director-navigations-voice.html")

@app.route('/flight-director-operations-voice.html')
def loadflightdirectoroperationsvoice():
    return render_template("flight-director-operations-voice.html")

@app.route('/flight-director-tactical-voice.html')
def loadflightdirectortacticalvoice():
    return render_template("flight-director-tactical-voice.html")

@app.route('/flight-director-engineering-voice.html')
def loadflightdirectorengineeringvoice():
    return render_template("flight-director-engineering-voice.html")

@app.route('/flight-director-admiral-voice.html')
def loadflightdirectoradmiralvoice():
    return render_template("flight-director-admiral-voice.html")

@app.route('/admiral.html')
def loadadmiral():
    return render_template("admiral.html")

@app.route('/admiral-self-destruct.html')
def loadadmiralselfdestruct():
    return render_template("admiral-self-destruct.html")

@app.route('/engineer.html')
def loadengineer():
    return render_template("engineer.html")

@app.route('/engineer-distribution.html')
def loadengineerdistribution():
    return render_template("engineer-distribution.html")

@app.route('/engineer-reactor-monitoring.html')
def loadengineerreactormonitoring():
    return render_template("engineer-reactor-monitoring.html")
  
@app.route('/navigations.html')
def loadnavigations():
    return render_template("navigations.html")
  
@app.route("/navigations-speed-control.html")
def loadnavigationsspeed():
    return render_template("navigations-speed-control.html")
  
@app.route("/navigations-thrusters.html")
def loadnavigationsthrusters():
    return render_template("navigations-thrusters.html")
  
@app.route("/tactical.html")
def loadtactical():
    return render_template("tactical.html")
  
@app.route("/tactical-special-weapons-control.html")
def loadtacticalspecialweaponscontrol():
    return render_template("tactical-special-weapons-control.html")

@app.route("/tactical-onboard-security.html")
def loadtacticalonboardsecurity():
    return render_template("tactical-onboard-security.html")
  
@app.route("/operations.html")
def loadoperations():
    return render_template("operations.html")
  
@app.route("/operations-short-range-communication.html")
def loadoperationsshortrange():
    return render_template("operations-short-range-communication.html")
  
@app.route("/operations-long-range-communication.html")
def loadoperationslongrange():
    return render_template("operations-long-range-communication.html")
  
@app.route("/operations-transporter-control.html")
def loadoperationstransportercontrol():
    return render_template("operations-transporter-control.html")

if __name__ == "__main__":
    socketio.run(app, "0.0.0.0", 3000)
