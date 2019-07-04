cube(`AnalyticsEvent`, {
    sql: `select * from analytics_events`,
    title: `Параметры событий`,
     
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