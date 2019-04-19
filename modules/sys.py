import sys
sys.path.append('/home/roopam/Desktop/Python/Basics')
import module1      #Also from module1 import * better
module1.testFn()

#First video Youtube

# sys.stderr.write('Stderr Error\n')
# sys.stderr.flush()
# sys.stdout.write('Stdout error\n')

# print(sys.argv)
# if len(sys.argv) > 1:
#     print(sys.argv[1])

# #Function that takes an argument from the command line.
# def main(arg):
#     print('The argument passed from command line is', arg)

# main(sys.argv[1])


#2nd video
print(sys.version)          #Tells the environment you're on(Python version)
print(sys.copyright)
print(sys.executable)
print(sys.builtin_module_names)
print(sys.builtin_module_names[-5])

#3rd video

print('module1' in sys.modules) #Returns true if a created module is actually imported in our script or not.
print(sys.platform)

exit(1) #You can also do sys.exit(1) to specify a particular exit code as per your requirement.