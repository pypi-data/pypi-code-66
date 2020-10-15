from unittest import TestResult, TextTestRunner, registerResult
import time

from sumoapputils.common.utils import get_test_logger

logger = get_test_logger()


class CustomTextTestResult(TestResult):

    def __init__(self, stream=None, descriptions=None, verbosity=None):
        super(CustomTextTestResult, self).__init__(stream, descriptions, verbosity)
        self.warnings = []
        self.appname = None

    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if doc_first_line:
            return '\n'.join((str(test), doc_first_line))
        else:
            return str(test).replace("(testapp.TestApp)", "")

    def startTest(self, test):
        super(CustomTextTestResult, self).startTest(test)

    def addSuccess(self, test):
        super(CustomTextTestResult, self).addSuccess(test)
        test_name = self.getDescription(test)
        status = "WARNING" if test_name in self.get_test_names(self.warnings) else "PASS"
        logger.debug(test_name + " ... " + status)

    def addError(self, test, err):
        super(CustomTextTestResult, self).addError(test, err)
        logger.debug(self.getDescription(test) + " ... " + "ERROR")

    def addFailure(self, test, err):
        super(CustomTextTestResult, self).addFailure(test, err)
        logger.debug(self.getDescription(test) + " ... " + "FAIL")

    def addSkip(self, test, reason):
        super(CustomTextTestResult, self).addSkip(test, reason)
        logger.debug(self.getDescription(test) + " ... " + "SKIPPED")

    def addExpectedFailure(self, test, err):
        super(CustomTextTestResult, self).addExpectedFailure(test, err)
        logger.debug(self.getDescription(test) + " ... " + "EXPECTED FAILURE")

    def addUnexpectedSuccess(self, test):
        super(CustomTextTestResult, self).addUnexpectedSuccess(test)
        logger.debug(self.getDescription(test) + " ... " + "UNEXPECTED SUCCESS")

    def printErrors(self):
        self.printErrorList('ERROR', self.errors)
        self.printErrorList('FAIL', self.failures)
        self.printErrorList('WARNING', self.warnings)

    def get_test_names(self, errors):
        test_names = []
        for test, err in errors:
            test_names.append(self.getDescription(test))
        return test_names

    def printErrorList(self, flavour, errors):
        for test, err in errors:
            test_name = self.getDescription(test)
            if flavour == "WARNING":
                logger.warning("%s: %s: %s" % (self.appname, test_name, err))
            else:
                logger.error("%s: %s: %s" % (self.appname, test_name, err))

    def print_final_output(self):

        expectedFails = unexpectedSuccesses = skipped = warnings = 0
        try:
            results = map(len, (self.expectedFailures,
                                self.unexpectedSuccesses,
                                self.skipped, self.warnings))
        except AttributeError:
            pass
        else:
            expectedFails, unexpectedSuccesses, skipped, warnings = results

        infos = []
        infos.append("APPNAME: %s | TOTAL TESTCASES: %d" % (self.appname, self.testsRun))
        if not self.wasSuccessful():
            failures = len(self.failures) + len(self.errors)
            infos.append("RESULT: FAILED | FAILURES: %d | FAILED TESTCASES: %s" % (
                failures, ",".join(set(self.get_test_names(self.failures + self.errors)))))
        else:
            infos.append("RESULT: ALL TESTS PASSED")
        if skipped:
            infos.append("SKIPPED: %d" % skipped)
        if expectedFails:
            infos.append("EXPECTED FAILURES: %d" % expectedFails)
        if unexpectedSuccesses:
            infos.append("UNEXPECTED SUCCESSES: %d" % unexpectedSuccesses)
        if warnings:
            infos.append("TOTAL WARNINGS: %d | TESTCASES WITH WARNINGS: %s" % (
                warnings, ",".join(set(self.get_test_names(self.warnings)))))

        if infos:
            logger.info("%s" % (" | ".join(infos)))
        else:
            logger.info("\n")


class CustomTextTestRunner(TextTestRunner):
    resultclass = CustomTextTestResult

    def run(self, test):
        "Run the given test case or test suite."
        result = self._makeResult()
        registerResult(result)
        result.failfast = self.failfast
        result.buffer = self.buffer
        startTime = time.time()
        startTestRun = getattr(result, 'startTestRun', None)
        if startTestRun is not None:
            startTestRun()
        try:
            test(result)
        finally:
            stopTestRun = getattr(result, 'stopTestRun', None)
            if stopTestRun is not None:
                stopTestRun()
        stopTime = time.time()
        timeTaken = stopTime - startTime
        result.printErrors()

        run = result.testsRun
        logger.info("Ran %d test%s in %.3fs\n" % (
            run, run != 1 and "s" or "", timeTaken))

        result.print_final_output()
        return result
