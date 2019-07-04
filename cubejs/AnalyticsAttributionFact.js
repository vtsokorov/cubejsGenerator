cube(`AnalyticsAttributionFact`, {
    sql: `select * from analytics_attributions_facts`,
    title: `��������� �������`,
     
    joins: {  
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
            type: `count`
         },  
        account_id: { 
            sql: `account_id`,
            type: `sum`,
            title: `������������� ������������� ��������`
         },  
        processor_id: { 
            sql: `processor_id`,
            type: `sum`,
            title: `������������� �������`
         },  
        conversion_id: { 
            sql: `conversion_id`,
            type: `sum`,
            title: `������������� ���������`
         },  
        object_id: { 
            sql: `object_id`,
            type: `sum`,
            title: `������������� �������`
         },  
        session_number: { 
            sql: `session_number`,
            type: `sum`,
            title: `���������� ����� ���������`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true
         },  
        last_session: { 
            sql: `last_session`,
            type: `string`,
            title: `�������� �� ��������� ����������`
         } 
    }
});