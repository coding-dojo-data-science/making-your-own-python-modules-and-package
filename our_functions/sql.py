def load_credentials(filename, verbose=True):
    import json
    with open(filename) as f:
        login = json.load(f)
    
    if verbose:
        print(f"[i] Credentials loaded from: {filename}")
        print('- Keys:')
        [print(f"    - {k}") for k in login.keys()]

    return login




def get_schema(table,debug=False):
    from sqlalchemy.types import Text, Integer, Float, NullType, Boolean, String
    ## save pandas dtypes in list, make empty dict
    dtypes = table.dtypes
    schema = {}
    
    # for each column
    for col in dtypes.index:
        ## print info if in debug mode
        if debug:
            print(f"{col} = {dtypes.loc[col]}")

        ## if its a string column (object)
        if dtypes.loc[col]=='object':
            
            ## Fill null values and make sure whole column is str
            data = table[col].fillna('').astype(str)
            
            ## get len first
            len_str = data.map(len).max()
            
            ## if the string is shorter than 21845 use String
            # (forget how i knew it was max size)
            if len_str < 21845:
                schema[col] = String( len_str + 1)
                
            ## If longer use Text
            else:
                schema[col] = Text(len_str+1)
        
        # if float make Float
        elif dtypes.loc[col] == 'float':
            schema[col] = Float()

        ## if int make Integer
        elif dtypes.loc[col] == 'int':
            schema[col] = Integer()
            
        ## if bool make Boolean
        elif dtypes.loc[col] == 'bool':
            schema[col] = Boolean()
            
    return schema
