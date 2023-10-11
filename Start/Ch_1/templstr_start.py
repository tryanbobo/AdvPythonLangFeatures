# Example file for Advanced Python: Language Features by Joe Marini
# demonstrate template string functions
from string import Template

# Usual string formatting with f-strings
str1 = "Advanced Python: Language Features"
str2 = "Joe Marini"
outputstr = f"You're watching {str1} by {str2}"
print(outputstr)

# TODO: create a template with placeholders
templ = Template("You're watching ${title} by ${author}")


# TODO: use the substitute method with keyword arguments
str2 = templ.substitute(title="Advanced Python...",
                        author="Ryan Bobobobo")
print(str2)
# TODO: use the substitute method with a dictionary
data = {
    "author": "Ryan Bobo",
    "title": "Some title that really draws people in"
}
str3 = templ.substitute(data)
print(str3)

####test####
x = 34
while (x := x-1.5) > 6:
    print(int(x), end=",")