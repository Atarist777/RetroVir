Title: Load Runner
Date: 2026-08-20
Category: P16-IIGS
Tags: bootvir, prodos16, appleiigs
Preview: gallery/viruses/appleii/loadrunnerscr2.png
Summary: This article is about the Load Runner virus...

### Details
* *infects*: bootblock, bank $E1 in memory.
* *Authors*: SUPER HACKER & SHYRKAN
* *detonation conditions:* 
* *size:* 1024 bytes (0-1 blocks).

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
