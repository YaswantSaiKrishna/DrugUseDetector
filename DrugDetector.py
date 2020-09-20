import sys
import pyodbc
import requests

azfunc = "<Your Function Url>" #FunctionName
url = azfunc + str(sys.argv[1])
r = requests.get(url)
x = r.json()
tab = str(x["text"])

query = "select uses from [dbo].[Med] where Name=" + "'" + tab + "'"
server = '<server>.database.windows.net' #Sql server name
database = '<Database Name>' #Database Name
username = '<Name>' #UserName
password = '<Password>' #Password   
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchone()
        while row:
            eng_use = str(*row)
            if sys.argv[2]:
                try:
                    translation = translator.translate(eng_use, dest=str(sys.argv[2]))
                    print(f"English : {eng_use}")
                    print(f"{sys.argv[2]} : {translation.text}")
                except:
                    print(f"Invalid language {eng_use}")
            else:
                print (eng_use)
            row = cursor.fetchone()
