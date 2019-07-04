# -*- coding: utf-8 -*-
from app import db


class CoMagicCallFact(db.Model):
    __tablename__ = 'comagic_calls_facts'
    __humanname__ = 'Звонки'
    __order__ = 1

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    dates_id = db.Column(db.Integer, db.ForeignKey('general_dates.id', name='comagic_calls_facts_general_dates'), nullable=False, info={'verbose_name': 'Идентификатор даты'})
    clientids_id = db.Column(db.Integer, db.ForeignKey('general_clientids.id', name='comagic_calls_facts_general_clientids'), nullable=False, info={'verbose_name': 'Идентификатор клиента'})
    locations_id = db.Column(db.Integer, db.ForeignKey('general_locations.id', name='comagic_calls_facts_general_locations'), nullable=False, info={'verbose_name': 'Идентификатор местоположения'})
    traffic_id = db.Column(db.Integer, db.ForeignKey('general_traffic.id', name='comagic_calls_facts_general_traffic'), nullable=False, info={'verbose_name': 'Идентификатор источника трафика'})
    sites_id = db.Column(db.Integer, db.ForeignKey('general_sites.id', name='comagic_calls_facts_general_sites'), nullable=False, info={'verbose_name': 'Идентификатор сайта'})
    calls_id = db.Column(db.Integer, db.ForeignKey('comagic_calls.id', name='comagic_calls_facts_comagic_calls'), nullable=False, info={'verbose_name': 'Идентификатор звонка'})
    campaigns_id = db.Column(db.Integer, db.ForeignKey('comagic_campaigns.id', name='comagic_calls_facts_comagic_campaigns'), nullable=False, info={'verbose_name': 'Идентификатор кампании'})
    wait_duration = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Длительность ожидания'})
    total_wait_duration = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Полная длительность ожидания'})
    talk_duration = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Длительность разговора'})
    clean_talk_duration = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Чистая длительность разговора'})
    total_duration = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Общая длительность звонка'})
    postprocess_duration = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Длительность постобработки'})

    general_traffic = db.relationship('GeneralTraffic', foreign_keys=traffic_id)
    general_sites = db.relationship('GeneralSite', foreign_keys=sites_id)
    general_clientids = db.relationship('GeneralClientId', foreign_keys=clientids_id)
    general_locations = db.relationship('GeneralLocation', foreign_keys=locations_id)
    general_dates = db.relationship('GeneralDate', foreign_keys=dates_id)
    comagic_calls = db.relationship('CoMagicCall', foreign_keys=calls_id)
    comagic_campaigns = db.relationship('CoMagicCampaign', foreign_keys=campaigns_id)

    __table_args__ = (
        db.Index('comagic_calls_facts_idx_1', account_id),
        db.Index('comagic_calls_facts_idx_2', dates_id),
    )

    def __repr__(self):
        return '<CoMagicCallFact %r>' % self.id


class CoMagicCall(db.Model):
    __tablename__ = 'comagic_calls'
    __humanname__ = 'Параметры звонков'
    __order__ = 3

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор звонка'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    call_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Внутренний идентификатор звонка'})
    finish_reason = db.Column(db.Unicode(128), nullable=False, info={'verbose_name': 'Причина окончания звонка'})
    direction = db.Column(db.Unicode(16), nullable=False, info={'verbose_name': 'Направление звонка'})
    call_source = db.Column(db.Unicode(32), nullable=False, info={'verbose_name': 'Источник звонка'})
    is_lost = db.Column(db.Boolean, nullable=False, info={'verbose_name': 'Потерянный звонок'})
    contact_phone_number = db.Column(db.Unicode(32), info={'verbose_name': 'Номер контакта'})
    virtual_phone_number = db.Column(db.Unicode(16), info={'verbose_name': 'Виртуальный номер'})
    visitor_id = db.Column(db.Unicode(16), info={'verbose_name': 'Идентификатор посетителя'})
    visitor_session_id = db.Column(db.Unicode(16), info={'verbose_name': 'Идентификатор сессии посетителя'})
    visitor_device = db.Column(db.Unicode(8), nullable=False, info={'verbose_name': 'Устройство пользователя'})
    channel = db.Column(db.Unicode(16), info={'verbose_name': 'Канал'})
    referrer = db.Column(db.Unicode(256), info={'verbose_name': 'Источник перехода'})

    __table_args__ = (
        db.Index('comagic_calls_idx_1', account_id),
        db.Index('comagic_calls_idx_2', call_id),
    )

    def __repr__(self):
        return '<CoMagicCall %r>' % self.id


class CoMagicReport(db.Model):
    __tablename__ = 'comagic_reports'
    __humanname__ = 'Выгруженные отчеты'
    __order__ = 4

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    processor_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор отчета'})
    simple_date = db.Column(db.Date, nullable=False, info={'verbose_name': 'Дата отчета'})
    row_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор строки'})
    row_data = db.Column(db.UnicodeText, nullable=False, info={'verbose_name': 'Содержимое строки'})

    __table_args__ = (
        db.Index('comagic_reports_idx_1', account_id),
        db.Index('comagic_reports_idx_2', processor_id),
        db.Index('comagic_reports_idx_3', simple_date),
    )

    def __repr__(self):
        return '<CoMagicReport %r>' % self.id


class CoMagicCampaign(db.Model):
    __tablename__ = 'comagic_campaigns'
    __humanname__ = 'Параметры кампаний'
    __order__ = 3

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор кампании'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    campaign_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Внутренний идентификатор кампании'})
    name = db.Column(db.Unicode(128), info={'verbose_name': 'Название кампании'})
    description = db.Column(db.Unicode(256), info={'verbose_name': 'Описание кампании'})
    campaign_type = db.Column(db.Unicode(16), info={'verbose_name': 'Тип кампании'})
    engine = db.Column(db.Unicode(16), info={'verbose_name': 'Платформа интегрированной кампании'})
    status = db.Column(db.Unicode(8), info={'verbose_name': 'Статус'})
    costs = db.Column(db.Numeric(18,2), info={'verbose_name': 'Расходы'})
    cost_ratio = db.Column(db.Integer, info={'verbose_name': 'Коэффициент расходов'})
    cost_ratio_operator = db.Column(db.Unicode(16), info={'verbose_name': 'Оператор расчета расходов'})

    __table_args__ = (
        db.Index('comagic_campaigns_idx_1', account_id),
        db.Index('comagic_campaigns_idx_2', campaign_id),
    )

    def __repr__(self):
        return '<CoMagicCampaign %r>' % self.id


class CoMagicCallTag(db.Model):
    __tablename__ = 'comagic_calls_tags'
    __humanname__ = 'Теги звонков'
    __order__ = 2

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    calls_id = db.Column(db.Integer, db.ForeignKey('comagic_calls.id', name='comagic_calls_tags_comagic_calls'), nullable=False, info={'verbose_name': 'Идентификатор звонка'})
    tag_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Внутренний идентификатор тега'})
    name = db.Column(db.Unicode(128), nullable=False, info={'verbose_name': 'Название тега'})
    tag_type = db.Column(db.Unicode(8), nullable=False, info={'verbose_name': 'Тип тега'})

    comagic_calls = db.relationship('CoMagicCall', foreign_keys=calls_id)

    __table_args__ = (
        db.Index('comagic_calls_tags_idx_1', account_id),
        db.Index('comagic_calls_tags_idx_2', calls_id),
    )

    def __repr__(self):
        return '<CoMagicCallTag %r>' % self.id


class CoMagicCallAttribute(db.Model):
    __tablename__ = 'comagic_calls_attributes'
    __humanname__ = 'Атрибуты звонков'
    __order__ = 2

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    calls_id = db.Column(db.Integer, db.ForeignKey('comagic_calls.id', name='comagic_calls_attributes_comagic_calls'), nullable=False, info={'verbose_name': 'Идентификатор звонка'})
    attribute_id = db.Column(db.Unicode(16), nullable=False, info={'verbose_name': 'Внутренний идентификатор атрибута'})
    name = db.Column(db.Unicode(128), nullable=False, info={'verbose_name': 'Название атрибута'})

    comagic_calls = db.relationship('CoMagicCall', foreign_keys=calls_id)

    __table_args__ = (
        db.Index('comagic_calls_attributes_idx_1', account_id),
        db.Index('comagic_calls_attributes_idx_2', calls_id),
    )

    def __repr__(self):
        return '<CoMagicCallAttribute %r>' % self.id
