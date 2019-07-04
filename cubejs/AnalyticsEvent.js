cube(`AnalyticsEvent`, {
    sql: `select * from analytics_events`,
    title: `��������� �������`,
     
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
            title: `��������� �������`
         },  
        action: { 
            sql: `action`,
            type: `string`,
            title: `�������� �������`
         },  
        label: { 
            sql: `label`,
            type: `string`,
            title: `����� �������`
         } 
    }
});