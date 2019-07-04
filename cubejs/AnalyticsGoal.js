cube(`AnalyticsGoal`, {
    sql: `select * from analytics_goals`,
    title: `Параметры целей`,
     
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
            title: `Идентификатор подключенного аккаунта`
         },  
        goal_id: { 
            sql: `goal_id`,
            type: `sum`,
            title: `Внутренний идентификатор цели`
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
            title: `Наименование цели`
         },  
        active: { 
            sql: `active`,
            type: `string`,
            title: `Активность`
         } 
    }
});