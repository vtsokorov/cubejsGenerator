cube(`AnalyticsEvent`, {
    sql: `select * from analytics_events`,
    title: `Параметры событий`,
     
    joins: {  
        GeneralAccounts: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsEvent}.account_id = ${GeneralAccounts}.account_id`
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
        category: { 
            sql: `category`,
            type: `string`,
            title: `Категория события`
         },  
        action: { 
            sql: `action`,
            type: `string`,
            title: `Действие события`
         },  
        label: { 
            sql: `label`,
            type: `string`,
            title: `Метка события`
         } 
    }
});