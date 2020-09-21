#!/usr/bin/python
# -*- coding: utf-8 -*-


#from __init__ import *
from tests.module.Logger import logger
import ftplib,os

class FtpUploadTracker:
  sizeWritten = 0
  totalSize = 0
  lastShownPercent = 0
  blockSize = 0

  def __init__(self, totalSize,blockSize):
    self.totalSize = totalSize
    self.blockSize = blockSize
    self.counter = 0

  def handle(self,block):
    self.sizeWritten += self.blockSize
    percentComplete = round(float(self.sizeWritten) * 100 / float(self.totalSize),2)
    self.counter += 1

    if percentComplete - self.lastShownPercent >=1  or percentComplete>=100:
      #进度超过1%才打日志
      logger.info("UploadFile2FtpServer.FtpUploadTracker.handle: "+str(percentComplete) + " % complete.sizeWritten="+str(self.sizeWritten)+";totalSize="+str(self.totalSize))
      self.lastShownPercent = percentComplete
      if self.counter>=999999:
        self.counter = 0

class NetworkOptModule:
  def __init__(self, ftpiphost='153.35.132.232',ftpusr='anonymous',ftppwd=''):
    self.ftpiphost = ftpiphost
    self.ftpusr = ftpusr
    self.ftppwd = ftppwd

  #确保ftp路径存在
  def EnsureFtpPathExist(self,remotepath='/autotest'):
    try:
      logger.debug("EnsureFtpPathExist:self.ftpiphost="+str(self.ftpiphost)+";remotepath="+str(remotepath))
      ftp = ftplib.FTP(self.ftpiphost)
      logger.debug("EnsureFtpPathExist:Connect FTP")
      ftp.login(self.ftpusr,self.ftppwd)
      logger.debug("EnsureFtpPathExist:login")
      patharr = remotepath.split("/")
      for pathindex in range(0,len(patharr)):
        tmpfolder = patharr[pathindex]
        logger.debug("EnsureFtpPathExist:tmpfolder="+str(tmpfolder))
        if tmpfolder != "":
          try:
            ftp.cwd(tmpfolder)
            logger.debug("EnsureFtpPathExist:cwd")
          except Exception,msg:
            ftp.mkd(tmpfolder)
            logger.debug("EnsureFtpPathExist:mkd")
            ftp.cwd(tmpfolder)
            logger.debug("EnsureFtpPathExist:cwd")
      ftp.quit()
      logger.debug("EnsureFtpPathExist:quit")
      logger.debug("EnsureFtpPathExist:succeed")
      return 0
    except Exception,msg:
      logger.warning("err,msg="+str(msg))
      return -1

  #上传文件到ftp服务器
  def UploadFile2FtpServer(self,localfile='',remotepath='/autotest',blocksize=1024):
    try:
      logger.debug("UploadFile2FtpServer:self.ftpiphost="+str(self.ftpiphost)+";localfile="+str(localfile)+";remotepath="+str(remotepath))
      logger.info("UploadFile2FtpServer.blocksize="+str(blocksize))
      if self.EnsureFtpPathExist(remotepath) != 0:
        logger.debug("UploadFile2FtpServer:failed,ftp path not exist")
        return -3
      ftp = ftplib.FTP(self.ftpiphost)
      logger.debug("UploadFile2FtpServer:Connect FTP")
      ftp.login(self.ftpusr,self.ftppwd)
      logger.debug("UploadFile2FtpServer:login")
      ftp.cwd(remotepath)
      logger.debug("UploadFile2FtpServer:cwd")
      #bufsize = 1024 #设置缓冲块大小
      localfile = r"%s"%localfile
      FileSize = -999
      if not os.path.isfile(localfile):
        logger.debug("UploadFile2FtpServer:failed,localfile not exist")
        return -2
      else:
        statinfo=os.stat(localfile)
        FileSize =  float(statinfo.st_size)


      logger.info("UploadFile2FtpServer.FileSize="+str(FileSize))
      uploadTracker = FtpUploadTracker(int(FileSize),int(blocksize))

      filename = str(os.path.basename(localfile))
      logger.debug("UploadFile2FtpServer:filename="+str(filename))
      try:
        ftp.delete(filename)              #删除远程文件
        logger.debug("UploadFile2FtpServer:delete remote file")
      except:
        filename = str(os.path.basename(localfile))
      localfile = unicode(localfile,'utf8')

      file_obj = open(localfile,'rb')#以读模式在本地打开文件
      logger.debug("UploadFile2FtpServer:open localfile")
      logger.debug("UploadFile2FtpServer:uploading localfile")
      ftp.storbinary('STOR %s' % filename,file_obj,blocksize,uploadTracker.handle)#上传文件
      logger.debug("UploadFile2FtpServer:localfile uploaded")
      file_obj.close()
      logger.debug("UploadFile2FtpServer:file_handler close")
      ftp.quit()
      logger.debug("UploadFile2FtpServer:ftp quit")
      logger.debug("UploadFile2FtpServer:succeed")
      return 0
    except Exception,msg:
      logger.warning("err,msg="+str(msg))
      return -1

if __name__ == '__main__':
  NetworkOptModule = NetworkOptModule()
  NetworkOptModule.UploadFile2FtpServer(r"D:\TDDOWNLOAD\xl_sdk_demo-debug.apk","/autotest")