'''
    CRUD operation of products
'''
import MySQLdb
from ProductNotFoundException import ProductNotFoundException 
hostname = 'localhost'
username = 'root'
password = 'password'
database = 'test_database'



def  createProducts(productname,price,description):
    try:
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
        
                  
        strInsert="INSERT INTO product_details(name,price,description) VALUES(%s,%s,%s)"
    
        cr.execute(strInsert,([productname,price,description]))
            
        # save data to database
        conn.commit()
        print("Records added")
    except Exception as e:
        print(e)
        print("Exception Raised ")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

def  findProductById(productid):
    try:
        
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
        
                  
        findProductById="SELECT * FROM product_details where id=%s"
    
        cr.execute(findProductById,([productid]))
           
        product = cr.fetchone()
        
        # save data to database
        conn.commit()
        if(product == None):
            raise ProductNotFoundException("Product with id "+str(productid)+ " not found in record")
        else:
            return product
    except ProductNotFoundException as r:
        print(r)
        if conn:
            conn.rollback()
    except Exception as e:
        print(e)
        print("Exception Raised ")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

def  findProductByName(productname):
    try:
        
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
        
                  
        findProductByName="SELECT * FROM product_details where name=%s"
    
        cr.execute(findProductByName,([productname]))
           
        product = cr.fetchone()
        
        if(product == None):
            raise ProductNotFoundException("Product with name "+str(productname)+ " not found in record")
        else:
            return product
    except ProductNotFoundException as r:
        print(r)
        if conn:
            conn.rollback()
    except Exception as e:
        print(e)
        print("Exception Raised ")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()


def  findProducts():
    try:
        
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
        
                  
        findProducts="SELECT * FROM product_details"
    
        cr.execute(findProducts)
           
        products = cr.fetchall()
        
        if(products == None):
            raise ProductNotFoundException("Products not found in record")
        else:
            return products
    except ProductNotFoundException as r:
        print(r)
        if conn:
            conn.rollback()
    except Exception as e:
        print(e)
        print("Exception Raised ")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()


def deleteById(productid):
    
    try:
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
    
        strDelete="DELETE FROM product_details WHERE id=%s"
    
        #sending sql queries
        cr.execute(strDelete,([productid]))
        
        if(cr.rowcount == 0):
            raise ProductNotFoundException("Product with id "+str(productid)+ " not found in record. Unable to delete it")
        else:
            # save data to database
            conn.commit()
            return "Product with id "+str(productid)+ " deleted"
          
        #print("deleted")
    except ProductNotFoundException as r:
        print(r)
        if conn:
            conn.rollback()
    except Exception:
        print("Exception Raised")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

def updateProduct(productid,productname):
    
    try:
        # connecting to the mysql database
        conn= MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    
        # opening the cursor
        cr = conn.cursor()
    
        strDelete="UPDATE product_details SET name = %s WHERE id=%s"
    
        #sending sql queries
        cr.execute(strDelete,([productname,productid]))
        
        if(cr.rowcount == 0):
            raise ProductNotFoundException("Product with id "+str(productid)+ " not found in record. Unable to update it")
        else:
            # save data to database
            conn.commit()
            return "Product with id "+str(productid)+ " updated"
          
        #print("deleted")
    except ProductNotFoundException as r:
        print(r)
        if conn:
            conn.rollback()
    except Exception:
        print("Exception Raised")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
            

#Code which calls createProducts has to pass productname,price,description
#productname=input("Enter product name :")
#price=int(input("Enter price product :"))
#description=input("Enter product description :")
#createProducts(productname,price,description)

#Find Product By Id
#r= findProductById(21)
#print(r)

#Find Product By Name
r= findProductByName('iPhone 166666')
print(r)

#Find All
#print(findProducts())

#Delete By Id 
#productid = input("Enter product id to be deleted : ")
#print(deleteById(productid))


#Update Functionality
#productid = input("Enter product id to be updated : ")
#productname=input("Enter product name :")
#r= updateProduct(productid,productname)
#print(r)