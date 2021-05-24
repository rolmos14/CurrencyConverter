from typing import List

from hstest.check_result import CheckResult
from hstest.stage_test import StageTest
from hstest.test_case import TestCase


class TestStage4(StageTest):

    def generate(self) -> List[TestCase]:
        list_tests = [
            TestCase(stdin='17', attach=[17]),
            TestCase(stdin='3.5', attach=[3.5]),
            TestCase(stdin='21', attach=[21]),
            TestCase(stdin='4.5', attach=[4.5])

        ]

        currs = {'rub': 2.98, 'ars': 0.82, 'hnl': 0.17, 'aud': 1.9622, 'mad': 0.208}
        for test in list_tests:
            attach_dict = {}
            for k, v in currs.items():
                attach_dict[k] = round(v * float(test.input), 2)
            test.attach.append(attach_dict)

        return list_tests

    def check(self, reply: str, attach) -> CheckResult:
        ccoins_att, currs_att = attach
        reply_parsed = reply.strip().split('\n')
        if len(reply_parsed) != 5:
            return CheckResult.wrong("Your output differs from the example")
        for repl in reply_parsed:
            repl = repl.lower()
            repl_parsed = repl.strip().split()
            if len(repl_parsed) != 11:
                return CheckResult.wrong("Your output differs from the example")
            try:
                cur = float(repl_parsed[3])
                ccoins = float(repl_parsed[-2])
                key = repl_parsed[4]
            except (ValueError, KeyError):
                return CheckResult.wrong("Format your output according to the example")
            if ccoins != ccoins_att:
                return CheckResult.wrong("The amount of conicoins is wrong")
            try:
                amount_curr = currs_att[key]
            except KeyError:
                return CheckResult.wrong("The currency name in the output of your program seems to be wrong:\n"
                                         "\"{0}\"".format(key.upper()))
            if abs(amount_curr - cur) > 0.2:
                return CheckResult.wrong(f"The amount of {key.upper()} is wrong")
            if not ('i will get' in repl and 'from the sale of' in repl and 'conicoins' in repl):
                return CheckResult.wrong("Format your output according to the example")
        return CheckResult.correct()


if __name__ == '__main__':
    TestStage4("cconverter.cconverter").run_tests()
