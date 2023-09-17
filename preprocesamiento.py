# Importing necessary libraries
import pandas as pd

# Loading the initial data files
clientes_df = pd.read_csv("clientes.csv")
pedidos_df = pd.read_csv("PEDIDOS12MESES_MASQUERESTAURANTES.csv")

# Merge
merged_result_df = pd.merge(clientes_df, pedidos_df , how='left', on ='phone')
# Cleaning up the 'warehouse' column values by stripping whitespace
vlp_filtered_df = merged_result_df[merged_result_df['warehouse'].str.strip() == 'VLP']

# Setting 'warehouse' column values to 'VLP' to ensure consistency
vlp_filtered_df['warehouse'] = 'VLP'

# Loading the additional data file provided by the user
otd_clientes_df = pd.read_csv("data/otd_clientes_df.csv")

# Defining a function to perform merging in batches to optimize memory usage
def batch_merge(left, right, left_on, right_on, batch_size=50000):
    merged_dfs = []

    # Iterating over batches of the left dataframe
    for i in range(0, left.shape[0], batch_size):
        left_batch = left.iloc[i:i+batch_size]
        merged_batch = pd.merge(left_batch, right, left_on=left_on, right_on=right_on, how='inner')
        merged_dfs.append(merged_batch)

    # Concatenating the batch results into a single dataframe
    merged_result = pd.concat(merged_dfs, ignore_index=True)
    return merged_result

# Performing the merge in batches using the 'phone' and date columns
merged_vlp_otd_batched_df = batch_merge(vlp_filtered_df, otd_clientes_df, 
                                        left_on=['phone', 'order_close_date'], 
                                        right_on=['phone', 'deliver_date'])

# Removing duplicate rows from the merged dataframe
merged_vlp_otd_no_duplicates_df = merged_vlp_otd_batched_df.drop_duplicates()

# Creando un mapeo único para cada número de teléfono
unique_phones = merged_vlp_otd_no_duplicates_df['phone'].unique()
phone_to_id_mapping = {phone: idx for idx, phone in enumerate(unique_phones, 1)}

# Reemplazando la columna 'phone' con la columna 'customer_id' usando el mapeo
merged_vlp_otd_no_duplicates_df['customer_id'] = merged_vlp_otd_no_duplicates_df['phone'].map(phone_to_id_mapping)

# Eliminando la columna 'phone' original
merged_vlp_otd_no_duplicates_df = merged_vlp_otd_no_duplicates_df.drop(columns=['phone'])

# Mostrando las primeras filas del dataframe anonimizado
anonimizado_head = merged_vlp_otd_no_duplicates_df.head()

# Guardando el dataframe anonimizado en un archivo CSV
anonimized_file_path = "data/merged_vlp_otd_anonimized.csv"
merged_vlp_otd_no_duplicates_df.to_csv(anonimized_file_path, index=False)