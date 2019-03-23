from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, String, Boolean, Text
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy import backref
from sqlalchemy.orm import backref

Base = declarative_base()

### TABLES ###
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(Text,nullable=False)
    password = Column(Text,nullable=False)
    admin = Column(Boolean,nullable=False)

class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True)
    rateClassify = Column(Text,nullable=False)
    rateIsolate = Column(Text,nullable=False)
    commentResult = Column(Text,nullable=True)
    commentSite = Column(Text,nullable=True)

class Submission(Base):
    __tablename__ = 'submission'

    id = Column(Integer, primary_key=True)
    animalLabel = Column(Text,nullable=False)
    firstLabel = Column(Text,nullable=False)
    permissionGallery = Column(Boolean,nullable=False)
    permissionDataset = Column(Boolean,nullable=False)
    modApproval = Column(Boolean,nullable=False)
    modReviewed = Column(Boolean,nullable=False)

    feedbackId = Column(Integer,ForeignKey('feedback.id'),nullable=True)
    userId = Column(Integer,ForeignKey('user.id'),nullable=True)

    feedback = relationship(Feedback, backref=backref("submission", uselist=False))
    user = relationship(User, backref="submission")

class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)
    type = Column(Text,nullable=False)
    path = Column(Text,nullable=False)
    
    submissionId = Column(Integer,ForeignKey('submission.id'))  

    submission = relationship(Submission, backref="images")
### END TABLES ###

# # One to many
# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     children = relationship("Child", backref="parent")

# # Many to one
# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     child_id = Column(Integer, ForeignKey('child.id'))
#     child = relationship("Child", backref="parents")
















# author = relationship("Author",backref="books")   
# child = relationship("Child", backref=backref("parent", uselist=False))

######################################################################################
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import Integer, String, Boolean, Text
# from sqlalchemy import Column, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# # from sqlalchemy import backref
# from sqlalchemy.orm import backref

# Base = declarative_base()

# ### TABLES ###
# class Image(Base):
#     __tablename__ = 'image'

#     id = Column(Integer, primary_key=True)
#     path = Column(Text,nullable=False)
#     # animal = Column(Text,nullable=False)
#     original = Column(Boolean,nullable=False)

#     # should add error handling in getter or at locations where getter is called
#     @property
#     def submission(self):
#         if self.original == True:
#             return self.originalLinkSub
#         else:
#             return self.isolateLinkSub

#     def toDictionary(self):
#         return {
#             "id": self.id,
#             "path": self.path,
#             "original": self.original
#         }

#     # def __repr__(self):
#     #     return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)



# class Feedback(Base):
#     __tablename__ = 'feedback'

#     id = Column(Integer, primary_key=True)
#     rateClassify = Column(Text,nullable=False)
#     rateIsolate = Column(Text,nullable=False)
#     commentResult = Column(Text,nullable=True)
#     commentSite = Column(Text,nullable=True)

# class User(Base):
#     __tablename__ = 'user'

#     id = Column(Integer, primary_key=True)
#     username = Column(Text,nullable=False)
#     password = Column(Text,nullable=False)
#     admin = Column(Boolean,nullable=False)

#     def toString(self):
#         return 'id:' + str(self.id) + ', username:' + str(self.username)


# # class Submission(Base):
# # 	__tablename__ = "submission"

# # 	id = Column(Integer, primary_key=True)
# # 	galleryPass = Column(Boolean,nullable=False)
# # 	modApproval = Column(Boolean,nullable=False)

# # 	originalId = Column(Integer,ForeignKey('image.id'))
# # 	isolateId = Column(Integer,ForeignKey('image.id'))
# # 	feedbackId = Column(Integer,ForeignKey('feedback.id'),nullable=True)
# # 	userId = Column(Integer,ForeignKey('user.id'),nullable=True)

# # 	originalImage = relationship(Image, foreign_keys=[originalId])
# # 	isolateImage = relationship(Image, foreign_keys=[isolateId])
# # 	# subFeedback = relationship(Feedback, foreign_keys=[feedbackId])
# # 	# subUser = relationship(User, foreign_keys=[userUsername])
# # 	subFeedback = relationship(Feedback)
# # 	subUser = relationship(User)

# class Submission(Base):
#     __tablename__ = 'submission'

#     id = Column(Integer, primary_key=True)
#     userPermission = Column(Boolean,nullable=False)
#     modApproval = Column(Boolean,nullable=False)
#     modReviewed = Column(Boolean,nullable=False)
#     animalLabel = Column(Text,nullable=False)


#     originalId = Column(Integer,ForeignKey('image.id'))
#     isolateId = Column(Integer,ForeignKey('image.id'))
#     feedbackId = Column(Integer,ForeignKey('feedback.id'),nullable=True)
#     userId = Column(Integer,ForeignKey('user.id'),nullable=True)

#     # Only one backref allowed ?needed?
#     # Backref names very important as 
#     originalImage = relationship(Image, foreign_keys=[originalId], backref=backref("originalLinkSub", uselist=False))
#     isolateImage = relationship(Image, foreign_keys=[isolateId], backref=backref("isolateLinkSub", uselist=False))
#     subFeedback = relationship(Feedback, backref=backref("submission", uselist=False))
#     subUser = relationship(User, backref="submission")

#     # originalImage = relationship(Image, foreign_keys=[originalId])
#     # isolateImage = relationship(Image, foreign_keys=[isolateId])
#     # subFeedback = relationship(Feedback)
#     # subUser = relationship(User)

# ### END TABLES ###

# # author = relationship("Author",backref="books")   
# # child = relationship("Child", backref=backref("parent", uselist=False))