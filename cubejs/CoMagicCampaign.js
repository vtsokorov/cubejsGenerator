cube(`CoMagicCampaign`, {
    sql: `select * from comagic_campaigns`,
    title: `Параметры кампаний`,
     
    joins: { 
    }, 
    measures: { 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true
         },  
        name: { 
            sql: `name`,
            type: `string`,
            title: `Название кампании`
         },  
        description: { 
            sql: `description`,
            type: `string`,
            title: `Описание кампании`
         },  
        campaign_type: { 
            sql: `campaign_type`,
            type: `string`,
            title: `Тип кампании`
         },  
        engine: { 
            sql: `engine`,
            type: `string`,
            title: `Платформа интегрированной кампании`
         },  
        status: { 
            sql: `status`,
            type: `string`,
            title: `Статус`
         },  
        cost_ratio_operator: { 
            sql: `cost_ratio_operator`,
            type: `string`,
            title: `Оператор расчета расходов`
         } 
    }
});