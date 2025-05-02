#what is python?

friends = ['Tylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend) 


# other languages 

for i in range(10):
    print("Hello, World!")

'''
bash:
for i in {1..10}; do
    echo Hello, World!
done

PowerShell:
for ($i=1; "i -le 10; $i++){
    Write-Host "Hello, World!"
}

'''
# hello, world
name = "kay"
print( "Hi " + name)

name = 'Sandra'
print( "Hi " + name)

# Python can be ur calculator
print(((1 +2) *3)/4)

# Practice quiz
'''
Replace the ___ placeholder and calculate the Golden ratio:  
 start fraction, 1, plus, square root of, 5, end square root, divided by, 2, end fraction.

Tip: to calculate the square root of a number 
x
xx, you can use x**(1/2).
'''

ratio = ( 1+5 ** 0.5) / 2
print(ratio)

# study guide

#Assignment of values to the variables:
years = 10
weeks_in_a_year = 52
# this variable is assigned an arithmetic calculation:
weeks_in_a_decade = years * weeks_in_a_year
# prints the calculation stored in the "week_in_a_decade" acriable:
print(weeks_in_a_decade)

# module quiz
'''
The market is six miles away from your home. The school is two miles away from your home.
 Use Python to calculate how much further the market is from your home than the school (in miles). 
 Note: Your result should be in the format of a number, not a sentence.
'''
toMarket = 6
toSchool = 2
howMuchfar = toMarket - toSchool
print(howMuchfar) # should print 4

'''
Consider this scenario about using Python to make calculations:

In a managed computing environment, there are 200 remote computers that must download 200 MB (megabytes) of updates each month. There are 1024 KB (kilobytes) in each MB.

Fill in the blank in the code below to compute the number of total kilobytes downloaded by all computers from the remote update server each month. 
Multiply the total number of computers by the download size in KB to calculate. 


'''

download_size_kb = 200 * 1024
total_computers = 200
total_kbs = download_size_kb * total_computers

print(total_kbs) # should print 40960000.0