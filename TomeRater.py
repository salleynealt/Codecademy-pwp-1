"""
    TomeRater Capstone by Shawn A. Alleyne
    Started: 06/18/2018
    Last Updated: 06/19/2018 Stopped end of page 5/11
    
    CLASSES
        User:
        Book:
            Fiction:
            Non_Fiction:
            
"""
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


# START MAIN
Hulk = Fiction("Hulk Smash V21","Marvel",1215)
print(Hulk)
# print("Book " + Hulk.title + " by " + Hulk.author )

    
