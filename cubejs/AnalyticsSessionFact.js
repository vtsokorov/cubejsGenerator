cube(`AnalyticsSessionFact`, {
    sql: `select * from analytics_sessions_facts`,
    title: `Посещения сайта`,
     
    joins: {  
        GeneralAccounts: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsSessionFact}.account_id = ${GeneralAccounts}.account_id`
         },  
        GeneralDate: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsSessionFact}.dates_id = ${GeneralDate}.id`
         },  
        GeneralSite: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsSessionFact}.sites_id = ${GeneralSite}.id`
         },  
        GeneralClientId: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsSessionFact}.clientids_id = ${GeneralClientId}.id`
         },  
        AnalyticsDevice: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsSessionFact}.devices_id = ${AnalyticsDevice}.id`
         },  
        GeneralTraffic: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsSessionFact}.traffic_id = ${GeneralTraffic}.id`
         },  
        GeneralLocation: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsSessionFact}.locations_id = ${GeneralLocation}.id`
         } 
    }, 
    measures: {  
        count: { 
            drillMembers: [id],
            type: `count`,
            title: `Идентификатор записи`
         },  
        sessions: { 
            sql: `sessions`,
            type: `sum`,
            title: `Сессии`
         },  
        bounces: { 
            sql: `bounces`,
            type: `sum`,
            title: `Отказы`
         },  
        pageviews: { 
            sql: `pageviews`,
            type: `sum`,
            title: `Просмотры страниц`
         },  
        duration: { 
            sql: `duration`,
            type: `sum`,
            title: `Продолжительность`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true,
            shown: true
         },  
        session_id: { 
            sql: `session_id`,
            type: `string`,
            title: `Идентификатор сеанса`
         },  
        user_type: { 
            sql: `user_type`,
            type: `string`,
            title: `Тип пользователя`
         } 
    }
});