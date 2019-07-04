cube(`GeneralLocation`, {
    sql: `select * from general_locations`,
    title: `��������� ��������������`,
     
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
        country_iso: { 
            sql: `country_iso`,
            type: `string`,
            title: `��� ������`
         },  
        country: { 
            sql: `country`,
            type: `string`,
            title: `������`
         },  
        region_iso: { 
            sql: `region_iso`,
            type: `string`,
            title: `��� �������`
         },  
        region: { 
            sql: `region`,
            type: `string`,
            title: `������`
         },  
        city: { 
            sql: `city`,
            type: `string`,
            title: `�����`
         },  
        latitude: { 
            sql: `latitude`,
            type: `string`,
            title: `������`
         },  
        longitude: { 
            sql: `longitude`,
            type: `string`,
            title: `�������`
         },  
        location_hash: { 
            sql: `location_hash`,
            type: `string`
         } 
    }
});