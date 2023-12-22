from typing import List, Optional

from sqlalchemy import Boolean, Column, DateTime, Double, ForeignKeyConstraint, Index, Integer, PrimaryKeyConstraint, SmallInteger, String, Text, Uuid, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Conversations(Base):
    __tablename__ = 'Conversations'
    __table_args__ = (
        ForeignKeyConstraint(['LastMessageId'], ['Messages.MessageId'], ondelete='RESTRICT', name='FK_Conversations_Messages_LastMessageId'),
        PrimaryKeyConstraint('ConversationId', name='PK_Conversations'),
        Index('IX_Conversations_LastMessageId', 'LastMessageId')
    )

    ConversationId = mapped_column(Uuid)
    Visavi = mapped_column(Boolean, nullable=False, server_default=text('false'))
    LastMessageId = mapped_column(Uuid)

    Messages: Mapped[Optional['Messages']] = relationship('Messages', foreign_keys=[LastMessageId], back_populates='Conversations_')
    Messages_: Mapped[List['Messages']] = relationship('Messages', uselist=True, foreign_keys='[Messages.ConversationId]', back_populates='Conversations1')
    UserConversationLinks: Mapped[List['UserConversationLinks']] = relationship('UserConversationLinks', uselist=True, back_populates='Conversations_')


class Fora(Base):
    __tablename__ = 'Fora'
    __table_args__ = (
        PrimaryKeyConstraint('ForumId', name='PK_Fora'),
    )

    ForumId = mapped_column(Uuid)
    Order = mapped_column(Integer, nullable=False)
    ViewPolicy = mapped_column(Integer, nullable=False)
    CreateTopicPolicy = mapped_column(Integer, nullable=False)
    Title = mapped_column(Text)
    Description = mapped_column(Text)

    ForumModerators: Mapped[List['ForumModerators']] = relationship('ForumModerators', uselist=True, back_populates='Fora_')
    ForumTopics: Mapped[List['ForumTopics']] = relationship('ForumTopics', uselist=True, back_populates='Fora_')


class Messages(Base):
    __tablename__ = 'Messages'
    __table_args__ = (
        ForeignKeyConstraint(['ConversationId'], ['Conversations.ConversationId'], ondelete='CASCADE', name='FK_Messages_Conversations_ConversationId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Messages_Users_UserId'),
        PrimaryKeyConstraint('MessageId', name='PK_Messages'),
        Index('IX_Messages_ConversationId', 'ConversationId'),
        Index('IX_Messages_UserId', 'UserId')
    )

    MessageId = mapped_column(Uuid)
    UserId = mapped_column(Uuid, nullable=False)
    ConversationId = mapped_column(Uuid, nullable=False)
    CreateDate = mapped_column(DateTime(True), nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False)
    Text_ = mapped_column('Text', Text)

    Conversations_: Mapped[List['Conversations']] = relationship('Conversations', uselist=True, foreign_keys='[Conversations.LastMessageId]', back_populates='Messages')
    Conversations1: Mapped['Conversations'] = relationship('Conversations', foreign_keys=[ConversationId], back_populates='Messages_')
    Users: Mapped['Users'] = relationship('Users', back_populates='Messages_')


class TagGroups(Base):
    __tablename__ = 'TagGroups'
    __table_args__ = (
        PrimaryKeyConstraint('TagGroupId', name='PK_TagGroups'),
    )

    TagGroupId = mapped_column(Uuid)
    Title = mapped_column(Text)

    Tags: Mapped[List['Tags']] = relationship('Tags', uselist=True, back_populates='TagGroups_')


class Users(Base):
    __tablename__ = 'Users'
    __table_args__ = (
        PrimaryKeyConstraint('UserId', name='PK_Users'),
    )

    UserId = mapped_column(Uuid)
    RegistrationDate = mapped_column(DateTime(True), nullable=False)
    Role = mapped_column(Integer, nullable=False)
    AccessPolicy = mapped_column(Integer, nullable=False)
    RatingDisabled = mapped_column(Boolean, nullable=False)
    QualityRating = mapped_column(Integer, nullable=False)
    QuantityRating = mapped_column(Integer, nullable=False)
    Activated = mapped_column(Boolean, nullable=False)
    CanMerge = mapped_column(Boolean, nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False)
    Login = Column(String(100))
    Email = Column(String(100))
    LastVisitDate = mapped_column(DateTime(True))
    TimezoneId = mapped_column(Text)
    Salt = mapped_column(String(120))
    PasswordHash = mapped_column(String(300))
    MergeRequested = mapped_column(Uuid)
    Status = mapped_column(String(200))
    Name = mapped_column(String(100))
    Location = mapped_column(String(100))
    Icq = mapped_column(String(20))
    Skype = mapped_column(String(50))
    Info = mapped_column(Text)
    ProfilePictureUrl = mapped_column(String(200))
    MediumProfilePictureUrl = mapped_column(String(200))
    SmallProfilePictureUrl = mapped_column(String(200))

    Messages_: Mapped[List['Messages']] = relationship('Messages', uselist=True, back_populates='Users')
    Bans: Mapped[List['Bans']] = relationship('Bans', uselist=True, foreign_keys='[Bans.ModeratorId]', back_populates='Users_')
    Bans_: Mapped[List['Bans']] = relationship('Bans', uselist=True, foreign_keys='[Bans.UserId]', back_populates='Users1')
    ChatMessages: Mapped[List['ChatMessages']] = relationship('ChatMessages', uselist=True, back_populates='Users_')
    Comments: Mapped[List['Comments']] = relationship('Comments', uselist=True, back_populates='Users_')
    ForumModerators: Mapped[List['ForumModerators']] = relationship('ForumModerators', uselist=True, back_populates='Users_')
    Games: Mapped[List['Games']] = relationship('Games', uselist=True, foreign_keys='[Games.AssistantId]', back_populates='Users_')
    Games_: Mapped[List['Games']] = relationship('Games', uselist=True, foreign_keys='[Games.MasterId]', back_populates='Users1')
    Games1: Mapped[List['Games']] = relationship('Games', uselist=True, foreign_keys='[Games.NannyId]', back_populates='Users2')
    Likes: Mapped[List['Likes']] = relationship('Likes', uselist=True, back_populates='Users_')
    Reports: Mapped[List['Reports']] = relationship('Reports', uselist=True, foreign_keys='[Reports.AnswerAuthorId]', back_populates='Users_')
    Reports_: Mapped[List['Reports']] = relationship('Reports', uselist=True, foreign_keys='[Reports.TargetId]', back_populates='Users1')
    Reports1: Mapped[List['Reports']] = relationship('Reports', uselist=True, foreign_keys='[Reports.UserId]', back_populates='Users2')
    Reviews: Mapped[List['Reviews']] = relationship('Reviews', uselist=True, back_populates='Users_')
    Tokens: Mapped[List['Tokens']] = relationship('Tokens', uselist=True, back_populates='Users_')
    Uploads: Mapped[List['Uploads']] = relationship('Uploads', uselist=True, back_populates='Users_')
    UserConversationLinks: Mapped[List['UserConversationLinks']] = relationship('UserConversationLinks', uselist=True, back_populates='Users_')
    Warnings: Mapped[List['Warnings']] = relationship('Warnings', uselist=True, foreign_keys='[Warnings.ModeratorId]', back_populates='Users_')
    Warnings_: Mapped[List['Warnings']] = relationship('Warnings', uselist=True, foreign_keys='[Warnings.UserId]', back_populates='Users1')
    BlackListLinks: Mapped[List['BlackListLinks']] = relationship('BlackListLinks', uselist=True, back_populates='Users_')
    Characters: Mapped[List['Characters']] = relationship('Characters', uselist=True, back_populates='Users_')
    ForumTopics: Mapped[List['ForumTopics']] = relationship('ForumTopics', uselist=True, back_populates='Users_')
    Readers: Mapped[List['Readers']] = relationship('Readers', uselist=True, back_populates='Users_')
    PendingPosts: Mapped[List['PendingPosts']] = relationship('PendingPosts', uselist=True, foreign_keys='[PendingPosts.AwaitingUserId]', back_populates='Users_')
    PendingPosts_: Mapped[List['PendingPosts']] = relationship('PendingPosts', uselist=True, foreign_keys='[PendingPosts.PendingUserId]', back_populates='Users1')
    Posts: Mapped[List['Posts']] = relationship('Posts', uselist=True, foreign_keys='[Posts.LastUpdateUserId]', back_populates='Users_')
    Posts_: Mapped[List['Posts']] = relationship('Posts', uselist=True, foreign_keys='[Posts.UserId]', back_populates='Users1')
    # Votes: Mapped[List['Votes']] = relationship('Votes', uselist=True, foreign_keys='[Votes.TargetUserId]', back_populates='Users_')
    # Votes_: Mapped[List['Votes']] = relationship('Votes', uselist=True, foreign_keys='[Votes.UserId]', back_populates='Users1')


class EFMigrationsHistory(Base):
    __tablename__ = '__EFMigrationsHistory'
    __table_args__ = (
        PrimaryKeyConstraint('MigrationId', name='PK___EFMigrationsHistory'),
    )

    MigrationId = mapped_column(String(150))
    ProductVersion = mapped_column(String(32), nullable=False)


class Bans(Base):
    __tablename__ = 'Bans'
    __table_args__ = (
        ForeignKeyConstraint(['ModeratorId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Bans_Users_ModeratorId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Bans_Users_UserId'),
        PrimaryKeyConstraint('BanId', name='PK_Bans'),
        Index('IX_Bans_ModeratorId', 'ModeratorId'),
        Index('IX_Bans_UserId', 'UserId')
    )

    BanId = mapped_column(Uuid)
    UserId = mapped_column(Uuid, nullable=False)
    ModeratorId = mapped_column(Uuid, nullable=False)
    StartDate = mapped_column(DateTime(True), nullable=False)
    EndDate = mapped_column(DateTime(True), nullable=False)
    AccessRestrictionPolicy = mapped_column(Integer, nullable=False)
    IsVoluntary = mapped_column(Boolean, nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False)
    Comment = mapped_column(Text)

    Users_: Mapped['Users'] = relationship('Users', foreign_keys=[ModeratorId], back_populates='Bans')
    Users1: Mapped['Users'] = relationship('Users', foreign_keys=[UserId], back_populates='Bans_')


class ChatMessages(Base):
    __tablename__ = 'ChatMessages'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_ChatMessages_Users_UserId'),
        PrimaryKeyConstraint('ChatMessageId', name='PK_ChatMessages'),
        Index('IX_ChatMessages_UserId', 'UserId')
    )

    ChatMessageId = mapped_column(Uuid)
    UserId = mapped_column(Uuid, nullable=False)
    CreateDate = mapped_column(DateTime(True), nullable=False)
    Text_ = mapped_column('Text', Text)

    Users_: Mapped['Users'] = relationship('Users', back_populates='ChatMessages')


class Comments(Base):
    __tablename__ = 'Comments'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Comments_Users_UserId'),
        PrimaryKeyConstraint('CommentId', name='PK_Comments'),
        Index('IX_Comments_EntityId', 'EntityId'),
        Index('IX_Comments_UserId', 'UserId')
    )

    CommentId = mapped_column(Uuid)
    EntityId = mapped_column(Uuid, nullable=False)
    UserId = mapped_column(Uuid, nullable=False)
    CreateDate = mapped_column(DateTime(True), nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False)
    LastUpdateDate = mapped_column(DateTime(True))
    Text_ = mapped_column('Text', Text)

    Users_: Mapped['Users'] = relationship('Users', back_populates='Comments')
    ForumTopics: Mapped[List['ForumTopics']] = relationship('ForumTopics', uselist=True, back_populates='Comments_')


class ForumModerators(Base):
    __tablename__ = 'ForumModerators'
    __table_args__ = (
        ForeignKeyConstraint(['ForumId'], ['Fora.ForumId'], ondelete='CASCADE', name='FK_ForumModerators_Fora_ForumId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_ForumModerators_Users_UserId'),
        PrimaryKeyConstraint('ForumModeratorId', name='PK_ForumModerators'),
        Index('IX_ForumModerators_ForumId', 'ForumId'),
        Index('IX_ForumModerators_UserId', 'UserId')
    )

    ForumModeratorId = mapped_column(Uuid)
    ForumId = mapped_column(Uuid, nullable=False)
    UserId = mapped_column(Uuid, nullable=False)

    Fora_: Mapped['Fora'] = relationship('Fora', back_populates='ForumModerators')
    Users_: Mapped['Users'] = relationship('Users', back_populates='ForumModerators')


class Games(Base):
    __tablename__ = 'Games'
    __table_args__ = (
        ForeignKeyConstraint(['AssistantId'], ['Users.UserId'], ondelete='RESTRICT', name='FK_Games_Users_AssistantId'),
        ForeignKeyConstraint(['MasterId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Games_Users_MasterId'),
        ForeignKeyConstraint(['NannyId'], ['Users.UserId'], ondelete='RESTRICT', name='FK_Games_Users_NannyId'),
        PrimaryKeyConstraint('GameId', name='PK_Games'),
        Index('IX_Games_AssistantId', 'AssistantId'),
        Index('IX_Games_MasterId', 'MasterId'),
        Index('IX_Games_NannyId', 'NannyId')
    )

    GameId = mapped_column(Uuid)
    CreateDate = mapped_column(DateTime(True), nullable=False)
    Status = mapped_column(Integer, nullable=False)
    MasterId = mapped_column(Uuid, nullable=False)
    HideTemper = mapped_column(Boolean, nullable=False)
    HideSkills = mapped_column(Boolean, nullable=False)
    HideInventory = mapped_column(Boolean, nullable=False)
    HideStory = mapped_column(Boolean, nullable=False)
    DisableAlignment = mapped_column(Boolean, nullable=False)
    HideDiceResult = mapped_column(Boolean, nullable=False)
    ShowPrivateMessages = mapped_column(Boolean, nullable=False)
    CommentariesAccessMode = mapped_column(Integer, nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False)
    ReleaseDate = mapped_column(DateTime(True))
    AssistantId = mapped_column(Uuid)
    NannyId = mapped_column(Uuid)
    AttributeSchemaId = mapped_column(Uuid)
    Title = mapped_column(Text)
    SystemName = mapped_column(Text)
    SettingName = mapped_column(Text)
    Info = mapped_column(Text)
    Notepad = mapped_column(Text)

    Users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[AssistantId], back_populates='Games')
    Users1: Mapped['Users'] = relationship('Users', foreign_keys=[MasterId], back_populates='Games_')
    Users2: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[NannyId], back_populates='Games1')
    BlackListLinks: Mapped[List['BlackListLinks']] = relationship('BlackListLinks', uselist=True, back_populates='Games_')
    Characters: Mapped[List['Characters']] = relationship('Characters', uselist=True, back_populates='Games_')
    GameTags: Mapped[List['GameTags']] = relationship('GameTags', uselist=True, back_populates='Games_')
    Readers: Mapped[List['Readers']] = relationship('Readers', uselist=True, back_populates='Games_')
    Rooms: Mapped[List['Rooms']] = relationship('Rooms', uselist=True, back_populates='Games_')
    #Votes: Mapped[List['Votes']] = relationship('Votes', uselist=True, back_populates='Games_')


class Likes(Base):
    __tablename__ = 'Likes'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Likes_Users_UserId'),
        PrimaryKeyConstraint('LikeId', name='PK_Likes'),
        Index('IX_Likes_EntityId', 'EntityId'),
        Index('IX_Likes_UserId', 'UserId')
    )

    LikeId = mapped_column(Uuid)
    EntityId = mapped_column(Uuid, nullable=False)
    UserId = mapped_column(Uuid, nullable=False)

    Users_: Mapped['Users'] = relationship('Users', back_populates='Likes')


class Reports(Base):
    __tablename__ = 'Reports'
    __table_args__ = (
        ForeignKeyConstraint(['AnswerAuthorId'], ['Users.UserId'], ondelete='RESTRICT', name='FK_Reports_Users_AnswerAuthorId'),
        ForeignKeyConstraint(['TargetId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Reports_Users_TargetId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Reports_Users_UserId'),
        PrimaryKeyConstraint('ReportId', name='PK_Reports'),
        Index('IX_Reports_AnswerAuthorId', 'AnswerAuthorId'),
        Index('IX_Reports_TargetId', 'TargetId'),
        Index('IX_Reports_UserId', 'UserId')
    )

    ReportId = mapped_column(Uuid)
    UserId = mapped_column(Uuid, nullable=False)
    TargetId = mapped_column(Uuid, nullable=False)
    CreateDate = mapped_column(DateTime(True), nullable=False)
    ReportText = mapped_column(Text)
    Comment = mapped_column(Text)
    AnswerAuthorId = mapped_column(Uuid)
    Answer = mapped_column(Text)

    Users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[AnswerAuthorId], back_populates='Reports')
    Users1: Mapped['Users'] = relationship('Users', foreign_keys=[TargetId], back_populates='Reports_')
    Users2: Mapped['Users'] = relationship('Users', foreign_keys=[UserId], back_populates='Reports1')


class Reviews(Base):
    __tablename__ = 'Reviews'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Reviews_Users_UserId'),
        PrimaryKeyConstraint('ReviewId', name='PK_Reviews'),
        Index('IX_Reviews_UserId', 'UserId')
    )

    ReviewId = mapped_column(Uuid)
    UserId = mapped_column(Uuid, nullable=False)
    CreateDate = mapped_column(DateTime(True), nullable=False)
    IsApproved = mapped_column(Boolean, nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False, server_default=text('false'))
    Text_ = mapped_column('Text', Text)

    Users_: Mapped['Users'] = relationship('Users', back_populates='Reviews')


class Tags(Base):
    __tablename__ = 'Tags'
    __table_args__ = (
        ForeignKeyConstraint(['TagGroupId'], ['TagGroups.TagGroupId'], ondelete='CASCADE', name='FK_Tags_TagGroups_TagGroupId'),
        PrimaryKeyConstraint('TagId', name='PK_Tags'),
        Index('IX_Tags_TagGroupId', 'TagGroupId')
    )

    TagId = mapped_column(Uuid)
    TagGroupId = mapped_column(Uuid, nullable=False)
    Title = mapped_column(Text)

    TagGroups_: Mapped['TagGroups'] = relationship('TagGroups', back_populates='Tags')
    GameTags: Mapped[List['GameTags']] = relationship('GameTags', uselist=True, back_populates='Tags_')


class Tokens(Base):
    __tablename__ = 'Tokens'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Tokens_Users_UserId'),
        PrimaryKeyConstraint('TokenId', name='PK_Tokens'),
        Index('IX_Tokens_EntityId', 'EntityId'),
        Index('IX_Tokens_UserId', 'UserId')
    )

    TokenId = mapped_column(Uuid)
    UserId = mapped_column(Uuid, nullable=False)
    CreateDate = mapped_column(DateTime(True), nullable=False)
    Type = mapped_column(Integer, nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False)
    EntityId = mapped_column(Uuid)

    Users_: Mapped['Users'] = relationship('Users', back_populates='Tokens')


class Uploads(Base):
    __tablename__ = 'Uploads'
    __table_args__ = (
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Uploads_Users_UserId'),
        PrimaryKeyConstraint('UploadId', name='PK_Uploads'),
        Index('IX_Uploads_EntityId', 'EntityId'),
        Index('IX_Uploads_UserId', 'UserId')
    )

    UploadId = mapped_column(Uuid)
    CreateDate = mapped_column(DateTime(True), nullable=False)
    UserId = mapped_column(Uuid, nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False)
    Original = mapped_column(Boolean, nullable=False, server_default=text('false'))
    EntityId = mapped_column(Uuid)
    FilePath = mapped_column(Text)
    FileName = mapped_column(Text)

    Users_: Mapped['Users'] = relationship('Users', back_populates='Uploads')


class UserConversationLinks(Base):
    __tablename__ = 'UserConversationLinks'
    __table_args__ = (
        ForeignKeyConstraint(['ConversationId'], ['Conversations.ConversationId'], ondelete='CASCADE', name='FK_UserConversationLinks_Conversations_ConversationId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_UserConversationLinks_Users_UserId'),
        PrimaryKeyConstraint('UserConversationLinkId', name='PK_UserConversationLinks'),
        Index('IX_UserConversationLinks_ConversationId', 'ConversationId'),
        Index('IX_UserConversationLinks_UserId', 'UserId')
    )

    UserConversationLinkId = mapped_column(Uuid)
    UserId = mapped_column(Uuid, nullable=False)
    ConversationId = mapped_column(Uuid, nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False)

    Conversations_: Mapped['Conversations'] = relationship('Conversations', back_populates='UserConversationLinks')
    Users_: Mapped['Users'] = relationship('Users', back_populates='UserConversationLinks')


class Warnings(Base):
    __tablename__ = 'Warnings'
    __table_args__ = (
        ForeignKeyConstraint(['ModeratorId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Warnings_Users_ModeratorId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Warnings_Users_UserId'),
        PrimaryKeyConstraint('WarningId', name='PK_Warnings'),
        Index('IX_Warnings_EntityId', 'EntityId'),
        Index('IX_Warnings_ModeratorId', 'ModeratorId'),
        Index('IX_Warnings_UserId', 'UserId')
    )

    WarningId = mapped_column(Uuid)
    UserId = mapped_column(Uuid, nullable=False)
    ModeratorId = mapped_column(Uuid, nullable=False)
    EntityId = mapped_column(Uuid, nullable=False)
    CreateDate = mapped_column(DateTime(True), nullable=False)
    Points = mapped_column(Integer, nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False)
    Text_ = mapped_column('Text', Text)

    Users_: Mapped['Users'] = relationship('Users', foreign_keys=[ModeratorId], back_populates='Warnings')
    Users1: Mapped['Users'] = relationship('Users', foreign_keys=[UserId], back_populates='Warnings_')


class BlackListLinks(Base):
    __tablename__ = 'BlackListLinks'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_BlackListLinks_Games_GameId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_BlackListLinks_Users_UserId'),
        PrimaryKeyConstraint('BlackListLinkId', name='PK_BlackListLinks'),
        Index('IX_BlackListLinks_GameId', 'GameId'),
        Index('IX_BlackListLinks_UserId', 'UserId')
    )

    BlackListLinkId = mapped_column(Uuid)
    GameId = mapped_column(Uuid, nullable=False)
    UserId = mapped_column(Uuid, nullable=False)

    Games_: Mapped['Games'] = relationship('Games', back_populates='BlackListLinks')
    Users_: Mapped['Users'] = relationship('Users', back_populates='BlackListLinks')


class Characters(Base):
    __tablename__ = 'Characters'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_Characters_Games_GameId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Characters_Users_UserId'),
        PrimaryKeyConstraint('CharacterId', name='PK_Characters'),
        Index('IX_Characters_GameId', 'GameId'),
        Index('IX_Characters_UserId', 'UserId')
    )

    CharacterId = mapped_column(Uuid)
    GameId = mapped_column(Uuid, nullable=False)
    UserId = mapped_column(Uuid, nullable=False)
    Status = mapped_column(Integer, nullable=False)
    CreateDate = mapped_column(DateTime(True), nullable=False)
    IsNpc = mapped_column(Boolean, nullable=False)
    AccessPolicy = mapped_column(Integer, nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False)
    LastUpdateDate = mapped_column(DateTime(True))
    Name = mapped_column(Text)
    Race = mapped_column(Text)
    Class = mapped_column(Text)
    Alignment = mapped_column(Integer)
    Appearance = mapped_column(Text)
    Temper = mapped_column(Text)
    Story = mapped_column(Text)
    Skills = mapped_column(Text)
    Inventory = mapped_column(Text)

    Games_: Mapped['Games'] = relationship('Games', back_populates='Characters')
    Users_: Mapped['Users'] = relationship('Users', back_populates='Characters')
    CharacterAttributes: Mapped[List['CharacterAttributes']] = relationship('CharacterAttributes', uselist=True, back_populates='Characters_')
    Posts: Mapped[List['Posts']] = relationship('Posts', uselist=True, back_populates='Characters_')
    RoomClaims: Mapped[List['RoomClaims']] = relationship('RoomClaims', uselist=True, back_populates='Characters_')


class ForumTopics(Base):
    __tablename__ = 'ForumTopics'
    __table_args__ = (
        ForeignKeyConstraint(['ForumId'], ['Fora.ForumId'], ondelete='CASCADE', name='FK_ForumTopics_Fora_ForumId'),
        ForeignKeyConstraint(['LastCommentId'], ['Comments.CommentId'], ondelete='RESTRICT', name='FK_ForumTopics_Comments_LastCommentId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_ForumTopics_Users_UserId'),
        PrimaryKeyConstraint('ForumTopicId', name='PK_ForumTopics'),
        Index('IX_ForumTopics_ForumId', 'ForumId'),
        Index('IX_ForumTopics_LastCommentId', 'LastCommentId'),
        Index('IX_ForumTopics_UserId', 'UserId')
    )

    ForumTopicId = mapped_column(Uuid)
    ForumId = mapped_column(Uuid, nullable=False)
    UserId = mapped_column(Uuid, nullable=False)
    CreateDate = mapped_column(DateTime(True), nullable=False)
    Attached = mapped_column(Boolean, nullable=False)
    Closed = mapped_column(Boolean, nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False)
    Title = mapped_column(Text)
    Text_ = mapped_column('Text', Text)
    LastCommentId = mapped_column(Uuid)

    Fora_: Mapped['Fora'] = relationship('Fora', back_populates='ForumTopics')
    Comments_: Mapped[Optional['Comments']] = relationship('Comments', back_populates='ForumTopics')
    Users_: Mapped['Users'] = relationship('Users', back_populates='ForumTopics')


class GameTags(Base):
    __tablename__ = 'GameTags'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_GameTags_Games_GameId'),
        ForeignKeyConstraint(['TagId'], ['Tags.TagId'], ondelete='CASCADE', name='FK_GameTags_Tags_TagId'),
        PrimaryKeyConstraint('GameTagId', name='PK_GameTags'),
        Index('IX_GameTags_GameId', 'GameId'),
        Index('IX_GameTags_TagId', 'TagId')
    )

    GameTagId = mapped_column(Uuid)
    GameId = mapped_column(Uuid, nullable=False)
    TagId = mapped_column(Uuid, nullable=False)

    Games_: Mapped['Games'] = relationship('Games', back_populates='GameTags')
    Tags_: Mapped['Tags'] = relationship('Tags', back_populates='GameTags')


class Readers(Base):
    __tablename__ = 'Readers'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_Readers_Games_GameId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Readers_Users_UserId'),
        PrimaryKeyConstraint('ReaderId', name='PK_Readers'),
        Index('IX_Readers_GameId', 'GameId'),
        Index('IX_Readers_UserId', 'UserId')
    )

    ReaderId = mapped_column(Uuid)
    GameId = mapped_column(Uuid, nullable=False)
    UserId = mapped_column(Uuid, nullable=False)

    Games_: Mapped['Games'] = relationship('Games', back_populates='Readers')
    Users_: Mapped['Users'] = relationship('Users', back_populates='Readers')
    RoomClaims: Mapped[List['RoomClaims']] = relationship('RoomClaims', uselist=True, back_populates='Readers_')


class Rooms(Base):
    __tablename__ = 'Rooms'
    __table_args__ = (
        ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_Rooms_Games_GameId'),
        ForeignKeyConstraint(['NextRoomId'], ['Rooms.RoomId'], ondelete='RESTRICT', name='FK_Rooms_Rooms_NextRoomId'),
        ForeignKeyConstraint(['PreviousRoomId'], ['Rooms.RoomId'], ondelete='RESTRICT', name='FK_Rooms_Rooms_PreviousRoomId'),
        PrimaryKeyConstraint('RoomId', name='PK_Rooms'),
        Index('IX_Rooms_GameId', 'GameId'),
        Index('IX_Rooms_NextRoomId', 'NextRoomId', unique=True),
        Index('IX_Rooms_PreviousRoomId', 'PreviousRoomId')
    )

    RoomId = mapped_column(Uuid)
    GameId = mapped_column(Uuid, nullable=False)
    AccessType = mapped_column(Integer, nullable=False)
    Type = mapped_column(Integer, nullable=False)
    OrderNumber = mapped_column(Double(53), nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False)
    Title = mapped_column(Text)
    PreviousRoomId = mapped_column(Uuid)
    NextRoomId = mapped_column(Uuid)

    Games_: Mapped['Games'] = relationship('Games', back_populates='Rooms')
    Rooms: Mapped[Optional['Rooms']] = relationship('Rooms', remote_side=[RoomId], foreign_keys=[NextRoomId], back_populates='Rooms_reverse')
    Rooms_reverse: Mapped[List['Rooms']] = relationship('Rooms', uselist=True, remote_side=[NextRoomId], foreign_keys=[NextRoomId], back_populates='Rooms')
    Rooms_: Mapped[Optional['Rooms']] = relationship('Rooms', remote_side=[RoomId], foreign_keys=[PreviousRoomId], back_populates='Rooms__reverse')
    Rooms__reverse: Mapped[List['Rooms']] = relationship('Rooms', uselist=True, remote_side=[PreviousRoomId], foreign_keys=[PreviousRoomId], back_populates='Rooms_')
    PendingPosts: Mapped[List['PendingPosts']] = relationship('PendingPosts', uselist=True, back_populates='Rooms_')
    Posts: Mapped[List['Posts']] = relationship('Posts', uselist=True, back_populates='Rooms_')
    RoomClaims: Mapped[List['RoomClaims']] = relationship('RoomClaims', uselist=True, back_populates='Rooms_')


class CharacterAttributes(Base):
    __tablename__ = 'CharacterAttributes'
    __table_args__ = (
        ForeignKeyConstraint(['CharacterId'], ['Characters.CharacterId'], ondelete='CASCADE', name='FK_CharacterAttributes_Characters_CharacterId'),
        PrimaryKeyConstraint('CharacterAttributeId', name='PK_CharacterAttributes'),
        Index('IX_CharacterAttributes_CharacterId', 'CharacterId')
    )

    CharacterAttributeId = mapped_column(Uuid)
    AttributeId = mapped_column(Uuid, nullable=False)
    CharacterId = mapped_column(Uuid, nullable=False)
    Value = mapped_column(Text)

    Characters_: Mapped['Characters'] = relationship('Characters', back_populates='CharacterAttributes')


class PendingPosts(Base):
    __tablename__ = 'PendingPosts'
    __table_args__ = (
        ForeignKeyConstraint(['AwaitingUserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_PendingPosts_Users_AwaitingUserId'),
        ForeignKeyConstraint(['PendingUserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_PendingPosts_Users_PendingUserId'),
        ForeignKeyConstraint(['RoomId'], ['Rooms.RoomId'], ondelete='CASCADE', name='FK_PendingPosts_Rooms_RoomId'),
        PrimaryKeyConstraint('PendingPostId', name='PK_PendingPosts'),
        Index('IX_PendingPosts_AwaitingUserId', 'AwaitingUserId'),
        Index('IX_PendingPosts_PendingUserId', 'PendingUserId'),
        Index('IX_PendingPosts_RoomId', 'RoomId')
    )

    PendingPostId = mapped_column(Uuid)
    AwaitingUserId = mapped_column(Uuid, nullable=False)
    PendingUserId = mapped_column(Uuid, nullable=False)
    RoomId = mapped_column(Uuid, nullable=False)
    CreateDate = mapped_column(DateTime(True), nullable=False)

    Users_: Mapped['Users'] = relationship('Users', foreign_keys=[AwaitingUserId], back_populates='PendingPosts')
    Users1: Mapped['Users'] = relationship('Users', foreign_keys=[PendingUserId], back_populates='PendingPosts_')
    Rooms_: Mapped['Rooms'] = relationship('Rooms', back_populates='PendingPosts')


class Posts(Base):
    __tablename__ = 'Posts'
    __table_args__ = (
        ForeignKeyConstraint(['CharacterId'], ['Characters.CharacterId'], ondelete='RESTRICT', name='FK_Posts_Characters_CharacterId'),
        ForeignKeyConstraint(['LastUpdateUserId'], ['Users.UserId'], ondelete='RESTRICT', name='FK_Posts_Users_LastUpdateUserId'),
        ForeignKeyConstraint(['RoomId'], ['Rooms.RoomId'], ondelete='CASCADE', name='FK_Posts_Rooms_RoomId'),
        ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Posts_Users_UserId'),
        PrimaryKeyConstraint('PostId', name='PK_Posts'),
        Index('IX_Posts_CharacterId', 'CharacterId'),
        Index('IX_Posts_LastUpdateUserId', 'LastUpdateUserId'),
        Index('IX_Posts_RoomId', 'RoomId'),
        Index('IX_Posts_UserId', 'UserId')
    )

    PostId = mapped_column(Uuid)
    RoomId = mapped_column(Uuid, nullable=False)
    UserId = mapped_column(Uuid, nullable=False)
    CreateDate = mapped_column(DateTime(True), nullable=False)
    IsRemoved = mapped_column(Boolean, nullable=False)
    CharacterId = mapped_column(Uuid)
    LastUpdateUserId = mapped_column(Uuid)
    LastUpdateDate = mapped_column(DateTime(True))
    Text_ = mapped_column('Text', Text)
    Commentary = mapped_column(Text)
    MasterMessage = mapped_column(Text)

    Characters_: Mapped[Optional['Characters']] = relationship('Characters', back_populates='Posts')
    Users_: Mapped[Optional['Users']] = relationship('Users', foreign_keys=[LastUpdateUserId], back_populates='Posts')
    Rooms_: Mapped['Rooms'] = relationship('Rooms', back_populates='Posts')
    Users1: Mapped['Users'] = relationship('Users', foreign_keys=[UserId], back_populates='Posts_')
    #Votes: Mapped[List['Votes']] = relationship('Votes', uselist=True, back_populates='Posts_')


class RoomClaims(Base):
    __tablename__ = 'RoomClaims'
    __table_args__ = (
        ForeignKeyConstraint(['ParticipantId'], ['Readers.ReaderId'], ondelete='CASCADE', name='FK_RoomClaims_Readers_ParticipantId'),
        ForeignKeyConstraint(['ParticipantId'], ['Characters.CharacterId'], ondelete='CASCADE', name='FK_RoomClaims_Characters_ParticipantId'),
        ForeignKeyConstraint(['RoomId'], ['Rooms.RoomId'], ondelete='CASCADE', name='FK_RoomClaims_Rooms_RoomId'),
        PrimaryKeyConstraint('RoomClaimId', name='PK_RoomClaims'),
        Index('IX_RoomClaims_ParticipantId', 'ParticipantId'),
        Index('IX_RoomClaims_RoomId', 'RoomId')
    )

    RoomClaimId = mapped_column(Uuid)
    ParticipantId = mapped_column(Uuid, nullable=False)
    RoomId = mapped_column(Uuid, nullable=False)
    Policy = mapped_column(Integer, nullable=False)

    Readers_: Mapped['Readers'] = relationship('Readers', back_populates='RoomClaims')
    Characters_: Mapped['Characters'] = relationship('Characters', back_populates='RoomClaims')
    Rooms_: Mapped['Rooms'] = relationship('Rooms', back_populates='RoomClaims')


# class Votes(Base):
#     __tablename__ = 'Votes'
#     __table_args__ = (
#        # ForeignKeyConstraint(['GameId'], ['Games.GameId'], ondelete='CASCADE', name='FK_Votes_Games_GameId'),
#         ForeignKeyConstraint(['PostId'], ['Posts.PostId'], ondelete='CASCADE', name='FK_Votes_Posts_PostId'),
#         ForeignKeyConstraint(['TargetUserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Votes_Users_TargetUserId'),
#         ForeignKeyConstraint(['UserId'], ['Users.UserId'], ondelete='CASCADE', name='FK_Votes_Users_UserId'),
#         PrimaryKeyConstraint('VoteId', name='PK_Votes'),
# #        Index('IX_Votes_GameId', 'GameId'),
#         Index('IX_Votes_PostId', 'PostId'),
#         Index('IX_Votes_TargetUserId', 'TargetUserId'),
#         Index('IX_Votes_UserId', 'UserId')
#     )

