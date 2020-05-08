import os

import stat_attributes as attributes
from services import execute, remove
from stat_makefile import StatMakefile


class TestsRunner(object):

    def __init__(self, makefileName, commandToCompile, isVerbose=True):
        self.__fileName = makefileName
        self.__makefile = StatMakefile(makefileName)
        self.__beSilent = not isVerbose
        self.__log = []
        self.__clearOutputs()
        self.__command = commandToCompile

    def __clearOutputs(self):
        for directory in attributes.OUTPUT_SUB_DIRECTORIES:
            remove(self.__getOutputPath(directory))

    def __getOutputPath(self, *args):
        return os.path.join(attributes.OUTPUT_DIRECTORY, self.__makefile.name, *args)

    def compile(self):
        environ = dict(os.environ, PRIVATE_NAME=self.__makefile.name)
        status, log = execute( self.__command.format(self.__fileName), beSilent=self.__beSilent, env=environ)
        self.__log.extend(log)
        if status:
            raise TestsRunnerException('Package "{0}" failed to compile.'.format(self.__fileName))

    def run(self):
        status, log = execute(self.__getOutputPath('bin', self.__makefile[StatMakefile.EXEC]), beSilent=self.__beSilent)
        self.__log.extend(log)
        if status:
            message = 'The executable of package "{0}" failed with error-code {1:#X}.\n'.format(self.__fileName, status & 0xFFFFFFFF)
            self.__log.append(message)
            raise TestsRunnerException(message)

    def getLog(self):
        return self.__log

    def writeLog(self, extraInfo=''):
        logFilePath = '/'.join([attributes.LOGS_DIRECTORY, self.__makefile.name + '.log'])
        with open(logFilePath, 'a') as fp:
            fp.writelines(self.__log)
            fp.write(extraInfo)

class TestsRunnerException(Exception):
    """
    Custom exception for STAT test-package runner
    """