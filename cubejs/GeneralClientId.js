cube(`GeneralClientId`, {
    sql: `select * from general_clientids`,
    title: `Параметры посетителей`,
     
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
        clientid: { 
            sql: `clientid`,
            type: `string`,
            title: `Идентификатор посетителя сайта`
         },  
        userid: { 
            sql: `userid`,
            type: `string`,
            title: `Идентификатор пользователя`
         },  
        phone: { 
            sql: `phone`,
            type: `string`,
            title: `Телефон клиента`
         },  
        email: { 
            sql: `email`,
            type: `string`,
            title: `e-mail клиента`
         } 
    }
});