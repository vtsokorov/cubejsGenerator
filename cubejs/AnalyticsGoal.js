cube(`AnalyticsGoal`, {
    sql: `select * from analytics_goals`,
    title: `Параметры целей`,
     
    joins: {  
        GeneralAccounts: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsGoal}.account_id = ${GeneralAccounts}.account_id`
         } 
    }, 
    measures: { 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true,
            shown: true
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