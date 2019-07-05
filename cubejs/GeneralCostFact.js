cube(`GeneralCostFact`, {
    sql: `select * from general_costs_facts`,
    title: `Статистика по расходам`,
     
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
            type: `count`,
            title: `Идентификатор записи`
         },  
        account_id: { 
            sql: `account_id`,
            type: `sum`,
            title: `Идентификатор подключенного аккаунта`
         },  
        impressions: { 
            sql: `impressions`,
            type: `sum`,
            title: `Показы`
         },  
        clicks: { 
            sql: `clicks`,
            type: `sum`,
            title: `Клики`
         },  
        cost: { 
            sql: `cost`,
            type: `sum`,
            title: `Расходы`
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