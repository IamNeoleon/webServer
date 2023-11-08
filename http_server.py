
from sendResurses import SendResurses
from dataBaseManager import DataBaseManager
import helper
 

class SimpleGetHandler(SendResurses):   

    def homePage(self, param):
        result = ''
        
        if param is None:
            result = DataBaseManager.get_data("SELECT * FROM books")
        else:
            result = DataBaseManager.get_data("SELECT * FROM books WHERE name_book=?", (param,))

        book_template = helper.read_tampleate("template/book.html")

        data_page = ""
        for book in result:
            print(book)
            data_page += helper.setParamTemp(book_template, id = book[0], book_name = book[1], book_short_desc = book[3])

        content = helper.read_tampleate("template/index.html")
        content = helper.setParamTemp(content, cards = data_page)
        print(result)
        self.renderPage(content)


    def remove(self, param):
        DataBaseManager.remove("DELETE FROM people WHERE id = ?", (param,))
        print("Объект с ID={param} удален!".format(param = param))


    def do_GET(self):
        path, param = helper.split_Path_And_Param(self.path)


        if path == "/index.html" or path == "/":                    
            self.homePage(param)
        elif path == "/remove":
            self.remove(param)
        else:            
            self.getContent(self.path)


