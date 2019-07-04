cube(`CoMagicCall`, {
    sql: `select * from comagic_calls`,
    title: `Параметры звонков`,
     
    joins: { 
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
        call_id: { 
            sql: `call_id`,
            type: `sum`,
            title: `Внутренний идентификатор звонка`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true
         },  
        finish_reason: { 
            sql: `finish_reason`,
            type: `string`,
            title: `Причина окончания звонка`
         },  
        direction: { 
            sql: `direction`,
            type: `string`,
            title: `Направление звонка`
         },  
        call_source: { 
            sql: `call_source`,
            type: `string`,
            title: `Источник звонка`
         },  
        is_lost: { 
            sql: `is_lost`,
            type: `string`,
            title: `Потерянный звонок`
         },  
        contact_phone_number: { 
            sql: `contact_phone_number`,
            type: `string`,
            title: `Номер контакта`
         },  
        virtual_phone_number: { 
            sql: `virtual_phone_number`,
            type: `string`,
            title: `Виртуальный номер`
         },  
        visitor_id: { 
            sql: `visitor_id`,
            type: `string`,
            title: `Идентификатор посетителя`
         },  
        visitor_session_id: { 
            sql: `visitor_session_id`,
            type: `string`,
            title: `Идентификатор сессии посетителя`
         },  
        visitor_device: { 
            sql: `visitor_device`,
            type: `string`,
            title: `Устройство пользователя`
         },  
        channel: { 
            sql: `channel`,
            type: `string`,
            title: `Канал`
         },  
        referrer: { 
            sql: `referrer`,
            type: `string`,
            title: `Источник перехода`
         } 
    }
});