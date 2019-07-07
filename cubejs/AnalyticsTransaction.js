cube(`AnalyticsTransaction`, {
    sql: `select * from analytics_transactions`,
    title: `Параметры заказов`,
     
    joins: {  
        GeneralAccounts: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsTransaction}.account_id = ${GeneralAccounts}.account_id`
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
        transaction_id: { 
            sql: `transaction_id`,
            type: `string`,
            title: `Внутренний идентификатор транзакции`
         },  
        unique_id: { 
            sql: `unique_id`,
            type: `string`,
            title: `Уникальный идентификатор`
         } 
    }
});