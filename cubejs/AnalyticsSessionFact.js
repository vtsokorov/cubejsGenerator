cube(`AnalyticsSessionFact`, {
    sql: `select * from analytics_sessions_facts`,
    title: `��������� �����`,
     
    joins: {  
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
            type: `count`
         },  
        account_id: { 
            sql: `account_id`,
            type: `sum`,
            title: `������������� ������������� ��������`
         },  
        sessions: { 
            sql: `sessions`,
            type: `sum`,
            title: `������`
         },  
        bounces: { 
            sql: `bounces`,
            type: `sum`,
            title: `������`
         },  
        pageviews: { 
            sql: `pageviews`,
            type: `sum`,
            title: `��������� �������`
         },  
        duration: { 
            sql: `duration`,
            type: `sum`,
            title: `�����������������`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true
         },  
        session_id: { 
            sql: `session_id`,
            type: `string`,
            title: `������������� ������`
         },  
        user_type: { 
            sql: `user_type`,
            type: `string`,
            title: `��� ������������`
         } 
    }
});