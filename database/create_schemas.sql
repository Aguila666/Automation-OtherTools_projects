USE AutomationProjectsDB;
GO

CREATE SCHEMA etl;
GO

CREATE SCHEMA pipelines;
GO

CREATE SCHEMA monitoring;
GO

CREATE SCHEMA automation;
GO

CREATE SCHEMA staging;
GO

CREATE SCHEMA warehouse;
GO

CREATE SCHEMA orchestration;
GO

CREATE SCHEMA cloud;
GO

PRINT 'Schemas created successfully.';
GO


USE AutomationProjectsDB;
GO

SELECT name
FROM sys.schemas
ORDER BY name;