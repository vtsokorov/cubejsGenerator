cube(`AnalyticsCostFact`, {
    sql: `select * from analytics_costs_facts`,
    title: `Статистика по объявлениям`,
     
    joins: {  
        GeneralAccounts: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsCostFact}.account_id = ${GeneralAccounts}.account_id`
         },  
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
            type: `count`,
            title: `Идентификатор записи`
         },  
        impressions_context: { 
            sql: `impressions_context`,
            type: `sum`,
            title: `Показы в рекламной сети`
         },  
        impressions_search: { 
            sql: `impressions_search`,
            type: `sum`,
            title: `Показы на поиске`
         },  
        impressions: { 
            sql: `impressions`,
            type: `sum`,
            title: `Показы`
         },  
        clicks_context: { 
            sql: `clicks_context`,
            type: `sum`,
            title: `Клики в рекламной сети`
         },  
        clicks_search: { 
            sql: `clicks_search`,
            type: `sum`,
            title: `Клики на поиске`
         },  
        clicks: { 
            sql: `clicks`,
            type: `sum`,
            title: `Клики`
         },  
        cost_context: { 
            sql: `cost_context`,
            type: `sum`,
            title: `Расходы в рекламной сети`
         },  
        cost_search: { 
            sql: `cost_search`,
            type: `sum`,
            title: `Расходы на поиске`
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
            primaryKey: true,
            shown: true
         } 
    }
});