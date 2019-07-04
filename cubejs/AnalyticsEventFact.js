cube(`AnalyticsEventFact`, {
    sql: `select * from analytics_events_facts`,
    title: `Достигнутые события`,
     
    joins: {  
        GeneralDate: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsEventFact}.dates_id = ${GeneralDate}.id`
         },  
        GeneralSite: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsEventFact}.sites_id = ${GeneralSite}.id`
         },  
        GeneralClientId: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsEventFact}.clientids_id = ${GeneralClientId}.id`
         },  
        AnalyticsDevice: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsEventFact}.devices_id = ${AnalyticsDevice}.id`
         },  
        GeneralTraffic: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsEventFact}.traffic_id = ${GeneralTraffic}.id`
         },  
        GeneralLocation: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsEventFact}.locations_id = ${GeneralLocation}.id`
         },  
        AnalyticsEvent: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsEventFact}.events_id = ${AnalyticsEvent}.id`
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
        total_events: { 
            sql: `total_events`,
            type: `sum`,
            title: `Количество`
         },  
        unique_events: { 
            sql: `unique_events`,
            type: `sum`,
            title: `Количество уникальных`
         },  
        event_value: { 
            sql: `event_value`,
            type: `sum`,
            title: `Ценность`
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