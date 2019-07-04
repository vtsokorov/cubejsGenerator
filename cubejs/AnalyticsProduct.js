cube(`AnalyticsProduct`, {
    sql: `select * from analytics_products`,
    title: `��������� �������`,
     
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
            title: `������������� ������������� ��������`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true
         },  
        product_id: { 
            sql: `product_id`,
            type: `string`,
            title: `���������� ������������� ������`
         },  
        category: { 
            sql: `category`,
            type: `string`,
            title: `��������� ������`
         },  
        brand: { 
            sql: `brand`,
            type: `string`,
            title: `����� ������`
         },  
        name: { 
            sql: `name`,
            type: `string`,
            title: `������������ ������`
         } 
    }
});