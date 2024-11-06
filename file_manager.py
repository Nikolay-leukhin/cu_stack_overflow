import time


def write_to_df_report(df, file_name):
    df.to_csv(f'{file_name}', sep='\t', index=False, encoding='utf-8')


def log_exception(exception):
    with open('logger.txt', 'a', encoding='utf-8') as file:
        file.write(f"Time: {time.time()} | Exception {exception} \n")