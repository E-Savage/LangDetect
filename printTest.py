ascii_art = """\
 (                                             (                                       
 )\\ )                                          )\\ )          )           )             
(()/(    )       (  (    (     ) (  (    (    (()/(    (  ( /(  (     ( /((   )     (  
 /(_))( /(  (    )\\))(  ))\\ ( /( )\\))(  ))\\    /(_))  ))\\ )\\())))\\ (  )\\())\\ /((   ))\\ 
(_))  )(_)) )\\ )((_))\\ /((_))(_)|(_))\\ /((_)  (_))_  /((_|_))//((_))\\(_))((_|_))\\ /((_)
| |  ((_)_ _(_/( (()(_|_))(((_)_ (()(_|_))     |   \\(_)) | |_(_)) ((_) |_ (_))((_|_))  
| |__/ _` | ' \\)) _` || || / _` / _` |/ -_)    | |) / -_)|  _/ -_) _||  _|| \\ V // -_) 
|____\\__,_|_||_|\\__, | \\_,_\\__,_\\__, |\\___|    |___/\\___| \\__\\___\\__| \\__||_|\\_/ \\___| 
                |___/           |___/                                                 
"""

# Split the ASCII art into rows based on newline characters
rows = ascii_art.strip().split('\n')

# Create a 2D list using list comprehension
# Convert each row into a list of characters
two_d_list = [list(row) for row in rows]

# Print the resulting 2D list
for row in two_d_list:
    for char in row:
        print(char, end="")
