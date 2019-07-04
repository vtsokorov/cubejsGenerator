cube(`AnalyticsProduct`, {
    sql: `select * from analytics_products`,
    title: `Параметры товаров`,
     
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
        product_id: { 
            sql: `product_id`,
            type: `string`,
            title: `Внутренний идентификатор товара`
         },  
        category: { 
            sql: `category`,
            type: `string`,
            title: `Категория товара`
         },  
        brand: { 
            sql: `brand`,
            type: `string`,
            title: `Бренд товара`
         },  
        name: { 
            sql: `name`,
            type: `string`,
            title: `Наименование товара`
         } 
    }
});