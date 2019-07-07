cube(`GeneralDate`, {
    sql: `select * from general_dates`,
    title: `Параметры дат`,
     
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
        quarter_label: { 
            sql: `quarter_label`,
            type: `string`,
            title: `Квартал`
         },  
        month_label: { 
            sql: `month_label`,
            type: `string`,
            title: `Месяц`
         },  
        weekday_label: { 
            sql: `weekday_label`,
            type: `string`,
            title: `День недели`
         },  
        date_hash: { 
            sql: `date_hash`,
            type: `string`,
            title: `Хеш-сумма записи`
         } 
    }
});