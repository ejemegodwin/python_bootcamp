# Example - and
age = 20 #12
has_id = True

if age >= 18 and has_id:
    print("Access Granted")
else:
    print("Access Denied")

# or
is_admin = False
is_owner = True

if is_admin or is_owner:
    print("You can edit this file.")

# not
is_logged_in = False

if not is_logged_in:
    print("Please log in.")

# Exercise 
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can Enter")
else:
    print("You cannot Enter")

is_admin = False
is_owner = True

if is_admin or is_owner:
    print("You can edit this file")