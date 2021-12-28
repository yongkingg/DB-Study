## autoincrement
## primary key 
# 테이블 내 동일한 레코드가 입력되는 경우 이를 구분해 줄 수 있는 식별자를 만들어 사용하는 데 이 식별자를 기본키라고 한다. 이 기본키는 각 테이블마다 단 하나씩만 설정할 수 있다. 그리고 아래의 조건을 만족해야 한다. 
# 유일성 - 기본키를 구성하는 컬럼은 테이블에서 레코드를 식별할 수 있도록 유일해야 함
# 최소성 -  유일성을 만족하는 한도 내에서 최소한의 컬럼으로 구성되어야 함
# 개체 무결성 -  기본키가 가지고 있는 값의 유일성이 보장받아야 함.

# 다음 코드를 보자

# import sqlite3

# class DataBase:
#     def __init__(self):
#         self.conn = None
#         self.cur = None
#         self.result = None

#     def makeDataBase(self):
#         self.conn = sqlite3.connect("DataBase.db") # 데이터베이스와 연결
#         self.cur = self.conn.cursor() # 커서 객체를 생성함


#         self.cur.execute("CREATE TABLE carBrand(brand_id INTEGER PRIMARY KEY, brandName TEXT);")
#         self.cur.execute("INSERT INTO carBrand VALUES(1,'Kia');")
#         self.cur.execute("INSERT INTO carBrand VALUES(2,'Hyundai');")
#         self.cur.execute("INSERT INTO carBrand VALUES(3,'BMW');")
#         self.cur.execute("INSERT INTO carBrand VALUES(4,'Benz');")
#         self.cur.execute("INSERT INTO carBrand VALUES(5,'Audi');")
#         self.conn.commit()

# brand_id 라는 컬럼을 만들어 brandName을 구분해주는 모습이다. 이 테이블에서는 brand_id가 결국 primary key인 것이다.
# sqlite3에서는 primary key가 정수인 경우 이를 자동으로 증가하게 만들어 줄 수 있다. 테이블을 만들때, AUTOINCREMENT 코드를 추가하기만 하면된다. 아래 코드를 참고하자. 

import sqlite3

class DataBase:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.result = None

    def makeDataBase(self):
        self.conn = sqlite3.connect("DataBase.db")
        self.cur = self.conn.cursor() 
        # self.cur.execute("DROP TABLE carBrand;")
        self.cur.execute("CREATE TABLE carBrand(brand_id INTEGER PRIMARY KEY AUTOINCREMENT, brandName TEXT);")
        self.cur.execute("INSERT INTO carBrand(brandName) VALUES('Kia');")
        self.cur.execute("INSERT INTO carBrand(brandName) VALUES('BMW');")
        self.cur.execute("INSERT INTO carBrand(brandName) VALUES('Benz');")
        self.cur.execute("INSERT INTO carBrand(brandName) VALUES('Audi');")
        self.cur.execute("INSERT INTO carBrand(brandName) VALUES('Kia');")
        self.conn.commit()



# 데이터를 INSERT 할때, brandName에만 데이터를 추가해도, 자동적으로 brand_id 컬럼에 정수가 추가되는 모습을 볼 수 있다. 이를 통해 중복데는 데이터가 있어도, primary key로 제어할 수 있다. 

## foreign  key 
# 외래키란 테이블의 필드 중에서 다른 테이블의 행과 식별할 수 있는 키를 의미한다. 
# 일반적으로 외래키가 포함된 테이블을 자식 테이블이라 하며, 외래키 값을 갖고 있는 테이블은 부모 테이블이라 한다.
# 즉, 외래키란 테이블과 테이블을 연결하기 위해 사용되는 키이다. 
# 다음 코드를 참고하여 보자.

# import sqlite3

# class DataBase:
#     def __init__(self):
#         self.conn = None
#         self.cur = None
#         self.result = None

#     def makeDataBase(self):
#         self.conn = sqlite3.connect("DataBase.db")
#         self.cur = self.conn.cursor() 
#         self.cur.execute("DROP TABLE carBrand;")
#         self.cur.execute("DROP TABLE playList;")

#         self.cur.execute("CREATE TABLE carBrand(brand_id INTEGER PRIMARY KEY AUTOINCREMENT, brandName TEXT);")
#         self.cur.execute("CREATE TABLE carInfor(brandName TEXT, size TEXT,  carName TEXT);")

# 다음 코드를 실행하면, 두개의 테이블이 생성되는데 이 두개의 테이블은 동일한 brandName 컬럼으로 이어져있다. 이 두개의 테이블은 brandName 을 통해 동시에 컨트롤 할 수 있는데, 이를 foreign  key(외래키) 라고 한다.


    def create(self, table, column, data):    
        self.sql = "INSERT INTO " + table + "(" 
        for index in range(0, len(column)):
            self.sql += column[index]
            if index < len(column)-1:
                self.sql += ", "
        self.sql += ")"
        self.sql += " VALUES("
        for index in range(0, len(column)):
            self.sql += "'" + data[index] + "'"
            if index < len(column)-1:
                self.sql += ", "
        self.sql += ");"
        self.cur.execute(self.sql)
        self.conn.commit()
    def read(self,table,column,data):
        self.sql = "SELECT * FROM " + table + " WHERE ("
        if len(column) == 1:
            for index in range(0,len(column)):
                self.sql += column[index]
                if index < len(column) -1:
                    self.sql += ", "
            self.sql += " = " + "'"
            for index in range(0,len(column)):
                self.sql += data[index]
                if index < len(column) - 1:
                    self.sql += "', '"
            self.sql += "');"
        else:
            for index in range(0,len(column)):
                self.sql += column[index] + "="
                self.sql += "'" + data[index]+"'"
                if index < len(column) -1:
                    self.sql += " and "
            self.sql += ");"
        self.cur.execute(self.sql)
        self.result = self.cur.fetchall()
        return self.result
    def update(self,table,originalColumn,setColumn,originalData,setData):
        self.sql = "UPDATE " + table + " SET " + "("
        for index in range(0,len(setColumn)):
            self.sql += setColumn[index]
            if index < len(setColumn)-1:
                self.sql += ", "
            self.sql += ")" + " = " + "('"
        for index in range(0,len(setData)):
            self.sql += setData[index]
            if index < len(setData)-1:
                self.sql += ", "
            self.sql += "')"
            self.sql += " WHERE " + "("
        for index in range(0,len(originalColumn)):
            self.sql += originalColumn[len(originalColumn)-index-1]
            if index < len(originalColumn)-1:
                self.sql += ", "
        self.sql += ")" + "=" + "('"
        for index in range(0,len(originalData)):
            self.sql += originalData[index]
            if index < len(originalData)-1:
                self.sql += ", "
            self.sql += "');"
        self.cur.execute(self.sql)
        self.conn.commit()
    def delete(self, table, column, data):
        self.sql = "DELETE FROM " + table + " WHERE " + column + "=" + "'" + data + "'" ";"
        self.cur.execute(self.sql)
        self.conn.commit()
    
if __name__ == "__main__":
    database = DataBase()
    database.makeDataBase()
