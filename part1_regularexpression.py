import re
import urllib.request
 
# regular expression that can find all amounts of money in a text
# regular expression:
# [\$|\£|\€]{0,1}\d+,?\.?\d+[mb]{0,1}[n]{0,1}[p|\$|\£|\€]{0,1}[^%]
def is_money(string):
    regex = r'[\$|\£|\€]{0,1}\d+,?\.?\d+[mb]{0,1}[n]{0,1}[p|\$|\£|\€]{0,1}[^%]'
    return re.findall(regex,string,re.UNICODE)


# regular expression that can matching all phone numbers listed below
# regular expression:
# ^[+]?[0-9]?[\s.-]?\(?([0-9]{3})?\)?[\s.-]?[0-9]{3}[\s.-]?[0-9]{4}[0-9]?$
def is_phone_number(string):
    regex = r"^[+]?[0-9]?[\s.-]?\(?([0-9]{3})?\)?[\s.-]?[0-9]{3}[\s.-]?[0-9]{4}[0-9]?$"
    return re.search(regex, string)

# extract text from the web page
response = urllib.request.urlopen('https://www.bbc.com/news/business-41779341')
html = response.read()
z_data=str(html.decode('UTF-8'))
#print(z_data)

#chech money
print()
print("chech money --------------- ")
string = "for 3.8% example £50,000 and £117.3m 30p, 500m euro, 338bn euros, $15bn and $92.88 "
#string = z_data
string = string.replace('USD', '$') #
string = string.replace('pound', '£') #
string = string.replace('euro', '€') #
string = string.replace(' ', '') #remove spaces
new = is_money(string)
#new = re.findall(r'[\$|\£|\€]{0,1}\d+,?\.?\d+[mb]{0,1}[n]{0,1}[p|\$|\£|\€]{0,1}[^%]',string,re.UNICODE)
for prices in new:
    print(prices[:-1])



#chech phone number
print()
print("chech phone number --------------- ")

string = "555.123.4565"
flag = is_phone_number(string)
print(string + "\t\t" + str(flag))

string = "+1-(800)-545-2468"
flag = is_phone_number(string)
print(string + "\t" + str(flag))

string = "2-(800)-545-2468"
flag = is_phone_number(string)
print(string + "\t" + str(flag))

string = "3-800-545-2468"
flag = is_phone_number(string)
print(string + "\t\t" + str(flag))

string = "555-123-3456"
flag = is_phone_number(string)
print(string + "\t\t" + str(flag))

string = "555 222 3342"
flag = is_phone_number(string)
print(string + "\t\t" + str(flag))

string = "(234) 234 2442"
flag = is_phone_number(string)
print(string + "\t\t" + str(flag))

string = "(243)-234-2342"
flag = is_phone_number(string)
print(string + "\t\t" + str(flag))

string = "1234567890"
flag = is_phone_number(string)
print(string + "\t\t" + str(flag))

string = "123.456.7890"
flag = is_phone_number(string)
print(string + "\t\t" + str(flag))

string = "123.4567"
flag = is_phone_number(string)
print(string + "\t\t" + str(flag))

string = "123-4567"
flag = is_phone_number(string)
print(string + "\t\t" + str(flag))

string = "1234567900"
flag = is_phone_number(string)
print(string + "\t\t" + str(flag))

string = "12345678900"
flag = is_phone_number(string)
print(string + "\t\t" + str(flag))
