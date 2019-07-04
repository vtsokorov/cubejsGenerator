cube(`AnalyticsDevice`, {
    sql: `select * from analytics_devices`,
    title: `��������� ���������`,
     
    joins: { 
    }, 
    measures: {  
        count: { 
            drillMembers: [id],
            type: `count`
         },  
        account_id: { 
            sql: `account_id`,
            type: `sum`,
            title: `������������� ������������� ��������`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true
         },  
        category: { 
            sql: `category`,
            type: `string`,
            title: `��� ����������`
         },  
        browser: { 
            sql: `browser`,
            type: `string`,
            title: `�������`
         },  
        browser_version: { 
            sql: `browser_version`,
            type: `string`,
            title: `������ ��������`
         },  
        os: { 
            sql: `os`,
            type: `string`,
            title: `������������ �������`
         },  
        os_version: { 
            sql: `os_version`,
            type: `string`,
            title: `������ ������������ �������`
         } 
    }
});