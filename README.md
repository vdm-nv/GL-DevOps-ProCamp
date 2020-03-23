Description
Python script which prints basic information about Linux OS to console.

The script should accept a single parameter to specify which metrics set to print:
    cpu - prints CPU metrics
    mem - prints RAM metrics
		
Requirements:
 - python 3
 - pip
 - psutil

Installation:
pip install psutil

Examples:
python metrics.py cpu
####################CPU####################
system.cpu.idle 27836.91
system.cpu.user 20.1
system.cpu.guest 0.0
system.cpu.iowait 106.13
system.cpu.stolen 0.0
system.cpu.system 25.23
###########################################

python metrics.py mem
####################MEMORY####################
virtual total 2082521088
virtual used 286105600
virtual free 1484484608
virtual shared 9531392
swap total 2144333824
swap used 0
swap free 2144333824
##############################################




