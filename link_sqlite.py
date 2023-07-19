#!/usr/bin/python3

# Author   : JasonHung
# Date     : 20230315
# Update   : 20230315
# Function : sqlite3

import logging , sqlite3


################################################################################################################################################
#
# main
#
################################################################################################################################################
class main_content:

    ########
    # log
    ########
    log_format = "%(asctime)s , %(message)s"
    logging.basicConfig(format=log_format , level=logging.INFO , datefmt="%H:%M:%S")

    def __init__(self):
        self.main()
    
    def main(self):
        
        conn = sqlite3.connect('control/test.db')
        try:
            c = conn.cursor()

            sql = "select name from test3"
            res = c.execute(sql).fetchall()

            for val in res:
                print(str(val[0]))

            logging.info("select success.")

        except Exception as e:
            logging.info(str(e))
        finally:
            conn.commit()
            conn.close()

################################################################################################################################################
#
# start
#
################################################################################################################################################
if __name__  == "__main__":
    main = main_content()
