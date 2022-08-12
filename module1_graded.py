#Most hard drives are divided into sectors of 512 bytes each. Our disk has a size of 16 GB. Fill in the blank to calculate how many sectors the disk has. Note: Your result should be in the format of just a number, not a sentence.
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size / sector_size

print(sector_amount)


#Use Python to calculate how many different passwords can be formed with 6 lower case English letters.  For a 1 letter password, there would be 26 possibilities.  For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities.  Using this information, print the amount of possible passwords that can be formed with 6 letters.

letter = 6
print(26**letter)
