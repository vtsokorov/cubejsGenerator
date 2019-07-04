cube(`GeneralDate`, {
    sql: `select * from general_dates`,
    title: `Параметры дат`,
     
    joins: { 
    }, 
    measures: {  
        count: { 
            drillMembers: [id],
            type: `count`
         },  
        year: { 
            sql: `year`,
            type: `sum`,
            title: `Год`
         },  
        quarter: { 
            sql: `quarter`,
            type: `sum`,
            title: `Номер квартала`
         },  
        month: { 
            sql: `month`,
            type: `sum`,
            title: `Номер месяца`
         },  
        week: { 
            sql: `week`,
            type: `sum`,
            title: `Номер недели`
         },  
        weekday: { 
            sql: `weekday`,
            type: `sum`,
            title: `Номер дня недели`
         },  
        day: { 
            sql: `day`,
            type: `sum`,
            title: `День`
         },  
        hour: { 
            sql: `hour`,
            type: `sum`,
            title: `Час`
         },  
        minute: { 
            sql: `minute`,
            type: `sum`,
            title: `Минута`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true
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