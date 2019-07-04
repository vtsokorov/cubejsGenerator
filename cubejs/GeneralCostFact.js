cube(`GeneralCostFact`, {
    sql: `select * from general_costs_facts`,
    title: `���������� �� ��������`,
     
    joins: {  
        GeneralDate: { 
            relationship: `belongsTo`,
            sql: `${GeneralCostFact}.dates_id = ${GeneralDate}.id`
         },  
        GeneralSite: { 
            relationship: `belongsTo`,
            sql: `${GeneralCostFact}.sites_id = ${GeneralSite}.id`
         },  
        GeneralTraffic: { 
            relationship: `belongsTo`,
            sql: `${GeneralCostFact}.traffic_id = ${GeneralTraffic}.id`
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
        impressions: { 
            sql: `impressions`,
            type: `sum`,
            title: `������`
         },  
        clicks: { 
            sql: `clicks`,
            type: `sum`,
            title: `�����`
         },  
        cost: { 
            sql: `cost`,
            type: `sum`,
            title: `�������`
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