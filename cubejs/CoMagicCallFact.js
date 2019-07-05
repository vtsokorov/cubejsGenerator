cube(`CoMagicCallFact`, {
    sql: `select * from comagic_calls_facts`,
    title: `Звонки`,
     
    joins: {  
        GeneralDate: { 
            relationship: `belongsTo`,
            sql: `${CoMagicCallFact}.dates_id = ${GeneralDate}.id`
         },  
        GeneralClientId: { 
            relationship: `belongsTo`,
            sql: `${CoMagicCallFact}.clientids_id = ${GeneralClientId}.id`
         },  
        GeneralLocation: { 
            relationship: `belongsTo`,
            sql: `${CoMagicCallFact}.locations_id = ${GeneralLocation}.id`
         },  
        GeneralTraffic: { 
            relationship: `belongsTo`,
            sql: `${CoMagicCallFact}.traffic_id = ${GeneralTraffic}.id`
         },  
        GeneralSite: { 
            relationship: `belongsTo`,
            sql: `${CoMagicCallFact}.sites_id = ${GeneralSite}.id`
         },  
        CoMagicCall: { 
            relationship: `belongsTo`,
            sql: `${CoMagicCallFact}.calls_id = ${CoMagicCall}.id`
         },  
        CoMagicCampaign: { 
            relationship: `belongsTo`,
            sql: `${CoMagicCallFact}.campaigns_id = ${CoMagicCampaign}.id`
         } 
    }, 
    measures: {  
        count: { 
            drillMembers: [id],
            type: `count`,
            title: `Идентификатор записи`
         },  
        account_id: { 
            sql: `account_id`,
            type: `sum`,
            title: `Идентификатор подключенного аккаунта`
         },  
        wait_duration: { 
            sql: `wait_duration`,
            type: `sum`,
            title: `Длительность ожидания`
         },  
        total_wait_duration: { 
            sql: `total_wait_duration`,
            type: `sum`,
            title: `Полная длительность ожидания`
         },  
        talk_duration: { 
            sql: `talk_duration`,
            type: `sum`,
            title: `Длительность разговора`
         },  
        clean_talk_duration: { 
            sql: `clean_talk_duration`,
            type: `sum`,
            title: `Чистая длительность разговора`
         },  
        total_duration: { 
            sql: `total_duration`,
            type: `sum`,
            title: `Общая длительность звонка`
         },  
        postprocess_duration: { 
            sql: `postprocess_duration`,
            type: `sum`,
            title: `Длительность постобработки`
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