# -*- coding: utf-8 -*-
# /usr/bin/env python2
#ana script dosyası budur. myfunctions.py de tanımlanan fonksiyonlar kullanılarak hesaplamalar burada yapılabilir.

#import sqlite3
import MySQLdb
import myfunctions
class trustNetwork:
    def __init__(self):
        pass

def main():
    obj=myfunctions.functions()
    obj.connectToDB()

    try:
        ############################## BEGIN ############FOR TEST PURPOSES
        ##################################################################
        # obj.test()
        # print obj.evaluatedUsersList(contentID=1)
        # print obj.evaluatedContents(userID=1,categoryID=3)
        # print obj.givenRating(userID=1,contentID=15)

        # print obj.evaluateCredibilityOfUser(1,3,mode=None)
        # print obj.evaluateQualityOfContent(5) #due to lack of necessary values(all credibilty,content quality values etc), this function may not be give result when  used this way. But this is no problem. You can use all evaluate form (evaluateAllContentsQuality)
        # print obj.evaluateExpertiseOfUser(self,userID,categoryID) #due to lack of necessary values(all credibility values etc), this function may not be give result when  used this way. But this is no problem.You can use all evaluate form (evaluateAllUsersExpertise)

        # print obj.getCountsOfAllRatingsGivenFromAuser(1)
        # print obj.getCountsOfGivenRatingInACategoryForUser(1,3)

        # print obj.getUserCredibility(userID=1,categoryID= 2)
        # print obj.getUserExpertise(userID=1,categoryID=2)
        # print obj.getEvaluatedCategoriesForUser(1)
        # print obj.getQualityOfContent(productID= 1)
        # print obj.getCategoryOfContent(contentID=1)

        # print obj.setUserCredibility(userID=1,categoryID=2,credibility=3.53333)
        # print obj.setUserExpertise(userID=1,categoryID=2,expertise=0.6161)
        # print obj.setQualityOfContent(productID=3,quality=0.11212)
        # print obj.setAllCategoryAssociation([1,1,1])
        # print obj.setUserCategoryPreferance(1,1,0.12121212)

        # print obj.evaluateAllUsersCredibility(mode=None)
        # print obj.evaluateAllContentsQuality()
        # print obj.evaluateAllUsersExpertise()
        # print obj.evaluateAllCategoryAssociationMatrix()
        # print obj.evaluateSupportc1c2(1,2)
        # print obj.calculateEvaluationPrefForUser(1)
        # obj.evaluateAllUserCategoryEvaluationPreferences()
        # obj.evaluateNeededEPTrByArray2(3,4)


        # obj.setAssociationMatrixToNumpy()
        # obj.setUserPreferenceMatrixToNumpy()
        # obj.multiplyAssociaionAndPreference()



        ############################  END #### FOR TEST PURPOSES#
        #########################################################













##########BEGIN##YOU CAN RUN LIKE THIS#######################
#############################################################

        print obj.evaluateAllUsersCredibility(mode='initial')
        print obj.evaluateAllContentsQuality()
        print obj.evaluateAllUsersCredibility(mode=None)
        print obj.evaluateAllContentsQuality()
        print obj.evaluateAllUsersCredibility(mode=None)
        print obj.evaluateAllContentsQuality()
        print obj.evaluateAllUsersExpertise()
        print obj.evaluateAllCategoryAssociationMatrix()
        print obj.evaluateAllUserCategoryEvaluationPreferences()

        #begin#you need to use these four together
        obj.setAssociationMatrixToNumpy()
        obj.setUserPreferenceMatrixToNumpy()
        obj.multiplyAssociaionAndPreference()
        obj.evaluateNeededEPTrForTextfile('testusers.txt')
        ##end#you need to use these four together

##########END##YOU CAN RUN LIKE THIS#######################
###########################################################
    except Exception as e:
        print e
        obj.conn.commit()
    finally:
        obj.conn.commit()
        obj.disconnectFromDB()



if __name__=='__main__':
    main()

