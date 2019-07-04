cube(`AnalyticsMcfFact`, {
    sql: `select * from analytics_mcf_facts`,
    title: `�������������� ������������������`,
     
    joins: {  
        GeneralDate: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsMcfFact}.dates_id = ${GeneralDate}.id`
         },  
        GeneralTraffic: { 
            relationship: `belongsTo`,
            sql: `${AnalyticsMcfFact}.traffic_id = ${GeneralTraffic}.id`
         } 
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
         },  
        assisted_count: { 
            sql: `assisted_count`,
            type: `sum`,
            title: `���������� ���������������� ������� � ����������`
         },  
        assisted_value: { 
            sql: `assisted_value`,
            type: `sum`,
            title: `�������� ���������������� ������� � ����������`
         },  
        first_count: { 
            sql: `first_count`,
            type: `sum`,
            title: `���������� ��������� � ������� ��������������`
         },  
        first_value: { 
            sql: `first_value`,
            type: `sum`,
            title: `�������� ��������� � ������� ��������������`
         },  
        last_count: { 
            sql: `last_count`,
            type: `sum`,
            title: `���������� ��������� � ���������� ��������������`
         },  
        last_value: { 
            sql: `last_value`,
            type: `sum`,
            title: `�������� ��������� � ���������� ��������������`
         },  
        total_count: { 
            sql: `total_count`,
            type: `sum`,
            title: `����� ���������� ���������`
         },  
        total_value: { 
            sql: `total_value`,
            type: `sum`,
            title: `����� �������� ���������`
         } 
    }, 
    dimensions: {  
        id: { 
            sql: `id`,
            type: `number`,
            primaryKey: true
         },  
        conversion_type: { 
            sql: `conversion_type`,
            type: `string`,
            title: `��� ���������`
         },  
        goal_number: { 
            sql: `goal_number`,
            type: `string`,
            title: `����� ����`
         } 
    }
});