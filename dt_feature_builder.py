from datetime import datetime
from datetime import date
import calendar


def week_of_month(target_date):
    # https://stackoverflow.com/questions/25249033/week-of-a-month-pandas
    target_date = target_date.to_datetime()

    days_this_month = calendar.mdays[target_date.month]
    for i in range(1, days_this_month):
        d = datetime(target_date.year, target_date.month, i)
        if d.day - d.weekday() > 0:
            start_date = d
            break
    # now we can use the modulo 7 appraoch
    week_of_month = (target_date - start_date).days // 7 + 1
    return week_of_month


def day_of_quarter(target_date)
    # calculate the day in the quarter
    target_date = target_date.to_datetime()
    
    current_quarter = round((current_date.month - 1) / 3 + 1)
    current_year = target_date.year
    # current year quarter start dates
    q1 = date(current_year, 1, 1)
    q2 = date(current_year, 4, 1)
    q3 = date(current_year, 7, 1)
    q4 = date(current_year, 10, 1)
    # calucate number of days since quarter start
    if current_quarter == 1:
        day_of_quarter = target_date - q1
    elif current_quarter == 2:
        day_of_quarter = target_date - q2
    elif current_quarter == 3:
        day_of_quarter = target_date - q3
    elif current_quarter == 4:
        day_of_quarter = target_date - q4
    return day_of_quarter


def week_of_quarter(target_date)
    # calculate the day in the quarter
    return week_of_quarter


def month_of_quarter(target_date)
    # calculate the month in the quarter
    target_date = target_date.to_datetime()
    target_month = target_date.month - 1
    month_of_quarter = (target_month % 3) + 1
    return month_of_quarter


def datetime_feature_generator(df, date_col, freq):
    """
    Partition a datetime column into new feature columns
    :param host: input dataframe
    :param date_col: column name to partition into features
    :param freq: frequency of date column; ie weekly, monthly, etc
    :return df: dataframe with new columns
    """
    if freq == 'daily':
        df = daily_feature_generator(df, date_col)
        df = weekly_feature_generator(df, date_col)
        df = monthly_feature_generator(df, date_col)
        df = quarterly_feature_generator(df, date_col)
    if freq in ['daily', 'weekly']:
        df = weekly_feature_generator(df, date_col)
        df = monthly_feature_generator(df, date_col)
        df = quarterly_feature_generator(df, date_col)
    if freq in ['daily', 'weekly', 'monthly']:
        df = monthly_feature_generator(df, date_col)
        df = quarterly_feature_generator(df, date_col)
    if freq in ['daily', 'weekly', 'monthly', 'quarterly']:
        df = quarterly_feature_generator(df, date_col)
    if freq in ['daily', 'weekly', 'monthly', 'quarterly', 'yearly']:
        df = yearly_feature_generator(df, date_col)
    return df
    
def daily_feature_generator(df, date_col):
    # weekday T/F
    df['is_weekday'] = df[date_col].dt.weekday
    # day of week
    df['day_of_year'] = df[date_col].dt.dayofweek
    # day of month
    df['day_of_month'] = df[date_col].dt.day
    # day of quarter
    df['day_of_quarter'] = df[date_col].apply(day_of_quarter)
    # day of year
    df['day_of_year'] = df[date_col].dt.dayofyear
    return df


def weekly_feature_generator(df, date_col):
    # week in month
    df['week_of_month'] = df[date_col].apply(week_of_month)
    # week of year
    df['week_of_year'] = df[date_col].dt.weekofyear
    # week in quarter
    # TODO
    return df


def monthly_feature_generator(df, date_col):
    # month in quarter
    df['month_of_quarter'] = df[date_col].apply(week_of_month)
    # month in year
    df['month_of_year'] = df[date_col].dt.month
    return df


def quarterly_feature_generator(df, date_col):
    # quarter in year
    df['quarter_of_year'] = df[date_col].dt.quarter
    return df


def yearly_feature_generator(df, date_col):
    # year as int
    df['year'] = df[date_col].dt.year
    return df
