USE [master]
GO

DROP DATABASE IF EXISTS [EdxStaging]
GO

CREATE DATABASE [EdxStaging]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'EdxStaging', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL13.SQL2016\MSSQL\DATA\EdxStaging.mdf' , SIZE = 3082560KB , MAXSIZE = UNLIMITED, FILEGROWTH = 10%)
 LOG ON 
( NAME = N'EdxStaging_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL13.SQL2016\MSSQL\DATA\EdxStaging_log.ldf' , SIZE = 1188288KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO

ALTER DATABASE [EdxStaging] SET COMPATIBILITY_LEVEL = 130
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [EdxStaging].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [EdxStaging] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [EdxStaging] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [EdxStaging] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [EdxStaging] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [EdxStaging] SET ARITHABORT OFF 
GO

ALTER DATABASE [EdxStaging] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [EdxStaging] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [EdxStaging] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [EdxStaging] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [EdxStaging] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [EdxStaging] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [EdxStaging] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [EdxStaging] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [EdxStaging] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [EdxStaging] SET  DISABLE_BROKER 
GO

ALTER DATABASE [EdxStaging] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [EdxStaging] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [EdxStaging] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [EdxStaging] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [EdxStaging] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [EdxStaging] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [EdxStaging] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [EdxStaging] SET RECOVERY SIMPLE 
GO

ALTER DATABASE [EdxStaging] SET  MULTI_USER 
GO

ALTER DATABASE [EdxStaging] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [EdxStaging] SET DB_CHAINING OFF 
GO

ALTER DATABASE [EdxStaging] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [EdxStaging] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO

ALTER DATABASE [EdxStaging] SET DELAYED_DURABILITY = DISABLED 
GO

ALTER DATABASE [EdxStaging] SET QUERY_STORE = OFF
GO

USE [EdxStaging]
GO

ALTER DATABASE SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = OFF;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET LEGACY_CARDINALITY_ESTIMATION = PRIMARY;
GO

ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 0;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET MAXDOP = PRIMARY;
GO

ALTER DATABASE SCOPED CONFIGURATION SET PARAMETER_SNIFFING = ON;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET PARAMETER_SNIFFING = PRIMARY;
GO

ALTER DATABASE SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = OFF;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET QUERY_OPTIMIZER_HOTFIXES = PRIMARY;
GO

ALTER DATABASE [EdxStaging] SET  READ_WRITE 
GO

DROP TABLE IF EXISTS [dbo].[Edx_DailyEvents]
GO

-- Create table to store telemetry data
CREATE TABLE [dbo].[Edx_DailyEvents](
	[filename] [varchar] (255) NOT NULL,
	[username] [nvarchar](255) NULL,
	[event_type] [varchar](2000) NULL,
	[ip] [varchar](64) NULL,
	[agent] [varchar](4000) NULL,
	[host] [varchar](255) NULL,
	[referer] [varchar](2000) NULL,
	[accept_language] [varchar](500) NULL,
	[eventtime] [varchar](50) NULL,
	[session] [varchar](100) NULL,
	[name] [varchar](250) NULL,
	[event_source] [varchar](250) NULL,
	[user_id] [varchar](100) NULL,
	[org_id] [varchar](100) NULL,
	[course_id] [varchar](255) NULL,
	[path] [varchar](2000) NULL,
	[component] [varchar](100) NULL,
	[app_version] [varchar](50) NULL,
	[app_name] [varchar](100) NULL,
	[grade] [numeric](10, 2) NULL,
	[attempts] [int] NULL,
	[max_grade] [numeric](10, 2) NULL,
	[code] [varchar](150) NULL,
	[id] [varchar](150) NULL,
	[mode] [varchar](100) NULL,
	[eventtextcode] [varchar](50) NULL,
	[eventtexttype] [varchar](50) NULL,
	[eventtextid] [varchar](200) NULL,
	[eventnewtime] [varchar](50) NULL,
	[eventoldtime] [varchar](50) NULL,
	[eventcurrenttime] [varchar](50) NULL,
	[certificateenrollmentmode] [nvarchar](100) NULL,
	[certificateid] [nvarchar](100) NULL,
	[certificategenerationmode] [nvarchar](100) NULL,
	[certificateurl] [nvarchar](255) NULL,
	[certificatecourseid] [nvarchar](255) NULL,
	[certificatesocialnetwork] [nvarchar](255) NULL,
	[certificatesourceurl] [nvarchar](255) NULL,
	[eventsub_problemid] [varchar](100) NULL,
	[eventsub_inputtype] [varchar](100) NULL,
	[eventsub_responsetype] [varchar](100) NULL,
	[eventsub_variant] [varchar](100) NULL,
	[eventsub_correct] [varchar](100) NULL
) ON [PRIMARY]
GO