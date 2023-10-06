import pyodbc

class DBOBJECTS:
    def __INIT__(self, coID, name, phone, city, postcode):
        self.coID = coID
        self.name = name
        self.phone = phone
        self.city = city
        self.postcode = postcode
    def __repr__(self):
        return f"Variables = {self.coID}, {self.name}, {self.phone}, {self.city}, {self.postcode}"
    

    def setVar(self, data = ()):
        for i in range(len(data)):
            if data[i] != None:
                match i:
                    case 0:
                        self.coID = data[i]
                    case 1:
                        self.name = data[i]
                    case 2:
                        self.phone = data[i]
                    case 3:
                        self.city = data[i]
                    case 4:
                        self.postcode = data[i]


class DB:
    def __init__(self, connectionString):
        self.connectionString = connectionString
        self.connection = pyodbc.connect(self.connectionString)
        self.cursor = self.connection.cursor()
    def __repr__(self):
        return f"Values : {self.connectionString} , {self.cursor}, {self.cursor} "
    
    def executeAll(self,executeString):
        return tuple(self.cursor.execute(executeString).fetchall())
    def executeLine(self,executeString):
        return tuple(self.cursor.execute(executeString).fetchone())
    def loadObjectTable(self, execString):
        objectList = []
        row = self.executeLine(execString)
        while row != None:
            newOBJ = DBOBJECTS()
            print("Adding : ")
            print(row)
            newOBJ.setVar(row)
            objectList.append(newOBJ)
            row = self.getCursor().fetchone()
        print(f"""  Loaded objects:
______________________________________________________________________
            
            {objectList}
______________________________________________________________________""")
        return objectList
        

    def closeConnection(self, connection):
        self.connection.close()
    def getConnection(self):
        return self.connection
    def getCursor(self):
        return self.cursor
    def getConnectionString(self):
        return self.connectionString
    