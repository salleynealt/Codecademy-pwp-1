"""
    TomeRater Capstone by Shawn A. Alleyne
    Started: 06/18/2018
    Last Updated: 07/08/2018 

    FUNCTIONS:
        fun_isblank

        fun_chkascii127

        fun_validemail

                          
    CLASSES
        cls.User:
            Methods:       get_email,change_email,read_book,get_average_rating
                           get_worth_of_collection,get_number_books,get_my_books
            Construtors:   _int -> create, _repr -> print, _eq -> == , _hash -> dict-key

          
        cls.Book:
            Methods:       get_title,get_isbn,set_isbn,add_rating,get_average_rating
                           get_price,set_price,add_review 
            Construtors:   _int -> create , _repr -> print, _eq -> == , _hash -> dict-key
            
            cls.Fiction:
                Methods:       get_author
                Construtors:   _int -> create , _repr -> print

            cls.Non_Fiction:
                Methods:       
                Construtors:   _int -> create , _repr -> print

        cls.TomeRater:
            Methods:       create_book,create_novel,create_non_fiction,add_book_to_user,add_user
                           print_catalog,print_users,get_most_read_book,highest_rated_book,most_positive_user
                           modify_user_email,check_newisbn,store_isbn,remove_isbn,change_isbn
                           get_worth_of_user,get_n_most_read_books,get_n_most_prolific_readers
                           get_n_most_expensive_books,sendmailer,new_book_mailer,recommnd_books
            Construtors:   _int -> create, _repr -> print, _eq -> ==

"""

# START fun_isblank
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
# END fun_isblank


# START fun_chkascii127
def fun_chkascii127(prm_str_validate,prm_extra_chars="",prm_use_default=True):
  rtn_bol_Valid = False
  str_Ascii = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  str_SpecailChars = "!#$%&'*+-/=?^_`{|}~"
  str_usechars = ""
  int_len_strval = int(len(prm_str_validate))
  int_good_chars = 0
    
  if prm_use_default == True:
    str_usechars += str_SpecailChars
      
  if not fun_isblank(prm_extra_chars):
    str_usechars += prm_extra_chars  

  str_use_validate = prm_str_validate.upper()
  for curr_char in str_use_validate:
    int_hasChar = str_Ascii.find(curr_char)
    int_hasSpc = str_usechars.find(curr_char)
    if int_hasChar >= 0 or int_hasSpc >=0:
      int_good_chars +=1
      
  if int_good_chars == int_len_strval:
    rtn_bol_Valid = True

  return(rtn_bol_Valid)
# END fun_chkascii127


# START fun_validemail
def fun_validemail(prm_str_chk_email):
  
  
  """
  Email Validation Rules
  FORMAT: [localpart]@[domain].[end]

  General Rule
       Must have one @ and at least one .
   
  localpart / emailpart1
	64 character max ascii [1-127] 
	no double dots ".."
	a-z, A-Z, 0-9, or any of !#$%&'*+-/=?^_`{|}~.
	
  domain / emailpart2
  	63 characters max
	 a-z, A-Z, 0-9, or one of !#$%&'*+-/=?^_`{|}~
	can not start or end with "-"
	
  end / classification / emailpart3 US Standard	
	.com,.org,.net,.int,.edu,.gov,.mil
  """

  str_emailpart1 = ""
  str_emailpart2 = ""
  str_emailpart3 = ""
  bol_goodpart1 = False
  bol_goodpart2 = False
  bol_goodpart3 = False
  bol_goodemail = False
  int_idx_pt1 = 0
  int_count_ptdiv1 = 0
  int_idx_pt2 = 0
  int_count_ptdiv2 = 0
  bol_stop = False
  str_stopped = ""
  str_specialchrs = "!#$%&'*+-/=?^_`{|}~."

  #must have a single "@"
  #must have at least one "."

  # Verification Loop
  int_verfy_count = 0
  int_len_email = len(prm_str_chk_email)
  str_CommonUS_ends = "com,org,net,int,edu,gov,mil"

  while bol_stop == False :
    # Count amount of special chars
    if int_verfy_count == 0:
      int_curr_indx = 0

      for curr_char in prm_str_chk_email:
        
        if curr_char == "@":
          int_idx_pt1 = int_curr_indx
          int_count_ptdiv1 +=1

        if curr_char == ".":
          int_idx_pt2 = int_curr_indx
          int_count_ptdiv2 +=1
          
        if curr_char == " ":
          bol_stop = True
          str_stopped = "Space found in the email."
          
        int_curr_indx +=1

      if int_count_ptdiv1 > 1 or int_idx_pt1 == 0 or int_idx_pt1 == (int_len_email - 1):
             bol_stop = True
             str_stopped = "Invalid email: Check the @ didvisor."

      if int_idx_pt2 == 0 or int_idx_pt2 == (int_len_email - 1):
          bol_stop = True
          str_stopped = "Invalid email: A period can not start or end an email."
          
             
    if int_verfy_count == 1:
      str_emailpart1 =   prm_str_chk_email[:int_idx_pt1]
      if len(str_emailpart1) > 64:
          bol_stop = True
          str_stopped = "Invalid email: The local identifier is too long [sixty-four (64) characters max]."
      elif str_emailpart1.count("..") > 0:
        bol_stop = True
        str_stopped = "Invalid email: The local identifier can no have double dots/periods."
      else:
        bol_goodpart1 = fun_chkascii127(str_emailpart1,".")
        if bol_goodpart1 == False:
          bol_stop = True
          str_stopped = "Invalid email: The local identifier failed Acii-127 compliance."
      
    if int_verfy_count == 2:
      str_emailpart2 =   prm_str_chk_email[int_idx_pt1 + 1:int_idx_pt2]
      if len(str_emailpart2) > 63:
        bol_stop = True
        str_stopped = "Invalid email: The domain identifier is too long [sixty-three (63) characters max]."
      elif str_emailpart2[0] == "-" or str_emailpart2[-1] == "-":
        bol_stop = True
        str_stopped = "Invalid email: The domain identifier can not start or end with dash [-]."
      else:
        bol_goodpart2 = fun_chkascii127(str_emailpart2)
        if bol_goodpart2 == False:
          bol_stop = True
          str_stopped = "Invalid email: The domain identifier failed Acii-127 compliance."
   
    if int_verfy_count == 3:
      str_emailpart3 =   prm_str_chk_email[int_idx_pt2 + 1:]
      if str_CommonUS_ends.count(str_emailpart3) > 0:
        bol_goodpart3 = True
      else:
        bol_stop = True
        str_stopped = "Invalid email: The email site classification failed USA standards."
    
    if int_verfy_count == 4:
      if bol_stop == False and bol_goodpart1 == True and bol_goodpart2 == True and bol_goodpart3 == True:
        bol_goodemail = True
        bol_stop = True

    if int_verfy_count == 7:
      bol_stop = True
      
    int_verfy_count +=1
    if not fun_isblank(str_stopped):
      print(str_stopped)
      
  return(bol_goodemail)
# END fun_validemail
   
  
# START CLASS USER  
class User(object):
    name   = ""
    email  = ""
    tot_book_cost = 0
    fav_genre = ""
    fav_author = ""
    books  = {} #book:rating
        
    def __init__(self, name, email,fav_genre = "",fav_author = ""):        
        if fun_validemail(email) == True:
          self.name   = name
          self.email  = email
          self.books  = {}
          self.fav_genre = fav_genre
          self.fav_author = fav_author
        else:
          print("Can not create user")
          self = None
          

    def get_email(self):
        return(self.email)


    def change_email(self, address):
        if fun_validemail(address) == True: 
          self.email = address
          str_mess = self.name + "'s email has been updated."
          print( str_mess)
        else:
          print("Can not change to an invalid email address.")


    def read_book(self,book,my_rating=None,my_review=""):
      if book:
        self.books[book] = my_rating
        if book.price > 0:
          self.tot_book_cost += book.price
        if not fun_isblank(my_review):
              book.add_review(my_review)

              
    def get_number_books(self):
      int_rtn_num_books = len(self.books)
      return(int_rtn_num_books)

    
    def get_my_books(self):
        rtn_lst_my_books = []
        rtn_lst_my_books = list(self.books.keys())
        return(rtn_lst_my_books)
      
      
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


    def get_worth_of_collection(self):
        rtn_flt_worth = 0.00
        str_mess = ""
        for ck_book in self.books:
          flt_curr_price = ck_book.get_price()
          if flt_curr_price > 0:
            rtn_flt_worth += flt_curr_price
        if rtn_flt_worth == self.tot_book_cost:
          str_mess = "We kept good track for our collection cost."          
        else:
          str_mess = "Changing collection cost from $ {0:.2f}".format(self.tot_book_cost) + " to $ {0:.2f}".format(rtn_flt_worth)
          self.tot_book_cost = rtn_flt_worth
        print(str_mess)         
        return(rtn_flt_worth)
      

    def __hash__(self):
      return hash((self.name, self.email))
    
    
    def __repr__(self):
        int_books = len(self.books)
        str_review = ""
        if int_books <= 0:
            str_review = " has not reviewed any books"
        elif int_books == 1:
            str_review = " has reviewed one book"
        else:     
            str_review = " has reviewed " + str(int_books) + " books"
            
        str_mess  = "User " + self.name + " with email address " + self.email + str_review 

        if self.tot_book_cost > 0:
          str_mess  += " and has spent " + "${:0.2F}".format(self.tot_book_cost) + " on his/her book collection."
        else:
          str_mess  += "."
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
    price = 0.00
    genre = ""
    reviews = []
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


    def get_price(self):
      return(self.price)

    
    def set_price(self,prm_book_price=0):
      if prm_book_price >0 and prm_book_price < 1000.00:
        str_mess = self.title + " price has changed from ${:0.2F}".format(self.price) + " to ${:0.2F}".format(prm_book_price)
        self.price = prm_book_price
        print(str_mess)        


    def add_review(self,new_review):
      if not fun_isblank(new_review):
        self.reviews.append(new_review)

    
    def __init__(self, title, isbn,my_genre = "",my_book_price=0.00):
        self.title = title
        self.isbn  = isbn
        if not fun_isblank(my_genre):
          self.genre = my_genre
        if my_book_price != 0.00:
          self.price = my_book_price
        self.reviews = []
        self.ratings = [] 
        

    def __repr__(self):
        str_mess = self.title + " has ISBN: " + str(self.isbn)
        if not fun_isblank(self.genre):
          str_mess += " Genre: " + self.genre
        if self.price > 0 :
          str_mess += " Price: ${:0.2F}".format(self.price)
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
    
    def __init__(self,title,author,isbn,genre = "",book_price=0):
        super().__init__(title, isbn,genre,book_price)
        self.author = author


    def get_author(self):
        return(self.author)


    def __repr__(self):
        str_mess = self.title + " by " + self.author
        if not fun_isblank(self.genre):
          str_mess += " Genre: " + self.genre
        if self.price > 0 :
          str_mess += " Price: ${:0.2F}".format(self.price)
        return(str_mess)
# END CLASS FICTION 


# START CLASS NON_FICTION 
class Non_Fiction(Book):
    subject = ""
    level   = ""
    
    def __init__(self,title, subject,level,isbn,genre = "",book_price=0):
        super().__init__(title, isbn,genre,book_price)
        self.subject = subject
        self.level = level        


    def __repr__(self):
        str_mess = self.title + " a " + self.level + " manual on " + self.subject
        if not fun_isblank(self.genre):
          str_mess += " Genre: " + self.genre
        if self.price > 0 :
          str_mess += " Price: ${:0.2F}".format(self.price)
        return(str_mess)
# END CLASS NON_FICTION


# START CLASS TOMERATER
class TomeRater():
    
    def __init__(self):
        self.users = {}           #email:obj_user
        self.books = {}           #obj_book:num_times_read
        self.all_isbns = []       #all isbn's seen

        
    def create_book(self,title,isbn,genre = "",book_price=0):
        bol_newisbn = False
        bol_newisbn = self.check_newisbn(isbn)
        
        if bol_newisbn == True:
          rtn_obj_new_book = Book(title,isbn,genre,book_price)
          self.store_isbn(isbn)
          if rtn_obj_new_book and len(self.users) > 3:
            self.new_book_mailer(rtn_obj_new_book)
          return(rtn_obj_new_book)
        else:
          print("Can not create this book isbn is not unique.")


    def create_novel(self,title,author,isbn,genre = "",book_price=0):
        bol_newisbn = False
        bol_newisbn = self.check_newisbn(isbn)
        if bol_newisbn == True:
          rtn_obj_new_book = Fiction(title,author,isbn,genre,book_price)
          self.store_isbn(isbn)
          if rtn_obj_new_book and len(self.users) > 3:
            self.new_book_mailer(rtn_obj_new_book)            
          return(rtn_obj_new_book)
        else:
          print("Can not create this novel isbn is not unique.")  


    def create_non_fiction(self,title,subject,level,isbn,genre = "",book_price=0):
        bol_newisbn = False
        bol_newisbn = self.check_newisbn(isbn)
        if bol_newisbn == True:
          rtn_obj_new_book = Non_Fiction(title,subject,level,isbn,genre,book_price)
          self.store_isbn(isbn)
          if rtn_obj_new_book and len(self.users) > 3:
            self.new_book_mailer(rtn_obj_new_book)
          return(rtn_obj_new_book)
        else:
          print("Can not create this manual isbn is not unique.")


    def add_book_to_user(self,book,user_email,rating=None,review=""):
        obj_user = self.users.get(user_email,"")
        if obj_user:
            obj_user.read_book(book,rating,review)
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
            
    
    def add_user(self,user_name,user_email,user_books=None,fav_genre = "",fav_author = ""):
      if fun_validemail(user_email) == True:
        obj_old_user = self.users.get(user_email,None)
        if obj_old_user == None:
          obj_new_user = User(user_name,user_email,fav_genre,fav_author )
          self.users[user_email] = obj_new_user
          if user_books != None:
            for book in user_books:
              self.add_book_to_user(book,user_email,0,"")
        else:
          print("A user with this eamil already exist.")
      else:
        print("Can not add user with an invalid email address.")
        

    def print_catalog(self):
        for book in self.books:
            print(book)


    def print_users(self):
        for user in self.users.values():
          if fun_isblank(user.name) and  fun_isblank(user.email):
            del user
          else:  
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


    def modify_user_email(self,old_email,new_email):
      rtn_bol_mod = False
      bol_good_email = fun_validemail(old_email)
      if bol_good_email == True:
        try:
          chg_user = self.users[old_email]
          bol_chgd = chg_user.change_email(new_email)
          if bol_chgd == True:
            self.users.pop(old_email)
            self.users[new_email] = chg_user
            rtn_bol_mod = True
        except KeyError:
          print("Email address",old_email,"does not belong to a user in the system.")
          
      return(rtn_bol_mod)          

      
    def check_newisbn(self,prm_isbn):
      rtn_bol_new = False
      int_isbn_count = self.all_isbns.count(prm_isbn)
      if int_isbn_count == 0:
        rtn_bol_new = True
      return(rtn_bol_new)

    
    def store_isbn(self,prm_isbn):
      bol_new_isbn = False
      bol_new_isbn = self.check_newisbn(prm_isbn)
      if bol_new_isbn == True:
        self.all_isbns.append(prm_isbn)
      return(bol_new_isbn) 


    def remove_isbn(self,prm_isbn):
      bol_new_isbn = True
      bol_new_isbn = self.check_newisbn(prm_isbn)
      if bol_new_isbn == False:
        self.all_isbns.remove(prm_isbn)
      return(not bol_new_isbn)


    def change_isbn(self,book,prm_old_isbn,prm_new_isbn):
      bol_changed = False
      str_mess = ""
      if book and book.isbn == prm_old_isbn:
        bol_can_remove = False
        bol_can_add = False        
        bol_can_remove = not self.check_newisbn(prm_old_isbn)
        bol_can_add = self.check_newisbn(prm_new_isbn)
        if bol_can_remove == True and bol_can_add == True:
          self.remove_isbn(prm_old_isbn)
          self.store_isbn(prm_new_isbn)
          book.isbn = prm_new_isbn
          bol_changed = True
          str_mess = "ISBN changed from " + str(prm_old_isbn) + " to " + str(prm_new_isbn)
        else:
          str_mess = "An invalid new isbn can not be added"
      else:
        str_mess = "Unable to update isbn. The old isbn does not match with the book."

      print(str_mess)
      return(bol_changed)

    
    def get_worth_of_user(self, user_email):
      rtn_flt_amount = 0
      bol_good_email = fun_validemail(user_email)
      if bol_good_email == True:
        curr_user = self.users[user_email]
        if curr_user:
          rtn_flt_amount = curr_user.get_worth_of_collection()
      else:
        print("Unable to find a user with email " + user_email + "\n Can not evaluate book collection value.") 
      return(rtn_flt_amount)


    def get_n_most_read_books(self, prm_int_top_amt):
        rtn_lst_books = []
        lst_times_read = []
        lst_times_read = list(self.books.values())
        lst_times_read.sort()       #low-high
        lst_times_read.reverse()    #high-low
        int_max_books = len(lst_times_read)
        bol_stop_count = False
      
        int_max_rtn = min(prm_int_top_amt,int_max_books)
        if int_max_rtn >= 1:
            int_add_elmnt = 0
            dct_compare_books = self.books.copy()
            for int_loop_count in range(0,int_max_rtn):
                for book_cmp,book_read in dct_compare_books.items():
                    if book_read == lst_times_read[int_loop_count]:
                        int_add_elmnt += 1
                        rtn_lst_books.append(book_cmp)
                        dct_compare_books[book_cmp] = 0
                        if int_add_elmnt == int_max_rtn:
                            bol_stop_count = True
                        if bol_stop_count == True:
                          break
                if bol_stop_count == True:
                  break
            if prm_int_top_amt > int_max_books:
                print("There are only",int_max_books,"books can not return",prm_int_top_amt,"books.")
        return(rtn_lst_books)
    
                
    def get_n_most_prolific_readers(self, prm_int_top_readers):
        dct_compare_readers = {}    #user_object:num_books_read
        lst_num_books = []          #num_books_read
        rtn_lst_readers = []
        bol_stop_count = False
        for reader in self.users.values():
            if reader:
                int_num_books = reader.get_number_books()
                if int_num_books >= 1:
                    dct_compare_readers[reader] = int_num_books
                    lst_num_books.append(int_num_books)
               
        int_max_readers = len(dct_compare_readers)
        lst_num_books.sort()
        lst_num_books.reverse()
        int_max_rtn = min(prm_int_top_readers,int_max_readers)
        int_add_elmnt = 0
        for int_loop_count in range(0,int_max_rtn):
            for reader_cmp,books_bought in dct_compare_readers.items():
                if books_bought == lst_num_books[int_loop_count]:
                    int_add_elmnt += 1
                    rtn_lst_readers.append(reader_cmp)
                    dct_compare_readers[reader_cmp] = 0
                    if int_add_elmnt == int_max_rtn:
                        bol_stop_count = True
                        if bol_stop_count == True:
                            break
            if bol_stop_count == True:
                break

        if prm_int_top_readers > int_max_readers:
            print("There are only",int_max_readers,"users with book collections, can not return",prm_int_top_readers,"readers.")

        return(rtn_lst_readers)


    def get_n_most_expensive_books(self, prm_int_pricey_books):
        dct_compare_books = {}      #book_object:price
        lst_book_prices = []        #book_price
        rtn_lst_books = []
        bol_stop_count = False

        for book in self.books:
            if book:
                flt_book_price = book.get_price()
                if flt_book_price >= 0:
                    dct_compare_books[book] = flt_book_price
                    lst_book_prices.append(flt_book_price)
                    
        int_max_books = len(dct_compare_books)
        lst_book_prices.sort()
        lst_book_prices.reverse()
        int_max_rtn = min(prm_int_pricey_books,int_max_books)
        int_add_elmnt = 0
        for int_loop_count in range(0,int_max_rtn):
            for book_cmp,book_price in dct_compare_books.items():
                if book_price == lst_book_prices[int_loop_count]:
                    int_add_elmnt += 1
                    rtn_lst_books.append(book_cmp)
                    dct_compare_books[book_cmp] = 0
                    if int_add_elmnt == int_max_rtn:
                        bol_stop_count = True
                        if bol_stop_count == True:
                            break
            if bol_stop_count == True:
                break

        if prm_int_pricey_books > int_max_books:
            print("There are only",int_max_books,"users with book collections, can not return",prm_int_pricey_books,"books.")

        return(rtn_lst_books)                   


    def sendmailer(self, prm_str_event, prm_str_reason ,prm_user_obj,prm_lst_of_books):        
        flt_discount = 0
        str_emailheader = ""
        str_emailsubject = ""
        str_emailbody = "" 
        flt_reg_price = 0
        flt_dis_price = 0
        book_obj = None
        
        if type(prm_lst_of_books) == list:
          int_num_books = len(prm_lst_of_books)
        else:
          int_num_books = 1
          
        if not fun_isblank(prm_str_event) and prm_user_obj and int_num_books  > 0:
            
            str_emailheader = "From: TomeRator Book Club \n" + "To: " + prm_user_obj.get_email() 
            str_emailbody = "     Hello " + prm_user_obj.name + ", \n"
            
            if prm_str_event == "New Book":
                str_emailsubject = "Subject: !! New Book Added !! "
                try:
                    
                    if int_num_books > 1:
                      book_obj = prm_lst_of_books[0]
                    else:
                      book_obj = prm_lst_of_books
                      
                    if fun_isblank(prm_str_reason):
                        prm_str_reason = "General"

                    if prm_str_reason == "General":
                        flt_discount = 0.05 #5%
                    elif prm_str_reason == "Author":
                        flt_discount = 0.08 #8%
                    elif prm_str_reason == "Genre":
                        flt_discount = 0.10 #10%
                    str_emailbody += "       We wanted to let you know we just got a new book " + book_obj.title
                    if hasattr(book_obj,"author"):
                        str_emailbody += " by author " + book_obj.author
                    if not fun_isblank(book_obj.genre):
                        str_emailbody += " under the genre of " + book_obj.genre + ". \n"
                    flt_reg_price = book_obj.price
                    if flt_discount > 0:
                       flt_dis_price = flt_reg_price * (1 - flt_discount)

                    if flt_dis_price > 0:
                       str_emailbody += "      Being a club member allows you to get this book in the next month not for ${:0.2F}".format(flt_reg_price) + " but at the discounted price of ${:0.2F}".format(flt_dis_price)
                    else:
                       str_emailbody += "This book is available to you at the great price of ${:0.2F}".format(flt_reg_price)
                       
                    str_emailbody += "\n \n \n     Thank you for being a reader with us. \n"
                    
                    print("-"*40)
                    print(str_emailheader)
                    print(str_emailsubject)
                    print("-"*40)
                    print(str_emailbody)
                    print("=-"*50,"\n")
                    
                except ValueError:
                  pass
                except TypeError:
                   pass
                
                
            elif prm_str_event == "Recommend":
                str_emailsubject = "Subject: Book Recommendation(s)"
                
                if fun_isblank(prm_str_reason):
                    prm_str_reason = "General"                    

                if prm_str_reason == "General" :
                    flt_discount = 0.05 #5%
                    str_emailbody += "       We found a few recommendations of books based on you preferences \n"
                    
                elif prm_str_reason == "FirstOfMonth":
                    flt_discount = 0.08 #8%
                    str_emailbody += "       It is the first of the month and we have few recommendations of books based on you preferences \n"
                elif prm_str_reason == "Clearance-1":
                    flt_discount = 0.20 #20%
                    str_emailbody += "       We are having a 20% off clearance we have few recommendations of books you may want to consider \n"
                elif prm_str_reason == "Clearance-2":
                    flt_discount = 0.30 #30%
                    str_emailbody += "       We are having a 30% off clearance we have few recommendations of books you may want to consider \n"
                elif prm_str_reason == "MustGo":
                    flt_discount = 0.50 #50%
                    str_emailbody += "       We wanted you to know that we are have a must go clearance with up to 50% off. Don't miss out this is your chance to get \n"                    
                for int_loop in range(0,int_num_books):
                    try:
                        if int_num_books > 1:
                          book_obj = prm_lst_of_books[int_loop]
                        else:
                          book_obj = prm_lst_of_books[0]
                      
                        str_emailbody += "     " + book_obj.title
                        flt_reg_price = book_obj.price
                        
                        if hasattr(book_obj,"author"):
                            str_emailbody += " by author " + book_obj.author
                            
                        if not fun_isblank(book_obj.genre):
                            str_emailbody += " under the genre of " + book_obj.genre                                       
                        
                        if flt_discount > 0:
                           flt_dis_price = flt_reg_price * (1 - flt_discount)

                        if flt_dis_price > 0:
                           str_emailbody += " regular price  ${:0.2F}".format(flt_reg_price) + " discount to ${:0.2F}".format(flt_dis_price) + "\n"
                        else:
                           str_emailbody += " for the great price of  ${:0.2F}".format(flt_reg_price) + "\n"

                        str_emailbody += "\n \n \n     Thank you for being a reader with us. \n"

                        print("-"*40)
                        print(str_emailheader)
                        print(str_emailsubject)
                        print("-"*40)
                        print(str_emailbody)
                        print("=-"*50,"\n")                    
                    
                    except ValueError:
                        pass
                    except TypeError:
                       pass       
        else:
            print("All the infomation needed to send mailers is not present.")


    def new_book_mailer(self,prm_book_obj):        
        str_book_author = ""
        str_book_genre = ""
        lst_used_users = []
        if prm_book_obj:
            str_book_genre = prm_book_obj.genre
            if hasattr(prm_book_obj,"author"):
              str_book_author =  prm_book_obj.author
              if not fun_isblank(str_book_author):
                for curr_user in self.users.values():
                    if not fun_isblank(curr_user.fav_author) and ( curr_user.fav_author == str_book_author or curr_user.fav_author.find(str_book_author) >=0):
                        self.sendmailer("New Book", "Author" ,curr_user,prm_book_obj)
                        lst_used_users.append(curr_user)
                    
            if not fun_isblank(str_book_genre):
                for curr_user in self.users.values():
                    if lst_used_users.count(curr_user) == 0:
                        self.sendmailer("New Book", "Genre" ,curr_user,prm_book_obj)
                        lst_used_users.append(curr_user)
              
            for curr_user in self.users.values():
                if lst_used_users.count(curr_user) == 0:
                  self.sendmailer("New Book", "" ,curr_user,prm_book_obj)
                  
                        
    def recommnd_books(self,prm_str_event):
        for curr_user in self.users.values():
            int_rmmnd_count = 0
            lst_rmmnd_books = []
            lst_of_collection = []
            if not fun_isblank(curr_user.fav_genre) or not fun_isblank(curr_user.fav_author):
                lst_of_collection = curr_user.get_my_books()
                int_num_books = len(lst_of_collection)
                for chk_book in self.books.keys():
                    if int_num_books > 1 and lst_of_collection.count(chk_book) > 0:
                        pass
                    else:
                        # Assumes one genre per book
                        if chk_book.genre.upper() in curr_user.fav_genre.upper():
                            int_rmmnd_count +=1
                            lst_rmmnd_books.append(chk_book)
                        else:
                            # Assumes one author per book
                            if hasattr(chk_book,"author"):
                                if chk_book.author.upper() in curr_user.fav_author.upper():
                                    int_rmmnd_count +=1
                                    lst_rmmnd_books.append(chk_book)
                                                                
                        if int_rmmnd_count == 5:
                            break
                        
                if int_rmmnd_count > 0:
                    #print("!!!! TESTING recommnd_books ",prm_str_event,"count",int_rmmnd_count,"User ", curr_user,lst_rmmnd_books,"   !!!")
                    self.sendmailer("Recommend", prm_str_event,curr_user,lst_rmmnd_books)

      
    def __repr__(self):
      str_mess = "TomeRater has " + str(len(self.users)) + " readers and " + str(len(self.all_isbns)) + " unquie books."
      return(str_mess)
        

    def __eq__(self, other_TomeRater):
      rtn_equal = False
      if self.users.keys() == other_TomeRater.users.keys() and self.all_isbns == other_TomeRater.all_isbns:
        rtn_equal = True
      return(rtn_equal)
      
# END CLASS TOMERATER




    
