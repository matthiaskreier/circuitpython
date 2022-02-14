# this is the first file to be executed after startup

# let's point to another file (easier to change)
#target = "apps/helloworld.py"
target = "apps/boot_blink_post.py"
#target = "apps/led4.py"
#target = "apps/pinmap.py"
#target = "apps/prime.py"
#target = "rvr/drive1.py"

print("Opening {0}".format(target))
exec(open(target).read())
