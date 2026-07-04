USE master;
GO

IF NOT EXISTS (
    SELECT name
    FROM sys.databases
    WHERE name = 'AutomationProjectsDB'
)
BEGIN
    CREATE DATABASE AutomationProjectsDB;
END
GO

PRINT 'Database AutomationProjectsDB created successfully.';
GO
