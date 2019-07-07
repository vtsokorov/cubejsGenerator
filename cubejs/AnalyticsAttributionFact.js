cube(`AnalyticsAttributionFact`, {
    sql: `select * from analytics_attributions_facts`,
    title: `Атрибуция трафика`,
     
    joins: {  
        GeneralAccounts: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsAttributionFact}.account_id = ${GeneralAccounts}.account_id`
         },  
        GeneralDate: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsAttributionFact}.dates_id = ${GeneralDate}.id`
         },  
        GeneralSite: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsAttributionFact}.sites_id = ${GeneralSite}.id`
         },  
        GeneralClientId: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsAttributionFact}.clientids_id = ${GeneralClientId}.id`
         },  
        AnalyticsDevice: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsAttributionFact}.devices_id = ${AnalyticsDevice}.id`
         },  
        GeneralTraffic: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsAttributionFact}.traffic_id = ${GeneralTraffic}.id`
         },  
        GeneralLocation: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsAttributionFact}.locations_id = ${GeneralLocation}.id`
         } 
    }, 
    measures: {  
        count: { 
            drillMembers: [id],
            type: `count`,
            title: `Идентификатор записи`
         },  
        processor_id: { 
            sql: `processor_id`,
            type: `sum`,
            title: `Идентификатор задания`
         },  
        conversion_id: { 
            sql: `conversion_id`,
            type: `sum`,
            title: `Идентификатор конверсии`
         },  
        object_id: { 
            sql: `object_id`,
            type: `sum`,
            title: `Идентификатор объекта`
         },  
        session_number: { 
            sql: `session_number`,
            type: `sum`,
            title: `Порядковый номер посещения`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true,
            shown: true
         },  
        last_session: { 
            sql: `last_session`,
            type: `string`,
            title: `Является ли последним посещением`
         } 
    }
});