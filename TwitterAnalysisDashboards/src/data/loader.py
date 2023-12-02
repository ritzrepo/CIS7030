import pandas as pd

class DataSchema: 
    TWEETID = "Tweet_ID"
    USERNAME = "Username"
    TEXT = "Text" 
    RETWEETS = "Retweets"
    LIKES = "Likes"
    TIMESTAMP = "Timestamp"
    MONTH = "month"
    YEAR = "year"
    DATE = "date"
 
 
def load_twitter_data(path:str)-> pd.DataFrame:
    #load the data from TWEETER csv
    # Unnamed: Tweet_ID	Username	Text	Retweets	Likes	Timestamp
    data = pd.read_csv(
        path,
        dtype={
            DataSchema.TWEETID:str,
            DataSchema.USERNAME:str,
            DataSchema.TEXT: str,
            DataSchema.RETWEETS:int,
            DataSchema.LIKES:int,
            DataSchema.TIMESTAMP:str,
        }, na_values=["NA", "N/A"],
        parse_dates=[DataSchema.TIMESTAMP],
    )
    data[DataSchema.MONTH] = data[DataSchema.TIMESTAMP].dt.month.astype(str)
    data[DataSchema.YEAR]= data[DataSchema.TIMESTAMP].dt.year.astype(str)
    data[DataSchema.DATE]= data[DataSchema.TIMESTAMP].dt.date.astype(str)
    return data

# # Unnamed: 0,Username,User ID,Number of Posts,Followers Count,Following Count,
# # Bio,External URL,emails,down_date,Hashtag
# class InstagramDataSchema: 
#     USERNAME = "Username"
#     USERID = "User ID"
#     NOOFPOSTS = "Number of Posts" 
#     FOLLOWERSCOUNT = "Followers Count"
#     FOLLOWINGCOUNT = "Following Count"
#     BIO = "Bio"
#     ENTERNALURL = "External URL"
#     EMAILS = "emails"
#     DOWNDATE = "down_date"
#     HASHTAG = "Hashtag"
#     CHANNEL = "ChannelName"
#     CHANNELID = "ChannelId"
#     MONTH = "year"
#     YEAR = "month"
#     DATE = "date"
# def load_instagram_stats_data(path:str)-> pd.DataFrame:
#     #load the data from subscription csv
#     # Unnamed: 0,Channel_name,Subscribers,Views,Total_videos,playlist_id,Date
#     data = pd.read_csv(
#         path,
#         dtype={
#             InstagramDataSchema.USERNAME:str,
#             InstagramDataSchema.USERID:str,
#             InstagramDataSchema.NOOFPOSTS:int,
#             InstagramDataSchema.FOLLOWERSCOUNT: int,
#             InstagramDataSchema.FOLLOWINGCOUNT:int,
#             InstagramDataSchema.BIO:str,
#             InstagramDataSchema.ENTERNALURL:str,
#             InstagramDataSchema.EMAILS:str,
#             InstagramDataSchema.HASHTAG:str,
#             InstagramDataSchema.CHANNEL:str,
#             InstagramDataSchema.CHANNELID:str,
#             InstagramDataSchema.DOWNDATE:str,
 
 
#         }, na_values=["NA", "N/A"],
#         parse_dates=[InstagramDataSchema.DOWNDATE],
#     )
#     data[InstagramDataSchema.MONTH] = data[InstagramDataSchema.DOWNDATE].dt.month.astype(str)
#     data[InstagramDataSchema.YEAR]= data[InstagramDataSchema.DOWNDATE].dt.year.astype(str)
#     data[InstagramDataSchema.DATE]= data[InstagramDataSchema.DOWNDATE].dt.date.astype(str)
#     return data


# # Id,ChannelId,ChannelTitle,Title,Description,Published_date,Views,Likes,Favorites,
# # Comments,down_date,Tags,Dislikes,ContentDuration
# class VideoDataSchema: 
#     VDOID ="Id"
#     VDOCHANNELID = "ChannelId"
#     VDOCHANNELTITLE = "ChannelTitle"
#     VDOTITLE = "Title" 
#     VDOTITLEID = "videotitleid" 
#     VDODESCRIPTION = "Description"
#     VDOPUBLISHEDDATE = "Published_date"
#     VDOVIEWS = "Views"
#     VDOLIKES = "Likes"
#     VDOFAVORITES = "Favorites"
#     VDOCOMMENTS = "Comments"
#     VDOTAGS = "Tags"
#     VDODISLIKES = "Dislikes"
#     VDOCONTENTDURATION = "ContentDuration"
#     VDODOWNDATE = "down_date"
#     VDOPUBLISHEDYEAR = "publishedyear"
#     VDOPUBLISHEDMONTH = "publishedmonth"
#     VDOPUBLISHEDON= "publishedon"
#     VDODOWNYEAR = "downyear"
#     VDODOWNMONTH = "downmonth"
#     VDODOWNLOADON = "downloadon"

# def load_channelvideostats_data(path: str) -> pd.DataFrame:
#     # Load the data from the CSV
#     data = pd.read_csv(
#         path,
#         dtype={
#             VideoDataSchema.VDOID: str,
#             VideoDataSchema.VDOCHANNELID: str,
#             VideoDataSchema.VDOCHANNELTITLE: str,
#             VideoDataSchema.VDOTITLE: str,
#             VideoDataSchema.VDOTITLEID: str,
#             VideoDataSchema.VDODESCRIPTION: str,
#             VideoDataSchema.VDOPUBLISHEDDATE: str,
#             VideoDataSchema.VDOVIEWS: str,
#             VideoDataSchema.VDOLIKES: str,
#             VideoDataSchema.VDOFAVORITES: str,
#             VideoDataSchema.VDOCOMMENTS: int,
#             VideoDataSchema.VDODOWNDATE: str,
#             VideoDataSchema.VDOTAGS: str,
#             VideoDataSchema.VDODISLIKES: str,
#             VideoDataSchema.VDOCONTENTDURATION: str,
 
#         }, na_values=["NA", "N/A"],
#         parse_dates=[VideoDataSchema.VDODOWNDATE, VideoDataSchema.VDOPUBLISHEDDATE]
#     )
#     data[VideoDataSchema.VDODOWNMONTH] = data[VideoDataSchema.VDODOWNDATE].dt.month.astype(str)
#     data[VideoDataSchema.VDODOWNYEAR] = data[VideoDataSchema.VDODOWNDATE].dt.year.astype(str)
#     data[VideoDataSchema.VDODOWNLOADON] = data[VideoDataSchema.VDODOWNDATE].dt.date.astype(str)
#     data[VideoDataSchema.VDOPUBLISHEDMONTH] = data[VideoDataSchema.VDOPUBLISHEDDATE].dt.month.astype(str)
#     data[VideoDataSchema.VDOPUBLISHEDYEAR] = data[VideoDataSchema.VDOPUBLISHEDDATE].dt.year.astype(str)
#     data[VideoDataSchema.VDOPUBLISHEDON] = data[VideoDataSchema.VDOPUBLISHEDDATE].dt.date.astype(str)
#     data[VideoDataSchema.VDOID] = data[VideoDataSchema.VDOID].astype(str)
#     data[VideoDataSchema.VDOTITLE] = data[VideoDataSchema.VDOTITLE].astype(str)
#     data[VideoDataSchema.VDOTITLEID] = data[VideoDataSchema.VDOCHANNELTITLE] + "|" + data[VideoDataSchema.VDOID] + "|" + data[VideoDataSchema.VDOTITLE].str[:5]


#     return data
 
# #  Id	VideoId	TopLevelCommentId	Comment	Author	AuthorChannelUrl	AuthorChannelId	CanRate	
# # ViewerRating	Likes	PublishedAt	UpdatedAt	AuthorChannel	down_date

# class CommentsDataSchema: 
#     VIDEOID = "VideoId"
#     TOPLEVELCOMMENTID = "TopLevelCommentId"
#     COMMENT = "Comment" 
#     AURTHOR = "Author"
#     AURTHORCHANNELURL = "AuthorChannelUrl"
#     AURTHORCHANNELID = "AuthorChannelId"
#     CANRATE = "CanRate"
#     VIEWERRATING = "ViewerRating"
#     LIKES = "Likes"
#     PUBLISHEDAT = "PublishedAt"
#     UPDATEDAT = "UpdatedAt"
#     AURTHORCHANNEL = "AuthorChannel"
#     DOWNDATE = "down_date"
#     YEAR = "year"
#     MONTH = "month"
#     DATE = "date"


# def load_comment_data(path:str)-> pd.DataFrame:
 
#     data = pd.read_csv(
#         path,
#         dtype={
#             CommentsDataSchema.VIDEOID:str,
#             CommentsDataSchema.TOPLEVELCOMMENTID:str,
#             CommentsDataSchema.COMMENT :str,
#             CommentsDataSchema.AURTHOR :str,
#             CommentsDataSchema.AURTHORCHANNEL:str,
#             CommentsDataSchema.AURTHORCHANNELID:str,
#             CommentsDataSchema.CANRATE :str,
#             CommentsDataSchema.VIEWERRATING :str,
#             CommentsDataSchema.LIKES :str,
#             CommentsDataSchema.PUBLISHEDAT :str,
#             CommentsDataSchema.UPDATEDAT :str,
#             CommentsDataSchema.AURTHORCHANNEL:str,
#             CommentsDataSchema.DOWNDATE :str,
#             CommentsDataSchema.YEAR :int,
#             CommentsDataSchema.DATE :str,
#             CommentsDataSchema.MONTH :int
#         }, na_values=["NA", "N/A"],
#         parse_dates=[DataSchema.DOWNDATE],
#     )
#     data[DataSchema.MONTH] = data[DataSchema.DOWNDATE].dt.month.astype(str)
#     data[DataSchema.YEAR]= data[DataSchema.DOWNDATE].dt.year.astype(str)
#     data[DataSchema.DATE]= data[DataSchema.DOWNDATE].dt.date.astype(str)
#     return data



# Unnamed: 0_x	Id_x	VideoId	TopLevelCommentId	Comment	Author	AuthorChannelUrl
# AuthorChannelId	CanRate	ViewerRating	Likes_x	PublishedAt	UpdatedAt	
# AuthorChannel	down_date_x	Unnamed: 0_y	Id_y	ChannelId	ChannelTitle
# Title	Description	Published_date	Views	Likes_y	Favorites	Comments	
# down_date_y	Tags	Dislikes	ContentDuration

# class Video_channel_CommentDataSchema: 
#     VIDEOID = "VideoId"
#     TOPLEVELCOMMENTID = "TopLevelCommentId"
#     COMMENT = "Comment" 
#     AURTHOR = "Author"
#     AURTHORCHANNELURL = "AuthorChannelUrl"
#     AURTHORCHANNELID = "AuthorChannelId"
#     CANRATE = "CanRate"
#     VIEWERRATING = "ViewerRating"
#     LIKES = "Likes"
#     PUBLISHEDAT = "PublishedAt"
#     UPDATEDAT = "UpdatedAt"
#     AURTHORCHANNEL = "AuthorChannel"
#     DOWNDATEX = "down_date_x"
#     CHANNELID = "ChannelId"
#     CHANNELTITLE = "ChannelTitle"
#     TITLE = "Title"
#     DESCRIPTION = "Description"
#     PUBLISHEDDATE = "Published_date"
#     VIEWS = "Views"
#     LIKESY = "Likes_y"
#     FAVORITES = "Favorites"
#     DOWNDATEY = "down_date_y"  
#     TAGS = "Tags"  
#     DISLIKES = "Dislikes"  
#     CONTENTDURATION = "ContentDuration"  
#     YEAR = "year"
#     MONTH = "month"
#     DATE = "date"


# def load_Video_channel_Comment_data(path:str)-> pd.DataFrame:
# # def load_Video_channel_Comment_data(path:str , top_n=None)-> pd.DataFrame: 
#     data = pd.read_csv(
#         path,
#         dtype={
#             Video_channel_CommentDataSchema.VIDEOID:str,
#             Video_channel_CommentDataSchema.TOPLEVELCOMMENTID:str,
#             Video_channel_CommentDataSchema.COMMENT :str,
#             Video_channel_CommentDataSchema.AURTHOR :str,
#             Video_channel_CommentDataSchema.AURTHORCHANNEL:str,
#             Video_channel_CommentDataSchema.AURTHORCHANNELID:str,
#             Video_channel_CommentDataSchema.CANRATE :str,
#             Video_channel_CommentDataSchema.VIEWERRATING :str,
#             Video_channel_CommentDataSchema.LIKES :str,
#             Video_channel_CommentDataSchema.PUBLISHEDAT :str,
#             Video_channel_CommentDataSchema.UPDATEDAT :str,
#             Video_channel_CommentDataSchema.AURTHORCHANNEL:str,
#             Video_channel_CommentDataSchema.DOWNDATEX :str,
#             Video_channel_CommentDataSchema.CHANNELID  :str,
#             Video_channel_CommentDataSchema.CHANNELTITLE :str,
#             Video_channel_CommentDataSchema.TITLE  :str,
#             Video_channel_CommentDataSchema.DESCRIPTION  :str,
#             Video_channel_CommentDataSchema.PUBLISHEDDATE  :str,
#             Video_channel_CommentDataSchema.VIEWS  :int,
#             Video_channel_CommentDataSchema.LIKESY  :int,
#             Video_channel_CommentDataSchema.FAVORITES  :str,
#             Video_channel_CommentDataSchema.DOWNDATEY  :str,
#             Video_channel_CommentDataSchema.TAGS  :str, 
#             Video_channel_CommentDataSchema.DISLIKES  :int,
#             Video_channel_CommentDataSchema.CONTENTDURATION  :str,
#             Video_channel_CommentDataSchema.YEAR :int,
#             Video_channel_CommentDataSchema.DATE :str,
#             Video_channel_CommentDataSchema.MONTH :int
#         }, na_values=["NA", "N/A"],
#         parse_dates=[Video_channel_CommentDataSchema.DOWNDATEX],
#     )
#     data[Video_channel_CommentDataSchema.MONTH] = data[Video_channel_CommentDataSchema.DOWNDATEX].dt.month.astype(str)
#     data[Video_channel_CommentDataSchema.YEAR]= data[Video_channel_CommentDataSchema.DOWNDATEX].dt.year.astype(str)
#     data[Video_channel_CommentDataSchema.DATE]= data[Video_channel_CommentDataSchema.DOWNDATEX].dt.date.astype(str)
#     # if top_n:
#     #     data = data.head(top_n)
 
#     return data