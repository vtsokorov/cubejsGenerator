cube(`GeneralLocation`, {
    sql: `select * from general_locations`,
    title: `Параметры местоположений`,
     
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
            title: `Код страны`
         },  
        country: { 
            sql: `country`,
            type: `string`,
            title: `Страна`
         },  
        region_iso: { 
            sql: `region_iso`,
            type: `string`,
            title: `Код региона`
         },  
        region: { 
            sql: `region`,
            type: `string`,
            title: `Регион`
         },  
        city: { 
            sql: `city`,
            type: `string`,
            title: `Город`
         },  
        latitude: { 
            sql: `latitude`,
            type: `string`,
            title: `Широта`
         },  
        longitude: { 
            sql: `longitude`,
            type: `string`,
            title: `Долгота`
         },  
        location_hash: { 
            sql: `location_hash`,
            type: `string`
         } 
    }
});