cube(`AnalyticsMcfFact`, {
    sql: `select * from analytics_mcf_facts`,
    title: `Многоканальные последовательности`,
     
    joins: {  
        GeneralDate: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsMcfFact}.dates_id = ${GeneralDate}.id`
         },  
        GeneralTraffic: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsMcfFact}.traffic_id = ${GeneralTraffic}.id`
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
            title: `Идентификатор подключенного аккаунта`
         },  
        assisted_count: { 
            sql: `assisted_count`,
            type: `sum`,
            title: `Количество вспомогательного участия в конверсиях`
         },  
        assisted_value: { 
            sql: `assisted_value`,
            type: `sum`,
            title: `Значение вспомогательного участия в конверсиях`
         },  
        first_count: { 
            sql: `first_count`,
            type: `sum`,
            title: `Количество конверсий с первого взаимодействия`
         },  
        first_value: { 
            sql: `first_value`,
            type: `sum`,
            title: `Значение конверсий с первого взаимодействия`
         },  
        last_count: { 
            sql: `last_count`,
            type: `sum`,
            title: `Количество конверсий с последнего взаимодействия`
         },  
        last_value: { 
            sql: `last_value`,
            type: `sum`,
            title: `Значение конверсий с последнего взаимодействия`
         },  
        total_count: { 
            sql: `total_count`,
            type: `sum`,
            title: `Общее количество конверсий`
         },  
        total_value: { 
            sql: `total_value`,
            type: `sum`,
            title: `Общее значение конверсий`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true
         },  
        conversion_type: { 
            sql: `conversion_type`,
            type: `string`,
            title: `Тип конверсии`
         },  
        goal_number: { 
            sql: `goal_number`,
            type: `string`,
            title: `Номер цели`
         } 
    }
});