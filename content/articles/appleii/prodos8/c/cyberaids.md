Title: CyberAIDS
Date: 2026-08-20
Category: PRODOS8
Tags: file, prodos8
Preview: gallery/viruses/appleii/cyberaids1.0.png
Summary: This article is about the CyberAIDS virus...

### Details
* *Versions*: 1.0; 2.01; (also its culmination Festering Hate and subsequently Doom's Day).
* *Author*: The BOY! & Tom E. Hawk.
* *detonation conditions*: when the counter in the last byte of block 2 becomes equal to 16.
* *size*: Adds 5.5 blocks to the SYS file, for a total of 2816 bytes.

### Description
With the proliferation of computer bulletin board systems across the country during the 1980s, a number of them were dedicated to talented hackers who were interested in cracking copy-protected software. This interest sometimes extended to breaking into secure computer systems, and sometimes it even involved theft from those systems. Unlike many BBSs, which wanted as wide an exposure as possible, to attract greater and greater numbers of members, these underground hacker systems were intended to be quiet, private, and invitation-only. This was done to avoid attention, especially from authorities trying to track those who were breaking into secure systems.

The culture of these underground hacker groups was not unlike that of street gangs; the status of a hacker group member was based on the daring and impact of his exploits. The more sophisticated the copy-protection system, the more skill was required to break that protection. The hacker who was successful in cracking a piece of software also wanted to call attention to his exploits. This was usually done by including a startup screen that said something like, “Hey! Look at me! Look at what I did!”, prominently featuring the codename of the hacker or hackers (such as “The Grand Vizier” or “Ma$ter Hackr$”), and possibly the name of their group or BBS. With time, some of these hackers turned their attention to ProDOS and looked at ways not to defeat copy protection (ProDOS was unprotected), but instead at how to create a virus for it. And just like the vanity splash screens put on cracked commercial software, the virus writers wanted to let the world know who had made this virus.

It took nearly five years after the introduction of ProDOS in 1983 for someone to write a virus that targeted it. The CyberAIDS virus, which appeared in 1988, reproduced by randomly attaching itself to SYS files in the root directory of all mounted disks. The virus was sophisticated enough to bypass locked files by unlocking them first. However, write-protecting the disk would prevent the virus from being able to alter those SYS files. This virus never attacked the PRODOS file, as doing so would simply crash the system.

CyberAIDS attaches itself to system files by moving the original six bytes of the file from the beginning to the end, replacing these six bytes with a JMP to the virus and three consecutive bytes of $13, used as an identifier.

When executing a SYS file containing the CyberAIDS virus, the code jumps directly to the virus's executable code; the disk drive is turned off and then turned back on. While the disk was spinning for the second time, one part of the virus read and incremented the counter in the last byte of block 2, while the other infected one SYS file in the root directory in alphabetical order. It then returned control to the program, remaining resident in RAM. It did not look into subdirectories, and when the counter reached 16, the virus activated, erasing the directory and volume bit map and displaying this screen, smoothly moving from bottom to top:

![Screenshot of Skull Aids virus]({static}/gallery/viruses/appleii/skullaids.png)

After which the following screen appeared:

![Screenshot of Skull Aids virus]({static}/gallery/viruses/appleii/cyberaids1.0.png)

Some time later, the virus was modified by Tom E. Hawk, who increased the counter to 23, changed the detonation to overwrite blocks $0000-$0006 with zeros, and modified the detonation screen. The date 13/04/88 is Bruce Fancher's birthday.

![Screenshot of Skull Aids virus]({static}/gallery/viruses/appleii/cyberaids2.01reconstr.png)

In the magazine 2600 The Plague published a description of CyberAIDS and its structure for future virus writers.

## CyberAIDS Structure
Application Resident Virus Outline

	A. INITIALIZE.
    	1. Find current location of virus in memory.
    	2. Relocate itself to predefined memory location.
    	3. Make sure DOS is active and ready to accept system calls.
    	4. Move original application header (6 bytes) back to original memory.

	B. SEARCH.
    	1. Choose random volume (disk device). 
			a. Make sure volume is not write protected
			b. Make sure volume is on line (no I/O error)
		2. Increment disk counter (See NOTE1) and go to destroy (See NOTE2) if necessary.
		3. Check for enough space on volume.
		4. Choose candidate file.
			a. File must be a system or application file.
			b. File must not be already infected (choose appropriate method for identifying infected files).
			c. File must be small enough to allow viral attachment (so that the application and virus code both fit in memory).
			d. If the file is locked then unlock it.

	C. INFECT.
    	1. Open candidate file.
		2. Load first block of candidate file into a main.buffer.
		3. Take first (6 bytes) and save to alt.buffer (also known as SH).
		4. Calculate viral location in new file.
			a.Viral.Addr= — Application. Start.Addr + Length.of.Application + 6
		5. Store a JUMP Viral.Addr at beginning of file.
		6. Rewrite main.buffer.
		7. Set file pointer to end of file (for append).
		8. Write the alt.buff (6 bytes).
		9. Write the viral code afterwards.
		10. Close candidate file.

	D. DESTROY (Optional).
		1. Lock out Keyboard and Reset Key if possible. 
		2. Destroy data.
			a. Recognize all disk devices (hard disks, floppies, 3.5", ram).
			b. Wipe out the directory (FAT) blocks of each device.
			c. Wipe out key block for each file in each directory block.
		3. Do graphics and music (optional).
			a. Totally up to virus writer.
		4. Present text message (optional).
			a. Totally up to virus writer.

    E. LEAVE.
		1. Jump back to Application.Start.Addr
			a. Thus continue as if nothing had happened.

NOTE1: The disk counter is a particular byte on the disk that the virus uses to hold the value of how many times that virus has run with that particular disk inserted (active).  

NOTE2: DESTROY or LEAVE is executed depending on the status of the disk counter.

### Infected file structure

(a) Normal (not infected file)  
+----+---------------------+----+  
| SH | rest of application | EOF |  
+----+---------------------+----+

(b) Infected file  
+----+---------------------+----+----+-----+  
| JC | rest of application | SH | VC | EOF |  
+----+---------------------+----+----+-----+

SH = Standard Header (first few bytes of the original file's executable code).  
JC = Jump Code (jumps to the address of the virus).  
VC = Viral Code (see Virus Outline).  
EOF = End of File. 
