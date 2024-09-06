from scraping.bloomberg_com import bloomberg_com
from scraping.dailyfx_com import dailyfx_com
from scraping.investing_com import get_pair, investing_com, investing_com_summary
from scraping.fx_calendar import fx_calendar
if __name__ == '__main__':      
  print(investing_com_summary("D"))