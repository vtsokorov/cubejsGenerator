cube(`AnalyticsGoalFact`, {
    sql: `select * from analytics_goals_facts`,
    title: `Достигнутые цели`,
     
    joins: {  
        GeneralDate: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsGoalFact}.dates_id = ${GeneralDate}.id`
         },  
        GeneralSite: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsGoalFact}.sites_id = ${GeneralSite}.id`
         },  
        GeneralClientId: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsGoalFact}.clientids_id = ${GeneralClientId}.id`
         },  
        AnalyticsDevice: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsGoalFact}.devices_id = ${AnalyticsDevice}.id`
         },  
        GeneralTraffic: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsGoalFact}.traffic_id = ${GeneralTraffic}.id`
         },  
        GeneralLocation: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsGoalFact}.locations_id = ${GeneralLocation}.id`
         },  
        AnalyticsGoal: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsGoalFact}.goals_id = ${AnalyticsGoal}.id`
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
        completions: { 
            sql: `completions`,
            type: `sum`,
            title: `Количество`
         },  
        goal_value: { 
            sql: `goal_value`,
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