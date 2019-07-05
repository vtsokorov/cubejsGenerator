cube(`AnalyticsDevice`, {
    sql: `select * from analytics_devices`,
    title: `Параметры устройств`,
     
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
        category: { 
            sql: `category`,
            type: `string`,
            title: `Тип устройства`
         },  
        browser: { 
            sql: `browser`,
            type: `string`,
            title: `Браузер`
         },  
        browser_version: { 
            sql: `browser_version`,
            type: `string`,
            title: `Версия браузера`
         },  
        os: { 
            sql: `os`,
            type: `string`,
            title: `Операционная система`
         },  
        os_version: { 
            sql: `os_version`,
            type: `string`,
            title: `Версия операционной системы`
         } 
    }
});