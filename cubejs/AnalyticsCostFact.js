cube(`AnalyticsCostFact`, {
    sql: `select * from analytics_costs_facts`,
    title: `���������� �� �����������`,
     
    joins: {  
        GeneralDate: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsCostFact}.dates_id = ${GeneralDate}.id`
         },  
        GeneralSite: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsCostFact}.sites_id = ${GeneralSite}.id`
         },  
        GeneralTraffic: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsCostFact}.traffic_id = ${GeneralTraffic}.id`
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
        impressions_context: { 
            sql: `impressions_context`,
            type: `sum`,
            title: `������ � ��������� ����`
         },  
        impressions_search: { 
            sql: `impressions_search`,
            type: `sum`,
            title: `������ �� ������`
         },  
        impressions: { 
            sql: `impressions`,
            type: `sum`,
            title: `������`
         },  
        clicks_context: { 
            sql: `clicks_context`,
            type: `sum`,
            title: `����� � ��������� ����`
         },  
        clicks_search: { 
            sql: `clicks_search`,
            type: `sum`,
            title: `����� �� ������`
         },  
        clicks: { 
            sql: `clicks`,
            type: `sum`,
            title: `�����`
         },  
        cost_context: { 
            sql: `cost_context`,
            type: `sum`,
            title: `������� � ��������� ����`
         },  
        cost_search: { 
            sql: `cost_search`,
            type: `sum`,
            title: `������� �� ������`
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