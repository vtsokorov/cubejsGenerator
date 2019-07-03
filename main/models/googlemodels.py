# -*- coding: utf-8 -*-
from app import db


class AnalyticsGoal(db.Model):
    __tablename__ = 'analytics_goals'
    __humanname__ = 'Параметры целей'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор цели'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    goal_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Внутренний идентификатор цели'})
    name = db.Column(db.Unicode(256), info={'verbose_name': 'Наименование цели'})
    active = db.Column(db.Boolean, info={'verbose_name': 'Активность'})

    __table_args__ = (
        db.Index('analytics_goals_idx_1', account_id),
        db.Index('analytics_goals_idx_2', goal_id),
    )

    def __repr__(self):
        return '<AnalyticsGoal %r>' % self.goal_id


class AnalyticsSessionFact(db.Model):
    __tablename__ = 'analytics_sessions_facts'
    __humanname__ = 'Посещения сайта'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    dates_id = db.Column(db.Integer, db.ForeignKey('general_dates.id', name='analytics_sessions_facts_general_dates'), nullable=False, info={'verbose_name': 'Идентификатор даты'})
    sites_id = db.Column(db.Integer, db.ForeignKey('general_sites.id', name='analytics_sessions_facts_general_sites'), nullable=False, info={'verbose_name': 'Идентификатор сайта'})
    clientids_id = db.Column(db.Integer, db.ForeignKey('general_clientids.id', name='analytics_sessions_facts_general_clientids'), nullable=False, info={'verbose_name': 'Идентификатор клиента'})
    devices_id = db.Column(db.Integer, db.ForeignKey('analytics_devices.id', name='analytics_sessions_facts_analytics_devices'), nullable=False, info={'verbose_name': 'Идентификатор типа устройства'})
    traffic_id = db.Column(db.Integer, db.ForeignKey('general_traffic.id', name='analytics_sessions_facts_general_traffic'), nullable=False, info={'verbose_name': 'Идентификатор источника трафика'})
    locations_id = db.Column(db.Integer, db.ForeignKey('general_locations.id', name='analytics_sessions_facts_general_locations'), nullable=False, info={'verbose_name': 'Идентификатор местоположения'})
    session_id = db.Column(db.Unicode(64), nullable=False, info={'verbose_name': 'Идентификатор сеанса'})
    user_type = db.Column(db.Unicode(32), nullable=False, info={'verbose_name': 'Тип пользователя'})
    sessions = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Сессии'})
    bounces = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Отказы'})
    pageviews = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Просмотры страниц'})
    duration = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Продолжительность'})

    general_dates = db.relationship('GeneralDate', foreign_keys=dates_id)
    general_traffic = db.relationship('GeneralTraffic', foreign_keys=traffic_id)
    general_sites = db.relationship('GeneralSite', foreign_keys=sites_id)
    general_clientids = db.relationship('GeneralClientId', foreign_keys=clientids_id)
    general_locations = db.relationship('GeneralLocation', foreign_keys=locations_id)
    analytics_devices = db.relationship('AnalyticsDevice', foreign_keys=devices_id)

    __table_args__ = (
        db.Index('analytics_sessions_facts_idx_1', account_id),
        db.Index('analytics_sessions_facts_idx_2', dates_id),
        db.Index('analytics_sessions_facts_idx_3', clientids_id),
        db.Index('analytics_sessions_facts_idx_4', traffic_id),
    )

    def __repr__(self):
        return '<AnalyticsSessionFact %r>' % self.id


class AnalyticsTransaction(db.Model):
    __tablename__ = 'analytics_transactions'
    __humanname__ = 'Параметры заказов'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор транзакции'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    transaction_id = db.Column(db.Unicode(128), nullable=False, info={'verbose_name': 'Внутренний идентификатор транзакции'})
    unique_id = db.Column(db.Unicode(64), info={'verbose_name': 'Уникальный идентификатор'})

    __table_args__ = (
        db.Index('analytics_transactions_idx_1', account_id),
        db.Index('analytics_transactions_idx_2', transaction_id),
    )

    def __repr__(self):
        return '<AnalyticsTransaction %r>' % self.transaction_id


class AnalyticsCostFact(db.Model):
    __tablename__ = 'analytics_costs_facts'
    __humanname__ = 'Статистика по объявлениям'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    dates_id = db.Column(db.Integer, db.ForeignKey('general_dates.id', name='analytics_costs_facts_general_dates'), nullable=False, info={'verbose_name': 'Идентификатор даты'})
    sites_id = db.Column(db.Integer, db.ForeignKey('general_sites.id', name='analytics_costs_facts_general_sites'), nullable=False, info={'verbose_name': 'Идентификатор сайта'})
    traffic_id = db.Column(db.Integer, db.ForeignKey('general_traffic.id', name='analytics_costs_facts_general_traffic'), nullable=False, info={'verbose_name': 'Идентификатор источника трафика'})
    impressions_context = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Показы в рекламной сети'})
    impressions_search = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Показы на поиске'})
    impressions = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Показы'})
    clicks_context = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Клики в рекламной сети'})
    clicks_search = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Клики на поиске'})
    clicks = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Клики'})
    cost_context = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Расходы в рекламной сети'})
    cost_search = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Расходы на поиске'})
    cost = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Расходы'})

    general_dates = db.relationship('GeneralDate', foreign_keys=dates_id)
    general_traffic = db.relationship('GeneralTraffic', foreign_keys=traffic_id)
    general_sites = db.relationship('GeneralSite', foreign_keys=sites_id)

    __table_args__ = (
        db.Index('analytics_costs_facts_idx_1', account_id),
        db.Index('analytics_costs_facts_idx_2', dates_id),
        db.Index('analytics_costs_facts_idx_3', traffic_id),
    )

    def __repr__(self):
        return '<AnalyticsCostFact %r>' % self.id


class AnalyticsGoalFact(db.Model):
    __tablename__ = 'analytics_goals_facts'
    __humanname__ = 'Достигнутые цели'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    dates_id = db.Column(db.Integer, db.ForeignKey('general_dates.id', name='analytics_goals_facts_general_dates'), nullable=False, info={'verbose_name': 'Идентификатор даты'})
    sites_id = db.Column(db.Integer, db.ForeignKey('general_sites.id', name='analytics_goals_facts_general_sites'), nullable=False, info={'verbose_name': 'Идентификатор сайта'})
    clientids_id = db.Column(db.Integer, db.ForeignKey('general_clientids.id', name='analytics_goals_facts_general_clientids'), nullable=False, info={'verbose_name': 'Идентификатор клиента'})
    devices_id = db.Column(db.Integer, db.ForeignKey('analytics_devices.id', name='analytics_goals_facts_analytics_devices'), nullable=False, info={'verbose_name': 'Идентификатор типа устройства'})
    traffic_id = db.Column(db.Integer, db.ForeignKey('general_traffic.id', name='analytics_goals_facts_general_traffic'), nullable=False, info={'verbose_name': 'Идентификатор источника трафика'})
    locations_id = db.Column(db.Integer, db.ForeignKey('general_locations.id', name='analytics_goals_facts_general_locations'), nullable=False, info={'verbose_name': 'Идентификатор местоположения'})
    goals_id = db.Column(db.Integer, db.ForeignKey('analytics_goals.id', name='analytics_goals_facts_analytics_goals'), nullable=False, info={'verbose_name': 'Идентификатор цели'})
    completions = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Количество'})
    goal_value = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Ценность'})

    analytics_goals = db.relationship('AnalyticsGoal', foreign_keys=goals_id)
    general_dates = db.relationship('GeneralDate', foreign_keys=dates_id)
    general_traffic = db.relationship('GeneralTraffic', foreign_keys=traffic_id)
    general_clientids = db.relationship('GeneralClientId', foreign_keys=clientids_id)
    general_locations = db.relationship('GeneralLocation', foreign_keys=locations_id)
    analytics_devices = db.relationship('AnalyticsDevice', foreign_keys=devices_id)
    general_sites = db.relationship('GeneralSite', foreign_keys=sites_id)

    __table_args__ = (
        db.Index('analytics_goals_facts_idx_1', account_id),
        db.Index('analytics_goals_facts_idx_2', dates_id),
        db.Index('analytics_goals_facts_idx_3', clientids_id),
        db.Index('analytics_goals_facts_idx_4', traffic_id),
    )

    def __repr__(self):
        return '<AnalyticsGoalFact %r>' % self.id


class AnalyticsTransactionFact(db.Model):
    __tablename__ = 'analytics_transactions_facts'
    __humanname__ = 'Оформленные заказы'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    dates_id = db.Column(db.Integer, db.ForeignKey('general_dates.id', name='analytics_transactions_facts_general_dates'), nullable=False, info={'verbose_name': 'Идентификатор даты'})
    sites_id = db.Column(db.Integer, db.ForeignKey('general_sites.id', name='analytics_transactions_facts_general_sites'), nullable=False, info={'verbose_name': 'Идентификатор сайта'})
    clientids_id = db.Column(db.Integer, db.ForeignKey('general_clientids.id', name='analytics_transactions_facts_general_clientids'), nullable=False, info={'verbose_name': 'Идентификатор клиента'})
    devices_id = db.Column(db.Integer, db.ForeignKey('analytics_devices.id', name='analytics_transactions_facts_analytics_devices'), nullable=False, info={'verbose_name': 'Идентификатор типа устройства'})
    traffic_id = db.Column(db.Integer, db.ForeignKey('general_traffic.id', name='analytics_transactions_facts_general_traffic'), nullable=False, info={'verbose_name': 'Идентификатор источника трафика'})
    locations_id = db.Column(db.Integer, db.ForeignKey('general_locations.id', name='analytics_transactions_facts_general_locations'), nullable=False, info={'verbose_name': 'Идентификатор местоположения'})
    transactions_id = db.Column(db.Integer, db.ForeignKey('analytics_transactions.id', name='analytics_transactions_facts_analytics_transactions'), nullable=False, info={'verbose_name': 'Идентификатор транзакции'})
    revenue = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Доход'})
    shipping = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Доставка'})
    tax = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Налог'})

    analytics_transactions = db.relationship('AnalyticsTransaction', foreign_keys=transactions_id)
    general_dates = db.relationship('GeneralDate', foreign_keys=dates_id)
    general_traffic = db.relationship('GeneralTraffic', foreign_keys=traffic_id)
    general_clientids = db.relationship('GeneralClientId', foreign_keys=clientids_id)
    analytics_devices = db.relationship('AnalyticsDevice', foreign_keys=devices_id)
    general_locations = db.relationship('GeneralLocation', foreign_keys=locations_id)
    general_sites = db.relationship('GeneralSite', foreign_keys=sites_id)

    __table_args__ = (
        db.Index('analytics_transactions_facts_idx_1', account_id),
        db.Index('analytics_transactions_facts_idx_2', dates_id),
        db.Index('analytics_transactions_facts_idx_3', clientids_id),
        db.Index('analytics_transactions_facts_idx_4', traffic_id),
    )

    def __repr__(self):
        return '<AnalyticsTransactionFact %r>' % self.id


class AnalyticsProductFact(db.Model):
    __tablename__ = 'analytics_products_facts'
    __humanname__ = 'Приобретенный товар'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    dates_id = db.Column(db.Integer, db.ForeignKey('general_dates.id', name='analytics_products_facts_general_dates'), nullable=False, info={'verbose_name': 'Идентификатор даты'})
    sites_id = db.Column(db.Integer, db.ForeignKey('general_sites.id', name='analytics_products_facts_general_sites'), nullable=False, info={'verbose_name': 'Идентификатор сайта'})
    clientids_id = db.Column(db.Integer, db.ForeignKey('general_clientids.id', name='analytics_products_facts_general_clientids'), nullable=False, info={'verbose_name': 'Идентификатор клиента'})
    devices_id = db.Column(db.Integer, db.ForeignKey('analytics_devices.id', name='analytics_products_facts_analytics_devices'), nullable=False, info={'verbose_name': 'Идентификатор типа устройства'})
    traffic_id = db.Column(db.Integer, db.ForeignKey('general_traffic.id', name='analytics_products_facts_general_traffic'), nullable=False, info={'verbose_name': 'Идентификатор источника трафика'})
    locations_id = db.Column(db.Integer, db.ForeignKey('general_locations.id', name='analytics_products_facts_general_locations'), nullable=False, info={'verbose_name': 'Идентификатор местоположения'})
    transactions_id = db.Column(db.Integer, db.ForeignKey('analytics_transactions.id', name='analytics_products_facts_analytics_transactions'), nullable=False, info={'verbose_name': 'Идентификатор транзакции'})
    products_id = db.Column(db.Integer, db.ForeignKey('analytics_products.id', name='analytics_products_facts_analytics_products'), nullable=False, info={'verbose_name': 'Идентификатор товара'})
    quantity = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Количество'})
    item_revenue = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Доход'})

    analytics_products = db.relationship('AnalyticsProduct', foreign_keys=products_id)
    analytics_transactions = db.relationship('AnalyticsTransaction', foreign_keys=transactions_id)
    general_clientids = db.relationship('GeneralClientId', foreign_keys=clientids_id)
    general_traffic = db.relationship('GeneralTraffic', foreign_keys=traffic_id)
    general_dates = db.relationship('GeneralDate', foreign_keys=dates_id)
    analytics_devices = db.relationship('AnalyticsDevice', foreign_keys=devices_id)
    general_locations = db.relationship('GeneralLocation', foreign_keys=locations_id)
    general_sites = db.relationship('GeneralSite', foreign_keys=sites_id)

    __table_args__ = (
        db.Index('analytics_products_facts_idx_1', account_id),
        db.Index('analytics_products_facts_idx_2', dates_id),
        db.Index('analytics_products_facts_idx_3', clientids_id),
        db.Index('analytics_products_facts_idx_4', traffic_id),
    )

    def __repr__(self):
        return '<AnalyticsProductFact %r>' % self.id


class AnalyticsProduct(db.Model):
    __tablename__ = 'analytics_products'
    __humanname__ = 'Параметры товаров'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор товара'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    product_id = db.Column(db.Unicode(64), nullable=False, info={'verbose_name': 'Внутренний идентификатор товара'})
    category = db.Column(db.Unicode(256), info={'verbose_name': 'Категория товара'})
    brand = db.Column(db.Unicode(256), info={'verbose_name': 'Бренд товара'})
    name = db.Column(db.Unicode(256), info={'verbose_name': 'Наименование товара'})

    __table_args__ = (
        db.Index('analytics_products_idx_1', account_id),
        db.Index('analytics_products_idx_2', product_id),
    )

    def __repr__(self):
        return '<AnalyticsProduct %r>' % self.product_id


class AnalyticsDevice(db.Model):
    __tablename__ = 'analytics_devices'
    __humanname__ = 'Параметры устройств'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор типа устройства'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    category = db.Column(db.Unicode(16), nullable=False, info={'verbose_name': 'Тип устройства'})
    browser = db.Column(db.Unicode(128), info={'verbose_name': 'Браузер'})
    browser_version = db.Column(db.Unicode(128), info={'verbose_name': 'Версия браузера'})
    os = db.Column(db.Unicode(128), info={'verbose_name': 'Операционная система'})
    os_version = db.Column(db.Unicode(128), info={'verbose_name': 'Версия операционной системы'})

    __table_args__ = (
        db.Index('analytics_devices_idx_1', account_id),
    )

    def __repr__(self):
        return '<AnalyticsDevice %r>' % self.id


class AnalyticsMcfFact(db.Model):
    __tablename__ = 'analytics_mcf_facts'
    __humanname__ = 'Многоканальные последовательности'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    dates_id = db.Column(db.Integer, db.ForeignKey('general_dates.id', name='analytics_mcf_facts_general_dates'), nullable=False, info={'verbose_name': 'Идентификатор даты'})
    traffic_id = db.Column(db.Integer, db.ForeignKey('general_traffic.id', name='analytics_mcf_facts_general_traffic'), nullable=False, info={'verbose_name': 'Идентификатор источника трафика'})
    assisted_count = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Количество вспомогательного участия в конверсиях'})
    assisted_value = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Значение вспомогательного участия в конверсиях'})
    first_count = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Количество конверсий с первого взаимодействия'})
    first_value = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Значение конверсий с первого взаимодействия'})
    last_count = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Количество конверсий с последнего взаимодействия'})
    last_value = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Значение конверсий с последнего взаимодействия'})
    total_count = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Общее количество конверсий'})
    total_value = db.Column(db.Numeric(18,2), nullable=False, info={'verbose_name': 'Общее значение конверсий'})
    conversion_type = db.Column(db.Unicode(16), info={'verbose_name': 'Тип конверсии'})
    goal_number = db.Column(db.Unicode(16), info={'verbose_name': 'Номер цели'})

    general_dates = db.relationship('GeneralDate', foreign_keys=dates_id)
    general_traffic = db.relationship('GeneralTraffic', foreign_keys=traffic_id)

    __table_args__ = (
        db.Index('analytics_mcf_facts_idx_1', account_id),
        db.Index('analytics_mcf_facts_idx_2', dates_id),
        db.Index('analytics_mcf_facts_idx_3', traffic_id),
    )

    def __repr__(self):
        return '<AnalyticsMcfFact %r>' % self.id


class AnalyticsEvent(db.Model):
    __tablename__ = 'analytics_events'
    __humanname__ = 'Параметры событий'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор события'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    category = db.Column(db.Unicode(128), info={'verbose_name': 'Категория события'})
    action = db.Column(db.Unicode(128), info={'verbose_name': 'Действие события'})
    label = db.Column(db.Unicode(128), info={'verbose_name': 'Метка события'})

    __table_args__ = (
        db.Index('Copy_of_analytics_goals_idx_1', account_id),
    )

    def __repr__(self):
        return '<AnalyticsEvent %r>' % self.goal_id


class AnalyticsEventFact(db.Model):
    __tablename__ = 'analytics_events_facts'
    __humanname__ = 'Достигнутые события'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    dates_id = db.Column(db.Integer, db.ForeignKey('general_dates.id', name='analytics_events_facts_general_dates'), nullable=False, info={'verbose_name': 'Идентификатор даты'})
    sites_id = db.Column(db.Integer, db.ForeignKey('general_sites.id', name='analytics_events_facts_general_sites'), nullable=False, info={'verbose_name': 'Идентификатор сайта'})
    clientids_id = db.Column(db.Integer, db.ForeignKey('general_clientids.id', name='analytics_events_facts_general_clientids'), nullable=False, info={'verbose_name': 'Идентификатор клиента'})
    devices_id = db.Column(db.Integer, db.ForeignKey('analytics_devices.id', name='analytics_events_facts_analytics_devices'), nullable=False, info={'verbose_name': 'Идентификатор типа устройства'})
    traffic_id = db.Column(db.Integer, db.ForeignKey('general_traffic.id', name='analytics_events_facts_general_traffic'), nullable=False, info={'verbose_name': 'Идентификатор источника трафика'})
    locations_id = db.Column(db.Integer, db.ForeignKey('general_locations.id', name='analytics_events_facts_general_locations'), nullable=False, info={'verbose_name': 'Идентификатор местоположения'})
    events_id = db.Column(db.Integer, db.ForeignKey('analytics_events.id', name='analytics_events_facts_analytics_events'), nullable=False, info={'verbose_name': 'Идентификатор события'})
    total_events = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Количество'})
    unique_events = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Количество уникальных'})
    event_value = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Ценность'})

    analytics_events = db.relationship('AnalyticsEvent', foreign_keys=events_id)
    general_dates = db.relationship('GeneralDate', foreign_keys=dates_id)
    general_traffic = db.relationship('GeneralTraffic', foreign_keys=traffic_id)
    general_clientids = db.relationship('GeneralClientId', foreign_keys=clientids_id)
    general_locations = db.relationship('GeneralLocation', foreign_keys=locations_id)
    analytics_devices = db.relationship('AnalyticsDevice', foreign_keys=devices_id)
    general_sites = db.relationship('GeneralSite', foreign_keys=sites_id)

    __table_args__ = (
        db.Index('analytics_events_facts_idx_1', account_id),
        db.Index('analytics_events_facts_idx_2', dates_id),
        db.Index('analytics_events_facts_idx_3', clientids_id),
        db.Index('analytics_events_facts_idx_4', traffic_id),
    )

    def __repr__(self):
        return '<AnalyticsEventFact %r>' % self.id


class AnalyticsHit(db.Model):
    __tablename__ = 'analytics_hits'
    __humanname__ = 'Полученные хиты'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    full_date = db.Column(db.DateTime, nullable=False, info={'verbose_name': 'Дата и время хита'})
    clientid = db.Column(db.Unicode(64), nullable=False, info={'verbose_name': 'Идентификатор посетителя сайта'})
    hit = db.Column(db.UnicodeText, nullable=False, info={'verbose_name': 'Параметры хита'})

    __table_args__ = (
        db.Index('analytics_hits_idx_1', account_id),
    )

    def __repr__(self):
        return '<AnalyticsHit %r>' % self.id


class AnalyticsAttributionFact(db.Model):
    __tablename__ = 'analytics_attributions_facts'
    __humanname__ = 'Атрибуция трафика'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    processor_id = db.Column(db.Integer, info={'verbose_name': 'Идентификатор задания'})
    dates_id = db.Column(db.Integer, db.ForeignKey('general_dates.id', name='analytics_attributions_facts_general_dates'), nullable=False, info={'verbose_name': 'Идентификатор даты'})
    sites_id = db.Column(db.Integer, db.ForeignKey('general_sites.id', name='analytics_attributions_facts_general_sites'), nullable=False, info={'verbose_name': 'Идентификатор сайта'})
    clientids_id = db.Column(db.Integer, db.ForeignKey('general_clientids.id', name='analytics_attributions_facts_general_clientids'), nullable=False, info={'verbose_name': 'Идентификатор клиента'})
    devices_id = db.Column(db.Integer, db.ForeignKey('analytics_devices.id', name='analytics_attributions_facts_analytics_devices'), nullable=False, info={'verbose_name': 'Идентификатор типа устройства'})
    traffic_id = db.Column(db.Integer, db.ForeignKey('general_traffic.id', name='analytics_attributions_facts_general_traffic'), nullable=False, info={'verbose_name': 'Идентификатор источника трафика'})
    locations_id = db.Column(db.Integer, db.ForeignKey('general_locations.id', name='analytics_attributions_facts_general_locations'), nullable=False, info={'verbose_name': 'Идентификатор местоположения'})
    conversion_id = db.Column(db.Integer, info={'verbose_name': 'Идентификатор конверсии'})
    object_id = db.Column(db.Integer, info={'verbose_name': 'Идентификатор объекта'})
    session_number = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Порядковый номер посещения'})
    last_session = db.Column(db.Boolean, nullable=False, info={'verbose_name': 'Является ли последним посещением'})

    general_locations = db.relationship('GeneralLocation', foreign_keys=locations_id)
    general_sites = db.relationship('GeneralSite', foreign_keys=sites_id)
    general_traffic = db.relationship('GeneralTraffic', foreign_keys=traffic_id)
    general_clientids = db.relationship('GeneralClientId', foreign_keys=clientids_id)
    analytics_devices = db.relationship('AnalyticsDevice', foreign_keys=devices_id)
    general_dates = db.relationship('GeneralDate', foreign_keys=dates_id)

    __table_args__ = (
        db.Index('analytics_attributions_facts_idx_1', account_id),
        db.Index('analytics_attributions_facts_idx_2', dates_id),
        db.Index('analytics_attributions_facts_idx_3', clientids_id),
        db.Index('analytics_attributions_facts_idx_4', traffic_id),
    )

    def __repr__(self):
        return '<AnalyticsAttributionFact %r>' % self.id


class AnalyticsReport(db.Model):
    __tablename__ = 'analytics_reports'
    __humanname__ = 'Выгруженные отчеты'

    id = db.Column(db.Integer, primary_key=True, info={'verbose_name': 'Идентификатор записи'})
    account_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор подключенного аккаунта'})
    processor_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор отчета'})
    simple_date = db.Column(db.Date, nullable=False, info={'verbose_name': 'Дата отчета'})
    row_id = db.Column(db.Integer, nullable=False, info={'verbose_name': 'Идентификатор строки'})
    row_data = db.Column(db.UnicodeText, nullable=False, info={'verbose_name': 'Содержимое строки'})

    __table_args__ = (
        db.Index('analytics_reports_idx_1', account_id),
        db.Index('analytics_reports_idx_2', processor_id),
        db.Index('analytics_reports_idx_3', simple_date),
    )

    def __repr__(self):
        return '<AnalyticsReport %r>' % self.id
