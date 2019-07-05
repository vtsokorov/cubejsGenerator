cube(`AnalyticsGoal`, {
    sql: `select * from analytics_goals`,
    title: `Параметры целей`,
     
    joins: { 
    }, 
    measures: { 
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