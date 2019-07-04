cube(`GeneralSite`, {
    sql: `select * from general_sites`,
    title: `��������� ������`,
     
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
        domain: { 
            sql: `domain`,
            type: `string`,
            title: `�������� ���`
         },  
        description: { 
            sql: `description`,
            type: `string`,
            title: `��������`
         } 
    }
});