cube(`GeneralAccounts`, {
    sql: `select * from general_accounts`,
    title: `Параметры источников данных`,
     
    joins: { 
    }, 
    measures: { 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true,
            shown: true
         },  
        caption: { 
            sql: `caption`,
            type: `string`,
            title: `Название источника`
         },  
        service: { 
            sql: `service`,
            type: `string`,
            title: `Сервис`
         },  
        enabled: { 
            sql: `enabled`,
            type: `string`,
            title: `Включен`
         },  
        status: { 
            sql: `status`,
            type: `string`,
            title: `Статус загрузки`
         } 
    }
});