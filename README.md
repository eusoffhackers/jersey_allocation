# Jersey Allocation Automation
This repo contains the jersey allocation scripts, developed by Eusoff Hackers for use by Eusoff SMC. The objective of this script is to reduce the time cost and error rate of the annual jersey allocation process in Eusoff.

This process can be structured into two independent scripts - the normalization.py & smart_allocation.py scripts. The normalization.py script simply calculates the points for each sportsman (you will have to add in the wave number column yourself) and the smart_allocation.py script would allocate the jersey numbers.

## Getting Started
To begin, simply open up your local command line (Windows) or Terminal (Mac). Some simple commands on Command line can be found here: https://arian-celina.com/windows-cmd-macos-terminal-navigation/

### Prerequisites
You will need to install Git onto your computer following which you can copy the files from the repository into your local machine. (Copy and paste, but fancier).

1. Navigate to the folder on your personal computer on which you would like to store the folder with the scripts via Cmd/Terminal

Common Commands (Mac):
```
ls
cd [path to folder]
cd ..
```

Common Commands (Windows):
```
dir
cd [path to folder]
cd..
```

2. Type this into your Cmd/Terminal (each line is followed by the enter/return key):
```
git init
git clone https://github.com/eusoffhackers/jersey_allocation.git
```

Tadah! The folder is now on your computer! Good job.

## Running the Scripts
### Normalization Script

In order to run the script, simply type in the following commands:
```
python normalization.py
```

It will prompt you to name the output file, for now, just do the following:
```
Enter the output file name :SMC_test_output.csv
```

You should see a CSV file being created on your local computer with all the points calculated!

### Allocation Script
1. Copy the output csv of the Normalization Script into the `allocation` folder
```
cp SMC_test_output.csv allocation
```
Or just drag the file over on your computer

2. Change the working directory to the `allocation` folder using the cd command

3. In order to run the script, simply type in the following commands:
```
python smart-allocation.py
```
and follow the instructions on the terminal!

Notes: 
-2 means that you should deconflict. 
-1 means either the person's number is affected by a -2 or the person's numbers are all taken
So fix the -2s first before running the script again!

REMEMBER!!! Always run the script in waves! And if things go wrong, you can always restart (:



