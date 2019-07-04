cube(`AnalyticsTransaction`, {
    sql: `select * from analytics_transactions`,
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
        transaction_id: { 
            sql: `transaction_id`,
            type: `string`,
            title: `���������� ������������� ����������`
         },  
        unique_id: { 
            sql: `unique_id`,
            type: `string`,
            title: `���������� �������������`
         } 
    }
});