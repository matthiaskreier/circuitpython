# this is the first file to be executed after startup

#target = "apps/drive1.py"

print("Opening {}".format(target))
exec(open(target).read())
