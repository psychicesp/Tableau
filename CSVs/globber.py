#%%

import pandas as pd
#%%
years = [2019,2020]
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
months_dict = {
    '01':'January',
    '02':'February',
    '03':'March',
    '04':'April',
    '05':'May',
    '06':'June',
    '07':'July',
    '08':'August',
    '09':'September',
    '10':'October',
    '11':'November',
    '12':'December'
}
big_df = pd.DataFrame()
#%%
for year in years:
    for month in months:
        try:
            df = pd.read_csv(f"JC-{year}{month}-citibike-tripdata.csv")
            df['Year']=year
            df['Month']=months_dict[month]
            big_df = pd.concat([big_df,df])

        except:
            pass

# %%
big_df = big_df.reset_index()
big_df = big_df.reset_index()
big_df.rename(columns = {
    'level_0':'Trip_ID'
}, inplace = True)
big_df.drop('index', axis = 1, inplace = True)
big_df
#%%
big_df.set_index('Trip_ID').to_csv('bike_data.csv')
# %%
