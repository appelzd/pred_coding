/****** Object:  Table [dbo].[PyTest]    Script Date: 11/11/2019 8:20:00 PM ******/
DROP TABLE [dbo].[zDocumentSimilarity_Models]
GO

/****** Object:  Table [dbo].[zDocumentSimilarity_Models]    Script Date: 11/11/2019 8:20:00 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[zDocumentSimilarity_Models](
	[ModelId] [int] NOT NULL IDENTITY(1,1) ,
	[SearchDocids] [varchar](max) NOT NULL,
	[SearchIdentifier] [varchar](max) NULL,
) ON [PRIMARY]
GO



