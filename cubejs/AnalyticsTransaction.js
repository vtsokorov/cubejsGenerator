cube(`AnalyticsTransaction`, {
    sql: `select * from analytics_transactions`,
    title: `Параметры заказов`,
     
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