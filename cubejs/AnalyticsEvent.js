cube(`AnalyticsEvent`, {
    sql: `select * from analytics_events`,
    title: `Параметры событий`,
     
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