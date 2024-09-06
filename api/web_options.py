import constants.defs as defs

def make_options(k):

    return dict(key=k,text=k,value=k)

def get_options():

    ps=[p for p in defs.INVESTING_COM_PAIRS.keys()]
    ps.sort()


    return dict(granularities=[make_options(g) for g in defs.TFS.keys()], pairs=[make_options(p) for p in ps])