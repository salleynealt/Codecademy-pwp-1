"""
    TomeRater Capstone by Shawn A. Alleyne
    Started: 06/18/2018
    Last Updated: 06/20/2018 Stopped [Analysis Methods] 8/11
    
    CLASSES
        User:
        Book:
            Fiction:
            Non_Fiction:
            
"""
def fun_isblank(prm_test_obj):
  rtn_bol_isblank = False
  typ_obj_type = type(prm_test_obj)
 
  if typ_obj_type == str:
    str_test = prm_test_obj.strip()
    if str_test == "" :
      rtn_bol_isblank = True
  elif typ_obj_type == list:
    if len(prm_test_obj) <= 0:
      rtn_bol_isblank = True
  elif typ_obj_type == dict:
    if len(list(prm_test_obj)) <= 0:
      rtn_bol_isblank = True
  elif typ_obj_type == tuple:
    if len(list(prm_test_obj)) <= 0:
      rtn_bol_isblank = True      
  return(rtn_bol_isblank)


# START CLASS USER  
class User(object):
    name   = ""
    email  = ""
    books  = {}
        
    def __init__(self, name, email):
        self.name   = name
        self.email  = email        


    def get_email(self):
        return(self.email)


    def change_email(self, address):
        self.email = address
        str_mess = self.name + "'s email has been updated."
        print( str_mess)


    def read_book(book,rating=None):
        self.books[book] = rating

        
    def get_average_rating():
        int_tot_rating = 0
        int_avg_rating = 0
        int_curr_rating = 0
        int_num_books = 0
        for book_rated in self.books:
            int_num_books += 1 
            int_curr_rating = 0
            try:
                int_curr_rating = int(self.books[book_rated])
                int_tot_rating += int_curr_rating
            except ValueError:
                pass
            except TypeError:
                pass
            
        if int_num_books > 0 and int_curr_rating > 0:
            int_avg_rating = max(int(int_curr_rating / int_num_books),0)

        return(int_avg_rating)

    
    def __repr__(self):
        int_books = len(self.books)
        str_review = ""
        if int_books <= 0:
            str_review = "has not reviewed any books."
        elif int_books == 1:
            str_review = "has reviewed one book."
        else:     
            str_review = "has reviewed " + str(int_books) + " books."
            
        str_mess  = "User " + self.name + " with email address " + self.email + str_review 
        return(str_mess)


    def __eq__(self, other_user):
        rtn_equal = False
        if self.name == other_user.name and self.email == other_ser.email:
            rtn_equal = True
        return (trn_equal)
# END CLASS USER       

        
# START CLASS BOOK
class Book(object):
    title = ""
    isbn  = 0
    ratings = []

    def get_title():
        return(self.title)


    def get_isbn():
        return(self.isbn)


    def set_isbn(isbn=0):
        str_mess = ""
        self.isbn = isbn
        str_mess = "The book " + self.title + " isbn was updated."
        print(str_mess)


    def add_rating(rating=0):
        if rating >= 0 and rating <=4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating. Ratings must be 0-4.")


    def get_average_rating():
        int_count = 0
        int_tot_rate = 0
        int_avg_rate = 0
        
        for curr_rate in self.ratings:
            int_count += 1
            try:
                int_tot_rate += int(curr_rate)
            except ValueError:
                pass
            except TypeError:
                pass    

        if int_count > 0 and int_tot_rate > 0:
            int_avg_rate = int(int_tot_rate / int_count)
            
        return(int_avg_rate)

    
    def __init__(self, title, isbn):
        self.title = title
        self.isbn  = isbn       


    def __repr__(self):
        str_mess = self.title + " - " + str(self.isbn)
        return(str_mess)
        

    def __eq__(self, other_book):
        rtn_equal = False
        if self.title == other_book.title and self.isbn == other_book.isbn:
            rtn_equal = True
        return(rtn_equal)


    def __hash__(self):
        return hash((self.title, self.isbn))

# END CLASS BOOK



# START CLASS FICTION     
class Fiction(Book) :
    author = ""
    
    def __init__(self,title,author,isbn):
        super().__init__(title, isbn)
        self.author = author


    def get_author():
        return(self.author)


    def __repr__(self):
        str_mess = self.title + " by " + self.author
        return(str_mess)
# END CLASS FICTION 


# START CLASS NON_FICTION 
class Non_Fiction(Book):
    subject = ""
    level   = ""
    
    def __init__(self,title, subject,level,isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level


    def __repr__(self):
        str_mess = self.title + " a " + self.level + " manual on " + self.subject
        return(str_mess)
# END CLASS NON_FICTION


# START CLASS NON_FICTION
class TomeRater():
    
    def __init__(self):
        self.users = {}  #email:obj_userid
        self.books = {}  #obj_bookid:num_times_read

        
    def create_book(title,isbn):
        rtn_obj_new_book = Book(title,isbn)
        return(rtn_obj_new_book)


    def create_novel(title,author,isbn):
        rtn_obj_new_book = Fiction(title,author,isbn)
        return(rtn_obj_new_book)


    def create_non_fiction(title,subject,level,isbn):
        rtn_obj_new_book = Non_Fiction(title,subject,level,isbn)
        return(rtn_obj_new_book)
    

    def add_book_to_user(book,email,rating=None):
        obj_user = self.user.get(email,"")
        if not fun_isblank(str_user_name):
            obj_user.read_book(book,rating)
            book.add_rating(rating)
            try:
                int_num_reads = int(self.books.get(book,0))
                if int_num_reads >= 0:
                    int_num_reads += 1
                    self.books[book] = int_num_reads  
                else:
                    print("Error bad number of books [add_book_to_user] " + email)       
            except ValueError:
                pass
            except TypeError:
                pass    
        else:
            str_mess = "No user with email " + email + " !"
            print(str_mess)
            
    
    def add_user(name,email,books=None):
        obj_new_user = User(name,email)
        if books != None:
            for book in books:
                add_book_to_user(book,email)

    
    
    
# END CLASS NON_FICTION


# START MAIN
Hulk = Fiction("Hulk Smash V21","Marvel",1215)
print(Hulk)
# print("Book " + Hulk.title + " by " + Hulk.author )
