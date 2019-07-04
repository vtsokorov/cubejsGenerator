cube(`GeneralTraffic`, {
    sql: `select * from general_traffic`,
    title: `��������� �������`,
     
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
        grouping: { 
            sql: `grouping`,
            type: `string`,
            title: `�������� ������`
         },  
        source: { 
            sql: `source`,
            type: `string`,
            title: `��������`
         },  
        medium: { 
            sql: `medium`,
            type: `string`,
            title: `�����`
         },  
        campaign: { 
            sql: `campaign`,
            type: `string`,
            title: `��������`
         },  
        content: { 
            sql: `content`,
            type: `string`,
            title: `����������`
         },  
        keyword: { 
            sql: `keyword`,
            type: `string`,
            title: `�������� �����`
         },  
        landing_page: { 
            sql: `landing_page`,
            type: `string`,
            title: `�������� �����`
         },  
        traffic_hash: { 
            sql: `traffic_hash`,
            type: `string`,
            title: `��� ��������`
         } 
    }
});