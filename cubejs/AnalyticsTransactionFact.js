cube(`AnalyticsTransactionFact`, {
    sql: `select * from analytics_transactions_facts`,
    title: `����������� ������`,
     
    joins: {  
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
            type: `count`
         },  
        account_id: { 
            sql: `account_id`,
            type: `sum`,
            title: `������������� ������������� ��������`
         },  
        revenue: { 
            sql: `revenue`,
            type: `sum`,
            title: `�����`
         },  
        shipping: { 
            sql: `shipping`,
            type: `sum`,
            title: `��������`
         },  
        tax: { 
            sql: `tax`,
            type: `sum`,
            title: `�����`
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