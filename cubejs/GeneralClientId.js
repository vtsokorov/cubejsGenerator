cube(`GeneralClientId`, {
    sql: `select * from general_clientids`,
    title: `��������� �����������`,
     
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
        clientid: { 
            sql: `clientid`,
            type: `string`,
            title: `������������� ���������� �����`
         },  
        userid: { 
            sql: `userid`,
            type: `string`,
            title: `������������� ������������`
         },  
        phone: { 
            sql: `phone`,
            type: `string`,
            title: `������� �������`
         },  
        email: { 
            sql: `email`,
            type: `string`,
            title: `e-mail �������`
         } 
    }
});