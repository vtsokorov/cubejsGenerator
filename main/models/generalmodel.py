# -*- coding: utf-8 -*-
from app import db


class GeneralLocation(db.Model):
    __tablename__ = 'general_locations'
    __humanname__ = 'Параметры местоположений'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор местоположения'})
    country_iso = db.Column(db.Unicode(8), info={'verbose_name': 'Код страны'})
    country = db.Column(db.Unicode(64), info={'verbose_name': 'Страна'})
    region_iso = db.Column(db.Unicode(8), info={'verbose_name': 'Код региона'})
    region = db.Column(db.Unicode(128), info={'verbose_name': 'Регион'})
    city = db.Column(db.Unicode(64), info={'verbose_name': 'Город'})
    latitude = db.Column(db.Unicode(32), info={'verbose_name': 'Широта'})
    longitude = db.Column(db.Unicode(32), info={'verbose_name': 'Долгота'})
    location_hash = db.Column(db.Unicode(32))

    __table_args__ = (
        db.Index('general_locations_idx_1', location_hash),
    )

    def __repr__(self):
        return '<GeneralLocation %r>' % self.id


class GeneralDate(db.Model):
    __tablename__ = 'general_dates'
    __humanname__ = 'Параметры дат'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор даты'})
    full_date = db.Column(db.DateTime, nullable=False, info={'verbose_name': 'Дата и время'})
    year = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Год'})
    quarter = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Номер квартала'})
    quarter_label = db.Column(db.Unicode(3), nullable=False, info={'verbose_name': 'Квартал'})
    month = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Номер месяца'})
    month_label = db.Column(db.Unicode(10), nullable=False, info={'verbose_name': 'Месяц'})
    week = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Номер недели'})
    weekday = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Номер дня недели'})
    weekday_label = db.Column(db.Unicode(11), nullable=False, info={'verbose_name': 'День недели'})
    day = db.Column(db.Integer, nullable=False, info={'verbose_name': 'День'})
    hour = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Час'})
    minute = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Минута'})
    date_hash = db.Column(db.Unicode(32), nullable=False, info={'verbose_name': 'Хеш-сумма записи'})
    simple_date = db.Column(db.Date, nullable=False, info={'verbose_name': 'Дата'})

    __table_args__ = (
        db.Index('general_dates_idx_1', date_hash),
        db.Index('general_dates_idx_2', full_date),
        db.Index('general_dates_idx_3', simple_date),
    )

    def __repr__(self):
        return '<GeneralDate %r>' % self.id


class GeneralTraffic(db.Model):
    __tablename__ = 'general_traffic'
    __humanname__ = 'Параметры трафика'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор источника трафика'})
    grouping = db.Column(db.Unicode(128), info={'verbose_name': 'Название группы'})
    source = db.Column(db.Unicode(256), info={'verbose_name': 'Источник'})
    medium = db.Column(db.Unicode(256), info={'verbose_name': 'Канал'})
    campaign = db.Column(db.Unicode(256), info={'verbose_name': 'Кампания'})
    content = db.Column(db.Unicode(256), info={'verbose_name': 'Объявление'})
    keyword = db.Column(db.Unicode(256), info={'verbose_name': 'Ключевое слово'})
    landing_page = db.Column(db.Unicode(256), info={'verbose_name': 'Страница входа'})
    traffic_hash = db.Column(db.Unicode(32), info={'verbose_name': 'Хэш траффика'})

    __table_args__ = (
        db.Index('general_traffic_idx_1', traffic_hash),
    )

    def __repr__(self):
        return '<GeneralTraffic %r>' % self.id


class GeneralClientId(db.Model):
    __tablename__ = 'general_clientids'
    __humanname__ = 'Параметры посетителей'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор клиента'})
    clientid = db.Column(db.Unicode(64), nullable=False, info={'verbose_name': 'Идентификатор посетителя сайта'})
    userid = db.Column(db.Unicode(64), info={'verbose_name': 'Идентификатор пользователя'})
    phone = db.Column(db.Unicode(64), info={'verbose_name': 'Телефон клиента'})
    email = db.Column(db.Unicode(64), info={'verbose_name': 'e-mail клиента'})

    __table_args__ = (
        db.Index('general_clientids_idx_1', clientid),
    )

    def __repr__(self):
        return '<GeneralClientId %r>' % self.id


class GeneralSite(db.Model):
    __tablename__ = 'general_sites'
    __humanname__ = 'Параметры сайтов'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор сайта'})
    domain = db.Column(db.Unicode(64), info={'verbose_name': 'Доменное имя'})
    description = db.Column(db.Unicode(256), info={'verbose_name': 'Описание'})

    __table_args__ = (
        db.Index('general_sites_idx_1', domain),
    )

    def __repr__(self):
        return '<GeneralSite %r>' % self.id


class GeneralCostFact(db.Model):
    __tablename__ = 'general_costs_facts'
    __humanname__ = 'Статистика по расходам'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    dates_id = db.Column(db.Integer, db.ForeignKey('general_dates.id', name='general_costs_facts_general_dates'), nullable=False, info={'verbose_name': 'Идентификатор даты'})
    sites_id = db.Column(db.Integer, db.ForeignKey('general_sites.id', name='general_costs_facts_general_sites'), nullable=False, info={'verbose_name': 'Идентификатор сайта'})
    traffic_id = db.Column(db.Integer, db.ForeignKey('general_traffic.id', name='general_costs_facts_general_traffic'), nullable=False, info={'verbose_name': 'Идентификатор источника трафика'})
    impressions = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Показы'})
    clicks = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Клики'})
    cost = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Расходы'})

    general_dates = db.relationship('GeneralDate', foreign_keys=dates_id)
    general_traffic = db.relationship('GeneralTraffic', foreign_keys=traffic_id)
    general_sites = db.relationship('GeneralSite', foreign_keys=sites_id)

    __table_args__ = (
        db.Index('general_costs_facts_idx_1', account_id),
        db.Index('general_costs_facts_idx_2', dates_id),
        db.Index('general_costs_facts_idx_3', traffic_id),
    )

    def __repr__(self):
        return '<GeneralCostFact %r>' % self.id


class GeneralAccounts(db.Model):
    __tablename__ = 'general_accounts'
    __humanname__ = 'Параметры источников данных'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    caption = db.Column(db.Unicode(128), nullable=False, info={'verbose_name': 'Название источника'})
    service = db.Column(db.Unicode(64), nullable=False, info={'verbose_name': 'Сервис'})
    enabled = db.Column(db.Boolean, nullable=False, info={'verbose_name': 'Включен'})
    status = db.Column(db.Unicode(32), info={'verbose_name': 'Статус загрузки'})
    interval_start = db.Column(db.Date, info={'verbose_name': 'Дата начала интервала'})
    interval_end = db.Column(db.Date, info={'verbose_name': 'Дата окончания интервала'})

    __table_args__ = (
        db.Index('general_accounts_idx_1', account_id),
    )

    def __repr__(self):
        return '<GeneralAccounts %r>' % self.id
