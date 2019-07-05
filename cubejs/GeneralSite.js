cube(`GeneralSite`, {
    sql: `select * from general_sites`,
    title: `Параметры сайтов`,
     
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
        domain: { 
            sql: `domain`,
            type: `string`,
            title: `Доменное имя`
         },  
        description: { 
            sql: `description`,
            type: `string`,
            title: `Описание`
         } 
    }
});