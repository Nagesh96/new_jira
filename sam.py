import ftplib
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

try:
    # Get FTP server details from environment variables
    ftp_host = os.environ.get('FTP_SERVER')
    ftp_user = os.environ.get('WTS_FTP_USERNAME')
    ftp_pass = os.environ.get('WTS_FTP_PASSWORD')

    logging.info('WTS- FTP host: ' + str(ftp_host))
    logging.info('WTS- FTP user: ' + str(ftp_user))

    # Connect to the FTP server
    f = ftplib.FTP(ftp_host)

    # Login
    f.login(user=ftp_user, passwd=ftp_pass)

    # Change directory
    f.cwd('/FTP-WTS-DAE/Transactions/Monthly WTS Trade Data')

    logging.info('WTS 100 FTP Login Success')

except ftplib.error_perm as error:
    logging.error('WTS 100 FTP Login Failed: ' + str(error))

except Exception as e:
    logging.error('An unexpected error occurred: ' + str(e))

finally:
    # Ensure FTP connection is closed
    if 'f' in locals():
        f.quit()
