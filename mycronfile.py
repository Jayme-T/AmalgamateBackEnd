from crontab import CronTab

# Get the current list of cron jobs
cron = CronTab(user=True)

# Go through the list looking for the one we want to change
def schedulingaturn(mins, hours, dom, m, dow):
   for job in cron:
      if 'scheduleturn.py' in job.command:
         #print "HELLO?:", job   
         minutes = mins
         hours=hours
         day_of_month=dom
         month=m
         dow=dow
         schedule = "{0} {1} {2} {3} {4}".format(minutes, hours, day_of_month, month, dow)
         print schedule
         job.setall(schedule)
      #job.dow.on()
      else:
         print "nope"
   cron.write()
def schedulingawater(mins, hours, dom, m, dow):
   for job in cron:
      if 'schedulewater.py' in job.command:
         #print "HELLO?:", job   
         minutes = mins
         hours=hours
         day_of_month=dom
         month=m
         dow=dow
         schedule = "{0} {1} {2} {3} {4}".format(minutes, hours, day_of_month, month, dow)
         print schedule
         job.setall(schedule)
      #job.dow.on()
      else:
         print "nope"
   cron.write()
#schedulingaturn('0', '0', '*/3', '*', '*')
#schedulingawater('0', '0', '*/5', '*', '*')

   


   
