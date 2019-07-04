cube(`GeneralTraffic`, {
    sql: `select * from general_traffic`,
    title: `Параметры трафика`,
     
    joins: { 
    }, 
    measures: {  
        count: { 
            drillMembers: [id],
            type: `count`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true
         },  
        grouping: { 
            sql: `grouping`,
            type: `string`,
            title: `Название группы`
         },  
        source: { 
            sql: `source`,
            type: `string`,
            title: `Источник`
         },  
        medium: { 
            sql: `medium`,
            type: `string`,
            title: `Канал`
         },  
        campaign: { 
            sql: `campaign`,
            type: `string`,
            title: `Кампания`
         },  
        content: { 
            sql: `content`,
            type: `string`,
            title: `Объявление`
         },  
        keyword: { 
            sql: `keyword`,
            type: `string`,
            title: `Ключевое слово`
         },  
        landing_page: { 
            sql: `landing_page`,
            type: `string`,
            title: `Страница входа`
         },  
        traffic_hash: { 
            sql: `traffic_hash`,
            type: `string`,
            title: `Хэш траффика`
         } 
    }
});