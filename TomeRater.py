"""
    TomeRater Capstone by Shawn A. Alleyne
    Started: 06/18/2018
    Last Updated: 06/25/2018 Stopped [Get Creative] 10/11
                  
    CLASSES
        cls.User:
          Methods:       get_email,change_email,read_book,get_average_rating
          Construtors:   repr -> print, eq -> ==

          
        cls.Book:
            Methods:       get_title,get_isbn,set_isbn,add_rating,get_average_rating
            Construtors:   repr -> print, eq -> == , hash -> ??
            
            cls.Fiction:
                Methods:       get_author
                Construtors:   repr -> print

            cls.Non_Fiction:
                Methods:       
                Construtors:   repr -> print

        cls.TomeRater:
            Methods:       create_book,create_novel,create_non_fiction,add_book_to_user,add_user
                           print_catalog,print_users,most_read_book,highest_rated_book,most_positive_user
            Construtors:   
           
"""
def fun_isblank(prm_test_obj):
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
    books  = {} #book:rating
        
    def __init__(self, name, email):
        self.name   = name
        self.email  = email
        self.books  = {}


    def get_email(self):
        return(self.email)


    def change_email(self, address):
        self.email = address
        str_mess = self.name + "'s email has been updated."
        print( str_mess)


    def read_book(self,book,rating=None):
        self.books[book] = rating

        
    def get_average_rating(self):
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
            
        if int_num_books > 0 and int_tot_rating > 0:
            int_avg_rating = max(int(int_tot_rating / int_num_books),0)

        return(int_avg_rating)

    
    def __repr__(self):
        int_books = len(self.books)
        str_review = ""
        if int_books <= 0:
            str_review = " has not reviewed any books."
        elif int_books == 1:
            str_review = " has reviewed one book."
        else:     
            str_review = " has reviewed " + str(int_books) + " books."
            
        str_mess  = "User " + self.name + " with email address " + self.email + str_review 
        return(str_mess)


    def __eq__(self, other_user):
        rtn_equal = False
        if self.name == other_user.name and self.email == other_user.email:
            rtn_equal = True
        return (rtn_equal)
# END CLASS USER       

        
# START CLASS BOOK
class Book(object):
    title = ""
    isbn  = 0
    ratings = [] #list of numbers 0 to 4

    def get_title(self):
        return(self.title)


    def get_isbn(self):
        return(self.isbn)


    def set_isbn(self,isbn=0):
        str_mess = ""
        self.isbn = isbn
        str_mess = "The book " + self.title + " isbn was updated."
        print(str_mess)


    def add_rating(self,rating=0):
        if rating >= 0 and rating <=4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating. Ratings must be 0-4.")


    def get_average_rating(self):
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
        self.ratings = []


    def __repr__(self):
        str_mess = self.title + " has ISBN: " + str(self.isbn)
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


    def get_author(self):
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


# START CLASS TOMERATER
class TomeRater():
    
    def __init__(self):
        self.users = {}  #email:obj_user
        self.books = {}  #obj_book:num_times_read

        
    def create_book(self,title,isbn):
        rtn_obj_new_book = Book(title,isbn)
        return(rtn_obj_new_book)


    def create_novel(self,title,author,isbn):
        rtn_obj_new_book = Fiction(title,author,isbn)
        return(rtn_obj_new_book)


    def create_non_fiction(self,title,subject,level,isbn):
        rtn_obj_new_book = Non_Fiction(title,subject,level,isbn)
        return(rtn_obj_new_book)
    

    def add_book_to_user(self,book,user_email,rating=None):
        obj_user = self.users.get(user_email,"")
        if obj_user:
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
            
    
    def add_user(self,user_name,user_email,user_books=None):
        obj_new_user = User(user_name,user_email)
        self.users[user_email] = obj_new_user
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book,user_email,0)


    def print_catalog(self):
        for book in self.books:
            print(book)


    def print_users(self):
        for user in self.users.values():
            print(user)

                
    def get_most_read_book(self):
        int_highread = 0
        obj_most_book = None
        
        for book, num_read in self.books.items():
            if num_read > int_highread:
              obj_most_book  = book
              int_highread = num_read 
        return(obj_most_book)


    def highest_rated_book(self):
        int_highrate = 0        
        for book in self.books:
           curr_avg = book.get_average_rating()
           if curr_avg  > int_highrate:
              int_highrate = curr_avg
              obj_high_book = book
        return(obj_high_book)


    def most_positive_user(self):
        int_positive = 0
        obj_posv_usr = None
        for curr_user in self.users.values():
            curr_avg = curr_user.get_average_rating()
            if curr_avg  > int_positive :
              int_positive  = curr_avg
              obj_posv_usr = curr_user
        return(obj_posv_usr)
    
# END CLASS TOMERATER

