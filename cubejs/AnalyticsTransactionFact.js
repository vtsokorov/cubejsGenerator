cube(`AnalyticsTransactionFact`, {
    sql: `select * from analytics_transactions_facts`,
    title: `Оформленные заказы`,
     
    joins: {  
        GeneralAccounts: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsTransactionFact}.account_id = ${GeneralAccounts}.account_id`
         },  
        GeneralDate: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsTransactionFact}.dates_id = ${GeneralDate}.id`
         },  
        GeneralSite: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsTransactionFact}.sites_id = ${GeneralSite}.id`
         },  
        GeneralClientId: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsTransactionFact}.clientids_id = ${GeneralClientId}.id`
         },  
        AnalyticsDevice: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsTransactionFact}.devices_id = ${AnalyticsDevice}.id`
         },  
        GeneralTraffic: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsTransactionFact}.traffic_id = ${GeneralTraffic}.id`
         },  
        GeneralLocation: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsTransactionFact}.locations_id = ${GeneralLocation}.id`
         },  
        AnalyticsTransaction: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsTransactionFact}.transactions_id = ${AnalyticsTransaction}.id`
         } 
    }, 
    measures: {  
        count: { 
            drillMembers: [id],
            type: `count`,
            title: `Идентификатор записи`
         },  
        revenue: { 
            sql: `revenue`,
            type: `sum`,
            title: `Доход`
         },  
        shipping: { 
            sql: `shipping`,
            type: `sum`,
            title: `Доставка`
         },  
        tax: { 
            sql: `tax`,
            type: `sum`,
            title: `Налог`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true,
            shown: true
         } 
    }
});