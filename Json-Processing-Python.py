import json
import datetime
import pyodbc
import cProfile
import pstats
import types
import codecs
import os
import sys

def parseJsonAndReturnString (data, filename):
    row_del = "\n"
    column_del = "\t"
    defaultval = u""
    
    #Initialize
    event_type = defaultval
    application_version = defaultval
    application_name = defaultval
    event_grade = defaultval
    event_attempts = defaultval
    event_max_grade = defaultval
    event_code = defaultval
    event_id = defaultval
    event_mode = defaultval
    event_user_id = defaultval
    #For Video events
    eventtext_code = defaultval
    eventtext_type = defaultval
    eventtext_id = defaultval
    eventtext_new_time = defaultval
    eventtext_old_time = defaultval
    eventtext_current_time = defaultval
    eventtext_enrollment_mode = defaultval
    #For Certificate events
    eventtext_certificate_id = defaultval
    eventtext_generation_mode = defaultval
    eventtext_certificate_url = defaultval
    eventtext_course_id = defaultval
    eventtext_social_network = defaultval
    eventtext_source_url = defaultval
    #For EventSub
    eventsub_problemid = defaultval
    eventsub_inputtype = defaultval
    eventsub_responsetype = defaultval
    eventsub_variant = defaultval
    eventsub_correct = defaultval
       
    username = data.get("username", defaultval)
    event_type = (data.get("event_type", defaultval)).encode("ascii", "ignore")
    ip = data.get("ip", defaultval)
    agent = data.get("agent", defaultval) 
    host = data.get("host", defaultval)
    referer = data.get("referer", defaultval)
    accept_language = data.get("accept_language", defaultval)
    time = data.get("time", defaultval)
    session = data.get("session", defaultval)
    name = data.get("name", defaultval)
    event_source = data.get("event_source", defaultval)

    #context json
    user_id = str(data.get("context").get("user_id", defaultval))
    org_id = data.get("context").get("org_id", defaultval)
    course_id = data.get("context").get("course_id", defaultval)
    path = data.get("context").get("path", defaultval)
    component = data.get("context").get("component", defaultval)
    application = data.get("context").get("application", defaultval)
    #parse application json if available
    if application != defaultval:
        application_version = application.get("version", defaultval)
        application_name = application.get("name", defaultval)

    #event json
    eventtext = data.get("event")

    if len(eventtext) > 0:

        if type(eventtext) is types.DictType:

            event_grade = str(eventtext.get("grade", defaultval))
            event_attempts = str(eventtext.get("attempts", defaultval))
            event_max_grade = str(eventtext.get("max_grade", defaultval))
            event_code = eventtext.get("code", defaultval)
            event_id = eventtext.get("id", defaultval)
            event_mode = eventtext.get("mode", defaultval)

            #Associated fields are EventSub_*
            event_submission = eventtext.get("submission", defaultval)
            
            if event_submission != defaultval:
                #As name is dynamic in name:value get the key and decode json based on key
                event_sub_key = event_submission.keys()
                if len(event_sub_key) == 1: 
                    eventsub = event_submission.get(event_sub_key[0])
                    if type(eventsub) is types.DictType:
                        eventsub_problemid = event_sub_key[0]
                        eventsub_inputtype = eventsub.get("input_type", defaultval)
                        eventsub_responsetype = eventsub.get("response_type", defaultval)
                        eventsub_variant = str(eventsub.get("variant", defaultval))
                        eventsub_correct = str(eventsub.get("correct", defaultval))
                

        #This code can be optimized as these eventtext fields are needed for VIDEO and CERTIFICATE events only
        elif type(eventtext) in types.StringTypes and isJson(eventtext):

            eventjson = json.loads(eventtext)

            if type(eventjson) is types.DictType:
                #Video events
                eventtext_code = eventjson.get("code", defaultval)
                eventtext_type = eventjson.get("type", defaultval)
                eventtext_id = eventjson.get("id", defaultval)
                eventtext_new_time = str(eventjson.get("new_time", defaultval))
                eventtext_old_time = str(eventjson.get("old_time", defaultval))
                eventtext_current_time = str(eventjson.get("currentTime", defaultval))
                
                #Certificate events
                eventtext_enrollment_mode = eventjson.get("enrollment_mode", defaultval)
                eventtext_certificate_id = eventjson.get("certificate_id", defaultval)
                eventtext_generation_mode = eventjson.get("generation_mode", defaultval)
                eventtext_certificate_url = eventjson.get("certificate_url", defaultval)
                eventtext_course_id = eventjson.get("course_id", defaultval)
                eventtext_social_network = eventjson.get("social_network", defaultval)
                eventtext_source_url = eventjson.get("source_url", defaultval)

        else:
            pass

    # build parsed string   
    parsedstr = filename + column_del + username + column_del + event_type + column_del + ip + column_del + agent + column_del + host + column_del + referer + column_del + accept_language + column_del + time + column_del + session + column_del + name + column_del + event_source + column_del + user_id + column_del + org_id + column_del + course_id + column_del + path + column_del + component + column_del + application_version + column_del + application_name + column_del + event_grade + column_del + event_attempts + column_del + event_max_grade + column_del + event_code + column_del + event_id + column_del + event_mode + column_del + eventtext_code + column_del + eventtext_type + column_del + eventtext_id + column_del + eventtext_new_time + column_del + eventtext_old_time + column_del + eventtext_current_time + column_del + eventtext_enrollment_mode + column_del + eventtext_certificate_id + column_del + eventtext_generation_mode + column_del + eventtext_certificate_url + column_del + eventtext_course_id + column_del + eventtext_social_network + column_del + eventtext_source_url + column_del + eventsub_problemid + column_del + eventsub_inputtype + column_del + eventsub_responsetype + column_del + eventsub_variant + column_del + eventsub_correct + row_del
    
    return (parsedstr)

def isJson(myjson):
    try:
        jsonobj = json.loads(myjson)
    except ValueError, e:
        return False
    return True

def writetoSQL(outputfile):
    
    # define sql server configuration
    uname = sys.argv[5]
    password = sys.argv[6]
    database = sys.argv[4]
    port = sys.argv[3]
    server = sys.argv[2]
    driver = "{SQL Server}"
    tablename = "dbo.Edx_DailyEvents"
    inputfile = outputfile

    # Build connection string
    conn = "UID=%s;PWD=%s;DATABASE=%s;PORT=%s;SERVER=%s;driver=%s" %(uname,password,database,port,server,driver)
    cnxn = pyodbc.connect(conn)
    cursor = cnxn.cursor()
    
    bulkinsertstr = "BULK INSERT " + tablename + " FROM '" + inputfile + "' WITH (FIELDTERMINATOR = '\t', ROWTERMINATOR = '\n', TABLOCK); " 

    # Load tsv file in SQL Server
    cursor.execute(bulkinsertstr)
    cnxn.commit()
    cnxn.close()
    
def printProfilerResults (pr):
    s = StringIO.StringIO()
    sortby = "tottime"
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print s.getvalue()

try:
    # Initialize
    starttime = datetime.datetime.today()
    endtime = starttime
    enableProfiler = 0
    line = u""
    
    if len(sys.argv) < 7:
        raise Exception("Required arguements missing")
    
    jsonfile = sys.argv[1]
    
    if os.path.exists(jsonfile)==False:
        raise Exception("Input file not found")
      
    inputfile = os.path.basename(jsonfile)
    outputfile = jsonfile.replace("json", "tsv") 
    
    # Start profiler if value is set to 1
    if enableProfiler == 1:
        pr = cProfile.Profile()
        pr.enable()

    # File for writing parsed json
    tsv_f = open(outputfile, "w")
    
    # Read json file
    f = codecs.open(jsonfile, mode = "r", encoding = "utf-8")

    # Iterate through each line, parse json and write structure to tsv file 
    for line in f:
        data = json.loads(line)   
        tsv_f.write(parseJsonAndReturnString(data, inputfile))
             
    # This is required as bulk insert cannot access the file 
    tsv_f.close()
    
    # Load tsv file in SQL Server
    writetoSQL(outputfile)
    
    # Basic logging
    print "\nJson parsing completed"
    endtime = datetime.datetime.today()
    print "Time taken to complete the program = ", (endtime - starttime)
     
except Exception as e:
    print "Error: ", e
    print "\n", line
    raise
       
finally:
    # Close file pointers
    if "tsv_f" in locals():
        if tsv_f.closed == False:
            tsv_f.close()

    if "f" in locals():
        if f.closed == False:
            f.close()
        
    # Print statistics of profile
    if enableProfiler == 1:
        pr.disable()
        printProfilerResults(pr)