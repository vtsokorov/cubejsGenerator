cube(`AnalyticsProductFact`, {
    sql: `select * from analytics_products_facts`,
    title: `Приобретенный товар`,
     
    joins: {  
        GeneralDate: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsProductFact}.dates_id = ${GeneralDate}.id`
         },  
        GeneralSite: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsProductFact}.sites_id = ${GeneralSite}.id`
         },  
        GeneralClientId: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsProductFact}.clientids_id = ${GeneralClientId}.id`
         },  
        AnalyticsDevice: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsProductFact}.devices_id = ${AnalyticsDevice}.id`
         },  
        GeneralTraffic: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsProductFact}.traffic_id = ${GeneralTraffic}.id`
         },  
        GeneralLocation: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsProductFact}.locations_id = ${GeneralLocation}.id`
         },  
        AnalyticsTransaction: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsProductFact}.transactions_id = ${AnalyticsTransaction}.id`
         },  
        AnalyticsProduct: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsProductFact}.products_id = ${AnalyticsProduct}.id`
         } 
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
        quantity: { 
            sql: `quantity`,
            type: `sum`,
            title: `Количество`
         },  
        item_revenue: { 
            sql: `item_revenue`,
            type: `sum`,
            title: `Доход`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true
         } 
    }
});