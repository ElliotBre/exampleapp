import databaseDependencies

objectList = []

connectionString =  r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'
newDB = databaseDependencies.DB(connectionString)

#execString = input("Input an SQL command")
execString = 'SELECT * FROM company'

result = newDB.executeAll(execString)
print(f"""Working Database : 
_____________________________________________________________________

        {result}     
_____________________________________________________________________""")

objectList = newDB.loadObjectTable(execString)
newDB.closeConnection(newDB)