 # -*- coding: utf-8 -*-
# /usr/bin/env python2
#Bu dosya uzmanlık hesabına kadar (uzmanlık dahil) hesaplamalarda kullanılan fonksiyonları içerir.gerekli değerler (bu script tarafından) veritabanından alınır/veritabanına koyulur.. Hesaplama  fonksiyonları tek tek dogru sıra ile kullanılmalıdır.

#not: product ve content aynı anlamdadır. db database anlamındadır.
#import sqlite3
import MySQLdb
import numpy as np

class functions:
    #
    # productID=0
    # userID=0
    #
    # qualityOfProduct=0  # qj :    quality of content (AKA product) j
    # evaluatedUserSet=[] # U(qj):  set of users that evaluated the content
    # rating=0            # rij:    the rating value that user i(Ui) gave for content j  0<=rating<=1
    # credibilityOfUser=0 # ui-c:   credibility of user i on the content j's category
    #
    # associationMatrix=[] #A
    # preferenceMatrix=[]  #P
    # extendedPrefMatrix=[] #p*a
    categoryCount=4
    usercount=10
    categories=[1,2,3,4]


    def __init__(self):
        pass

    def connectToDB(self):


#FOR MYSQL
        try:
            self.conn= MySQLdb.connect(
                                host ="127.0.0.1", #mysql ip adresi
                                user="root",         # your username
                                passwd="",          #veritabanı parolası
                                # db="trustdatabase"
                                db="fakedb"   # name of the data base
                                 )
        except  Exception as e:
            print e


    # ########FOR SQLITE
    # def connectToDB(self):#tries to connect to db. creates connection object
    #     try:
    #         self.conn = sqlite3.connect('trustdatabase.sqlite3')
    #         # self.conn = sqlite3.connect('fakedb.sqlite3')
    #         print "db connection is ok"
    #     except Exception as e:
    #         print(e)
    def disconnectFromDB(self):
        try:
            self.conn.close()
        except Exception as e:
            print e



    def evaluatedUsersList(self,contentID): #takes content id, returns a list of userID's that evaluated the content
        evaluatedUserSet=[] # U(qj):  set of users that evaluated the content
        query1=("Select {} from {} Where {}={}".format("userID","Ratings","productID",int(contentID)))
        cursor = self.conn.cursor()
        cursor.execute(query1)
        try:
            evaluatedUserSet = cursor.fetchall()

        except Exception as e:
            print (e)
        if len(evaluatedUserSet)>0:
            return evaluatedUserSet
        else:
            print "no user that evaluated the content found!"
            return evaluatedUserSet
    def evaluatedContents(self,userID,categoryID=0):
        #takes an userID returns a contentID list that evaluated by given user. supply categoryID for a specific category(otherwise all categories)
        contentIDlist=[]
        if categoryID==0:
            query1=("Select {} from {} Where {} ={}".format("productID","Ratings","userID",int(userID)))
        elif categoryID!=0:
            query1=("Select {} from {} Where {}={} AND {}={}".format("productID","Ratings","userID",int(userID),"categoryID",int(categoryID)))
        else:
            query1=("Select {} from {} Where {}={} AND {}={}".format("productID","Ratings","userID",int(userID),"categoryID",int(categoryID)))

        cursor = self.conn.cursor()
        cursor.execute (query1)
        try:
            contentIDlist = cursor.fetchall()

        except Exception as e:
            print (e)

        if len(contentIDlist) <=0:
            print "no content found that evalueted by given user"
            return contentIDlist
        else:
            return contentIDlist
    def givenRating(self,userID,contentID):
        # returns the given rating by userid for  contentid
        rating=None            # rij:    the rating value that user i(Ui) gave for content j  0<=rating<=1
        ##!!!! returns 1<=rating<=5
        query1=("Select {} from {} Where {}={} AND {}={} ".format("rating","Ratings","productID",int(contentID),"userID",int(userID)))
        cursor = self.conn.cursor()
        cursor.execute(query1)
        try:
            rating = cursor.fetchone()

        except Exception as e:
            print (e)

        if rating == None:
            print "no rating found for the product (AKA content) by given user"
            return None
        else:
            return rating[0]


    def getUserCredibility(self, userID, categoryID):

        #returns credibilty value of a given user for a category (from database)
        credibility=None
        query1=("Select {} from {} Where {}={} AND {}={} ".format("credibility","User","userID ",int(userID)," categoryID",int(categoryID)))

        cursor = self.conn.cursor()
        cursor.execute(query1)
        try:
            credibility = cursor.fetchone()

        except Exception as e:
            print (e)

        if credibility==None:
            # print "no credibility value found in the category for given user" FOR INFO NEEDS
            return None
        else:
            return float(credibility[0])
    def getUserExpertise(self, userID,categoryID):
        #returns expertise of a user in a category
        expertise=None
        query1=("Select {} from {} Where {}={} AND {}={} ".format("expertise","User","userID",int(userID)," categoryID",int(categoryID)))
        cursor = self.conn.cursor()
        cursor.execute(query1)
        try:
            expertise = cursor.fetchone()

        except Exception as e:
            print (e)

        if expertise[0]==None or expertise==None:
            # print "no expertise value found in the category for given user"
            return None
        else:

            return float(expertise[0])
    def getEvaluatedCategoriesForUser(self,userID):
        #returns list of category ids that evaluated by given userid
        categorylist=None
        query1=("Select DISTINCT categoryID from Ratings Where userID ={} ".format(int(userID)))
        cursor = self.conn.cursor()
        toReturn=[]
        try:
            cursor.execute(query1)
            categorylist = cursor.fetchall()

        except Exception as e:
            print (e)

        if categorylist==None:
            print "no rating found for given user"
            return None
        else:
            for category in categorylist:
                toReturn.append(category[0])

            return toReturn
            # return categorylist



        pass
    def getQualityOfContent(self,productID):
        #returns quality of a content
        quality=None
        query1=("Select {} from {} Where {}={}  ".format("quality","Product"," productID",int(productID)))
        cursor = self.conn.cursor()
        cursor.execute(query1)
        try:
            quality = cursor.fetchone()

        except Exception as e:
            print (e)

        if quality==None:
            # print "no quality value found for given content" FOR INFO NEED
            return None
        else:
            return float(quality[0])
    def getCategoryOfContent(self,contentID):
        #returns categoryid of given content
        categoryID=None
        query1=("Select {} from {} Where {}={} Limit 1 ".format("categoryID","Ratings","productID",int(contentID)))
        cursor = self.conn.cursor()
        cursor.execute(query1)
        try:
            categoryID = cursor.fetchone()

        except Exception as e:
            print (e)

        if categoryID==None:
            print "cant found a category for given content"
            return None
        else:
            return int(categoryID[0])


    def setUserCredibility(self,userID,categoryID, credibility):
        #sets credibility of a user on a category
        query1 = ("Update {} set {}={} Where {}={} AND {}={} ".format("User","credibility",float(credibility),"userID",
                                                                      int(userID)," categoryID",int(categoryID)))
        query2= ("insert into {} ( {} )  values( {} ,{} ,{} ,{} ) ".format("User",
                    "expertise,credibility,userID,categoryID","Null",float(credibility),int(userID),int(categoryID)))
        result=None

        cursor = self.conn.cursor()
        result=self.getUserCredibility(int (userID),int(categoryID))

        if result==None: # if there is no credibility value then insert it
            try:

                cursor.execute(query2)
                # self.conn.commit() forperformance
            except Exception as e:

                print (e)
        else: # if there is already a credibility value then update it
            try:
                cursor.execute(query1)
                # self.conn.commit()forperformance
            except Exception as e:

                print (e)
        # self.conn.commit() # didnt use here because of performance issuesS
    def setUserExpertise(self,userID,categoryID,expertise):
#sets expertise value to db for a user on a category.
        query1 = ("Update {} set {}={} Where {}={} AND {}={} ".format("User","expertise",float(expertise),"userID",int(userID)," categoryID",int(categoryID)))
        # query2= ("insert into {} ( {} )  values( {} ,{} ,{} ,{} ) ". format("User", "expertise,credibility,userID,categoryID",float(expertise),"Null",int(userID),int(categoryID)))

        cursor = self.conn.cursor()

        ######################
        #IN CASE FOR NEED TO INSERT
        # result=self.getUserExpertise(userID,categoryID)

        # if result == None:  # if there is no expertise value then insert it
        #     try:
        #
        #         cursor.execute(query2)
        #
        #     except Exception as e:
        #
        #         print (e)
        # else:  # if there is already a expertise value then update it
        #     try:
        #         cursor.execute(query1)
        #
        #     except Exception as e:
        #
        #         print (e)

        ######################

        try:
            cursor.execute(query1)

        except Exception as e:

            print (e)



        # self.conn.commit() #didnt use here bacause of performance issues
    def setQualityOfContent(self,productID,quality):
        #Sets quality of content. İf already there is a value, tthen updates it, otherwise inserts to db
        query1 = ("Update {} set {}={} Where {}={} ".format("Product","quality",float(quality),"productID",int(productID)))
        query2= ("insert into {} ( {} )  values( {} ,{} ) ". format("Product", "productID,quality",int(productID),float(quality)))
        # print query2
        cursor = self.conn.cursor()
        result=self.getQualityOfContent(productID=int(productID))

        if result == None:  # if there is no expertise value then insert it
            try:

                cursor.execute(query2)
                # self.conn.commit() #TODO TEST
            except Exception as e:

                print (e)
        else:  # if there is already a expertise value then update it
            try:
                cursor.execute(query1)
                self.conn.commit()
            except Exception as e:
                print e


    def evaluateCredibilityOfUser(self,userID,categoryID,mode=None):
        # evaluates credibility of a user on a category and returns it (doesnt set to database)
        #for mode="initial", function takes quality of content a 0.5 always you can use this as initial calculation. This method used for performance concerns
        #İf mode wasnt supplied then no problem. İf value not found, it is used as 0.5 again, otherwise real value used (from db)

        # if you need to set value to database then use appropriate commented outed line.
        evaluatedContentIDlist=self.evaluatedContents(int(userID) , int(categoryID))
        numberOfEvaluation= len(evaluatedContentIDlist)

        summ=0

        qualityOfContent=0.5

        if mode=="initial":
            qualityOfContent=0.5
            for contentID in evaluatedContentIDlist:

                # print  self.givenRating(userID,contentID[0])[0]
                summ=summ+(1-abs(qualityOfContent-(int(self.givenRating(userID,contentID[0])))/5.0))

            credibilityOfUser=(1-(  1/(float(numberOfEvaluation+1))  )) * (summ/float(numberOfEvaluation))

            # print "credibilityOfUser id(",userID,")=",str( credibilityOfUser)


            # self.setUserCredibility(int(userID),int(categoryID),float(credibilityOfUser)) IF NEED TO PRINT TO DATABASE HERE

        else:
            for contentID in evaluatedContentIDlist:

                # print  self.givenRating(userID,contentID[0])[0]
                qualityOfContent=self.getQualityOfContent(contentID[0])
                if qualityOfContent==None:
                    qualityOfContent=0.5
                summ=summ+(1-abs(qualityOfContent-(int(self.givenRating(userID,contentID[0])))/5.0))

            credibilityOfUser=(1-(  1/(float(numberOfEvaluation+1))  )) * (summ/float(numberOfEvaluation))

            # print "credibilityOfUser id(",userID,")=",str( credibilityOfUser)


        # self.setUserCredibility(int(userID),int(categoryID),float(credibilityOfUser)) IF NEED TO PRINT TO DATABASE HERE
        return credibilityOfUser
    def evaluateQualityOfContent(self,contentID):
        # evaluates quality of a content ( qj  ) and returns it
        # take note values came from db implicitly via used functions
        userIDlist=self.evaluatedUsersList( int(contentID) )

        categoryID=self.getCategoryOfContent(int(contentID))

        sumofproduct=0
        sumofcredibilities=0
        for userID in userIDlist:

            userCredibility=self.getUserCredibility(userID[0],categoryID)
            sumofcredibilities=sumofcredibilities+userCredibility
            # sumofcredibilities=sumofcredibilities+0.5 testing
            # print sumofcredibilities

            sumofproduct=sumofproduct+(userCredibility*(self.givenRating(userID[0],contentID)/5.0)) # /5 to map 1<rating<5 to 0<rating<1
            # sumofproduct=sumofproduct+0.5*0.5 testing
            # print sumofproduct
        return sumofproduct/float(sumofcredibilities)
    def evaluateExpertiseOfUser(self,userID,categoryID):
        # evaluates expertise of a user on a category and returns it
        evaluatedContentIDlist=self.evaluatedContents( int(userID), int(categoryID) )
        numberOfEvaluation= len(evaluatedContentIDlist)
        sumofquality=0
        for contentID in evaluatedContentIDlist:
            sumofquality=sumofquality+ self.getQualityOfContent(contentID[0])
            # sumofquality=sumofquality+ 0.5
        expertise=( 1-(1/float((numberOfEvaluation+1)))          ) * (sumofquality/float(numberOfEvaluation)   )
        return expertise


    def evaluateAllUsersCredibility(self,mode=None):
        #using another function, this function evaluates all users credibility in db and sets them to database.Also prints to the screen
        query="Select DISTINCT userID,categoryID from Ratings order by UserID asc"
        results=None

        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            # print results
        except Exception as e:
            print (e)


        for result in results:
            # print result
            credibility= self.evaluateCredibilityOfUser(userID=int(result[0]),categoryID=int (result[1]),mode=mode)
            self.setUserCredibility(userID=int(result[0]),categoryID=int (result[1]),credibility=credibility)
            print "credibility for userid(",result[0],") in categoryid(",result[1],")=",credibility
    def evaluateAllUsersExpertise(self):
        #evaluates all users expertise value in db, sets to db and also prints to the screen
        query="SELECT distinct userID,categoryID from Ratings where categoryID in (select distinct categoryID from Ratings )  order by userID"
        results=None

        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()

        except Exception as e:
            print (e)

        # print results
        for result in results:
            # print result
            expertise= self.evaluateExpertiseOfUser(userID=int(result[0]),categoryID=int (result[1]))

            self.setUserExpertise(userID=int(result[0]),categoryID=int (result[1]),expertise=expertise)
            print "expertise value of userid(",int(result[0]),")"," in categoryid(",int(result[1]),")=" , expertise
    def evaluateAllContentsQuality(self):
        #evaluates all contents quality in db and sets values to db . Also prints to screen
        query="Select DISTINCT productID from Ratings"
        results=None

        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()

        except Exception as e:
            print (e)

        # print results
        # x=0
        # print results
        for result in results:
            # x=x+1
            # print "entry =" ,x
            # print result
            try:
                quality= self.evaluateQualityOfContent (contentID= int(result[0]))
                print  "Quality for productid(",result[0],")=",quality
                self.setQualityOfContent (productID= int(result[0]), quality=quality)
            except Exception as e :
                print "exception for contentid(",result[0],")", e
        # self.conn.commit() #didnt use in setQualityOfContent for performance purposes


    def evaluateAllCategoryAssociationMatrix(self):
        #evaluates A matrix, Then sets it to db
        #note: I didnt test this function on big dataset
        query="Select distinct categoryID from Ratings"

        result=None
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            # print result2
        except Exception as e:
            print (e)

        # print result
        associationmatrix=[]

        for category1 in result:
            for category2 in result:
                if category1[0]!=category2[0]:
                    c1c2=self.evaluateSupportc1c2(category1[0],category2[0])
                else:
                    c1c2=1
                associationmatrix.append([category1[0],category2[0],c1c2])
        self.setAllCategoryAssociation(associationmatrix)
        return associationmatrix
    def setAllCategoryAssociation(self,array):
        #sets (insert into) category association values array format=> [[category1, category2, association_value], [categorym, categoryn, association_valuen]]
        #this function used by evaluateAllCategoryAssociationMatrix
        #note: I didnt test this function on big dataset
        for one in array:
            category1=one[0]
            category2=one[1]
            value =one[2]

            query= ("insert into categoryAssociation ( category1,category2,value )  values( {} ,{} ,{} ) ".format(category1,category2,value))

            cursor = self.conn.cursor()

            try:
                cursor.execute(query)
            except Exception as e:
                print (e)
    def setUserCategoryPreferance(self,userid,categoryid,value):
        #sets a users category preference value to db (for given category)



        # print userid,categoryid,value

        query2= ("insert into {} ( {} )  values( {} ,{},{} ) ". format("UserPreference", "userID,categoryID,value",int(userid),int(categoryid),float(value)))
        # print query2
        cursor = self.conn.cursor()

        try:

            cursor.execute(query2)
            # self.conn.commit() #TODO TEST
        except Exception as e:
            print e
    def evaluateSupportc1c2(self,categoryID1,categorID2):
        #returns support for categoryID1 on categoryıd2
        query1="Select distinct userID from Ratings where categoryID={} And userID in (select userid from Ratings where categoryID={}) group by userID ".format(categoryID1,categorID2)
        query2="Select distinct userID from Ratings where categoryID={} group by userID ".format(categoryID1)

        result2=None
        cursor = self.conn.cursor()
        try:
            cursor.execute(query2)
            result2 = cursor.rowcount
            # print result2
        except Exception as e:
            print (e)

        if result2==None or result2==0:
            return 0

        else:
            result1=None
            try:
                cursor.execute(query1)
                result1 = cursor.rowcount
            except Exception as e:
                print (e)

            if result1==None:
                print "bir hata olustu"

            else :
                return result1/float(result2)
    def calculateEvaluationPrefForUser(self,userid):
        #returns  rate of rating number for each category (with category ids) given by a  user
        #rate1= rating count for category1 / all rating count
        #format of output
        # [[pref_value1,categoryid1),[pref_value2,categoryidx]]
        query="Select count(*),categoryID from Ratings where userID={} group by categoryID".format (userid)
        result=()
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except Exception as e:
            print (e)

        # print result

        if result==():
            print "no rating found by userid {} for any category".format(userid)
        else :
            toReturn=[]
            allRatingCountsForUser=float (self.getCountsOfAllRatingsGivenFromAuser(userid))#
            # print allRatingCountsForUser
            for category_count in result:
                toReturn.append([category_count[0]/allRatingCountsForUser,category_count[1]])

            return toReturn
    def evaluateAllUserCategoryEvaluationPreferences(self):
        #Calculates pe values, Prints to the screen. Also set pref. values to db
        #printing format=>
        #Evaluation preference for userid(1) is [[pref_value1, categoryid1], [pref_value2, categoryid2]]
        #Evaluation preference for userid(2) is [[pref_value1, categoryid1], [pref_value2, categoryid2]]
        #Note: WARNING This functions doesnt count 0 (for preference ) values. If you use values supplied by this function, use manuelly 0 for unknown values.
        #Pe
        query="select distinct userID from Ratings order by userID"
        results=None
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            # print results
        except Exception as e:
            print (e)
        # print results # all user id list
        for userid in results:
            prefArray=self.calculateEvaluationPrefForUser(userid[0])
            print "Evaluation preference for userid({}) is {}".format(userid[0],prefArray)
            for each in prefArray:
                self.setUserCategoryPreferance(userid=userid[0],categoryid=each[1],value=each[0])

    def setAssociationMatrixToNumpy(self):
        #reads category association (A matrix) values into a numpy array (from db). Array name is associationMatrix and it is global
        #note: (since array indices start from 0 but category ids from 1) index number is mines one for a category
        query1=("Select * from categoryAssociation ")
        cursor = self.conn.cursor()
        cursor.execute(query1)
        try:
            result = cursor.fetchall()

        except Exception as e:
            print (e)
        # print result

        self.associationMatrix=np.zeros(shape=(self.categoryCount,self.categoryCount))
        for one in result:
            # print int (one[0]),int(one[1]),float(one[2])
            self.associationMatrix[int (one[0])-1][int(one[1])-1]=float(one[2])
        print self.associationMatrix

    def setUserPreferenceMatrixToNumpy(self):
        #reads user preference (p matrix) values into a numpy array (from db). Array name is preferenceMatrix and it is global
        #note: (since array indices start from 0 but category ids from 1) index number is mines one for a category
        query1=("Select * from UserPreference ")
        cursor = self.conn.cursor()
        cursor.execute(query1)
        try:
            result = cursor.fetchall()

        except Exception as e:
            print (e)
        # print result

        self.preferenceMatrix=np.zeros(shape=(self.usercount,self.categoryCount))
        for one in result:
            # print int (one[0]),int(one[1]),float(one[2])
            self.preferenceMatrix[int (one[0])-1][int(one[1])-1]=float(one[2])
        print self.preferenceMatrix

    def multiplyAssociaionAndPreference(self):
        #multiplies preferenceMatrix and associationMatrix (that are global) to get extended matrix (extendedPrefMatrix) (P*=P*A)
        #note: (since array indices start from 0 but category ids from 1) index number is mines one for a category
        np.set_printoptions(threshold='nan')
        self.extendedPrefMatrix= np.dot(self.preferenceMatrix,self.associationMatrix)
        np.savetxt('extendedPrefs.txt',self.extendedPrefMatrix,fmt='%f')
        np.save('extendedPrefs',self.extendedPrefMatrix)
        print self.extendedPrefMatrix


    def evaluateNeededEPTrByArray2(self,userid1,userid2):
        #evaluates userid1's EPTr to userid2 then prints result to the screen

        extendedPreferences=np.load('extendedPrefs.npy')


        sumup=0
        sumdown=0
        try:
            for category in self.categories:

                # print bi[0]
                qr1=extendedPreferences[userid1-1][category-1]
                # print qr1
                query2="select expertise from User where userID={} and categoryID={}".format(userid2,category)
                # print query2
                cursor = self.conn.cursor()

                try:
                    cursor.execute(query2)
                    qr2=cursor.fetchone()


                except Exception as e:
                    print (e)

                if qr2==None:
                    qr2=[0]

                # print qr1[0]
                # print qr2[0]

                result=qr1*qr2[0]
                # print result
                sumup=sumup+result
                sumdown=sumdown+qr1

            print "contentuser",userid1 ,"'s trust to contentuser",userid2 ,"is", sumup/float(sumdown)
            message=str(userid1)+',' +str(userid2)+',' +str(sumup/float(sumdown))
        except Exception as e:
            print ('hata:','satir','contentuser',userid1,'contentuser',userid2,'detay:',e)
            message='ERROR:'+str(userid1)+','+str(userid2)+','+str(e)
        return message
    def evaluateNeededEPTrForTextfile(self,filename):
        #this function takes a filename then evaluates all user pairs eptr value. Output is printed to screen# also prints to the eptrs.txt file
        #file format must be
        #userid1,userid2
        #useridn,useridm
        #uses evaluateNeededEPTrByArray2 function
        outputfile=open ('eptrs.txt','w')

        the_file=open(filename, 'r')

        for line in the_file:
            x=line.replace(u'\n','').split(',')

            message=self.evaluateNeededEPTrByArray2(int(x[0]),int(x[1]))

            outputfile.write(message+'\n')
        outputfile.flush()
        outputfile.close()
    def getCountsOfGivenRatingInACategoryForUser(self,userid,categoryid):
        # evaluating count for a user in a category
        query="Select count(*) from Ratings where userID={} And categoryID={}".format (userid,categoryid)
        result=()
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchone()
        except Exception as e:
            print (e)
        if result[0]==0:
            print "no rating found for  categoryid {} for userid {}".format(categoryid,userid)
        else :
            return result[0]
    def getCountsOfAllRatingsGivenFromAuser(self,userid):
        query="Select count(*) from Ratings where userID={}".format (userid)
        result=()
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchone()
        except Exception as e:
            print (e)
        if result[0]==0:
            print "no rating found by userid {} for any category".format(userid)
        else :
            return result[0]


###########################################################################################################
###########################################################################################################
        #AFTER HERE THE FUNCTIONS SHOULDNT BE USED










    # def saveExtendedPreferenceTodb(self):
    #     extendedPreferences=np.load('carpim3.npy')
    #
    #     # print extendedPreferences
    #     for i in range(0,len(extendedPreferences)):
    #         for j in range(0,len(extendedPreferences[0]) ):
    #
    #
    #             preferenceValue=extendedPreferences[i][j]
    #             userid=i+1
    #             categoryid=j+1
    #             query="update User set extendedPreferenceValue={} where userID={} and categoryID={};".format(preferenceValue,userid,categoryid)
    #             print query
    #             # cursor = self.conn.cursor()
    #             # try:
    #             #     cursor.execute(query)
    #             #
    #             #
    #             # except Exception as e:
    #             #     print (e)
    #            #
    #             # self.conn.commit()

    def getAllUserCategoryPreferences(self):
        pass




























    def evaluateAllEPTr(self):

        users=range(1,22167)
        users.remove(20819)
        users.remove(21354)
        categories=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
        for contentProvider in users:
            for contentuser  in users:
                if contentuser==contentProvider:
                    break
                sumup=0
                sumdown=0
                for category in categories:
                    query1="select extendedPreferenceValue from User where userID={} and categoryID={}".format(contentuser,category)
                    # print query1
                    query2="select expertise from User where userID={} and categoryID={}".format(contentProvider,category)
                    # print query2
                    cursor = self.conn.cursor()
                    try:
                        cursor.execute(query1)
                        qr1=cursor.fetchone()


                    except Exception as e:
                        print (e)
                    try:
                        cursor.execute(query2)
                        qr2=cursor.fetchone()


                    except Exception as e:
                        print (e)
                    if qr1==None:

                        qr1=[0]
                    if qr2==None:
                        qr2=[0]

                    # print qr1[0]
                    # print qr2[0]

                    result=qr1[0]*qr2[0]
                    # print result
                    sumup=sumup+result
                    sumdown=sumdown+qr1[0]

                print "contentuser",contentuser ,"'s trust to contentProvider",contentProvider ,"is", sumup/float(sumdown)

    def evaluateAllEPTrByArray(self):
        extendedPreferences=np.load('carpim3.npy')
        users=range(1,22167)
        users.remove(20819)
        users.remove(21354)
        categories=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
        for contentuser in users:
            for contentProvider in users:

                sumup=0
                sumdown=0
                for category in categories:
                    qr1=extendedPreferences[contentuser-1][category-1]
                    query2="select expertise from User where userID={} and categoryID={}".format(contentProvider,category)
                    # print query2
                    cursor = self.conn.cursor()

                    try:
                        cursor.execute(query2)
                        qr2=cursor.fetchone()


                    except Exception as e:
                        print (e)

                    if qr2==None:
                        qr2=[0]

                    # print qr1[0]
                    # print qr2[0]

                    result=qr1*qr2[0]
                    # print result
                    sumup=sumup+result
                    sumdown=sumdown+qr1

                print "contentuser",contentuser ,"'s trust to contentProvider",contentProvider ,"is", sumup/float(sumdown)
    def evaluateNeededEPTrByArray(self):
        extendedPreferences=np.load('carpim3.npy')
        # trusts=np.load('trusts.npy')
        trusts=np.load('rastgeleikili.npy')
        # print trusts
        categories=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
        i=0
        for bi in trusts:

            i=i+1
            # if i<48200  :
            #     continue
            sumup=0
            sumdown=0
            try:
                for category in categories:

                    # print bi[0]
                    qr1=extendedPreferences[int(bi[0])-1][category-1]
                    query2="select expertise from User where userID={} and categoryID={}".format(bi[1],category)
                    # print query2
                    cursor = self.conn.cursor()

                    try:
                        cursor.execute(query2)
                        qr2=cursor.fetchone()


                    except Exception as e:
                        print (e)

                    if qr2==None:
                        qr2=[0]

                    # print qr1[0]
                    # print qr2[0]

                    result=qr1*qr2[0]
                    # print result
                    sumup=sumup+result
                    sumdown=sumdown+qr1

                print i,"contentuser",bi[0] ,"'s trust to contentProvider",bi[1] ,"is", sumup/float(sumdown)
            except Exception as e:
                print ('hata:','satir',i,'contentuser',bi[0],'contentprovider',bi[1],'detay:',e)

############### AFTER THİS POINT I TRIED TO FIX THE PROBLEM OF ONE PRODUCT IS IN TWO OR MORE CATEGORY. THIS IS DATASET SPECIFIC PROBLEM. (ONE PRODUCT HAS TO BELONG ONE CATEGORY FOR MY CODE.)

    def getCategoryForProblematicProducts(self,productID):
        query="select categoryid from (select categoryid, count (categoryid) as counts from ratings where productid={} group by categoryid) order by counts desc limit 1".format(productID)


        categoryID=None

        cursor = self.conn.cursor()
        cursor.execute(query)
        try:
            categoryID = cursor.fetchone()

        except Exception as e:
            print (e)

        if categoryID==None:
            print "cant found a category for given content"
            return None
        else:

            return int(categoryID[0])
    def evaluateQualityOfproblematicContent(self,contentID):
        userIDlist=self.evaluatedUsersList( int(contentID) )
        categoryID=self.getCategoryForProblematicProducts (int(contentID))

        sumofproduct=0
        sumofcredibilities=0
        for userID in userIDlist:

            userCredibility=self.getUserCredibility(userID[0],categoryID)
            # print userID[0]
            # print userCredibility
            if userCredibility==None:
                userCredibility=0.5
            sumofcredibilities=sumofcredibilities+userCredibility
            # sumofcredibilities=sumofcredibilities+0.5 testing
            # print sumofcredibilities

            sumofproduct=sumofproduct+(userCredibility*(self.givenRating(userID[0],contentID)/5.0)) # /5 to map 1<rating<5 to 0<rating<1
            # sumofproduct=sumofproduct+0.5*0.5 testing
            # print sumofproduct
        return sumofproduct/float(sumofcredibilities)
    def evaluateAllProblematicContentQuality(self):
        for i in [40,53,127,174,214,226,276,365,372,379,386,504,872,889,1082,1095,1269,1297,1305,1307,1373,1495,1524,1867,2398,2521,2525,2953,2983,2990,3223,3502,3547,3554,3559,3668,3681,3821,3870,4014,4486,4495,5210,5461,5648,5657,6803,7130,7282,7723,7840,8051,8242,8644,8654,8655,8680,8766,8917,8928,9265,10145,10310,10503,10640,10642,10928,10932,12388,12455,13063,13171,13279,14374,14393,14484,14771,15098,15194,16106,16312,16620,17718,17805,17980,18187,18550,18569,18656,18661,18732,18880,19600,19864,19913,20077,20126,21282,21497,21800,21915,21918,21994,22014,22143,22533,22540,22667,22907,23029,23051,23358,23374,23883,24126,24264,24810,24971,25043,25558,25587,25724,25807,25867,26146,26736,27148,27181,27761,27920,28138,29021,29036,29256,31188,31280,31428,31859,32068,32905,32955,33527,35226,35560,35735,36452,36613,37017,37087,37586,38085,38448,38837,40215,40836,42754,43344,43680,43790,46351,47239,47676,49784,50109,52473,53223,54065,55107,55673,56071,56634,57241,57332,58393,61156,63331,63344,63439,66196,68587,69097,69278,70458,70874,71088,71253,71588,71850,72475,72653,72759,74700,75561,75582,75864,78289,79458,82178,87205,88367,88769,90507,95425,95914,98176,98744,98889,105797,112139,115431,117851,117855,122398,122690,127814,138521,138935,140260,141634,146120,148816,148937,152384,153939,154706,157755,174574,178005,182463,188495,204742,204873,205181,205193,223893,252770]:

            quality=self.evaluateQualityOfproblematicContent (int (i))
            print i,quality
            self.setQualityOfContent(int(i),quality=quality)
    def updateProblematicContentCategories(self):
        for i in [40,53,127,174,214,226,276,365,372,379,386,504,872,889,1082,1095,1269,1297,1305,1307,1373,1495,1524,1867,2398,2521,2525,2953,2983,2990,3223,3502,3547,3554,3559,3668,3681,3821,3870,4014,4486,4495,5210,5461,5648,5657,6803,7130,7282,7723,7840,8051,8242,8644,8654,8655,8680,8766,8917,8928,9265,10145,10310,10503,10640,10642,10928,10932,12388,12455,13063,13171,13279,14374,14393,14484,14771,15098,15194,16106,16312,16620,17718,17805,17980,18187,18550,18569,18656,18661,18732,18880,19600,19864,19913,20077,20126,21282,21497,21800,21915,21918,21994,22014,22143,22533,22540,22667,22907,23029,23051,23358,23374,23883,24126,24264,24810,24971,25043,25558,25587,25724,25807,25867,26146,26736,27148,27181,27761,27920,28138,29021,29036,29256,31188,31280,31428,31859,32068,32905,32955,33527,35226,35560,35735,36452,36613,37017,37087,37586,38085,38448,38837,40215,40836,42754,43344,43680,43790,46351,47239,47676,49784,50109,52473,53223,54065,55107,55673,56071,56634,57241,57332,58393,61156,63331,63344,63439,66196,68587,69097,69278,70458,70874,71088,71253,71588,71850,72475,72653,72759,74700,75561,75582,75864,78289,79458,82178,87205,88367,88769,90507,95425,95914,98176,98744,98889,105797,112139,115431,117851,117855,122398,122690,127814,138521,138935,140260,141634,146120,148816,148937,152384,153939,154706,157755,174574,178005,182463,188495,204742,204873,205181,205193,223893,252770]:

            # quality=self.evaluateQualityOfproblematicContent (int (i))
            # print i
            category=self.getCategoryForProblematicProducts(i)
            print "contentid ",i,"is in category " ,category
            self.updateProblematicContentCategory(i,category)
    def updateProblematicContentCategory(self,productID,newcategory):
        query1 = ("Update {} set {}={} Where {}={} ".format("Ratings","categoryid",float(newcategory),"productID",int(productID)))
        # query2= ("insert into {} ( {} )  values( {} ,{} ,{} ,{} ) ". format("User", "expertise,credibility,userID,categoryID",float(expertise),"Null",int(userID),int(categoryID)))

        cursor = self.conn.cursor()

        try:
            cursor.execute(query1)

        except Exception as e:

            print (e)

