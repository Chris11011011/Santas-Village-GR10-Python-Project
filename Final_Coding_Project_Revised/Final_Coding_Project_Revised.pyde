add_library('minim')

def setup():
    global minim, gameScreen, star_state, christmaslights_state, canes_state, ornaments_state, presentstree_state, snowballLoaded, reloadTime, ammo, tickets #other
    global userNameBackground, mainMenuBackground, loadingScreenBackground, villageBackground, clickSE, userSong, menuSong, scoreSong, villageSong, houseSong, treeSong, snowmanSong, font, santaSleigh, santaSleighRight, tipsButton, backButton, ScenesBackground, present, treeScene, presentBoom, crosshair, star, christmaslights, canes, ornaments, presentstree, evilSnowman, snowmanScreen, snowball, gameBeep, splatter, scoreScreen, tipsScreen, checkMark, crossMark, pixelChild, bloodStain, santaMan, dreamMask, fire, houseScene, squeaky, santaAudio, eating, hiddenFace, hohoho #images/audios/fonts
    #global usernameScreen, menuScreen,scenesScreen, exitScreen, villageScreen, tipsScreen, houseScreen, treeScreen, snowmanScreen, exitScreen #scenes/functions
    global whichKey, asciList, controlKeys, nameIn, nameLimit, nameCount #Variables for usernamescreen
    global allBoundaries, validLocation, activeAreas, numAreas, removeBoundary, clickBoundary #Variables for menuScreen
    global backGroundX, backGroundY, backGroundWidth, backGroundHeight, santaWidth, santaHeight, incrSleighX, incrSleighY, santaX, santaY, rightBound, leftBound, upBound, bottomBound, currentSleigh, incrSnowballX, incrSnowballY, snowballX, snowballY, snowballHeight, snowballWidth, highScore, currentScore, incrSnowmanX, incrSnowmanY, snowmanX, snowmanY, snowmanHeight, snowmanWidth, snowBottomBound, snowUpBound #movement variables
    global dropPresent, presentX, presentY, presentWidth, presentHeight, incrPresentX, incrPresentY, subtractor #Present drop
    global fire_state, hidden_state, santa_state, maskX, maskY, maskIncrY, childX, childY, childIncrX, childIncrY, showFace, showBlood #house movement
    global winterForest, backHeight, backWidth, chunkSize, chunkIncr, chunkX, cornerPointX, cornerPointY, canvasX, canvasY #exitScreen stuff
    
    #Images/fonts/audios to load
    minim=Minim(this)
    loadingScreenBackground = loadImage("loadingScreen.jpg")
    userNameBackground = loadImage("winterforest.png")
    mainMenuBackground = loadImage("pixil-frame-0.png")
    santaSleigh = loadImage("Santawithreindeer.png")
    santaSleighRight = loadImage("Santawithreindeerright.png")
    villageBackground = loadImage("villageScreen.png")
    backButton = loadImage("backbutton.png")
    tipsButton = loadImage("tipsbutton.png")
    ScenesBackground = loadImage("sceneScreen.png")
    present = loadImage("presentimage.png")
    treeScene = loadImage("treedecorscene.png")
    presentBoom = loadImage("bigboom.png")
    crosshair = loadImage("crosshairsanta.png")
    star = loadImage("christmasstar.png")
    christmaslights = loadImage("christmaslights.png")
    canes = loadImage("canesofcandy.png")
    ornaments = loadImage("treeornaments.png")
    presentstree = loadImage("groupofpresents.png")
    evilSnowman = loadImage("evilSnowman.png")
    snowmanScreen = loadImage("snowmanscreen.png")
    snowball = loadImage("snowballimg.png")
    splatter = loadImage("splattersnow.png")
    scoreScreen = loadImage("scoreScreen.png")
    tipsScreen = loadImage("tipsScreen.png")
    checkMark = loadImage("checkMark.png")
    crossMark = loadImage("crossMark.png")
    pixelChild = loadImage("pixelChild.png")
    bloodStain = loadImage("bloodStain.png")
    santaMan = loadImage("santaman.png")
    dreamMask = loadImage("dreamMask.png")
    fire = loadImage("mcFire.png")
    houseScene = loadImage("houseScene.png")
    hiddenFace = loadImage("hiddenFace.png")
    winterForest = loadImage("winterBackground.jpg")
    
    font = loadFont("BradleyHandITC-40.vlw")
    
    clickSE = minim.loadFile("MouseSE.mp3")
    userSong = minim.loadFile("userSong.mp3")
    menuSong = minim.loadFile("menuSong.mp3")
    scoreSong = minim.loadFile("historicalv.mp3")
    villageSong = minim.loadFile("villageSong.mp3")
    houseSong = minim.loadFile("houseSong.mp3")
    treeSong = minim.loadFile("treeSong.mp3")
    snowmanSong = minim.loadFile("snowmanSong.mp3")
    gameBeep = minim.loadFile("gamebeep.mp3")
    squeaky = minim.loadFile("squeakyToy.mp3")
    santaAudio = minim.loadFile("secretSanta.mp3")
    eating = minim.loadFile("mcEating.mp3")
    hohoho = minim.loadFile("hohoho.mp3")
    
    #Universal background size
    size(1500,1000) #Canvas size
    fill(0,0,0) #Colour of canvas
    rect(0,0,1500,1000) #Shape
    image(loadingScreenBackground, 0, 0, 1500, 1000) #loading screen, but it doesn't really have a use.  In case there are delays, you'll notice a small glimpse of the loading screen.
    
    #Variables in general
    gameScreen = "usernameScreen" #Starting Screen
    
    #Variables/setup for usernamescreen
    asciList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0" #self explanatory
    controlKeys = [ UP, LEFT, DOWN, RIGHT ] #Arrow keys
    whichKey = '' #current key typed
    nameIn = "" #player username
    nameCount = 0 #Current number of characters in username
    nameLimit = 15 #Username limit
    
    
    #Variables/setup for menuScreen
    validLocation = - 1 #validlocation resetter.
    removeBoundary = False #Do not remove boundaries
    allBoundaries = [] #boundary list
    numAreas = 15 #number of buttons, but I altered depending on gameScreen !IMPORTANT! (will be re-stated before used)
    activeAreas = [ True for i in range( numAreas ) ] #amount of areas that can possibly be clicked

    #Boundaries for buttons (For reference.  Not currently active)
    
    # clickBoundary = [ ( 608, 280 ), (1011, 462 ) ] #start button "0"
    # # fill(180,180,180)
    # #image(imgDog,900,100,100,100)
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 27, 476 ), ( 378, 608 ) ] #scenes button "1"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 1232, 469 ), ( 1472, 590 ) ] #exit button "2"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 1284, 800 ), ( 1475, 893 ) ] #scores button "3"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 1275, 907 ), ( 1479, 973 ) ] #change user button "4"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 20, 500 ), ( 120, 600 ) ] #tips button "5"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 20, 850 ), ( 120, 950 ) ] #back button "6"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 200, 380 ), ( 620, 960 ) ] #house button "7"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 850, 400 ), ( 1160, 930 ) ] #tree button "8"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 1215, 600 ), ( 1500, 1000 ) ] #snowman button "9"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 325, 225 ), ( 425, 325 ) ] #special back button "10"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 365, 390 ), ( 747, 602 ) ] #village scene button "11"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 773, 387 ), ( 1131, 603 ) ] #house scene button "12"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 365, 628 ), ( 746, 846 ) ] #christmas tree scene button "13"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 771, 625 ), ( 1133, 845 ) ] #snowman scene button "14"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 19, 110 ), ( 210, 287 ) ] #tree lights button "15"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 19, 323 ), ( 210, 507 ) ] #tree candycane button "16"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 19, 548 ), ( 210, 730 ) ] #tree ornament button "17"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 1124, 0 ), ( 1500, 124 ) ] #tree reset button "18"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 1293, 208 ), ( 1475, 395 ) ] #tree star button "19"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 1293, 545 ), ( 1475, 728 ) ] #tree present button "10"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 1072, 2 ), ( 1283, 90 ) ] #house reset button "11"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 139, 526 ), ( 695, 976 ) ] #man sitting button "12"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 800, 500 ), ( 1032, 755 ) ] #fireplace button "13"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    # clickBoundary = [ ( 1145, 450 ), ( 1500, 1000 ) ] #santa interaction button "14"
    # # fill( 180,180,180 )
    # #image( imgCat,900,300,100,100 )
    # allBoundaries.append( clickBoundary )
    
    #Variables for sleigh movement 
    santaWidth = 450
    santaHeight = 200
    incrSleighX = 20
    incrSleighY = 20
    santaX = 200
    santaY = 200
    
    backGroundX = 0
    backGroundY = 0
    backGroundWidth = 1500
    backGroundHeight = 1000
    
    rightBound = 1500 #boundaries...
    bottomBound = 700
    leftBound = 0
    upBound = 0
    
    currentSleigh = santaSleighRight #to switch images when directions switch
    
    #Variables for present drops
    dropPresent = False #the toggle for when presents drop
    presentX = 0
    presentY = 120
    presentWidth = 50
    presentHeight = 50
    incrPresentX = 0
    incrPresentY = 10 #present drop speed
    subtractor = 20 #used when directions change so that the present can keep straight down
    
    #variables for tree scene (Tells us when images are active on trees)
    #star, christmaslights, canes, ornaments, presentstree
    star_state = False
    christmaslights_state = False
    canes_state = False
    ornaments_state = False
    presentstree_state = False
    
    #variables for snowman scene
    incrSnowmanX = 20
    incrSnowmanY = 20
    snowmanX = 600
    snowmanY = 400
    snowmanHeight = 300
    snowmanWidth = 200
    
    incrSnowballX = 40
    incrSnowballY = 40
    snowballX = 500
    snowballY = 500
    snowballHeight = 50
    snowballWidth = 50
    
    snowBottomBound = 850 #custom boundaries for snowman game
    snowUpBound = 160
    
    currentScore = 0 #current score
    highScore = 0 #high score (after game, if current score is greater than high score, it'll be replaced)
    snowballLoaded = False #snowball ammo toggle
    reloadTime = 0 #beggining reload time (edited to 30 later on throughout scenes)
    ammo = 0 #(current ammo ammount in the beginning)
    
    #variables for house scene
    fire_state = False #Tell us when images and things are active in house
    hidden_state = False
    santa_state = False
    showFace = False
    showBlood = False
    
    maskX = 150
    maskY = 560
    maskIncrY = 0
    
    childX = 708
    childY = 608
    childIncrX = 0
    childIncrY = 0
    
    #varibales for exitScreen
    
    backHeight = 300 #visible area being shown...
    backWidth = 600
    chunkSize = 0
    chunkIncr = 9
    chunkX = 0
    cornerPointX = 0
    cornerPointY = 0
    canvasX = 1500
    canvasY = 1000
    

    
def mouseReleased(): #for menuscreen
    global allBoundaries, validLocation, activeAreas, removeBoundary, NumAreas, clickBoundary
    
    validChoice = False
    for i in range( numAreas ): #for the amount of possible buttons in numAreas,
        if activeAreas[ i ]: #accesses these lists for the click boundaries
            validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
            validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
            validChoice = validXRange and validYRange
        if validChoice:
            validLocation = i #this is where the validLocation number assigned is created
            break 
                
    if validChoice and removeBoundary: #irrelevant for my code
        activeAreas[ i ] = False
        
def draw(): #main area where the visuals occur
    global minim, gameScreen, star_state, christmaslights_state, canes_state, ornaments_state, presentstree_state, snowballLoaded, reloadTime, ammo, tickets #other
    global userNameBackground, mainMenuBackground, loadingScreenBackground, villageBackground, clickSE, userSong, menuSong, scoreSong, villageSong, houseSong, treeSong, snowmanSong, font, santaSleigh, santaSleighRight, tipsButton, backButton, ScenesBackground, present, treeScene, presentBoom, crosshair, star, christmaslights, canes, ornaments, presentstree, evilSnowman, snowmanScreen, snowball, gameBeep, splatter, scoreScreen, tipsScreen, checkMark, crossMark, pixelChild, bloodStain, santaMan, dreamMask, fire, houseScene, squeaky, santaAudio, eating, hiddenFace, hohoho #images/audios/fonts
    #global  #scenes/functions
    global whichKey, asciList, controlKeys, nameIn, nameLimit, nameCount #Variables for usernamescreen
    global allBoundaries, validLocation, activeAreas, numAreas, removeBoundary, clickBoundary #Variables for menuScreen
    global backGroundX, backGroundY, backGroundWidth, backGroundHeight, santaWidth, santaHeight, incrSleighX, incrSleighY, santaX, santaY, rightBound, leftBound, upBound, bottomBound, currentSleigh, incrSnowballX, incrSnowballY, snowballX, snowballY, snowballHeight, snowballWidth, highScore, currentScore, incrSnowmanX, incrSnowmanY, snowmanX, snowmanY, snowmanHeight, snowmanWidth, snowBottomBound, snowUpBound #movement variables
    global dropPresent, presentX, presentY, presentWidth, presentHeight, incrPresentX, incrPresentY, subtractor#Present drop
    global fire_state, hidden_state, santa_state, maskX, maskY, maskIncrY, childX, childY, childIncrX, childIncrY, showFace, showBlood #house movement
    global winterForest, backHeight, backWidth, chunkSize, chunkIncr, chunkX, cornerPointX, cornerPointY, canvasX, canvasY #exitScreen stuff
    
    #audio rewinds
    clickSE.rewind() #rewinds the click audio so it can be replayed.  the audio file must be epaused and rewinded before it cen be replayed
    
    gameBeep.rewind() #rewinds the gamebeep for snowman game
    
    # print(validLocation) #used for testing
    # print(mouseX,mouseY)
    # print(dropPresent)
    # print(santaX, presentX)
    
    if gameScreen == "exitScreen": #exitscreen line
        
        hohoho.play() #ending audio
        
        chunkX = chunkX + chunkIncr #how the image moves forward
        if ( chunkX + chunkSize ) >= backWidth: #if it gets to a certain point, instead of resetting, I end program
            exit()
            
        copy ( winterForest,chunkX,100,backWidth, backHeight, cornerPointX, cornerPointY, canvasX, canvasY ) #the copying of image in a specififc spot
        image ( santaSleighRight, 600, 400, 400, 200 ) #santa image moving sitting on screen
            
        textFont(font, 100) #sets font and text size
        fill(200,0,0)
        text("Merry Christmas!  Goodbye!", 150, 200)#ending msg
    
    elif gameScreen == "usernameScreen": #username screen interaction #username screen line
        del allBoundaries[:] #removes all boundaries so it doesn't interfere
        numAreas = 1 
        clickBoundary = [ ( 608, 280 ), (1011, 462 ) ] #start button "0" #used so it doesn't crash due to no boundaries.  irrelevant to screen
        allBoundaries.append( clickBoundary )
        validLocation = "" #resets validLocation
        
        image(loadingScreenBackground, 0, 0, 1500, 1000)
        image(userNameBackground, 0, 0, 1500, 1000) #background screen image
        userSong.play() #song
        fill( 220,220,220 )
        rect( 350 ,200, 800, 600 ) #this is the square where the words are on
        fill( 150, 200, 200 )
        textFont( font, 40 )
        fill(0)
        text("Please enter your username...", 450, 270)
        text( "Enter your name > ", 360, 410 )
        text( nameIn, 720, 410 ) #writes your current username out
        textFont(font, 30)
        text("""Press '0' key to confirm name change""", 400, 600)
        text("Username limit is 15", 400, 700)
        
        if ( whichKey == "0" ) or ( nameCount >= nameLimit ): #0 or limit is equivalent to enter key
            clickSE.play()
            image(loadingScreenBackground, 0, 0, 1500, 1000)
            delay(1000)
            userSong.pause()
            userSong.rewind()
            gameScreen = "menuScreen"
        else: #uppercases whatever input you give to make it simpler
            if whichKey != "":
                nameIn += whichKey.upper() #Adds character to username
                nameCount += 1 #Counts number of characters in username
            
        whichKey = "" #resets whichkey so it doens't repeat
    
    elif gameScreen == "scenesScreen": #look at the above for repeated notes since I don't want to type so many things multiple times.  I will add unique notes though
        del allBoundaries[:]
        numAreas = 5
        clickBoundary = [ ( 325, 225 ), ( 425, 325 ) ] #special back button "0"

        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 365, 390 ), ( 747, 602 ) ] #village scene button "1"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 773, 387 ), ( 1131, 603 ) ] #house scene button "2"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 365, 628 ), ( 746, 846 ) ] #christmas tree scene button "3"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 771, 625 ), ( 1133, 845 ) ] #snowman scene button "4"
        allBoundaries.append( clickBoundary )
        
        image(ScenesBackground, 300, 200, 900, 700)
        image(backButton, 325, 225, 100, 100)
        
        if validLocation == 0: #special back button #if validLocation = the right value, the click boundary will activate and the things under the if statment will work
            clickSE.play() #plays click noise
            delay(1000) #you must delay or the sound wont play before it is looped over again
            gameScreen = "menuScreen" #changes gameScreen so a new image comes up
            validLocation = ""
        elif validLocation == 1: #village scene button
            clickSE.play()
            delay(1000)
            menuSong.pause()
            menuSong.rewind()
            gameScreen = "villageScreen"
            validLocation = ""
        elif validLocation == 2: #house scene button
            clickSE.play()
            delay(1000)
            menuSong.pause()
            menuSong.rewind()
            gameScreen = "houseScreen"
            validLocation = ""
        elif validLocation == 3: #village scene button
            clickSE.play()
            delay(1000)
            menuSong.pause()
            menuSong.rewind()
            gameScreen = "treeScreen"
            validLocation = ""
        elif validLocation == 4: #snowman scene button
            clickSE.play()
            delay(1000)
            currentScore = 0 #resets current score in snowman game
            menuSong.pause()
            menuSong.rewind()
            tickets = 500 #this is to reset ticket timer in the snowman game
            reloadTime = 30
            asciList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0" #restates asciilist so you can use lowercase r to reload
            gameScreen = "snowmanScreen"
            validLocation = ""
                
    elif gameScreen == "menuScreen": #main menu screen ( #look at the above for repeated notes since I don't want to type so many things multiple times.  I will add unique notes though)
        menuSong.play()
        del allBoundaries[:]
        numAreas = 5
        clickBoundary = [ ( 608, 280 ), (1011, 462 ) ] #start button "0"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 27, 476 ), ( 378, 608 ) ] #scenes button "1"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 1232, 469 ), ( 1472, 590 ) ] #exit button "2"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 1284, 800 ), ( 1475, 893 ) ] #scores button "3"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 1275, 907 ), ( 1479, 973 ) ] #change user button "4"
        allBoundaries.append( clickBoundary )
        
        rect(0,0,1500,1000)
        fill(0,0,0)
        image(mainMenuBackground, 0, 0, 1500, 1000)
        textFont( font, 80 )
        fill(255,255,255)
        text("Welcome:  " + nameIn, 350, 700)
        
        santaX += incrSleighX #x axis movement #states the increase of santa positions X & Y
        santaY += incrSleighY #y axis movement
        
        
        if santaX > rightBound - santaWidth: #border refelectors
            santaX = rightBound - santaWidth #calculates the pixels where the image must turn around
            incrSleighX = -incrSleighX #makes the direction go negative always making it go the other way
            currentSleigh = santaSleigh #switches image to the one facing left when reflected
        elif santaX < leftBound:
            santaX = leftBound
            incrSleighX = -incrSleighX
            currentSleigh = santaSleighRight #switches to image facing right when reflected
            
        if santaY > bottomBound - santaHeight:
            santaY = bottomBound - santaHeight
            incrSleighY = -incrSleighY
        elif santaY < upBound:
            santaY = upBound
            incrSleighY = -incrSleighY
            
        image(currentSleigh, santaX, santaY, santaWidth, santaHeight) #shows the new updated image every time
        
        if validLocation == 0: #Start button
            clickSE.play()
            image(loadingScreenBackground, 0, 0, 1500, 1000)
            delay(1000)
            menuSong.pause()
            menuSong.rewind()
            gameScreen = "villageScreen"
            validLocation = ""
        elif validLocation == 1: #Scenes button
            clickSE.play()
            delay(1000)
            gameScreen = "scenesScreen"
            validLocation = ""
        elif validLocation == 2: #Exit button
            clickSE.play()
            image(loadingScreenBackground, 0, 0, 1500, 1000)
            delay(1000)
            menuSong.pause()
            menuSong.rewind()
            gameScreen = "exitScreen"
            validLocation = ""
        elif validLocation == 3: #Scores button
            clickSE.play()
            delay(1000)
            menuSong.pause()
            menuSong.rewind()
            gameScreen = "scoresScreen"
            validLocation = ""
        elif validLocation == 4: #Username Screen
            clickSE.play()
            nameIn = ""
            nameCount = 0
            image(loadingScreenBackground, 0, 0, 1500, 1000)
            delay(1000)
            asciList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0" #restates the ascii list for username screen
            menuSong.pause()
            menuSong.rewind()
            gameScreen = "usernameScreen"
            validLocation = ""
            
        validLocation = - 1 #resets the validLocation just like the validLocation = "".  I just forgot to add this and found it as I was writing these notes....  All these validLocation = "" could have beeen summed up by this
    
    elif gameScreen == "villageScreen":
        villageSong.play()
        del allBoundaries[:]
        numAreas = 5
        clickBoundary = [ ( 20, 500 ), ( 120, 600 ) ] #tips button "0"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 20, 850 ), ( 120, 950 ) ] #back button "1"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 200, 380 ), ( 620, 960 ) ] #house button "2"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 850, 400 ), ( 1160, 930 ) ] #tree button "3"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 1215, 600 ), ( 1500, 1000 ) ] #snowman button "4"
        allBoundaries.append( clickBoundary )
        
        rect(0,0,1500,1000)
        fill(100,0,0)
        image(villageBackground, 0, 0, 1500, 1000)
        textFont(font, 60)
        fill(255,0,0)
        text("Welcome to the village " + nameIn + "!", 100, 100)
        asciList = [ 'a', 's', 'w', 'd', TAB, ENTER, BACKSPACE, " " ]
        
        if star_state == True: #this shows the saved settings you had in the christmas tree layout so it displays on the village screen at set cords
            image(star, 980, 510, 50, 50)
            
        if christmaslights_state == True:
            image(christmaslights, 950, 650, 120, 100)
            
        if canes_state == True:
            image(canes, 920, 800, 70, 50)
            
        if ornaments_state == True:
            image(ornaments, 1020, 800, 70, 50)
            
        if presentstree_state == True:
            image(presentstree, 910, 890, 200, 100 )
        
        if whichKey == " ":
            dropPresent = True
        
        whichKey = "" #resets whichkey so it doesn;t auto repeat
        
        santaY = 100 #Y axis stays still for santa at the set height of 100
        santaX += incrSleighX
        
        if santaX > rightBound - santaWidth: #border reflector
            santaX = rightBound - santaWidth
            incrSleighX = -incrSleighX
            currentSleigh = santaSleigh
        elif santaX < leftBound:
            santaX = leftBound
            incrSleighX = -incrSleighX
            currentSleigh = santaSleighRight
            
        presentX = santaX #states presentX
        
        if showBlood == True: #if this is true from the house scene.  It will show the stained blood on window if you had the child get eaten by the evil snata no witness man
            image(bloodStain, 387, 867, 60, 60)
        
        image(crosshair, santaX - 40, 900, 100, 100)
        image(currentSleigh, santaX, santaY, santaWidth, santaHeight)
        image(tipsButton, 20, 500, 100, 100)
        image(backButton, 20, 850, 100, 100)
        
                
        if dropPresent == True: #if the drop present is true which is activated by the SPACEBAR being pressed, it will allow the process to continue
            if presentY >= 950: #if it's greater than 950, it'll shut down and reset
                # print(presentX, presentY)
                # print("yee")
                presentY = 120
                subtractor = 0
                dropPresent = False
                
            elif presentY < 950: #if it's smaller than 950, it'll fall down in a somewhat centered, but straight pattern
                # presentX = santaX #x axis movement  (X STAYS STILL)
                presentY += incrPresentY #y axis movement 
                
                if currentSleigh == santaSleigh: #due to the change in direction, you need this to even out the drop!!!!! SUPER DUPER IMPORTANT
                    subtractor -= 20 # 20 is based off santaX's increment speed for the sleigh
                elif currentSleigh == santaSleighRight: #this is mirrored here to keep the drop centered as much as possible.
                    subtractor += 20
                
                presentX = presentX - subtractor #essentially keep presentX in the same spot without drifting off
            
            image(present, presentX, presentY, presentWidth, presentHeight)
            
            if presentY >= 950:
                presentX = presentX - 140
                image(presentBoom, presentX, 760, 400, 300) #boom goes the present
        
        if validLocation == 0: #tips button
            clickSE.play()
            delay(1000)
            villageSong.pause()
            villageSong.rewind()
            gameScreen = "tipsScreen"
            validLocation = ""
        elif validLocation == 1:#back button
            clickSE.play()
            image(loadingScreenBackground, 0, 0, 1500, 1000)
            delay(1000)
            villageSong.pause()
            villageSong.rewind()
            gameScreen = "menuScreen"
            validLocation = ""
        elif validLocation == 2: #house interaction
            clickSE.play()
            image(loadingScreenBackground, 0, 0, 1500, 1000)
            delay(1000)
            villageSong.pause()
            villageSong.rewind()
            gameScreen = "houseScreen"
            validLocation = ""
        elif validLocation == 3: #tree interaction
            clickSE.play()
            image(loadingScreenBackground, 0, 0, 1500, 1000)
            delay(1000)
            villageSong.pause()
            villageSong.rewind()
            gameScreen = "treeScreen"
            validLocation = ""
        elif validLocation == 4: #snowman interaction
            clickSE.play()
            image(loadingScreenBackground, 0, 0, 1500, 1000)
            currentScore = 0
            delay(1000)
            villageSong.pause()
            villageSong.rewind()
            tickets = 500
            asciList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0"
            reloadTime = 30
            gameScreen = "snowmanScreen"
            validLocation = ""
            
    elif gameScreen == "tipsScreen": #look at the above for repeated notes since I don't want to type so many things multiple times.  I will add unique notes though
        del allBoundaries[:]
        numAreas = 1
        
        clickBoundary = [ ( 325, 225 ), ( 425, 325 ) ] #special back button "0"
        # fill( 180,180,180 )
        #image( imgCat,900,300,100,100 )
        allBoundaries.append( clickBoundary )
        
        image(tipsScreen, 300, 200, 900, 700) #tips screen with pre drawn notes
        image(backButton, 325, 225, 100, 100)
        
        if validLocation == 0: #special back button
            clickSE.play()
            delay(1000)
            gameScreen = "villageScreen"
            validLocation = ""
            
    elif gameScreen == "houseScreen":  #look at the above for repeated notes since I don't want to type so many things multiple times.  I will add unique notes though
        houseSong.play
        del allBoundaries[:]
        numAreas = 5
        clickBoundary = [ ( 20, 850 ), ( 120, 950 ) ] #back button "0"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 1072, 2 ), ( 1283, 90 ) ] #house reset button "1"
        allBoundaries.append( clickBoundary )
    
        clickBoundary = [ ( 139, 526 ), ( 695, 976 ) ] #man sitting button "2"
        allBoundaries.append( clickBoundary )
    
        clickBoundary = [ ( 800, 500 ), ( 1032, 755 ) ] #fireplace button "3"
        allBoundaries.append( clickBoundary )
    
        clickBoundary = [ ( 1145, 450 ), ( 1500, 1000 ) ] #santa interaction button "4"
        allBoundaries.append( clickBoundary )
        
        rect(0,0,1500,1000)
        fill(100,0,0)
        image(houseScene, 0, 0, 1500, 1000)
        textFont(font, 60)
        fill(255,0,0)
        text("Look around the house!", 100, 80)
        
        image(backButton, 20, 850, 100, 100)
        
        if validLocation == 0: #back button
            clickSE.play()
            image(loadingScreenBackground, 0, 0, 1500, 1000)
            delay(1000)
            houseSong.pause()
            houseSong.rewind()
            gameScreen = "villageScreen"
            validLocation = ""
        elif validLocation == 1:#house reset button
            clickSE.play()
            delay(1000)
            fire_state = False #resets all of the states...
            hidden_state = False
            santa_state = False
            showFace = False
            showBlood = False
            squeaky.pause()
            squeaky.rewind()
            santaAudio.pause()
            santaAudio.rewind()
            eating.pause()
            eating.rewind()
            maskX = 150
            maskY = 560
            childX = 708
            childY = 608
            validLocation = ""
        elif validLocation == 2: #doggo button
            clickSE.play()
            delay(1000)
            hidden_state = True
            validLocation = ""
        elif validLocation == 3: #fireplace button
            clickSE.play()
            delay(1000)
            fire_state = True
            validLocation = ""
        elif validLocation == 4: #santa button
            clickSE.play()
            delay(1000)
            santa_state = True
            validLocation = ""
            
        if fire_state == True:
            image(fire, 855, 597, 150, 150) #shows the fire in fireplace
            
        if hidden_state == True: #if true, this will lead the events in which the mask moves down and deploys the mystery face
            squeaky.play()
            maskY += maskIncrY
            showFace = True
            if maskY < 899:
                maskIncrY = 15 #gives incentive for mask origin to move down
            else:
                maskIncrY = 0 #resets movement so it doesn't keep going down
                
        if showFace == True:        
            image(hiddenFace, 150, 565, 100, 100) #shows hidden face
        
        if santa_state == True: #shows the evil santa guy interacting with child
            santaAudio.play()
            childX += childIncrX
            if childX < 1050:
                childIncrX = 9
            elif childX > 1050:
                childIncrX = 0
                childY -= childIncrY
                if childY > 300:
                    childIncrY = 19
                elif childY < 300:
                    childIncrY = 0
                    delay(300)
                    if childX < 1150:
                        childIncrX = 100
                    elif childX > 1150:
                        childIncrX = 0
                        eating.play()
                        delay(2000)
                        showBlood = True
            
        image(dreamMask, maskX, maskY, 100, 100)
        image(pixelChild, childX, childY, 500, 400)
        image(santaMan, 1250, 300, 300, 700)
        
        if showBlood == True: #stains carpet right after child is eaten...
            image(bloodStain, 1215, 815, 200, 200)
            santa_state = False
        
    elif gameScreen == "treeScreen": #look at the above for repeated notes since I don't want to type so many things multiple times.  I will add unique notes though
        treeSong.play()
        del allBoundaries[:]
        numAreas = 7
        clickBoundary = [ ( 20, 850 ), ( 120, 950 ) ] #back button "0"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 19, 110 ), ( 210, 287 ) ] #tree lights button "1"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 19, 548 ), ( 210, 730 ) ] #tree ornament button "2"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 19, 323 ), ( 210, 507 ) ] #tree candycane button "3"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 1124, 0 ), ( 1500, 124 ) ] #tree reset button "4"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 1293, 208 ), ( 1475, 395 ) ] #tree star button "5"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( 1293, 545 ), ( 1475, 728 ) ] #tree present button "6"
        allBoundaries.append( clickBoundary )
        
        rect(0,0,1500,1000)
        fill(100,0,0)
        image(treeScene, 0, 0, 1500, 1000)
        textFont(font, 60)
        fill(255,0,0)
        text("Help design the tree!", 80, 60)
        
        image(backButton, 20, 850, 100, 100)
        
        if validLocation == 0: #back button
            clickSE.play()
            image(loadingScreenBackground, 0, 0, 1500, 1000)
            delay(1000)
            treeSong.pause()
            treeSong.rewind()
            gameScreen = "villageScreen"
            validLocation = ""
        elif validLocation == 1:#lights button
            clickSE.play()
            delay(1000)
            christmaslights_state = True
            validLocation = ""
        elif validLocation == 2: #ornament button
            clickSE.play()
            delay(1000)
            ornaments_state = True
            validLocation = ""
        elif validLocation == 3: #candycane button
            clickSE.play()
            delay(1000)
            canes_state = True
            validLocation = ""
        elif validLocation == 4: #reset tree button
            clickSE.play()
            delay(1000)
            star_state = False
            christmaslights_state = False
            canes_state = False
            ornaments_state = False
            presentstree_state = False
            validLocation = ""
        elif validLocation == 5: #star button
            clickSE.play()
            delay(1000)
            star_state = True
            validLocation = ""
        elif validLocation == 6: #present button
            clickSE.play()
            delay(1000)
            presentstree_state = True
            validLocation = ""
        
        if star_state == True: #if the buttons are clicked and these are set to TRUE, the images will show on the tree as well as in the village
            image(star, 710, 10, 100, 100)
            
        if christmaslights_state == True:
            image(christmaslights, 620, 200, 300, 400)
            
        if canes_state == True:
            image(canes,550, 600, 200, 100)
            
        if ornaments_state == True:
            image(ornaments, 800, 600, 200, 150)
            
        if presentstree_state == True:
            image(presentstree, 500, 820, 500, 170 )
        
    elif gameScreen == "snowmanScreen":  #look at the above for repeated notes since I don't want to type so many things multiple times.  I will add unique notes though
        snowmanSong.play()
        del allBoundaries[:]
        numAreas = 5
        
        clickBoundary = [ ( 20, 850 ), ( 120, 950 ) ] #back button "0"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( snowmanX + 80, snowmanY + 50 ), ( snowmanX + 130, snowmanY + 100 ) ] #snowman head button "1"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( snowmanX + 70, snowmanY + 115 ), ( snowmanX + 140, snowmanY + 185 ) ] #snowman middle button "2"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( snowmanX + 50, snowmanY + 185 ), ( snowmanX + 150, snowmanY + 305 ) ] #snowman bottom button "3"
        allBoundaries.append( clickBoundary )
        
        clickBoundary = [ ( snowballX + 10, snowballY + 10 ), ( snowballX + 30, snowballY +30 ) ] #snowball button "4"
        allBoundaries.append( clickBoundary )
        
        if validLocation == 0: #back button
            clickSE.play()
            image(loadingScreenBackground, 0, 0, 1500, 1000)
            delay(1000)
            snowmanSong.pause()
            snowmanSong.rewind()
            gameScreen = "villageScreen"
            validLocation = ""
        
        if tickets > 0: #if the tickets(basically the timer) are greater than 0, the game will be played normally
            tickets -= 1
        
            #for reference:
            # incrSnowmanX = 20
            # incrSnowmanY = 20
            # snowmanX = 600
            # snowmanY = 400
            # snowmanHeight = 300
            # snowmanWidth = 200
            
            # incrSnowballX = 40
            # incrSnowballY = 40
            # snowballX = 500
            # snowballY = 500
            # snowballHeight = 50
            # snowballWidth = 50
            
            # snowBottomBound = 999
            # snowUpBound = 160
            
            # currentScore = 0
            # highScore = 0
            
            rect(0,0,1500,1000)
            fill(100,0,0)
            image(snowmanScreen, 0, 0, 1500, 1000)
            textFont(font, 40)
            fill(255,0,0)
            text("Get as many hits on the snowman as you can!", 620, 50)
            textFont(font, 25)
            text("Head = +40pt / Middle = +20pt / Bottom = +10pt / Snowball = +200 Tickets", 620, 100)
                        
            snowmanX += incrSnowmanX #x axis movement
            snowmanY += incrSnowmanY #y axis movement
            
            if snowmanX > rightBound - snowmanWidth: #border refelectors
                snowmanX = rightBound - snowmanWidth
                incrSnowmanX = -incrSnowmanX
            elif snowmanX < leftBound:
                snowmanX = leftBound
                incrSnowmanX = -incrSnowmanX
                
            if snowmanY > snowBottomBound - snowmanHeight:
                snowmanY = snowBottomBound - snowmanHeight
                incrSnowmanY = -incrSnowmanY
            elif snowmanY < snowUpBound:
                snowmanY = snowUpBound
                incrSnowmanY = -incrSnowmanY
                
            image(evilSnowman, snowmanX, snowmanY, snowmanWidth, snowmanHeight)
            
            snowballX += incrSnowballX #x axis movement for snowball
            snowballY += incrSnowballY #y axis movement for snowball
            
            if snowballX > rightBound - snowballWidth: #border refelectors
                snowballX = rightBound - snowballWidth
                incrSnowballX = -incrSnowballX
            elif snowballX < leftBound:
                snowballX = leftBound
                incrSnowballX = -incrSnowballX
                
            if snowballY > snowBottomBound - snowballHeight:
                snowballY = snowBottomBound - snowballHeight
                incrSnowballY = -incrSnowballY
            elif snowballY < snowUpBound:
                snowballY = snowUpBound
                incrSnowballY = -incrSnowballY
                
            image(snowball, snowballX, snowballY, snowballWidth, snowballHeight)
            image(backButton, 20, 850, 100, 100)
            
            if snowballLoaded == True:
                ammo = 1 #gives you one ammo to be shown
                if validLocation == 1:#head button
                    gameBeep.play()
                    textFont(font, 50)
                    text("+40pt!", snowmanX, snowmanY - 70) #A little point image will show up near snowman
                    image(splatter, snowmanX + 80, snowmanY + 50, 50, 50)
                    currentScore = currentScore + 40 #adds to your current score
                    snowballLoaded = False #tells us that the snowball is no longer loaded so you can't shoot anymore
                    reloadTime = 30
                    delay(500)
                    gameBeep.pause()
                    validLocation = ""
                elif validLocation == 2:#middle button
                    gameBeep.play()
                    textFont(font, 50)
                    text("+20pt!", snowmanX, snowmanY - 70)
                    image(splatter, snowmanX + 70, snowmanY + 115, 70, 70)
                    currentScore = currentScore + 20
                    snowballLoaded = False
                    reloadTime = 30
                    delay(500)
                    gameBeep.pause()
                    validLocation = ""
                elif validLocation == 3:#bottom button
                    gameBeep.play()
                    textFont(font, 50)
                    text("+10pt!", snowmanX, snowmanY - 70)
                    image(splatter, snowmanX + 50, snowmanY + 185, 100, 120)
                    currentScore = currentScore + 10
                    snowballLoaded = False
                    reloadTime = 30
                    delay(500)
                    gameBeep.pause()
                    validLocation = ""
                elif validLocation == 4:#snowball button
                    gameBeep.play()
                    textFont(font, 50)
                    text("+200tickets!", snowballX + 200, snowballY - 70)
                    tickets += 200
                    image(splatter, snowballX, snowballY, 50, 50)
                    snowballLoaded = False
                    reloadTime = 30
                    delay(500)
                    gameBeep.pause()
                    validLocation = ""
            elif snowballLoaded == False: #if you're out of anowballs to shoot, it'll show you how to reload here
                validLocation = ""
                ammo = 0
                textFont(font, 40)
                fill(255, 255, 255)
                text("Press 'r' to reload!", 200, 900)
                if whichKey == "r":
                    textFont(font, 40)
                    fill(255,255,255)
                    text("Reloading... " + str(reloadTime), 650, 900)     # reloading text when you press r to reload.  displays cooldown
                    reloadTime -= 1 #cooldown subtractor for reload
                    if reloadTime <= 0: #once the cooldown is done, it'll give you another snowball that's loaded
                        snowballLoaded = True
                        whichKey = ""
                    
            textFont(font, 100)
            fill(255, 255, 255)
            text(str(ammo) + " / 1", 960, 920)       #shows ammo loaded out of 1
            fill(200, 0, 0)
            textFont(font, 40)
            text("Your Score:", 20, 50)
            text("Your Tickets:", 320, 50)
            textFont(font,60)
            text(currentScore, 20, 110)
            text(tickets, 320, 110)
            
        if tickets == 0: #when the tickets run out, it'll bring you to this which is written over old one.  NOTE: THIS IS THE SECOND IF STATEMENT ON THE SNOWMAN SCREEN.  It's parallel to the "if tickets are greater than 0"
            if currentScore > highScore: #executes the following if your currentscore is higher than the high score
                highScore = currentScore #replaces high score
                textFont(font, 60)
                fill(255,255,255)
                text("NEW BEST!", 600, 700) #says new best only if you get high score
            textFont(font, 100)
            fill(200, 0, 0)
            text("GAME OVER", 500, 400) #basic gameover and score displays
            textFont(font, 60)
            fill(255,255,255)
            text("Your Score:             High Score:", 400, 500)
            text(str(currentScore) + "                         " + str(highScore), 450, 600)
            
    elif gameScreen == "scoresScreen":
        scoreSong.play()
        del allBoundaries[:]
        numAreas = 1
        
        clickBoundary = [ ( 325, 225 ), ( 425, 325 ) ] #special back button "0"
        allBoundaries.append( clickBoundary )
        
        image(scoreScreen, 300, 200, 900, 700)
        image(backButton, 325, 225, 100, 100)
        
        if star_state == True:                   #this shows whether or not a checkmark or Xmark will be shown depending on which decorations are currently on the tree
            image(checkMark, 886, 460, 40, 40)
        elif star_state == False:
            image(crossMark, 886, 460, 40, 40)
            
        if presentstree_state == True:
            image(checkMark, 932, 522, 40, 40)
        elif presentstree_state == False:
            image(crossMark, 932, 522, 40, 40)
            
        if christmaslights_state == True:
            image(checkMark, 902, 588, 40, 40)
        elif christmaslights_state == False:
            image(crossMark, 902, 588, 40, 40)
            
        if ornaments_state == True:
            image(checkMark, 943, 650, 40, 40)
        elif ornaments_state == False:
            image(crossMark, 943, 650, 40, 40)
            
        if canes_state == True:
            image(checkMark, 957, 715, 40, 40)
        elif canes_state == False:
            image(crossMark, 957, 715, 40, 40)
            
        textFont(font, 100)
        fill(200,0,0)
        text(currentScore, 420, 620)
        text(highScore, 420, 800)
        
        if validLocation == 0: #special back button
            clickSE.play()
            scoreSong.pause()
            scoreSong.rewind()
            delay(1000)
            gameScreen = "menuScreen"
            validLocation = ""
            
def keyReleased(): #defines the whichkey stuff.  very important for the interaction with keys section
    global whichKey, asciList, controlKeys
    if key == CODED: #if the key pressed is logged down in python...
       if keyCode in controlKeys: #if the control keys (controlList)...
        whichKey = keyCode #whichKey will equal those
    elif key in asciList: #if they key pressed is in ascii list, then it'll be considered the new whichkey until reset by whichKey = ""
        whichKey = key 
    else:
        whichKey = '' #if anything lese, it will reset the key pressed so it doesn't give you nonsense
        
#This is the end of the beginning...
