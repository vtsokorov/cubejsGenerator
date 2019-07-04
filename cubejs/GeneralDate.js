cube(`GeneralDate`, {
    sql: `select * from general_dates`,
    title: `��������� ���`,
     
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
            title: `���`
         },  
        quarter: { 
            sql: `quarter`,
            type: `sum`,
            title: `����� ��������`
         },  
        month: { 
            sql: `month`,
            type: `sum`,
            title: `����� ������`
         },  
        week: { 
            sql: `week`,
            type: `sum`,
            title: `����� ������`
         },  
        weekday: { 
            sql: `weekday`,
            type: `sum`,
            title: `����� ��� ������`
         },  
        day: { 
            sql: `day`,
            type: `sum`,
            title: `����`
         },  
        hour: { 
            sql: `hour`,
            type: `sum`,
            title: `���`
         },  
        minute: { 
            sql: `minute`,
            type: `sum`,
            title: `������`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true
         },  
        full_date: { 
            sql: `full_date`,
            type: `string`,
            title: `���� � �����`
         },  
        quarter_label: { 
            sql: `quarter_label`,
            type: `string`,
            title: `�������`
         },  
        month_label: { 
            sql: `month_label`,
            type: `string`,
            title: `�����`
         },  
        weekday_label: { 
            sql: `weekday_label`,
            type: `string`,
            title: `���� ������`
         },  
        date_hash: { 
            sql: `date_hash`,
            type: `string`,
            title: `���-����� ������`
         } 
    }
});