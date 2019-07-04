cube(`AnalyticsGoal`, {
    sql: `select * from analytics_goals`,
    title: `��������� �����`,
     
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
         },  
        goal_id: { 
            sql: `goal_id`,
            type: `sum`,
            title: `���������� ������������� ����`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true
         },  
        name: { 
            sql: `name`,
            type: `string`,
            title: `������������ ����`
         },  
        active: { 
            sql: `active`,
            type: `string`,
            title: `����������`
         } 
    }
});