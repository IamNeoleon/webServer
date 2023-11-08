import sqlite3

class DataBaseManager:
    @staticmethod
    def setPath(path):
        DataBaseManager.path = path


    @staticmethod
    def remove(sql, param):
        conn = sqlite3.connect(DataBaseManager.path)
        cursor = conn.cursor()

        try:
            cursor.execute(sql, param)
            conn.commit()
            print("Данные успешно удалены.")
        except sqlite3.Error as e:
            print("Ошибка при удалении данных:", e)

        conn.close()


    @staticmethod
    def get_data(sql, param = None):
        con = sqlite3.connect(DataBaseManager.path)
        cursor = con.cursor()

        if param is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, param)

        res = []
        for raw in cursor.fetchall():
            res.append(raw)
            
        return res