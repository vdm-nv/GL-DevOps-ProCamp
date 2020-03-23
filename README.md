# Description
Python script which prints basic information about Linux OS to console.

The script should accept a single parameter to specify which metrics set to print:
* cpu - prints CPU metrics
* mem - prints RAM metrics
		
## Requirements:
 - python 3
 - pip
 - psutil

## Installation:
	pip install psutil

## Examples:
python metrics.py cpu<br />
####################CPU####################<br />
system.cpu.idle 27836.91<br />
system.cpu.user 20.1<br />
system.cpu.guest 0.0<br />
system.cpu.iowait 106.13<br />
system.cpu.stolen 0.0<br />
system.cpu.system 25.23<br />
###########################################<br />

python metrics.py mem<br />
####################MEMORY####################<br />
virtual total 2082521088<br />
virtual used 286105600<br />
virtual free 1484484608<br />
virtual shared 9531392<br />
swap total 2144333824<br />
swap used 0<br />
swap free 2144333824<br />
##############################################<br />
